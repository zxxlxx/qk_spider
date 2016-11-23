from unittest import TestCase

import sys
sys.path.append('..')

# -*- coding: utf-8 -*-
from app.datasource.bbd.bbd import BBD


class TestBBD(TestCase):
    def test_query(self):
        result = BBD

    def test_query_qyxx_jbxx(self):
        result = BBD.query_qyxx_jbxx(company=u'乾康（上海）金融信息服务股份有限公司')
        print(result.text)

    def test_query_qyxx_gdxx(self):
        self.fail()


if __name__ == '__main__':
    t = TestBBD()
    t.test_query_qyxx_jbxx()