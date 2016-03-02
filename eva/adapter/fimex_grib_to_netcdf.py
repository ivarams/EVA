import logging
import os.path

import eva
import eva.job
import eva.base.adapter


class FimexGRIB2NetCDFAdapter(eva.base.adapter.BaseAdapter):
    """
    This adapter fills a NetCDF file with GRIB data using Fimex.
    The adapter requires an external library called `eva-adapter-support`.
    """
    CONFIG = {
        'EVA_FG2NC_LIB': 'Path to .../eva-adapter-support/FimexGRIB2NetCDFAdapter',
        'EVA_FG2NC_TEMPLATEDIR': 'Path to the NetCDF template files required for this conversion',
    }

    REQUIRED_CONFIG = [
        'EVA_FG2NC_LIB',
        'EVA_FG2NC_TEMPLATEDIR',
        'EVA_INPUT_DATA_FORMAT_UUID',
        'EVA_INPUT_PRODUCT_UUID',
        'EVA_INPUT_SERVICE_BACKEND_UUID',
        'EVA_OUTPUT_BASE_URL',
        'EVA_OUTPUT_FILENAME_PATTERN',
        'EVA_OUTPUT_PRODUCT_UUID',
        'EVA_OUTPUT_SERVICE_BACKEND_UUID',
    ]

    def process_resource(self, resource):
        """
        @brief Generate a Job which converts GRIB to NetCDF using the
        eva-adapter-support library.
        """
        job = self.create_job(resource)

        self.executor.execute(job)

        if job.status != eva.job.COMPLETE:
            raise eva.exceptions.RetryException("GRIB to NetCDF conversion of '%s' failed." % resource.url)

        datainstance = self.register_output(job)
        self.logger.info('Successfully filled the NetCDF file %s with data from %s', datainstance.url, resource.url)

    def create_job(self, resource):
        """
        @brief Generate a Job object from a Productstatus Resource.
        """
        job = eva.job.Job()

        reftime = resource.data.productinstance.reference_time

        job.data = {
            'reftime': reftime,
            'version': resource.data.productinstance.version,
            'time_period_begin': resource.data.time_period_begin,
            'time_period_end': resource.data.time_period_end,
            'expires': resource.expires,
            'filename': reftime.strftime(self.env['EVA_OUTPUT_FILENAME_PATTERN']),
        }

        job.command = """#!/bin/bash
            {lib_fg2nc}/grib2nc \
                --input "{gribfile}" \
                --output "{destfile}" \
                --reference_time "{reftime}" \
                --template_directory "{templatedir}"
        """.format(
            gribfile=eva.url_to_filename(resource.url),
            reftime=reftime.strftime("%Y-%m-%dT%H:%M:%S%z"),
            lib_fg2nc=self.env['EVA_FG2NC_LIB'],
            templatedir=self.env['EVA_FG2NC_TEMPLATEDIR'],
            destfile=job.data['filename'],
        )

        return job

    def register_output(self, job):
        """
        @brief Create a Productstatus DataInstance based on a Job object.
        """
        productinstance = self.get_or_post_productinstance_resource(job)
        data = self.get_or_post_data_resource(productinstance, job)
        datainstance = self.post_datainstance_resource(data, job)
        self.logger.info('DataInstance %s, expires %s', datainstance, datainstance.expires)
        return datainstance

    def get_productstatus_dataformat(self, file_type):
        """
        Given a file type string, return a DataFormat object pointing to the
        correct data format.
        """
        # FIXME copied from ecreceive.dataset, except for parameter and exception
        qs = self.api.dataformat.objects.filter(name=file_type)
        if qs.count() == 0:
            raise Exception(
                "Data format '%s' was not found on the Productstatus server" % file_type
            )
        resource = qs[0]
        logging.debug('%s: Productstatus dataformat for %s' % (resource, file_type))
        return resource

    def get_productstatus_product(self):
        """
        @returns The Productstatus output Product resource.
        """
        return self.api.product[self.env['EVA_OUTPUT_PRODUCT_UUID']]

    def get_or_post_productinstance_resource(self, job):
        """
        Return a matching ProductInstance resource according to Product, reference time and version.
        """
        # FIXME mostly copied from ecreceive.dataset
        product = self.get_productstatus_product()
        parameters = {
            'product': product,
            'reference_time': job.data['reftime'],
            'version': job.data['version'],  # FIXME is this the correct version?
        }
        return self.api.productinstance.find_or_create(parameters)

    def get_or_post_data_resource(self, productinstance, job):
        """
        Return a matching Data resource according to ProductInstance and data file
        begin/end times.
        """
        # FIXME mostly copied from ecreceive.dataset
        parameters = {
            'productinstance': productinstance,
            'time_period_begin': job.data['time_period_begin'],
            'time_period_end': job.data['time_period_end'],
        }
        return self.api.data.find_or_create(parameters)

    def post_datainstance_resource(self, data, job):
        """
        Create a DataInstance resource at the Productstatus server, referring to the
        given data set.
        """
        # FIXME mostly copied from ecreceive.dataset
        resource = self.api.datainstance.create()
        resource.data = data
        resource.expires = job.data['expires']
        resource.format = self.get_productstatus_dataformat("NetCDF")
        resource.servicebackend = self.api.servicebackend[self.env['EVA_OUTPUT_SERVICE_BACKEND_UUID']]
        resource.url = os.path.join(self.env['EVA_OUTPUT_BASE_URL'], job.data['filename'])
        resource.save()
        return resource
