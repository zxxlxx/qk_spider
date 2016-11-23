# -*- coding: utf-8 -*-
import concurrent
import inspect
import queue

import requests

from app.datasource.third import Third
from app.datasource.utils.tools import params_to_dict
from app.util.logger import logger


class BBD(Third):

    source = 'BBD'
    params_mapping = {
        'enterprise_name': 'company',
        'begin_date': 'start',
        'end_date': 'end',
    }

    @classmethod
    def query(cls, *args, **kwargs):
        kwargs = BBD.pre_query_params(*args, **kwargs)
        result = queue.Queue()

        with concurrent.futures.ThreadPoolExecutor(max_workers=18) as executor:
            func_params = {func[1]: {param: kwargs.get(param) for param
                                     in inspect.signature(func[1]).parameters.keys()
                                     if kwargs.get(param) is not None}
                           for func in inspect.getmembers(BBD, predicate=inspect.ismethod)
                           if func[0].startswith('query_')}

            future_func = {executor.submit(func, **func_params[func]) for func in func_params.keys()}
            try:
                for future in concurrent.futures.as_completed(future_func, 15):
                    try:
                        data = future.result()
                        result.put(data)
                    except Exception as exc:
                        logger.error(exc)
            except TimeoutError as te:
                logger.error(te)

        result_final = []
        while True:
            try:
                data = result.get_nowait()
                if data:
                    result_final.append(data)
            except queue.Empty:
                break
        return result_final, BBD.source

    @classmethod
    def query_qyxx_jbxx(cls, company=None, qyxx_id=None):
        """
        企业工商数据-基本信息(Company与qyxx_id 二选一)
        :param company: 企业名称，精确匹配(key)
        :param qyxx_id: 企业信息ID
        :param qk: 用户唯一性验证
        :return:
        """
        url = 'http://dataom.api.bbdservice.com/api/bbd_qyxx_jbxx/'
        kwargs = params_to_dict(1)
        kwargs['ak'] = '6218684779c4132bbf9180e20e2ebc4d'
        result = requests.get(url=url, params=kwargs)
        return result

    @classmethod
    def query_qyxx_gdxx(cls, company=None, qyxx_id=None, page=None, page_size=None, start=None, end=None):
        """
        股东信息API查询
        :param company: 企业名称，精确匹配(key)
        :param qyxx_id: 企业名称，精确匹配(key)
        :param page: 企业名称，精确匹配(key)
        :param page_size: 每页显示的条数
        :param start: bbd_dotime ：格式2016-01-29
        :param end: bbd_dotime ：格式2016-01-29
        :return:
        """
        url = 'http://dataom.api.bbdservice.com/api/bbd_qyxx_gdxx/'
        kwargs = params_to_dict(1)
        kwargs['ak'] = '91718c463d479eeb5bcf41b8bac114'
        result = requests.get(url=url, params=kwargs)
        return result
