# -*- coding: utf-8 -*-

import sys
import os
import requests
import json
from pathlib import Path

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

print('Running' if __name__ == '__main__' else 'Importing', Path(__file__).resolve())


# TODO:unsolved reference config.py
# 用户名
NAME = "yecm@qkjr.com.cn"

# 密码
PASSWORD = "xfBJKD6x-vHuQZyrWfZ2"

# api url
NEZHA = "https://nezha.intellicredit.cn/api/v2/"

# 反欺诈API入口
CHEAT_LIST_BASE_URL = NEZHA + "applications/"

# 黑名单API入口
BACK_LIST_BASE_URL = NEZHA + "blacklist/"


class Zzc:
    """get zhong zhi cheng anti fraud data"""
    headers = {'Content-Type': 'application/json'}
    auth = (NAME, PASSWORD)

    def __init__(self):
        pass

    @classmethod
    def show_by_institution(cls, apply_id):
        """return a apply insformation by specify institution """
        result = requests.get(CHEAT_LIST_BASE_URL + apply_id,
                              auth=cls.auth,
                              headers=cls.headers,
                              timeout=1)

        if result.status_code == requests.codes.ok:
            page = result.json()
            r = True
        else:
            page = ''
            r = False
        return page, r

    @classmethod
    def create(cls, json_data):
        """create a loan apply information"""
        result = requests.post(CHEAT_LIST_BASE_URL,
                               json=json_data,
                               auth=cls.auth,
                               headers=cls.headers)
        return True if result.status_code == requests.codes.created else False

    @classmethod
    def update(cls, apply_id, json_data):
        """update a loan apply information"""
        result = requests.post(CHEAT_LIST_BASE_URL + apply_id,
                               json=json_data,
                               auth=cls.auth,
                               headers=cls.headers)
        return True if result.status_code == requests.codes.ok else False

if __name__ == '__main__':
    pass



