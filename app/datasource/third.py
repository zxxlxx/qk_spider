import abc
import copy


class Third(metaclass=abc.ABCMeta):
    params_mapping = {}

    def __init__(self):
        self.source = ''

    @abc.abstractmethod
    def query(self, result, *args, **kwargs):
        pass

    @property
    def source(self):
        return self.source

    def pre_query_params(self, *args, **kwargs):
        """
        与标准变量名之间的转换
        :param args:
        :param kwargs:
        :return:
        """
        temp = copy.deepcopy(kwargs)
        for arg in kwargs:
            if self.params_mapping.get(arg) is not None:
                temp.update({self.params_mapping.get(arg): temp.pop(arg)})
            else:
                temp.pop(arg)
        return temp
