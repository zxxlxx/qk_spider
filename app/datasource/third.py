import abc


class Third(metaclass=abc.ABCMeta):

    def __init__(self):
        self.source = ''

    @abc.abstractmethod
    def query(self, result, *args, **kwargs):
        pass

    @property
    def source(self):
        return self.source
