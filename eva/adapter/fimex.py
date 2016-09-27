import os
import datetime

import eva
import eva.base.adapter
import eva.job
import eva.exceptions
import eva.template

import productstatus


class FimexAdapter(eva.base.adapter.BaseAdapter):
    """!
    Generic FIMEX adapter that will accept virtually any parameter known to FIMEX.

    For flexibility, this adapter only takes three configuration options, that
    will allow users to set up any type of FIMEX job:

      * An output file name pattern
      * A generic command-line option string

    After generating the file, the adapter will post the information to
    Productstatus if the EVA_OUTPUT_* and EVA_PRODUCTSTATUS_* environments are
    specified.
    """

    CONFIG = {
        'EVA_FIMEX_PARAMETERS': {
            'type': 'string',
            'help': 'FIMEX command-line parameters.',
            'default': '',
        }
    }

    REQUIRED_CONFIG = [
        'EVA_FIMEX_PARAMETERS',
        'EVA_INPUT_DATA_FORMAT',
        'EVA_INPUT_PRODUCT',
        'EVA_INPUT_SERVICE_BACKEND',
        'EVA_OUTPUT_FILENAME_PATTERN',
    ]

    OPTIONAL_CONFIG = [
        'EVA_INPUT_PARTIAL',
        'EVA_OUTPUT_BASE_URL',
        'EVA_OUTPUT_DATA_FORMAT',
        'EVA_OUTPUT_LIFETIME',
        'EVA_OUTPUT_PRODUCT',
        'EVA_OUTPUT_SERVICE_BACKEND',
    ]

    def init(self):
        """!
        @brief Check that optional configuration is consistent.
        """
        if self.has_valid_output_config():
            self.post_to_productstatus = True
            self.require_productstatus_credentials()
            self.output_data_format = self.api.dataformat[self.env['EVA_OUTPUT_DATA_FORMAT']]
            self.output_product = self.api.product[self.env['EVA_OUTPUT_PRODUCT']]
            self.output_service_backend = self.api.servicebackend[self.env['EVA_OUTPUT_SERVICE_BACKEND']]
        else:
            self.post_to_productstatus = False
            self.logger.info('Will not post any data to Productstatus.')
        self.fimex_parameters = self.template.from_string(self.env['EVA_FIMEX_PARAMETERS'])
        self.output_filename = self.template.from_string(self.env['EVA_OUTPUT_FILENAME_PATTERN'])

    def has_valid_output_config(self):
        """!
        @return True if all optional output variables are configured, False otherwise.
        """
        return (
            (self.env['EVA_OUTPUT_BASE_URL'] is not None) and
            (self.env['EVA_OUTPUT_DATA_FORMAT'] is not None) and
            (self.env['EVA_OUTPUT_LIFETIME'] is not None) and
            (self.env['EVA_OUTPUT_PRODUCT'] is not None) and
            (self.env['EVA_OUTPUT_SERVICE_BACKEND'] is not None)
        )

    def create_job(self, message_id, resource):
        """!
        @brief Create a generic FIMEX job.
        """
        job = eva.job.Job(message_id, self.logger)

        job.input_filename = eva.url_to_filename(resource.url)
        job.reference_time = resource.data.productinstance.reference_time
        template_variables = {
            'datainstance': resource,
            'input_filename': os.path.basename(job.input_filename),
            'reference_time': job.reference_time,
        }

        # Render the Jinja2 templates and report any errors
        try:
            params = self.fimex_parameters.render(**template_variables)
            job.output_filename = self.output_filename.render(**template_variables)
        except Exception as e:
            raise eva.exceptions.InvalidConfigurationException(e)

        # Generate Fimex job
        command = ['#!/bin/bash']
        command += ['#$ -S /bin/bash']
        command += ["time fimex --input.file '%(input.file)s' --output.file '%(output.file)s' %(params)s" % {
            'input.file': job.input_filename,
            'output.file': job.output_filename,
            'params': params,
        }]
        job.command = '\n'.join(command)

        return job

    def finish_job(self, job):
        # Retry on failure
        if not job.complete():
            raise eva.exceptions.RetryException(
                "Fimex conversion of '%s' to '%s' failed." % (job.input_filename, job.output_filename)
            )

        # Succeed at this point if not posting to Productstatus
        if not self.post_to_productstatus:
            return

        # Post a new ProductInstance resource
        self.logger.info('Creating a new ProductInstance resource on the Productstatus server...')
        productinstance = eva.retry_n(
            self.post_productinstance_resource,
            args=(self.output_product, job.reference_time),
            exceptions=(productstatus.exceptions.ServiceUnavailableException,),
            give_up=30,
        )

        # Post a new Data resource
        self.logger.info('Creating a new Data resource on the Productstatus server...')
        data = eva.retry_n(
            self.get_or_post_data_resource,
            args=(productinstance, None, None),
            exceptions=(
                productstatus.exceptions.ServiceUnavailableException,
            ),
            give_up=30,
        )

        # Post a new DataInstance resource
        self.logger.info('Creating a new DataInstance resource on the Productstatus server...')
        url = os.path.join(self.env['EVA_OUTPUT_BASE_URL'], os.path.basename(job.output_filename))
        datainstance = eva.retry_n(
            self.post_datainstance_resource,
            args=(
                data,
                self.expiry_from_lifetime(),
                self.output_data_format,
                self.output_service_backend,
                url,
            ),
            exceptions=(productstatus.exceptions.ServiceUnavailableException,),
            give_up=30,
        )

        # All records written, log success
        self.logger.info('DataInstance %s, expires %s', datainstance, datainstance.expires)
        self.logger.info('The file %s has been successfully generated', datainstance.url)

    def post_productinstance_resource(self, product, reference_time):
        """!
        @brief Create a ProductInstance resource.
        """
        productinstance = self.api.productinstance.create()
        productinstance.product = product
        productinstance.reference_time = reference_time
        productinstance.save()
        return productinstance

    def get_or_post_data_resource(self, productinstance, time_period_begin, time_period_end):
        """!
        @brief Return a matching Data resource according to ProductInstance and
        data file begin/end times.
        """
        parameters = {
            'productinstance': productinstance,
            'time_period_begin': time_period_begin,
            'time_period_end': time_period_end,
        }
        return self.api.data.find_or_create(parameters)

    def post_datainstance_resource(self, data, expires, format, servicebackend, url):
        """!
        @brief Create a DataInstance resource at the Productstatus server,
        referring to the given data set.
        """
        resource = self.api.datainstance.create()
        resource.data = data
        resource.expires = expires
        resource.format = format
        resource.servicebackend = servicebackend
        resource.url = url
        resource.save()
        return resource
