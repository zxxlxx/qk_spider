from unittest import TestCase

import sys
sys.path.append('..')

# -*- coding: utf-8 -*-
from app.datasource.bbd.bbd import BBD


class TestBBD(TestCase):

    def test_query(self):
        params = {'enterprise_name': u'乾康（上海）金融信息服务股份有限公司'}
        result, _ = BBD.query(**params)
        pass

    def test_query_qyxx_jbxx(self):
        result = BBD.query_qyxx_jbxx(company=u'乾康（上海）金融信息服务股份有限公司')
        assert result.text

    def test_query_qyxx_gdxx(self):
        result = BBD.query_qyxx_gdxx(company=u'乾康（上海）金融信息服务股份有限公司')
        assert result.text

if __name__ == '__main__':
    t = TestBBD()
    # t.test_query_qyxx_jbxx()

