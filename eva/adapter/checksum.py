import eva
import eva.base.adapter
import eva.job
import eva.exceptions

import productstatus.exceptions


class ChecksumVerificationAdapter(eva.base.adapter.BaseAdapter):
    """!
    An adapter that verifies checksums on data sets according to auxiliary files.

    At the moment, only md5sum is supported, and is expected to be in the same
    directory as the data sets, with the suffix ".md5".

    If the checksum is correct, the .md5 file is deleted, and the hash is added
    to the Productstatus database. If the checksum fails, the file is left
    intact, and the task fails and is NOT restarted.
    """

    REQUIRED_CONFIG = [
        'EVA_INPUT_SERVICE_BACKEND',
    ]

    OPTIONAL_CONFIG = [
        'EVA_INPUT_DATA_FORMAT',
        'EVA_INPUT_PRODUCT',
        'EVA_INPUT_WITH_HASH',
    ]

    def init(self):
        """!
        @brief This adapter requires Productstatus write access to be of any use.
        """
        self.require_productstatus_credentials()
        if self.env['EVA_INPUT_WITH_HASH'] is not False:
            raise eva.exceptions.InvalidConfigurationException(
                'This adapter MUST be configured with EVA_INPUT_WITH_HASH=NO in order to avoid recursive loops.'
            )

    def create_job(self, message_id, resource):
        """!
        @brief Return a Job object that will check the file's md5sum against a
        stored hash in a corresponding file.
        """
        job = eva.job.Job(message_id, self.logger)
        job.dataset_filename = eva.url_to_filename(resource.url)
        job.md5_filename = job.dataset_filename + '.md5'

        lines = [
            '#!/bin/bash',
            '#$ -S /bin/bash',  # for GridEngine compatibility
            'set -e',
            'cat %(md5_filename)s',  # for hash detection in finish_job()
            'printf "%%s  %(dataset_filename)s\\n" $(cat %(md5_filename)s) | md5sum --check --status --strict -',
            'rm -fv %(md5_filename)s >&2',
        ]
        values = {
            'dataset_filename': job.dataset_filename,
            'md5_filename': job.md5_filename,
        }

        job.command = "\n".join(lines) + "\n"
        job.command = job.command % values
        return job

    def finish_job(self, job):
        if not job.complete():
            self.logger.error("md5sum checking of '%s' failed, skipping further processing!", job.resource.url)
            self.statsd.incr('md5sum_fail')
            return

        job.logger.info('Updating DataInstance with hash data...')
        job.resource.hash_type = str('md5')
        job.resource.hash = ''.join(job.stdout)

        # FIXME: how do we actually handle this error?
        assert len(job.resource.hash) == 32

        eva.retry_n(job.resource.save,
                    exceptions=(productstatus.exceptions.ServiceUnavailableException,),
                    give_up=0)

        job.logger.info('DataInstance %s has been updated with md5sum hash %s.', job.resource, job.resource.hash)