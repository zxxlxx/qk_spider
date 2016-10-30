import queue
from unittest import TestCase


# -*- coding: utf-8 -*-
from app.datasource.cup.cup import ChinaUnionPay


class TestChinaUnionPay(TestCase):

    def test_get_data(self, result):
        cup =ChinaUnionPay()
        result = queue.Queue()
        cup.query(result, user_name_cn=u'孙立超',
                  mobile_num='15829551989',
                  personal_id='210114198701251232',
                  card_id='610527199005154925')
        print(result)

if __name__ == '__main__':
    tcup = TestChinaUnionPay()
    result = queue.Queue()
    tcup.test_get_data(result)
