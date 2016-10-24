from unittest import TestCase


# -*- coding: utf-8 -*-
from app.datasource.cup.cup import ChinaUnionPay


class TestChinaUnionPay(TestCase):

    def test_get_data(self):
        cup =ChinaUnionPay()
        cup.get_data("6212263700008736284", "孙立超", "210114198701251232", "15829551989")
