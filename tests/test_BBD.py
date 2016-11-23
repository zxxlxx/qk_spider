from unittest import TestCase


# -*- coding: utf-8 -*-
from app.datasource.bbd.bbd import BBD


class TestBBD(TestCase):
    def test_query(self):
        self.fail()

    def test_query_qyxx_jbxx(self):
        BBD.query_qyxx_jbxx(company='qiankang', qyxx_id='adf')

    def test_query_qyxx_gdxx(self):
        self.fail()
