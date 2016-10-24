# -*- coding: utf-8 -*-

import sys
import os
import requests
from pathlib import Path
from ..configuration import config
import pkgutil

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

print('Running' if __name__ == '__main__' else 'Importing', Path(__file__).resolve())


class Zzc:
    """获取中智诚反欺诈数据"""
    config_zzc = config.get('zzc')
    
    # 用户名
    name = config_zzc.get('name')

    # 密码
    password = config_zzc.get('password')

    # 反欺诈API入口
    cheat_list_base_url = config_zzc.get('cheatListBaseUrl') + '/'

    # 黑名单API入口
    back_list_base_url = config_zzc.get('backListBaseUrl')

    headers = {'Content-Type': 'application/json; charset=utf8'}
    auth = (name, password)

    def __init__(self):
        pass

    def show_by_institution(self, apply_id):
        """return a apply insformation by specify institution """
        result = requests.get(Zzc.cheat_list_base_url + apply_id,
                              auth=self.auth,
                              headers=self.headers,
                              timeout=1)

        if result.status_code == requests.codes.ok:
            page = result.json()
            r = True
        else:
            page = ''
            r = False
        return page, r

    def create(self, json_data):
        """create a loan apply information"""
        result = requests.post(Zzc.cheat_list_base_url,
                               json=json_data,
                               auth=self.auth,
                               headers=self.headers)
        return True if result.status_code == requests.codes.created else False

    def update(self, apply_id, json_data):
        """update a loan apply information"""
        result = requests.put(Zzc.cheat_list_base_url + apply_id,
                              json=json_data,
                              auth=self.auth,
                              headers=self.headers)
        return True if result.status_code == requests.codes.ok else False

    def delete(self, apply_id):
        """删除一条已经上传的申请信息"""
        result = requests.delete(Zzc.cheat_list_base_url + apply_id,
                                 auth=self.auth,
                                 timeout=1)
        return True if result.status_code == requests.codes.no_content else False

    def anti_fraud_report(self, apply_id):
        """该请求获取当前的申请信息的反欺诈报告,包含规则引擎的结果以及黑名单的结果"""
        result = requests.get(Zzc.cheat_list_base_url + apply_id + '/report',
                              auth=self.auth,
                              timeout=30)
        return True if result.status_code == requests.codes.ok else False

    def rule_report(self, apply_id):
        """该请求将当前的申请信息提交规则引擎并获取规则执行结果.和反欺诈报告相比,该接口不包含黑名单查询命中的
        记录的详细信息,但是规则中使用黑名单碰撞的部分仍然可能出现.该接口速度快于反欺诈报告,不需要黑名单命中记录详情的
        用户可以只调用该接口"""
        result = requests.get(Zzc.cheat_list_base_url + apply_id + "/rule_result",
                              auth=self.auth,
                              timeout=10)
        return True if result.status_code == requests.codes.ok else False

if __name__ == '__main__':
    pass



