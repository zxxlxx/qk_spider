# -*- coding: utf-8 -*-
from unittest import TestCase
import pytest
import requests
import json
from app.datasource.zzc.zzc import Zzc


class TestZzc(TestCase):
    data = {"loan_term": 12, "loan_amount": 20000, "loan_purpose": "fangdai", "loan_type": "车货",
            "applicant": {"mobile": "18710723119", "name": "wangbing", "pid": "610527199005154925"}}

    def test_show_by_institution(self):
        result = Zzc.show_by_institution('AP201607179336771654')
        assert result[1]

    def test_create(self):
        json_data = json.dumps(self.data)
        result = Zzc.create(json_data)
        assert result

    def test_update(self):
        json_data = json.dumps(self.data)
        result = Zzc.update('AP201607179336771654', json_data)
        assert result

    def test_delete(self):
        pass

    def test_anti_fraud_report(self):
        pass

    def test_rule_report(self):
        pass
