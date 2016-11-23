# -*- coding: utf-8 -*-
import requests

from app.datasource.third import Third
from app.datasource.utils.tools import params_to_dict


class BBD(Third):

    source = 'BBD'
    params_mapping = {
        'user_name_cn': 'name',
        'personal_id': 'documentNo',
        'query_reason_id': 'queryReasonID',
        'card_id': 'cardNos',
        'begin_date': 'beginDate',
        'end_date': 'endDate',
        'card_id': 'accountNo',
        'mobile_num': 'mobile',
        'py_open_bank_id': 'cardNos',
        'license_no': 'licenseNo',
        'car_type': 'carType'
    }

    def query(self, *args, **kwargs):
        pass

    @staticmethod
    def query_qyxx_jbxx(company=None, qyxx_id=None):
        """
        企业工商数据-基本信息(Company与qyxx_id 二选一)
        :param company: 企业名称，精确匹配(key)
        :param qyxx_id: 企业信息ID
        :param qk: 用户唯一性验证
        :return:
        """
        url = 'http://dataom.api.bbdservice.com/api/bbd_qyxx_jbxx'
        kwargs = params_to_dict(1)
        kwargs['ak'] = '6218684779c4132bbf9180e20e2ebc4d'
        result = requests.get(url=url, params=kwargs)
        return result

    @staticmethod
    def query_qyxx_gdxx(company=None, qyxx_id=None, page=None, page_size=None, start=None, end=None):
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
        url = 'http://dataom.api.bbdservice.com/api/bbd_qyxx_gdxx'
        kwargs = params_to_dict(1)
        kwargs['ak'] = '91718c463d479eeb5bcf41b8bac114'
        result = requests.get(url=url, params=kwargs)
