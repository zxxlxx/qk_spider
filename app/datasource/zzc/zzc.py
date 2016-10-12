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
    """获取中智诚反欺诈数据"""
    headers = {'Content-Type': 'application/json; charset=utf8'}
    auth = (NAME, PASSWORD)

    def __init__(self):
        pass

    @classmethod
    def show_by_institution(cls, apply_id):
        """return a apply insformation by specify institution """
        result = requests.get(CHEAT_LIST_BASE_URL + apply_id,
                              auth=cls.auth,
                              headers=cls.headers,
                              timeout=1,
                              verify=False)

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
                               headers=cls.headers,
                               verify=False)
        return True if result.status_code == requests.codes.created else False

    @classmethod
    def update(cls, apply_id, json_data):
        """update a loan apply information"""
        result = requests.put(CHEAT_LIST_BASE_URL + apply_id,
                               json=json_data,
                               auth=cls.auth,
                               headers=cls.headers,
                               verify=False)
        return True if result.status_code == requests.codes.ok else False

    @classmethod
    def delete(cls, apply_id):
        """删除一条已经上传的申请信息"""
        result = requests.delete(CHEAT_LIST_BASE_URL + apply_id,
                                 auth=cls.auth,
                                 timeout=1,
                                 verify=False)
        return True if result.status_code == requests.codes.no_content else False

    @classmethod
    def anti_fraud_report(cls, apply_id):
        """该请求获取当前的申请信息的反欺诈报告,包含规则引擎的结果以及黑名单的结果"""
        result = requests.get(CHEAT_LIST_BASE_URL + apply_id + '/report',
                              auth=cls.auth,
                              timeout=30,
                              verify=False)
        return True if result.status_code == requests.codes.ok else False

    @classmethod
    def rule_report(cls, apply_id):
        """该请求将当前的申请信息提交规则引擎并获取规则执行结果.和反欺诈报告相比,该接口不包含黑名单查询命中的
        记录的详细信息,但是规则中使用黑名单碰撞的部分仍然可能出现.该接口速度快于反欺诈报告,不需要黑名单命中记录详情的
        用户可以只调用该接口"""
        result = requests.get(CHEAT_LIST_BASE_URL + apply_id + "/rule_result",
                              auth=cls.auth,
                              timeout=10,
                              verify=False)
        return True if result.status_code == requests.codes.ok else False

if __name__ == '__main__':
    pass



