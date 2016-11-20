import base64
from unittest import TestCase


# -*- coding: utf-8 -*-
from app.datasource.qianhai.dataSecurityUtil import DataSecurityUtil


class TestDataSecurityUtil(TestCase):
    key = 'SK803@!QLF-D25WEDA5E52DA'.encode()

    def test_digest(self):
        self.fail()

    def test_getPublicKey(self):
        self.fail()

    def test_encrypt(self):
        message = "Fuchk QianHai".encode()
        encry = DataSecurityUtil.encrypt(message, TestDataSecurityUtil.key)
        print(encry)

    def test_decrypt(self):
        abc = "eC3XXlsQd4RJD5XN3vcKNg==".encode()
        message = DataSecurityUtil.decrypt(abc, TestDataSecurityUtil.key)

        print(message.decode())
