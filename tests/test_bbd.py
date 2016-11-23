from unittest import TestCase

import sys
sys.path.append('..')

# -*- coding: utf-8 -*-
from app.datasource.bbd.bbd import BBD


class TestBBD(TestCase):

    def test_query(self):
        params = {'enterprise_name': u'乾康（上海）金融信息服务股份有限公司'}
        result = BBD.query(**params)

    def test_query_qyxx_jbxx(self):
        # result = BBD.query_qyxx_jbxx(company=u'乾康（上海）金融信息服务股份有限公司')
        # print(result.text)
        pass

    def test_query_qyxx_gdxx(self):
        pass


if __name__ == '__main__':
    t = TestBBD()
    # t.test_query_qyxx_jbxx()
    t.test_query()
    