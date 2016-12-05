# coding: utf-8

import datetime

import eva
import eva.executor
import eva.tests


class TestBase(eva.tests.TestBase):

    def test_in_array_or_empty(self):
        array = ['a', 'b', 'c']
        self.assertTrue(eva.in_array_or_empty('b', array))

    def test_in_array_or_empty_true_empty(self):
        array = []
        self.assertTrue(eva.in_array_or_empty('y', array))

    def test_in_array_or_empty_false(self):
        array = ['a', 'b', 'c']
        self.assertFalse(eva.in_array_or_empty('x', array))

    def test_url_to_filename(self):
        url = 'file:///foo/bar/baz.nc'
        filename = '/foo/bar/baz.nc'
        self.assertEqual(eva.url_to_filename(url), filename)

    def test_url_to_filename_wrong_protocol(self):
        with self.assertRaises(RuntimeError):
            eva.url_to_filename('https://example.com/foo.nc')

    def test_log_stdout_stderr(self):
        job = eva.job.Job('foo', self.globe)
        eva.executor.log_stdout_stderr(job, ['x'], [])

    def test_split_comma_separated(self):
        string = ' foo , bar,baz  '
        list_ = eva.split_comma_separated(string)
        self.assertListEqual(list_, ['foo', 'bar', 'baz'])

    def test_split_comma_separated_empty(self):
        string = ''
        list_ = eva.split_comma_separated(string)
        self.assertListEqual(list_, [])

    def test_zookeeper_group_id(self):
        self.assertEqual(eva.zookeeper_group_id(u'/this/~isaán/\000ID'), 'this.~isan..id')
        with self.assertRaises(eva.exceptions.InvalidGroupIdException):
            eva.zookeeper_group_id(u'áćé')
        with self.assertRaises(eva.exceptions.InvalidGroupIdException):
            eva.zookeeper_group_id('zookeeper')

    def test_strftime_iso8601(self):
        dt = datetime.datetime(year=2000, month=1, day=1, hour=12, minute=0, second=0)
        dt = eva.coerce_to_utc(dt)
        s = eva.strftime_iso8601(dt)
        self.assertEqual(s, '2000-01-01T12:00:00+0000')
        dt = 'foo'
        with self.assertRaises(AttributeError):
            eva.strftime_iso8601(dt)
        s = eva.strftime_iso8601(dt, null_string=True)
        self.assertEqual(s, 'NULL')

    def test_coerce_to_utc(self):
        dt = datetime.datetime(year=2000, month=1, day=1, hour=12, minute=0, second=0)
        dt_c = eva.coerce_to_utc(dt)
        self.assertEqual(dt_c.tzinfo.tzname(None), 'UTC')

    def test_epoch_with_timezone(self):
        dt = eva.epoch_with_timezone()
        self.assertEqual(dt.tzinfo.tzname(None), 'UTC')
        self.assertEqual(dt.timestamp(), 0)

    def test_netcdf_time_to_timestamp(self):
        s = "2015-01-01"
        dt = eva.netcdf_time_to_timestamp(s)
        self.assertEqual(dt.year, 2015)
        self.assertEqual(dt.month, 1)
        self.assertEqual(dt.day, 1)
        self.assertEqual(dt.hour, 0)
        self.assertEqual(dt.minute, 0)
        self.assertEqual(dt.second, 0)
        self.assertEqual(dt.tzinfo.tzname(None), 'UTC')
        s = "2016-06-13 06"
        dt = eva.netcdf_time_to_timestamp(s)
        self.assertEqual(dt.year, 2016)
        self.assertEqual(dt.month, 6)
        self.assertEqual(dt.day, 13)
        self.assertEqual(dt.hour, 6)
        self.assertEqual(dt.minute, 0)
        self.assertEqual(dt.second, 0)
        self.assertEqual(dt.tzinfo.tzname(None), 'UTC')

    def test_convert_to_bytes(self):
        self.assertEqual(eva.convert_to_bytes(1, 'B'), 1)
        self.assertEqual(eva.convert_to_bytes(1, 'K'), 1024)
        self.assertEqual(eva.convert_to_bytes(1, 'M'), 1048576)
        self.assertEqual(eva.convert_to_bytes(1, 'G'), 1073741824)
        self.assertEqual(eva.convert_to_bytes(1, 'T'), 1099511627776)  # futureproofing
        self.assertEqual(eva.convert_to_bytes(1.5, 'K'), 1536)
        self.assertEqual(eva.convert_to_bytes(1.5, 'k'), 1536)  # case difference
        self.assertEqual(eva.convert_to_bytes('1.5', 'k'), 1536)
        with self.assertRaises(ValueError):
            eva.convert_to_bytes(1.5, 'xB')

    def test_get_std_lines(self):
        """!
        @brief Test that the executor can deal with both input in bytes and strings
        as those two can appear depending on the executor instance.
        """
        std_string = "Situation normal all fantastic über!\nNo Errors."
        std_bytes = std_string.encode(encoding='utf8')
        self.assertEqual(eva.executor.get_std_lines(std_string), ['Situation normal all fantastic über!', 'No Errors.'])
        self.assertEqual(eva.executor.get_std_lines(std_bytes), ['Situation normal all fantastic über!', 'No Errors.'])
