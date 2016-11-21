# -*- coding: utf-8 -*-

import os
# import jpype

from app.datasource.third import Third
from app.util.logger import logger

from ..configuration import config
# from ...util.jvm import stop_jvm, start_jvm


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
       pass



    def query(self, result, *args, **kwargs):
        # r = self.__get_data(**kwargs)
        # result.put((r, self.source))
        # return result
        pass


