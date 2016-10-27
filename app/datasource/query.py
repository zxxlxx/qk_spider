import json
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

        data_sources = [PengYuan(), Zzc(), ChinaUnionPay()]
        self.finders = set()
        for data_source in data_sources:
            self.add_third(data_source)

        if third:
            self.finders.add(third)

        self.data_queue = queue.Queue()

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
            thread.join(5)
            if thread.isAlive():
                logger.error("查询线程{}超时".format(thread))

        final_result = {}
        while True:
            try:
                data, source = self.data_queue.get_nowait()
                final_result[source] = data
            except queue.Empty:
                break

        result_j = json.dumps(final_result)
        print(result_j)
        return result_j

