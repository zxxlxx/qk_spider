from unittest import TestCase
import pytest
import requests

from app.datasource.zzc.zzc import Zzc


# -*- coding: utf-8 -*-
class TestZzc(TestCase):
    def test_show_by_institution(self):
        zzc = Zzc()
        result = zzc.show_by_institution('AP201607179336771654')
        assert result[1] == requests.codes.ok
