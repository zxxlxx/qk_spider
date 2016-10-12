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
# 反欺诈API入口
CHEAT_LIST_BASE_URL = "https://nezha.intellicredit.cn/api/v2/applications/"
# 黑名单API入口
BACK_LIST_BASE_URL = "https://nezha.intellicredit.cn/api/v2/blacklist/"


class Zzc:
    """get zhong zhi cheng anti fraud data"""

    def __init__(self):
        self.headers = {'Content-Type': 'application/json'}

    def show_by_institution(self, apply_id):
        """return a apply insformation by specify institution """
        result = requests.get(CHEAT_LIST_BASE_URL + apply_id,
                              auth=(NAME, PASSWORD),
                              headers=self.headers,
                              timeout=1)
        if result.status_code == requests.codes.ok:
            page = result.json()
        else:
            page = ''
        return page, result.status_code



if __name__ == '__main__':
    pass



