import unittest
import logging

import productstatus
import productstatus.api
import productstatus.event

import eva.adapter
import eva.executor
import eva.statsd


BLANK_UUID = '00000000-0000-0000-0000-000000000000'
RANDOM_UUID = 'f194279e-dfa8-45ff-ab62-1b03d89e9705'
RANDOM_USERNAME = 'nonamewrongname'
RANDOM_KEY = 'nokeywrongkey'


class TestThreddsAdapter(unittest.TestCase):

    def setUp(self):
        self.env = {
            'EVA_INPUT_DATA_FORMAT': BLANK_UUID,
            'EVA_INPUT_PRODUCT': BLANK_UUID,
            'EVA_INPUT_SERVICE_BACKEND': BLANK_UUID,
            'EVA_PRODUCTSTATUS_USERNAME': RANDOM_USERNAME,
            'EVA_PRODUCTSTATUS_API_KEY': RANDOM_KEY,
        }
        self.productstatus_api = productstatus.api.Api('http://localhost:8000')
        self.logger = logging
        self.zookeeper = None
        self.statsd = eva.statsd.StatsDClient()
        self.executor = eva.executor.NullExecutor(None, self.env, self.logger, self.zookeeper, self.statsd)

    def create_adapter(self):
        self.adapter = eva.adapter.ThreddsAdapter(self.env, self.executor, self.productstatus_api, self.logger, self.zookeeper, self.statsd)

    def test_create(self):
        """!
        @brief Test that ThreddsAdapter can be instantiated.
        """
        self.create_adapter()
