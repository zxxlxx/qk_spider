# -*- coding: utf-8 -*-
import json
import sys

from app.util.jvm import start_jvm

if sys.version[0] == '2':
    import Queue as queue
else:
    import queue

import threading
from abc import ABCMeta, abstractmethod

from app.datasource.cup.cup import ChinaUnionPay
from app.datasource.pengyuan.pengyuan import PengYuan
from app.datasource.zzc.zzc import Zzc
from app.util.logger import logger
from multiprocessing.pool import ThreadPool
from ..util.logger import logger


class Query:

    # TODO 这里以后可以用迭代的方式完成
    def __init__(self, third=None):
        # start_jvm()
        data_sources = [Zzc, PengYuan, ChinaUnionPay]
        # data_sources = [PengYuan]
        self.finders = set()
        for data_source in data_sources:
            try:
                self.add_third(data_source())
            except Exception as ex:
                logger.error(repr(ex))

        if third:
            self.finders.add(third)

        self.data_queue = queue.Queue()

    def __del__(self):
        # stop_jvm()
        pass

    def add_third(self, third):
        self.finders.add(third)

    def remove(self, third):
        self.finders.remove(third)

    def query(self, *args, **kwargs):
        threads = []
        for finder in self.finders:
            try:
                thread = threading.Thread(target=finder.query, args=(self.data_queue, args), kwargs=kwargs)
                threads.append(thread)
                thread.start()
            except Exception as e:
                logger.error(repr(e))

        for thread in threads:
            thread.join(10)
            if thread.isAlive():
                logger.error("查询线程{}超时".format(thread))

        final_result = {}
        while True:
            try:
                data, source = self.data_queue.get_nowait()
                final_result[source] = data
            except queue.Empty:
                break

        result_j = final_result
        print("结果" + repr(result_j))
        return result_j

