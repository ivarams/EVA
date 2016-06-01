import datetime
import dateutil.tz
import copy
import time
import uuid

import eva
import eva.rpc
import eva.event

import productstatus.exceptions


class Eventloop(object):
    """!
    The main loop.
    """

    RECOVERABLE_EXCEPTIONS = (eva.exceptions.RetryException, productstatus.exceptions.ServiceUnavailableException,)

    def __init__(self,
                 productstatus_api,
                 listeners,
                 adapter,
                 environment_variables,
                 logger,
                 ):
        self.listeners = listeners
        self.productstatus_api = productstatus_api
        self.adapter = adapter
        self.env = environment_variables
        self.logger = logger
        self.event_queue = []
        self.do_shutdown = False
        self.message_timestamp_threshold = datetime.datetime.fromtimestamp(0, dateutil.tz.tzutc())

    def poll_listeners(self):
        """!
        @brief Poll for new messages from all message listeners.
        """
        for listener in self.listeners:
            try:
                event = listener.get_next_event()
                assert isinstance(event, eva.event.Event)
            except eva.exceptions.EventTimeoutException:
                continue
            except eva.exceptions.InvalidEventException as e:
                self.logger.warning('Received invalid event: %s', e)
                continue
            self.event_queue += [event]

    def queue_empty(self):
        """!
        @returns True if the event queue is empty, False otherwise.
        """
        return len(self.event_queue) == 0

    def process_first_in_queue(self):
        """!
        @brief Process the first event in the event queue.
        """
        if self.queue_empty():
            return
        event = self.event_queue[0]
        # Discard message if below timestamp threshold
        if event.timestamp() < self.message_timestamp_threshold:
            self.logger.warning('Skip processing event because resource is older than threshold: %s vs %s',
                                event.timestamp(),
                                self.message_timestamp_threshold)
        else:
            if isinstance(event, eva.event.RPCEvent):
                event.data.set_executor_instance(self)
                self.process_rpc_event(event)
            else:
                delay = event.get_processing_delay().total_seconds()
                if delay > 0:
                    self.logger.info('Sleeping %.1f seconds before processing next event due to event delay',
                                     delay)
                    time.sleep(delay)
                self.process_normal_event(event)
        event.acknowledge()

    def sort_queue(self):
        """!
        @brief Ensure that RPC requests are moved to the top of the queue.
        """
        self.event_queue.sort(key=lambda event: not isinstance(event, eva.event.RPCEvent))

    def shift_queue(self):
        """!
        @brief Delete the first event in the event queue.
        """
        if not self.queue_empty():
            del self.event_queue[0]

    def __call__(self):
        """!
        @brief Main loop. Checks for Productstatus events and dispatchs them to the adapter.
        """
        self.logger.info('Start processing events and RPC calls.')
        while not self.do_shutdown:
            self.poll_listeners()
            self.sort_queue()
            try:
                self.process_first_in_queue()
            except self.RECOVERABLE_EXCEPTIONS as e:
                self.logger.error('Restarting processing of event in 2 seconds due to error: %s', e)
                time.sleep(2.0)
                continue
            self.shift_queue()
        self.logger.info('Stop processing events and RPC calls.')

    def process_normal_event(self, event):
        """!
        @brief Process a non-RPC event.
        """
        self.logger.info('Start processing event: %s', str(event))
        self.adapter.validate_and_process_resource(event.id(), event.data)
        self.logger.info('Finished processing event: %s', str(event))

    def process_rpc_event(self, event):
        """!
        @brief Process the latest RPC message in the RPC queue.
        """
        self.logger.info('Processing RPC request: %s', str(event))
        try:
            event.data()
        except eva.exceptions.RPCFailedException as e:
            self.logger.error('Error while executing RPC request: %s', e)
        self.logger.info('Finished processing RPC request: %s', str(event))

    def set_message_timestamp_threshold(self, timestamp):
        """!
        @brief Fast-forward the message queue to a specific time.
        """
        ts = copy.copy(timestamp)
        if ts.tzinfo is None or ts.tzinfo.utcoffset(ts) is None:
            self.logger.warning('Received a naive datetime string, assuming UTC')
            ts = ts.replace(tzinfo=dateutil.tz.tzutc())
        self.message_timestamp_threshold = copy.copy(ts)
        self.logger.info('Forwarding message queue threshold timestamp to %s', self.message_timestamp_threshold)

    def process_all_in_product_instance(self, product_instance):
        """!
        @brief Process all child DataInstance objects of a ProductInstance.
        """
        while not self.do_shutdown:
            try:
                self.logger.info('Fetching DataInstance resources descended from %s', product_instance)
                instances = self.productstatus_api.datainstance.objects.filter(data__productinstance=product_instance).order_by('created')
                index = 1
                count = instances.count()
                self.logger.info('Processing %d DataInstance resources...', count)
                for resource in instances:
                    self.logger.info('[%d/%d] Processing %s', index, count, resource)
                    eva.retry_n(lambda: self.adapter.validate_and_process_resource(uuid.uuid4(), resource),
                                exceptions=self.RECOVERABLE_EXCEPTIONS,
                                give_up=0)
                    index += 1
            except self.RECOVERABLE_EXCEPTIONS as e:
                self.logger.error('A recoverable error occurred: %s', e)
                time.sleep(2.0)
                continue
            break

    def process_data_instance(self, data_instance_uuid):
        """!
        @brief Process a single DataInstance resource.
        """
        resource = self.productstatus_api.datainstance[data_instance_uuid]
        self.logger.info('Processing DataInstance %s', resource)
        self.adapter.validate_and_process_resource(uuid.uuid4(), resource)
        self.logger.info('Finished processing DataInstance %s', resource)

    def blacklist_uuid(self, uuid):
        """!
        @brief Omit processing a specific DataInstance for the lifetime of this EVA process.
        """
        self.adapter.blacklist_add(uuid)

    def forward_to_uuid(self, uuid):
        """!
        @brief Skip all Productstatus messages where parents or children do not
        contain the specified UUID. That includes Product, ProductInstance,
        Data, DataInstance, ServiceBackend and Format resources.
        """
        self.adapter.forward_to_uuid(uuid)

    def shutdown(self):
        """!
        @brief Shutdown EVA after the current resource has been processed.
        """
        self.logger.info('Received shutdown call, will stop processing resources.')
        self.do_shutdown = True
