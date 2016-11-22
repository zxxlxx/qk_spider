from unittest import TestCase


# -*- coding: utf-8 -*-
from app.datasource.qianhai.qianhai import QianHai


class TestQianHai(TestCase):

    url = 'https://test-qhzx.pingan.com.cn:5443/do/dmz/query/blacklist/v1/MSC8004'

    def test_format_json_encBusData(self):
        qh = QianHai()
        qh.format_json_encBusData()

    def test_send_json_with_https(self):
        user_name_cn=u'谭俊峰',
        mobile_num='18192349450',
        personal_id='430102197111062010',
        card_id='4340624220484768'
        self.qh.send_json_with_https(surl=TestQianHai.url, json= '')

