
import json
import sys
import os
from datetime import datetime

import requests
from pathlib import Path

from app.datasource.third import Third
from app.datasource.zzc.tranform import format_result
from ..utils.tools import params_to_dict, SafeSub
from ..configuration import config


class QianHai(Third):
    """
    钱海的查询接口
    """
    qh_config = config.get('qianhai')
    url = qh_config.get('url')
    user_name = qh_config.get('userName')
    user_password = qh_config.get('userPassword')
    net_type = qh_config.get('netType')
    trans_name = qh_config.get('transName')
    product_id = qh_config.get('productId')
    api_version = qh_config.get('apiVer')
    org_code = qh_config.get('orgCode')
    chnl_id = qh_config.get('chnlId')
    auth_code = qh_config.get('authCode')
    source = 'qianhai'

    headers = {'Content-Type': 'application/json; charset=utf8'}

    def query(self):
        pass

    def __format_json_header(self):
        transNo = datetime.now().strftime('qkjr_%Y%m%d%s')
        transDate = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        header = r'"header":{{' \
                 r'"orgCode": "{orgCode}", ' \
                 r'"chnlId": "{chnlId}",' \
                 r'"transNo": "{transNo}",' \
                 r'"transDate": "{transDate}",' \
                 r'"authCode": "{authCode}",' \
                 r'"authDate": "{authDate}"}}'.format(orgCode=QianHai.org_code,
                                                        chnlId=QianHai.chnl_id,
                                                        transNo=transNo,
                                                        transDate=transDate,
                                                        authCode=QianHai.auth_code,
                                                        authDate=transDate)
        return header

    def format_json_encBusData(self, *args, **kwargs):
        enc_bus_data = r'"busiData":{{' \
                       r'"batchNo": "{batchNo}",' \
                       r'"records":[' \
                       r'"idNo: "{idNo}",' \
                       r'"idTpye: "{idType}",' \
                       r'"name": "{name}",' \
                       r'"mobileNo": "{mobileNo}",' \
                       r'"cardNo": "{cardNo}",' \
                       r'"reasonNo": "{reasonNo}",' \
                       r'"email": "{email}",' \
                       r'"weiboNo": "{weiboNo}",' \
                       r'"weixinNo": "{weixinNo}",' \
                       r'"qqNo": "{qqNo}",' \
                       r'"taobaoNo": "{taobaoNo}",' \
                       r'"jdNo": "{jdNo}",' \
                       r'"amazonNo": "{amazonNo}",' \
                       r'"yhdNo": "{yhdNo}",' \
                       r'"entityAuthCode": "{entityAuthCode}",' \
                       r'"entityAuthDate": "{entityAuthDate}",' \
                       r'"seqNo": "{seqNo}"]'.format_map(SafeSub(kwargs))
        return enc_bus_data

    def __format_json_securityInfo(self, *args, **kwargs):

        security_info = r'securityInfo:{{' \
                        r'signatureValue: "{signatureValue}",' \
                        r'userName: "{userName}",' \
                        r'userPassword: "{userPassword}"'.format()
        return security_info

    def __format_json_xhd(self, *args, **kwargs):
        pass

    def send_json_with_https(self, surl, json):
        headers = self.headers
        headers['Content-Length'] = len(json)  # 这里现在不对
        json_request = json
        result = requests.post(surl,
                               json=json_request,
                               headers=QianHai.headers)


