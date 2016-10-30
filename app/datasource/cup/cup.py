# -*- coding: utf-8 -*-

import os
import jpype

from app.datasource.third import Third
from app.util.logger import logger

from ..configuration import config


class ChinaUnionPay(Third):
    """
    银联智策
    """
    cup_config = config.get('cup')
    development_id = cup_config.get('developmentId')
    private_key = cup_config.get('privateKey')
    public_key = cup_config.get('publicKey')
    debug_mode = bool(cup_config.get('debugMode'))
    api_location = cup_config.get('apiLocation')
    distinguish_code = cup_config.get('distinguishCode')
    source = 'cup'

    def __init__(self):
        self.jvm_path = jpype.getDefaultJVMPath()
        basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        jar_path = basedir + '/spiderJar.jar'
        self.jvmArg = "-Djava.class.path=" + jar_path

    def start_jvm(self):
        try:
            if jpype.isJVMStarted():
                jpype.shutdownJVM()
            jpype.startJVM(self.jvm_path, '-ea', self.jvmArg)
        except InterruptedError as e:
            logger.debug("JVM启动失败{}", e)

    def stop_jvm(self):
        jpype.shutdownJVM()

    def __get_data(self, user_name_cn, personal_id, mobile_num, card_id):
        """
        获取银联数据
        :param card_id: 银行卡号
        :param user_name_cn: 名字
        :param personal_id: 证件号
        :param mobile_num: 电话号码
        :return: 查询到的数据
        """
        self.start_jvm()
        Upa = jpype.JClass('upa.client.UPAClient')
        upa = Upa()
        upa.setDevelopmentId(self.development_id)
        # 设置私钥
        upa.setPrivateKey(self.private_key)
        # 设置公钥
        upa.setPublicKey(self.public_key)
        # 设置是否调试模式，true：调试，默认是false
        upa.setDebugMode(self.debug_mode)
        # 设置访问的url地址,URL为我司给出的String类型字符串
        upa.setApiLocation(self.api_location)
        # 设置银行卡卡号作参数，获取JSONObject类型的account score

        json_object = upa.getAuthCommonUPAScoreByAccountNo(card_id,
                                                           user_name_cn,
                                                           personal_id,
                                                           mobile_num,
                                                           self.distinguish_code)
        json = json_object.toString()
        self.stop_jvm()
        return json

    def query(self, result, *args, **kwargs):
        r = self.__get_data(**kwargs)
        result.put((r, self.source))
        return result

