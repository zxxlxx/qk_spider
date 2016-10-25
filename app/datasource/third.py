import abc


class Third(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def query(self, *args, **kwargs):
        pass