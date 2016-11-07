import eva
import eva.globe


class BaseListener(eva.ConfigurableObject, eva.globe.GlobalMixin):
    """!
    @brief Abstract base class for execution engines.
    """

    def __init__(self, globe, environment_variables, **kwargs):
        self.globe = globe
        self.env = environment_variables
        self.kwargs = kwargs
        self.read_configuration()
        self.print_environment(prefix='Listener configuration: ')

    def setup_listener(self):
        """!
        @brief Create objects neccessary to listen for events.
        """
        raise NotImplementedError()

    def close_listener(self):
        """!
        @brief Close any connections to the event listener.
        """
        raise NotImplementedError()

    def get_next_event(self):
        """!
        @brief Get the next event that should be processed.
        """
        raise NotImplementedError()

    def acknowledge(self):
        """!
        @brief Acknowledge that the most recent event has been taken
        responsibility for.
        """
        raise NotImplementedError()
