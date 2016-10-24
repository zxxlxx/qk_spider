# -*- coding: utf-8 -*-
import inspect
import sys
import os
import requests
from pathlib import Path
from ..utils.tools import params_to_dict
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
    back_list_base_url = config_zzc.get('backListBaseUrl') + '/'

    headers = {'Content-Type': 'application/json; charset=utf8'}
    auth = (name, password)

    def __init__(self):
        pass

    def af_show_by_institution(self, apply_id):
        """return a apply insformation by specify institution """
        result = requests.get(Zzc.cheat_list_base_url + apply_id,
                              auth=self.auth,
                              headers=self.headers,
                              timeout=1)
        return self.pre_result(result)

    def af_create(self, json_data):
        """create a loan apply information"""
        result = requests.post(Zzc.cheat_list_base_url,
                               json=json_data,
                               auth=self.auth,
                               headers=self.headers)
        return True if result.status_code == requests.codes.created else False

    def af_update(self, apply_id, json_data):
        """update a loan apply information"""
        result = requests.put(Zzc.cheat_list_base_url + apply_id,
                              json=json_data,
                              auth=self.auth,
                              headers=self.headers)
        return self.pre_result(result)

    def af_delete(self, apply_id):
        """删除一条已经上传的申请信息"""
        result = requests.delete(Zzc.cheat_list_base_url + apply_id,
                                 auth=self.auth,
                                 timeout=1)
        return True if result.status_code == requests.codes.no_content else False

    def af_report(self, apply_id):
        """该请求获取当前的申请信息的反欺诈报告,包含规则引擎的结果以及黑名单的结果"""
        result = requests.get(Zzc.cheat_list_base_url + apply_id + '/report',
                              auth=self.auth,
                              timeout=30)
        return self.pre_result(result)

    def af_rule_report(self, apply_id):
        """该请求将当前的申请信息提交规则引擎并获取规则执行结果.和反欺诈报告相比,该接口不包含黑名单查询命中的
        记录的详细信息,但是规则中使用黑名单碰撞的部分仍然可能出现.该接口速度快于反欺诈报告,不需要黑名单命中记录详情的
        用户可以只调用该接口"""
        result = requests.get(Zzc.cheat_list_base_url + apply_id + "/rule_result",
                              auth=self.auth,
                              timeout=10)
        return self.pre_result(result)

    def black_list(self):
        """
        该方法返回您所在的机构上传到中智诚共享库的全部黑名单，包括但不限于您的个人账户上传的黑名单。关于机构、个人账号以及权限的说明，请访问 中智诚反欺诈云平台权限管理说明 文档
        :return:
        """
        pass

    def black_create(self):
        """
        上传一条新的黑名单记录。
        :return:
        """
        pass

    def black_update(self):
        """
        更新一条已存在的黑名单
        :return:
        """
        pass

    def black_delete(self):
        """
        删除一条已存在的黑名单
        :return:
        """
        pass

    def black_show(self):
        """
        列出一条黑名单详情
        :return:
        """
        pass

    def black_search(self, name, pid, mobile,
                     home_address=None,
                     home_phone=None,
                     work_name=None,
                     work_address=None,
                     address=None,
                     work_phone=None,
                     sub_tenant=None):
        """
        通过黑名单查询 API 可在中智诚共享黑名单库中跨机构查询输入信息并返回结果。
        Note: 反欺诈报告接口的结果包含了黑名单查询以及规则引擎两部分内容。
        我们建议用户直接使用反欺诈报告接口以获得更丰富的反馈内容。
        用户输入一组信息，系统会在采用精确匹配及模糊匹配去查询数据库并返回结果。
        每条黑名单包含字段参见后文表格。查询结果不包括只有姓名一致的记录
        :param name: 只能为合法的中国姓名（包括汉字和少数民族名字里的点）
        :param pid: 符合身份证规范且为有效的中国身份证
        :param mobile: 长度为11位的数字，必须为合法手机号码
        :param home_address:
        :param home_phone:
        :param work_name:
        :param work_address:
        :param address:
        :param work_phone:
        :param sub_tenant: 该字段供平台机构使用，用于上报具体提交查询的机构或部门名称
        :return:
        """
        json_data = params_to_dict()
        result = requests.post(Zzc.back_list_base_url + 'search',
                               json=json_data,
                               auth=self.auth,
                               headers=self.headers)
        return self.pre_result(result)

    def pre_result(self, result):
        """
        预处理操作结果
        :param result:
        :return:
        """
        if result.status_code == requests.codes.ok:
            page = result.json()
            r = True
        else:
            r = False
        return page, r



if __name__ == '__main__':
    pass



