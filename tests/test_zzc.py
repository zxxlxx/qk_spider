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
        "applicant": {
            "mobile": "18710723119",
            "name": "王兵",
            "pid": "610527199005154925"
        }
    }

    def test_show_by_institution(self):
        result = Zzc.show_by_institution(TestZzc.apply_id)
        assert result[1]

    def test_create(self):
        result = Zzc.create(self.data)
        assert result

    def test_update(self):
        result = Zzc.update(TestZzc.apply_id, self.data)
        assert result

    def test_delete(self):
        result = Zzc.delete(TestZzc.apply_id)
        assert result

    def test_anti_fraud_report(self):
        result = Zzc.anti_fraud_report(TestZzc.apply_id)
        assert result

    def test_rule_report(self):
        result = Zzc.rule_report(TestZzc.apply_id)
        assert result

