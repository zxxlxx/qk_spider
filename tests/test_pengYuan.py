# -*- coding: utf-8 -*-
from unittest import TestCase
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

    def test_query_personal_id_risk(self, name, documentNo):
        sub_report = {10604: True, 10603: False, 14200: True}
        query_reason = {101: "货款审批",
                        102: "货款贷后管理",
                        103: "贷款催收",
                        104: "审核担保人信用",
                        105: "担保/融资审批",
                        202: "信用卡货后管理",
                        201: "信用卡审批",
                        203: "信用卡催收",
                        301: "加强税源基础管理",
                        302: "追缴欠税",
                        303: "商户信用",
                        304: "申报创新人才奖",
                        305: "失业人员小额贷款担保审批",
                        306: "深圳市外来务工人员积分入户申请",
                        401: "车货保证保险审批",
                        402: "审核国货保证保险担保人信用",
                        501: "求职",
                        502: "招聘",
                        503: "异议处理",
                        901: "了解个人信用",
                        999: "其他"
                        }
        sr = '10604'
        qr = '101'
        result = self.query_personal_id_risk(name, documentNo, sr, qr)
