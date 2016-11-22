# -*- coding: utf-8 -*-
import json
import sys

import concurrent

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
    data_sources = [Zzc, PengYuan]  # , ChinaUnionPay]
    data_queue = queue.Queue()

    def query(self, *args, **kwargs):
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.data_sources) * 5) as executor:

            future_func = {executor.submit(source().query, *args, **kwargs) for source in self.data_sources}
            try:
                for future in concurrent.futures.as_completed(future_func, 30):
                    try:
                        data = future.result()
                        self.data_queue.put(data)
                    except Exception as exc:
                        logger.error('查询异常: %s' % exc)
            except TimeoutError as te:
                logger.error(te)

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
