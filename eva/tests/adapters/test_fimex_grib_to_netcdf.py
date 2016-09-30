import eva
import eva.tests
import eva.tests.schemas
import eva.adapter
import eva.exceptions
import eva.job

import mock
import httmock
import datetime


class TestFimexGRIB2NetCDFAdapter(eva.tests.BaseTestAdapter):
    adapter_class = eva.adapter.FimexGRIB2NetCDFAdapter
    environment = {
        'EVA_FG2NC_LIB': '/lib_fg2nc',
        'EVA_FG2NC_TEMPLATEDIR': '/lib_fg2nc/template',
        'EVA_INPUT_DATA_FORMAT': 'foo',
        'EVA_INPUT_PRODUCT': 'foo',
        'EVA_INPUT_SERVICE_BACKEND': 'foo',
        'EVA_OUTPUT_BASE_URL': 'file:///path/to/new',
        'EVA_OUTPUT_FILENAME_PATTERN': '/new/%Y%m%dT%H%M%SZ/foo',
        'EVA_OUTPUT_PRODUCT': 'foo',
        'EVA_OUTPUT_SERVICE_BACKEND': 'foo',
        'EVA_PRODUCTSTATUS_API_KEY': 'foo',
        'EVA_PRODUCTSTATUS_USERNAME': 'foo',
    }

    def test_create_job(self):
        """!
        @brief Test that job creation generates the correct FIMEX command line.
        """
        self.create_adapter()
        resource = mock.MagicMock()
        resource.url = 'file:///foo/bar/baz'
        resource.data.productinstance.reference_time = eva.coerce_to_utc(datetime.datetime(2016, 1, 1, 18, 15, 0))
        with httmock.HTTMock(*eva.tests.schemas.SCHEMAS):
            job = self.create_job(resource)
        self.assertTrue('/lib_fg2nc/grib2nc' in job.command)
        self.assertTrue('--input "/foo/bar/baz"' in job.command)
        self.assertTrue('--output "/new/20160101T181500Z/foo"' in job.command)
        self.assertTrue('--reference_time "2016-01-01T18:15:00+0000"' in job.command)
        self.assertTrue('--template_directory "/lib_fg2nc/template"' in job.command)

    def test_finish_job_and_generate_resources(self):
        """!
        @brief Test that job finish works and doesn't throw any exceptions.
        """
        self.create_adapter()
        resource = mock.MagicMock()
        resource.url = 'file:///foo/bar/baz'
        resource.data.productinstance.reference_time = eva.coerce_to_utc(datetime.datetime(2016, 1, 1, 18, 15, 0))
        with httmock.HTTMock(*eva.tests.schemas.SCHEMAS):
            job = self.create_job(resource)
            job.set_status(eva.job.COMPLETE)
            self.adapter.finish_job(job)
            resources = self.generate_resources(job)
        self.assertEqual(len(resources['productinstance']), 1)
        self.assertEqual(len(resources['data']), 1)
        self.assertEqual(len(resources['datainstance']), 1)
        self.assertEqual(resources['datainstance'][0].partial, True)
        self.assertEqual(resources['datainstance'][0].url, 'file:///path/to/new/foo')
