import eva.exceptions


PROPERTIES = [
    'group_id',
    'logger',
    'mailer',
    'productstatus',
    'statsd',
    'zookeeper',
]


class Global(object):
    """!
    @brief Collection of objects that are of use to the entire application.
    Pass the instance of this class to any object that will need access to
    logging, mail services, ZooKeeper, StatsD, etc.
    """

    def __init__(self, **kwargs):
        try:
            for prop in PROPERTIES:
                setattr(self, prop, kwargs[prop])
        except KeyError:
            raise eva.exceptions.EvaException("Expected to receive '%s' as a keyword argument to class initialization" % prop)
        for key in kwargs:
            if key not in PROPERTIES:
                raise eva.exceptions.EvaException("The Globe object does not accept '%s' as a keyword argument, please see eva.globe.PROPERTIES" % key)


class GlobalMixin(object):
    """!
    @brief Mixin class for classes using the Global class, for easy access to
    the Global variables.

    The class member 'global' needs to be set to a Global instance for this
    mixin to work.
    """

    def set_globe(self, globe):
        self.globe = globe

    def __getattr__(self, name):
        if name not in PROPERTIES:
            raise AttributeError(name)
        return getattr(self.globe, name)
