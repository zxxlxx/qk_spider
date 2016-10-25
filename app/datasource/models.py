# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class InnerResult(dict):
    """
    内部使用的数据格式
    """
    source = ''
    received_time = None
    data = {}


