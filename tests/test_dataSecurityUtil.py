import base64
from unittest import TestCase

# -*- coding: utf-8 -*-
from app.datasource.qianhai.dataSecurityUtil import DataSecurityUtil


class TestDataSecurityUtil(TestCase):
    key = 'SK803@!QLF-D25WEDA5E52DA'.encode()

    def test_digest(self):
        self.fail()

    def test_sign_data(self):
        a = 'a'
        result = DataSecurityUtil.sign_data(a.encode())
        assert a == 'AlVsreY14EX3UwWlRms1R6NrX2N1XMKQMqdfkiz5eZihn5lnSbkufxFJjxencEyYXhmJGkUy' \
                    'gUS8tI+oHwzXZBEY36SdhsE1R7PSgAuew2DAX2nQDcqPd+XVt3AW2c5PHpM0PJQ' \
                    'o8xB6mh/Cx6PsCyzFxs1pFwaU72aMfutmaQ8='

    def test_getPublicKey(self):
        self.fail()

    def test_get_private_key(self):
        DataSecurityUtil.get_private_key()

    def test_encrypt(self):
        message = "q3[945eorigjpeqtjg;oaitpq3tj;kjpq0ruq[345rijf".encode()
        encry = DataSecurityUtil.encrypt(message, TestDataSecurityUtil.key)
        print(encry)

    def test_decrypt(self):
        abc = "NALzh0JM3QTkZj2QD9+zAxtwnlQHLXBo0UvkTOl+JIyAyBVeQKj6zH5jxpeTRRlD".encode()
        message = DataSecurityUtil.decrypt(abc, TestDataSecurityUtil.key)

        print(message.decode())


if __name__ == '__main__':
    # busi_data = '{"batchNo": "33adfsf323233", "records": [{"reasonCode": "01", "idNo": "362528198745421654", "idType": "0", "name": "唐唐", "seqNo": "r231545334545"}]}'
    busi_data = 'nimadeqianhaifuckqianhaiNMDCNMDQIANHAILAJIBITCHTHISisenoughlong'
    enc_busi_data = DataSecurityUtil.encrypt(busi_data.encode(), TestDataSecurityUtil.key)
    sig_value = DataSecurityUtil.sign_data(enc_busi_data)
    print(sig_value.decode())
