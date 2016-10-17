from unittest import TestCase


# -*- coding: utf-8 -*-
from app.datasource.pengyuan.pengyuan import PengYuan


class TestPengYuan(TestCase):

    def test_create_query_condition(self):
        py = PengYuan()
        py.create_query_condition()