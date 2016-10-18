# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class DataFormat(dict):
    """
    内部使用的数据格式
    """

    pass


class Query(metaclass=ABCMeta):

    @abstractmethod
    def query(self, *args, **kwargs):
        pass


