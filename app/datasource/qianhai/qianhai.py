import datetime
import json
import sys
import os
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

    headers = {'Content-Type': 'application/json; charset=utf8'}

    def __format_json_header(self):
        transNo = datetime.now.strftime('YYYYMMddhhmmss')
        transDate = datetime.now.strftime('%Y-%m-%d %h:%m:%s')

        header = r'header:{{' \
                 r'"orgCode: "{orgCode}", ' \
                 r'chnlId: "{chnlId}",' \
                 r'transNo: "{transNo}",' \
                 r'transDate: "{transDate}",' \
                 r'authCode: "{authCode}",' \
                 r'authDate: "{authDate}"}}'.format_map(orgCode=self.org_code,
                                                        chnlId=self.chnl_id,
                                                        transNo=self.transNo,
                                                        transDate=transDate,
                                                        authCode=self.auth_code,
                                                        authDate=transDate)
        return header

    def __format_json_encBusData(self, *args, **kwargs):
        enc_bus_data = r'busiData:{{' \
                       r'idNo: "{idNo},' \
                       r'idTpye: "{idType},' \
                       r'name: "{name}",' \
                       r'mobileNo: "{mobileNo}",' \
                       r'cardNo: "{cardNo}",' \
                       r'reasonNo: "{reasonNo}",' \
                       r'email: "{email}",' \
                       r'weiboNo: "{weiboNo}",' \
                       r'weixinNo: "{weixinNo}",' \
                       r'qqNo: "{qqNo}",' \
                       r'taobaoNo: "{taobaoNo}",' \
                       r'jdNo: "{jdNo}",' \
                       r'amazonNo: "{amazonNo}",' \
                       r'yhdNo: "{yhdNo}",' \
                       r'entityAuthCode: "{entityAuthCode}",' \
                       r'entityAuthDate: "{entityAuthDate}",' \
                       r'seqNo: "{seqNo}"'.format_map(SafeSub(kwargs))
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


