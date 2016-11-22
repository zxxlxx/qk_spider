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
        header = QianHai.format_json_header()
        enc_busi_data = QianHai.format_json_enc_busi_data(**TestQianHai.kwargs)
        busi_data = QianHai.format_json_busi_data(enc_busi_data)
        security_info = QianHai.format_json_security_info(enc_busi_data)

        message = '{' + header + ',' + busi_data + ',' + security_info + '}'

        # message = {"header":{"orgCode":"10000000","chnlId":"qhcs-dcs","transNo":"Trandsfsd1f1qk","transDate":"2015-02-02 14:12:14","authCode":"CRT001A2","authDate":"2015-12-02 14:12:14"},"busiData":"OHQMWgf3em8ngz2z3KIG+7jdAUksdWvBDHRfmifPF66qWqnRugeI/VgzgH1GC+2vFvFK/hHVayFD\r\npoIB5ySok2N2tc10p+IgUGbGcr7P64JJ6EpRB7e6lBNThe/UTQHtpejMVprg2F/07jqxyUdDAHH1\r\nw+aMOz69N/elrujlA1SiAWrDe9utHzmShKOEa+s+","securityInfo":{"signatureValue":"FR9TI1kRjQK20H/0Iu12HtTbpWajfUAEemtglH+SLdcSTNCTSYktbh2ZbupJvhm4mQ1n9wXJNGdu\r\nSO/lEBG9TMisnWOcNcrMY4Y7ReG99aYvieZHgJpRNQhXlKW3kJDoty7zT9FbJWyGWDRyBaj4IDB6\r\nbdlV2fiAK4sjrDwddh0=\r\n","userName":"V_PA025_QHCS_DCS","userPassword":"af8f60dd67906ac8287ba38343ee5f6b821ce6d9"}}

        message = '{"header":{"orgCode": "10000000", "chnlId": "qhcs-dcs","transNo": "201611221479824961","transDate": "2016-11-22 22:29:21","authCode": "CRT001A2","authDate": "2016-11-22 22:29:21"},"busiData": "OHQMWgf3em+DZKCpT63TC1pryHgDXmkK6Ei98pLWbW30szr1AkDFuW0eraalYIUs2aGPjgPeQpWvhEYhyfXe1y3RbT73iolClbaPftfG7wEsMyy0/YF5YuflTbO+PKsBEpJu7vCFm4GcejP8DzFczHib5GPyJWP7+SrVpTdzr5BkiCJVQBhsi4MtBongEG2ZY2l9YkynxH04GtXG5oGpI5AXjWI1ptn9eo+RUhPzzysgnNB+al8TXpZHqhFQaCUYRQynHj+iQiLy/Y9T09YFW08lUZqP/dPUhNoBoHSajRUALNnahs/UHM7ICacQ5cNFDBO4gn5jxl5pRDLgGN7Ee3l0GjDr+S149U2ItQFB9FIr1UJJ8txnjTi9qG+QuOnlCF+QOXBsZ7uUQp+dv8zz/sCkUv39C6ppFNe/E6q5GY+WUHSZeo/NibS6aRd1QRJfxXtLklSeHidzt11DvAFnr3jEgGXWkKPaDd8bH20D/cBcD9N1N/fr20uwVg/DV9KAeMSAZdaQo9px5aS/GsLHh2d96GsiZQdQtvfCTUMM+FsjF63G14wxQ6lORcHeUleMEXcwvGLEG8zwBZUcE2XOnA==","securityInfo":{"signatureValue": "I0i4Wu64NCTYLhTDdCW3gkGJ0HbBWvWY4GDKW/BbZTvjd4vjnJFE+eEX50id9pRaJqBgDO3NSJbmSB7Kd0vybJUT3PVcxmEjMxD5w18LzSxWVYCv8QDJqQChBV/gUyhwFNPT2Yh2jkL4VcmoSYR0Ga8PQ2J6trxHeMwY3xqoZ18=","userName": "V_PA025_QHCS_DCS","userPassword": "af8f60dd67906ac8287ba38343ee5f6b821ce6d9"}}'
        result = QianHai.send_json_with_https(surl=TestQianHai.url, json=message)

        print(result)

