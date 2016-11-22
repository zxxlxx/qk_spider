import base64
from unittest import TestCase

# -*- coding: utf-8 -*-
from cryptography.hazmat.primitives.asymmetric import rsa

from app.datasource.qianhai.dataSecurityUtil import DataSecurityUtil


class TestDataSecurityUtil(TestCase):
    key = 'SK803@!QLF-D25WEDA5E52DA'

    def test_digest(self):
        result = DataSecurityUtil.digest('weblogic1'.encode())
        assert result == 'af8f60dd67906ac8287ba38343ee5f6b821ce6d9'

    def test_sign_data(self):
        a = 'nimadeqianhaifuckqianhaiNMDCNMDQIANHAILAJIBITCHTHISisenoughlong'
        result = DataSecurityUtil.sign_data(a.encode())
        assert result.decode() == 'r+r2IIlA3AMf2MdDItqhs42XxlMyQ347VMN1OdUO5B+4' \
                                  '7CGYqAg9wI0+Xb708QcoHYqmcBg8hNvlcg+1sm6qDR0M8gV' \
                                  'a9CR/FL+7+VX5yMhs8mzf9chyIQ7CS9tx1XWAqIsKkR+ZFm' \
                                  'ALDx9wwysIOZzIP3oSgBAT7JH6763plbA='

        b = '6cV67bnedT6JYOO4lxJ9+p2p4J++wJVXGGAd87AEqG+STkFt9bbhGuz70I3HZrCIBJXVeidJ1E1k\r\nyALerm6I6A=='
        result2 = DataSecurityUtil.sign_data(b.encode())
        assert result2.decode() == 'x0Z/CC9AZYyfAkg9xuiIDKXm74LQfTW5LL4C1pUgsT8qkX9pp' \
                                   'WaUW6+vDPugxCQhL17hecA/neYz0GjQt6ekcNDu/7T5W4Wbxc77N' \
                                   '5Oa+DElCGBo+xxbaJFRby3GtiZNBwJoXR1pV5TH2B3nPe' \
                                   'qL/kChTSerQSc0OrfgbR2zrvA='

    def test_get_public_key(self):
        public_key = DataSecurityUtil.get_public_key()
        assert isinstance(public_key, rsa.RSAPublicKey)

    def test_verify_data(self):
        # DataSecurityUtil.verify_data()
        pass

    def test_get_private_key(self):
        DataSecurityUtil.get_private_key()

    def test_encrypt(self):
        message = "q3[945eorigjpeqtjg;oaitpq3tj;kjpq0ruq[345rijf".encode()
        encry = DataSecurityUtil.encrypt(message, TestDataSecurityUtil.key)
        assert encry == 'NALzh0JM3QTkZj2QD9+zAxtwnlQHLXBo0UvkTOl+JIyAyBVeQKj6zH5jxpeTRRlD'

    def test_decrypt(self):
        abc = "NALzh0JM3QTkZj2QD9+zAxtwnlQHLXBo0UvkTOl+JIyAyBVeQKj6zH5jxpeTRRlD".encode()
        message = DataSecurityUtil.decrypt(abc, TestDataSecurityUtil.key)
        assert message.decode() == 'q3[945eorigjpeqtjg;oaitpq3tj;kjpq0ruq[345rijf'


if __name__ == '__main__':
    # busi_data = '{"batchNo": "33adfsf323233", "records": [{"reasonCode": "01", "idNo": "362528198745421654", "idType": "0", "name": "唐唐", "seqNo": "r231545334545"}]}'
    busi_data = 'nimadeqianhaifuckqianhaiNMDCNMDQIANHAILAJIBITCHTHISisenoughlong'
    enc_busi_data = DataSecurityUtil.encrypt(busi_data.encode(), TestDataSecurityUtil.key)
    sig_value = DataSecurityUtil.sign_data(enc_busi_data).decode()
