# -*- coding: utf-8 -*-
from unittest import TestCase

import pydevd
pydevd.settrace('licho.iok.la', port=44957, stdoutToServer=True, stderrToServer=True)

import queue
import sys
sys.path.append('../')
from app.datasource.pengyuan.pengyuan import PengYuan


class TestPengYuan(TestCase):

    def test_create_query_condition(self, name='sunlc',
                                    # documentNo='2101141098701251234',
                                    # accountNo='637933021912',
                                    # openBankNo='1001',
                                    # mobile='168234214123',
                                    # subreportIDs='1234',
                                    # queryReasonID='fuck',
                                    refID=None):
        py = PengYuan()
        result = py.create_query_condition("123")
        assert result==b'<conditions><condition queryType="123"><item><name>name</name><value>sunlc</value></item></condition></conditions>'

    def test_query_personal_id_risk(self):
        sub_report = {10604: True, 10603: False, 14200: True}
        query_reason = {101: u"货款审批",
                        102: u"货款贷后管理",
                        103: u"贷款催收",
                        104: u"审核担保人信用",
                        105: u"担保/融资审批",
                        202: u"信用卡货后管理",
                        201: u"信用卡审批",
                        203: u"信用卡催收",
                        301: u"加强税源基础管理",
                        302: u"追缴欠税",
                        303: u"商户信用",
                        304: u"申报创新人才奖",
                        305: u"失业人员小额贷款担保审批",
                        306: u"深圳市外来务工人员积分入户申请",
                        401: u"车货保证保险审批",
                        402: u"审核国货保证保险担保人信用",
                        501: u"求职",
                        502: u"招聘",
                        503: u"异议处理",
                        901: u"了解个人信用",
                        999: u"其他"
                        }
        sr = '10604'
        qr = '101'
        py = PengYuan()
        result = py.query_personal_id_risk(name=u'孙立超',
                                           documentNo='210114198701251232',
                                           subreportIDs='10604',
                                           queryReasonID='101')
        print(result)

    def test_query(self, result):
        py = PengYuan()
        result = py.query(result, user_name_cn=u'阎伟晨',
                          mobile_num='15829551989',
                          personal_id='610102199407201510',
                          card_id='610527199005154925')
        print(result)

if __name__ == '__main__':
    tpy = TestPengYuan()
    result = queue.Queue()
    tpy.test_query(result)
