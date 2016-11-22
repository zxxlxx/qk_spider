from unittest import TestCase


# -*- coding: utf-8 -*-
from app.datasource.qianhai.dataSecurityUtil import DataSecurityUtil
from app.datasource.qianhai.qianhai import QianHai


class TestQianHai(TestCase):

    # url = 'https://test-qhzx.pingan.com.cn:5443/do/dmz/query/credoo/v1/MSC8005'
    url = 'https://test-qhzx.pingan.com.cn:5443/do/dmz/query/blacklist/v1/MSC8004'
    kwargs = {
        'batchNo': '29342fasdf',
        'personal_id': '430102197111062010',
        'user_name_cn': u'谭俊峰',
        'mobile_num': 'mobile_num',
        'card_id': '4340624220484768',
        'email': 'sunlc@qkjr.com.cn',
        'weibo_id': 'chinabhsun',
        'wechat_id': 'leecho_sun',
        'qq_id': '314509438',
        'taobao_id': 'chinabhsun',
        'jd_id': 'leechor_sun',
        'amazon_id': 'chinabhsun',
        'yhd_id': '',
        'auth_code': 'asdfasdhfh3',
        'auth_date': '2016-11-22 15:28:01',
        'seq_no': 'adfj'
    }

    def test_format_json_encBusData(self):
        qh = QianHai()
        result = qh.format_json_enc_busi_data(**TestQianHai.kwargs)
        print(result)

    def test_format_json_securityInfo(self):
        qh = QianHai()
        result = qh.format_json_security_info('fasdfasdfas')
        print(result)

    def test_send_json_with_https(self):
        qh = QianHai()
        user_name_cn=u'谭俊峰',
        mobile_num='18192349450',
        personal_id='430102197111062010',
        card_id='4340624220484768'
        # header = QianHai.format_json_header()
        # enc_busi_data = QianHai.format_json_enc_busi_data(**TestQianHai.kwargs)
        # busi_data = QianHai.format_json_busi_data(enc_busi_data)
        # security_info = QianHai.format_json_security_info(enc_busi_data)

        # message = '{' + header + ',' + busi_data + ',' + security_info + '}'

        message = '{"header":{"orgCode":"10000000","chnlId":"qhcs-dcs",' \
                  '"transNo":"Trandsfsd1f1qk","transDate":"2015-02-02 14:12:14",' \
                  '"authCode":"CRT001A2","authDate":"2015-12-02 4:12:14"},' \
                  '"busiData":"OHQMWgf3em8ngz2z3KIG+7jdAUksdWvBDHRfmifPF66qWqnRugeI/VgzgH1GC' \
                  '+2vFvFK/hHVayFDpoIB5ySok2N2tc10p+IgUGbGcr7P64JJ6EpRB7e6lB' \
                  'NThe/UTQHtpejMVprg2F/07jqxyUdDAHH1w+aMOz69N/elrujlA1SiAWr' \
                  'De9utHzmShKOEa+s+","securityInfo":{"signatureValue":"FR9T' \
                  'I1kRjQK20H/0Iu12HtTbpWajfUAEemtglH+SLdcSTNCTSYktbh2ZbupJ' \
                  'vhm4mQ1n9wXJNGduSO/lEBG9TMisnWOcNcrMY4Y7ReG99aYvieZHgJp' \
                  'RNQhXlKW3kJDoty7zT9FbJWyGWDRyBaj4IDB6bdlV2fiAK4sjrDwddh0=",' \
                  '"userName":"V_PA025_QHCS_DCS","userPassword":"af8f60dd6790' \
                  '6ac8287ba38343ee5f6b821ce6d9"}}'
        result = qh.send_json_with_https(surl=TestQianHai.url, json=message)

        print(result)

