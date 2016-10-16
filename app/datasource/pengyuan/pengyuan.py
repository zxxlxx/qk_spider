# -*- coding: utf-8 -*-
import os
from suds.client import Client
import logging
import io
from lxml import etree

import jpype
import os.path

import pydevd
pydevd.settrace('licho.iok.la', port=44957, stdoutToServer=True, stderrToServer=True)

basedir = os.path.abspath(os.path.dirname(__file__))

logging.basicConfig(level=logging.INFO)
logging.getLogger('suds.client').setLevel(logging.DEBUG)


class PengYuan:
    '''
    获取鹏元数据工具类
    '''

    URL = "http://www.pycredit.com:9001/services/WebServiceSingleQuery?wsdl"
    USER_NAME = 'qkwsquery'
    PASSWORD = 'qW+06PsdwM+y1fjeH7w3vw=='

    def __init__(self):
        self.jvm_path = jpype.getDefaultJVMPath()
        basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        jar_path = basedir + '/pengyuan.jar'
        self.jvmArg = "-Djava.class.path=" + jar_path
        self.client = Client(PengYuan.URL)

    def start_jvm(self):
        try:
            if jpype.isJVMStarted():
                jpype.shutdownJVM()
            jpype.startJVM(self.jvm_path, '-ea', self.jvmArg)
        except InterruptedError as e:
            logging.debug("JVM启动失败{}", e)

    def stop_jvm(self):
        jpype.shutdownJVM()

    def create_query_condition(self):
        """
        生成查询条件
        :return:
        """
        with io.open(basedir + '/id_test.xml', 'r', encoding='GBK') as c:
            condition = c.read()
        return condition

    def query(self, condition):
        """
        根据条件申请查询
        :param condition: 查询条件
        :return: 查询结果,返回查询到的值
        """
        self.client.set_options(port='WebServiceSingleQuery')
        bz_result = self.client.service.queryReport(PengYuan.USER_NAME, PengYuan.PASSWORD, condition, 'xml')\
            .encode('utf-8').strip()
        result = self.__format_result(bz_result)
        return result

    def __to_xml(self, bz_result):
        try:
            xml_data = etree.fromstring(bz_result)
        except ValueError as e:
            logging.error("结果转换xml失败{}!", e)
        return xml_data

    def __get_result_code(self, xml_result):
        code = xml_result.find('status')
        return code

    def __format_result(self, bz_result):
        xml_result = self.__to_xml(bz_result)
        if self.__get_result_code(xml_result) != 1:
            err_code = xml_result.find('errorCode').text
            err_message = xml_result.find('errorMessage').text
            logging.error("查询异常!异常代码:{}, 错误信息:{}", err_code, err_message)
            return
        rv = self.__format_result_value(xml_result)
        return rv

    def __get_result_value(self, xml_data):
        """
        获取结果中的结果值
        :param bz_result:
        :return:
        """
        data = bytes(xml_data.find('returnValue').text)
        rv = self.__format_result_value(data)
        return rv

    def __format_result_value(self, data):
        """
        对查询到结果结果进行解码
        :return:
        """
        self.start_jvm()
        ta = jpype.JPackage('cardpay').Base64
        b64 = ta()
        z_result = b64.decode(data)
        cs = jpype.JPackage('cardpay').CompressStringUtil
        rv = cs.decompress(z_result)
        self.stop_jvm()
        return rv

if __name__ == '__main__':
    py = PengYuan()
    condition = py.create_query_condition()
    result = py.query(condition)
    print(result)