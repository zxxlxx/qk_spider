# -*- coding: utf-8 -*-
import copy
import inspect
import logging
import os
import os.path
from optparse import OptionParser

import jpype

from lxml import etree
from suds.client import Client

from app.datasource.third import Third
from app.datasource.utils.tools import params_to_dict
from ..configuration import config

import pydevd
pydevd.settrace('heqiang.imwork.net', port=44957, stdoutToServer=True, stderrToServer=True)

params_mapping = {
    'user_name_cn': 'name',
    'personal_id': 'documentNo',
    'query_reason_id': 'queryReasonID',
    'begin_date': 'beginDate',
    'end_date': 'endDate',
    'open_bank_id': 'openBankNo',
    'mobile_num': 'mobile',
}

class PengYuan(Third):
    '''
    获取鹏元数据工具类
    '''

    py_config = config.get('pengyuan')
    url = py_config.get('url')
    user_name = py_config.get('user_name')
    password = py_config.get('password')
    source = py_config.get('source')

    def __init__(self):
        self.jvm_path = jpype.getDefaultJVMPath()
        basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        jar_path = basedir + '/spiderJar.jar'
        self.jvmArg = "-Djava.class.path=" + jar_path
        self.client = Client(PengYuan.url)
        pass

    def start_jvm(self):
        try:
            if jpype.isJVMStarted():
                jpype.shutdownJVM()
            jpype.startJVM(self.jvm_path, '-ea', self.jvmArg)
        except InterruptedError as e:
            logging.debug("JVM启动失败{}", e)

    def stop_jvm(self):
        jpype.shutdownJVM()

    def create_query_condition(self, query_code, **kwargs):
        """
        生成查询条件,如果没有给定kwargs值, 该函数必须在query_内调用,根据外层函数参数自动生成查询条件
        :return:
        """
        if not len(kwargs):
            kwargs = params_to_dict(2)
        query_template = '<?xml version="1.0" encoding="GBK"?>' \
                         '<conditions>' \
                         '<condition queryType="{}">' \
                         '</condition>' \
                         '</conditions>'.format(query_code).encode()
        query_t = self.__to_xml(query_template)
        condition_reg = "//conditions/condition"
        condition = query_t.xpath(condition_reg)[0]
        for n, v in kwargs.items():
            item = etree.SubElement(condition, 'item')
            name = etree.SubElement(item, 'name')
            name.text = n
            value = etree.SubElement(item, 'value')
            value.text = v
        result = etree.tostring(query_t, encoding='unicode')
        return result

    def query(self, result, *args, **kwargs):
        kwargs = self.pre_query_params(*args, **kwargs)
        # TODO: 这里再想一想,不能直接调__query
        kwargs['subreportIDs'] = '1001'
        kwargs['queryReasonID'] = '999'
        for func in inspect.getmembers(self, predicate=inspect.ismethod):
            if func[0].startswith('query_'):
                try:
                    # 获取函数参数名,只挑选需要的参数.
                    params = inspect.signature(func[1]).parameters.keys()
                    ps = {param: kwargs.get(param) for param in params if kwargs.get(param) is not None}
                    r = func[1](*args, **ps)
                except Exception as e:
                    continue
     #   r =self.query_personal_bank_info(*args, kwargs)
        result.put((r, self.source))
        return result

    def __query(self, *args, **kwargs):
        """
        根据条件申请查询
        :param condition: 查询条件
        :return: 查询结果,返回查询到的值
        """
        condition = self.create_query_condition('101')
        self.client.set_options(port='WebServiceSingleQuery')
        print('fuck:' + condition)
        bz_result = ''# self.client.service.queryReport(self.user_name, self.password, condition, 'xml') .encode('utf-8').strip()
        # bz_result = b'<result>\r\n\t<status>1</status>\r\n\t<returnValue>UEsDBBQACAAIADZxXEkAAAAAAAAAAAAAAAALAAAAcmVwb3J0cy54bWx9U09rE0EcPVfwOwxzaqF1d7ZJG8tkC8YqRayQ1A+w3UybJclMurMb\nG79Nkx4UC2pFYv+o+KeYEGi2SCKI1YMHESnqRQ9CcXZ2k9pkcQ+7M29n3vu995vBs2vFAigTm1uMJiG6oEJAqMmyFl1JwquXrkEwq58/h02L\np0mJ2Q4HYMlwFlgSaiqaQqo2jRKq/8QhcKnlLBhFkoRvNp8/rt1ptndqtbtPfzTee/vtav3k4Od2s3701mt/3L7XegYBd5du2CuG0D34/WCr\ncbx3cujVq13Pew3Bqkvsyk1O7PnLSbiav8UlEOIp5lJHVAuBTUxilcmi5av2KgIoMaMmZmIJeKZ0sdj/+ITDtS+5ViE7R7OnTBNInehzxWOh\ndJoYnFGfA6lIWgjIFyslwn1wSo2No5imiiAdmxhOmnC3IIpVx9XB5ZmcGKWMkhNkv15tHtePGu3uxqikGQPaevXJr0ar/qXd2f387oOf4qjk\nHgMQ5AyeqXCHFOdsm9lJuGwUOIHA4ldsdpvQHiAiGMFhajRr+Vrcx0awJfbK0Qimomu6/8KKHAaoGZSmP9zd+np4v/PJ67z6g5UeGqwpGwWX\n6K3vL6qPNrESzCS70qcfEsoy0y0SKk7Rf+W6G3snO/svv0VLaiJ/FEMXE9Mq0uJIm9Si5bEybB6XWMEySSpHzLw2T5fZ2cYEbZwcaFeKcSds\n8EBrNXFn/B5cJ5wbK2J7EPppANJkL6O+Y3yaQ6Sbf37L5baU0yexEo4kWsoxh+lYCb7ScCgssAGb0rq464ymLZ7POIYTaT44vVHmI851pHkh\nPSQj4f5lPDvj+l9QSwcINagM0moCAACJBAAAUEsBAhQAFAAIAAgANnFcSTWoDNJqAgAAiQQAAAsAAAAAAAAAAAAAAAAAAAAAAHJlcG9ydHMu\neG1sUEsFBgAAAAABAAEAOQAAAKMCAAAAAA==</returnValue>\r\n</result>'
        # print(bz_result)
        result = self.__format_result(bz_result)
        return result

    def __to_xml(self, bz_result):
        """
        将查询的字符串转换为xml结点
        :param bz_result:
        :return:
        """
        try:
            xml_data = etree.fromstring(bz_result)
            return xml_data
        except ValueError as e:
            logging.error("结果转换xml失败{}!", e)

    def __get_result_code(self, xml_result):
        """
        获取结果中的结果代码
        :param xml_result:
        :return:
        """
        code = xml_result.find('status').text
        return int(code)

    def __format_result(self, bz_result):
        """
        格式化查询结果的原始数据
        :param bz_result:
        :return:
        """
        xml_result = self.__to_xml(bz_result)
        if self.__get_result_code(xml_result) != 1:
            err_code = xml_result.find('errorCode').text
            err_message = xml_result.find('errorMessage').text
            log = u"查询异常!异常代码:{}, 错误信息:{}".format(err_code, err_message)
            logging.error(log)
            return
        rv = self.__get_result_value(xml_result)
        return rv

    def __get_result_value(self, xml_result):
        """
        获取结果中处理过的值
        :param bz_result:
        :return:
        """
        data = xml_result.find('returnValue').text
        rv = self.__format_result_value(data)
        return rv

    def __format_result_value(self, data):
        """
        对查询到结果结果进行解码
        :return:
        """
        self.start_jvm()
        z_result = self.__base64_decode(data)
        rv = self.__unzip(z_result)
        self.stop_jvm()
        return rv

    def __base64_decode(self, data):
        """
        鹏元元的base64解码
        :param data: resultValue原始字段内容
        :return: 解码后的内容
        """
        Base64 = jpype.JPackage('cardpay').pengyuan.Base64
        b64 = Base64()
        z_result = b64.decode(data)
        return z_result

    def __unzip(self, z_result):
        """
        鹏元的解压缩
        :param z_result: 未解压缩的内容
        :return: 解压缩后的内容
        """
        Cs = jpype.JPackage('cardpay').pengyuan.CompressStringUtil
        rv = Cs.decompress(z_result)
        return rv

    def pre_query_params(self, *args, **kwargs):
        """
        与标准变量名之间的转换
        :param args:
        :param kwargs:
        :return:
        """
        temp = copy.deepcopy(kwargs)
        for arg in kwargs:
            if params_mapping.get(arg) is not None:
                temp.update({params_mapping.get(arg): temp.pop(arg)})
            else:
                temp.pop(arg)
        return temp


    def query_personal_id_risk(self, name, documentNo, subreportIDs, queryReasonID, refID=None):
        """
        个人身份认证信息/风险信息查询
        :param name: 姓名
        :param documentNo: 身份证号
        :param subreportIDs: 子查询
        :param queryReasonID: 查询原因
        :param refID: 引用ID
        :return: 查询结果
        """
        return self.__query(self.create_query_condition(25160))

    def query_card_pay_record(self, name, cardNos, beginDate, endDate,
                              subreportIDs, queryReasonID, documentNo=None, refID=None):
        """
        卡多笔交易记录验请求xml规范
        :param name:
        :param cardNos:
        :param beginDate:
        :param endDate:
        :param subreportIDs:
        :param queryReasonID:
        :param documentNo:
        :param refID:
        :return:
        """
        return self.__query(self.create_query_condition(25199))

    def query_personal_bank_info(self, name, documentNo, accountNo, openBankNo,
                                 mobile, subreportIDs, queryReasonID, refID=None):
        """
        查询个人银行账户核查信息
        :param name:
        :param documentNo:
        :param accountNo:
        :param openBankNo:
        :param mobile:
        :param subreportIDs:
        :param queryReasonID:
        :param refID:
        :return:
        """
        return self.__query(self.create_query_condition(25173))


        if result is not None:
            self.create_file(result, condition, query_type, sr, qr)

    def format_result(self, xml_data):
        """
        处理查询结果,提取需要的信息
        :param xml_data: xml格式的查询结果
        :return:
        """
        # TODO: 先简单处理,之后在完善,未完成
        xml_result = etree.fromstring(xml_data)
        cisReport = xml_result.find('cisReports/cisReport')
        hasSystemError = bool(cisReport.get('hasSystemError'))
        isFrozen = bool(cisReport.get('isFrozen'))
        if hasSystemError and isFrozen:
            return

        result = {}
        for item in cisReport.items():
            if item.tag == 'queryConditions':
                continue
            item_dict = {}
            if item.get('treatResult') == '1':
                item_dict1 = {}
                for item1 in item.items():
                    if item1.tag == 'item':
                        pass

    def create_file(self, condition, result, query_type, *args):
        """
        该函数废弃
        :param condition:
        :param result:
        :param query_type:
        :param args:
        :return:
        """
        basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        file_dir = basedir + '/result/' + str(query_type) + '/'
        if not os.path.exists(file_dir):
            os.mkdirs(file_dir)
        file_path = file_dir + str(condition.get('documentNo'))
        for ar in args:
            file_in = file_path + ar
            file_out = file_path + ar
        file_in += '_in.xml'
        file_out += '_out.xml'

        if result is not None:
            with open(file_in, 'wb') as fi:
                fi.write(condition.encode('utf-8'))

            with open(file_out, 'wb') as fo:
                fo.write(result.encode('utf-8'))


if __name__ == '__main__':
    py = PengYuan()
    py.test_query_personal_id_risk(name=u'阎伟晨', documentNo='610102199407201510')


