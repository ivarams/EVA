import eva.job


class BaseAdapter(object):
    """
    Adapters contain all the information and configuration needed to translate
    a Productstatus event into job execution.
    """

    def __init__(self, api):
        """
        @param api Productstatus API object
        """
        self.api = api

    def match(self, event, resource):
        """
        @brief Check if the event and resource fits this adapter.
        @param event The message sent by the Productstatus server.
        @param resource The Productstatus resource referred to by the event.
        @returns A Job object if the message fits this adapter, else None.
        """
        raise NotImplementedError()

    def finish(self, job):
        """
        @brief Finish a job that was previously created by 'match', e.g. by updating Productstatus.
        @param job A Job object.
        """
        pass


class NullAdapter(BaseAdapter):
    """
    An adapter that matches nothing.
    """
    def match(self, event, resource):
        return


class TestDownloadAdapter(BaseAdapter):
    """
    An adapter that downloads any posted DataInstance using wget.
    """
    def match(self, event, resource):
        if event.resource != 'datainstance':
            return
        job = eva.job.Job(self)
        job.set_status(eva.job.PREPARED)
        job.command = """#!/bin/bash -x
        echo "Running on host: `hostname`"
        echo "Working directory: `pwd`"
        echo "Productstatus DataInstance points to %(url)s"
        echo "Now downloading file..."
        wget %(url)s
        echo "Finished."
        """ % {
            'url': resource.url
        }
        return job
