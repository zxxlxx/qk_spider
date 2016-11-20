# -*- coding: utf-8 -*-
import base64

from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

class DataSecurityUtil:


    def digest(self, origin_byte):
        pass

    def getPublicKey(self):
        pass

    def get_private_key(self):
        pass

    @staticmethod
    def encrypt(origin, key):
        """
        加密，算法3DES，模式：ECB
        :param origin: 待加密的bytes
        :param key: 密钥
        :return: 加密后的BASE64编码
        """
        cipher = Cipher(algorithms.TripleDES(key), modes.ECB(), default_backend())
        encryptor = cipher.encryptor()
        padder = padding.PKCS7(64).padder()
        padder_data = padder.update(origin) + padder.finalize()
        print(len(padder_data))
        ct = encryptor.update(padder_data) + encryptor.finalize()
        result = base64.b64encode(ct)
        return result

    @staticmethod
    def decrypt(data, key):
        """
        解密：算法：3DES
        :param data: 待解密bytes
        :param key: 密钥
        :return: 解密厚的bytes
        """

        data = base64.b64decode(data)
        cipher = Cipher(algorithms.TripleDES(key), modes.ECB(), default_backend())
        decryptor = cipher.decryptor()
        origin = decryptor.update(data) + decryptor.finalize()
        unpadder = padding.PKCS7(64).unpadder()
        origin_result = unpadder.update(origin) + unpadder.finalize()
        return origin_result

