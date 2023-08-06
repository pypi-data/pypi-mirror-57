class Singleton:
    """Implementation of the borg/singleton pattern"""
    _shared_state = {}

    def __init__(self):
        """Initialize borg class"""
        self.__dict__ = self._shared_state
