# -*- coding: utf-8 -*-
from unittest import TestCase
import pytest
import requests
import json
from app.datasource.zzc.zzc import Zzc


class TestZzc(TestCase):
    apply_id = 'AP201607179336771654'
    data = {
        "loan_term": 12,
        "loan_amount": 20000,
        "loan_purpose": "fangdai",
        "loan_type": "车货",
        "mobile_num": "18710723118",
        "user_name_cn": "王兵",
        "personal_id": "610527199005154925"
    }
    zzc = Zzc()

    def test_show(self):
        result = self.zzc.af_show(TestZzc.apply_id)
        assert result[1]

    def test_create(self):
        result = self.zzc.af_create(**self.data)
        assert result

    def test_update(self):
        result = self.zzc.af_update(TestZzc.apply_id, self.data)
        assert result

    def test_delete(self):
        result = self.zzc.af_delete(TestZzc.apply_id)
        assert result

    def test_anti_fraud_report(self):
        result = self.zzc.af_report(**self.data)
        assert result

    def test_rule_report(self):
        result = self.zzc.af_rule_report(TestZzc.apply_id)
        assert result

    def test_black_search(self):
        result = self.zzc.black_search("孙立超", "210114198701251232", "15829551989")
