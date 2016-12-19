"""
RESTful API for controlling and monitoring EVA.
"""


import eva
import eva.globe
import eva.gpg
import eva.rest.resources

import falcon
import json
import re
import wsgiref.simple_server


class RequireJSON(object):
    def process_request(self, req, resp):
        if not req.client_accepts_json:
            raise falcon.HTTPNotAcceptable('This API only supports responses encoded as JSON.')

        if req.method in ('POST', 'PUT') and req.content_length not in (None, 0):
            if 'application/json' not in req.content_type:
                raise falcon.HTTPUnsupportedMediaType('This API only supports requests encoded as JSON.')


class RequireGPGSignedRequests(eva.globe.GlobalMixin):
    def __init__(self):
        self.header_regex = re.compile(r'^X-EVA-Request-Signature-\d+$', re.IGNORECASE)

    def _gpg_signature_from_headers(self, headers):
        signature = []
        keys = sorted(headers.keys())
        for key in keys:
            if not self.header_regex.match(key):
                continue
            signature += [headers[key]]
        return signature

    def _check_signature(self, payload, signature):
        checker = eva.gpg.GPGSignatureChecker(payload, signature)
        result = checker.verify()
        if result.exit_code != 0:
            self.logger.warning('GPG verification of request failed: %s', result.stderr[0])
            for line in result.stderr:
                self.logger.warning(line)
            raise falcon.HTTPUnauthorized('GPG verification of request failed.')
        self.logger.info('Request is properly signed by %s with %s key %s at %s', result.signer, result.key_type, result.key_id, eva.strftime_iso8601(result.timestamp))

    def process_request(self, req, resp):
        if req.method == 'GET':
            return
        signature = self._gpg_signature_from_headers(req.headers)
        self.logger.info('Verifying request signature:')
        [self.logger.info(s) for s in signature]
        self._check_signature(req.context['body'], signature)


class JSONTranslator(object):
    def process_request(self, req, resp):
        req.context['body'] = ''
        if req.content_length in (None, 0):
            return

        body = req.stream.read()
        if not body:
            raise falcon.HTTPBadRequest('Empty request body', 'A valid JSON document is required.')

        try:
            req.context['body'] = body.decode('utf-8')
            req.context['doc'] = json.loads(req.context['body'])

        except (ValueError, UnicodeDecodeError):
            raise falcon.HTTPError(
                falcon.HTTP_753,
                'Malformed JSON', 'Could not decode the request body. The JSON was incorrect or not encoded as UTF-8.',
            )

    def process_response(self, req, resp, resource):
        if 'result' not in req.context:
            return

        resp.body = json.dumps(req.context['result'])


class Server(eva.globe.GlobalMixin):
    """
    Run a HTTP REST API based on Falcon web framework.
    """

    def __init__(self, globe, host=None, port=None):
        self.set_globe(globe)
        gpg_middleware = RequireGPGSignedRequests()
        gpg_middleware.set_globe(globe)
        self.app = falcon.API(middleware=[
            RequireJSON(),
            JSONTranslator(),
            gpg_middleware,
        ])
        self._resources = []
        self._setup_resources()
        if host is None and port is None:
            self.server = None
            return
        self.server = wsgiref.simple_server.make_server(host, port, self.app)
        self.server.timeout = 0.001

    def _setup_resources(self):
        self._add_resource('control', '/control/{method}', eva.rest.resources.ControlResource())
        self._add_resource('health', '/health', eva.rest.resources.HealthResource())
        self._add_resource('job', '/jobs/{job_id}', eva.rest.resources.JobResource())
        self._add_resource('jobs', '/jobs', eva.rest.resources.JobsResource())
        self._add_resource('process', '/process/{method}', eva.rest.resources.ProcessResource())

    def _add_resource(self, name, path, resource):
        self._resources += [name]
        setattr(self, name, resource)
        resource.set_globe(self.globe)
        self.app.add_route(path, resource)

    def set_eventloop_instance(self, eventloop):
        for resource in self._resources:
            instance = getattr(self, resource)
            instance.set_eventloop_instance(eventloop)

    def respond_to_next_request(self):
        if not self.server:
            return
        self.server.handle_request()
