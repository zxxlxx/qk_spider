# -*- coding: utf-8 -*-
from lxml import etree
import sys
import xmltodict
from app import db, create_app
from app.info import *
from app.util.logger import logger
from sqlalchemy.exc import StatementError

sys.path.append("..")


def remove_xml_head(xml_string):
    """
    去除xml文档头部
    :param xml_string: 完整xml文档内容
    :return: 去除xml头部的字符串
    """
    index = xml_string.find('>')
    if xml_string[index - 1] is '?':
        return xml_string[index + 1:].strip()
    else:
        return xml_string.strip()


def process_person_id_risk(report):
    """
    处理个人身份认证信息
    :param report: 鹏元查询接口返回数据
    :return: 无返回值，将结果存入Person
    """
    temp = remove_xml_head(report)
    document = etree.XML(temp)
    result_report = document.find('cisReport/policeCheck2Info/item')
    if result_report is None:
        return
    selected = etree.tostring(result_report, encoding='UTF-8')
    selected_dict = xmltodict.parse(selected, xml_attribs=False)
    name = selected_dict['item']['name']
    identity = selected_dict['item']['documentNo']
    status = selected_dict['item']['result']
    photo = selected_dict['item']['photo']
    # 写入个人基本信息表
    person = Person.query.filter_by(identity=identity).first()
    if person is None:
        person = Person()
    person.identity = identity
    person.name = name
    person.photo = photo
    person.identity_status = status
    # 先存个人信息，后续要用到其ID
    try:
        db.session.add(person)
        db.session.commit()
    except StatementError as e:
        logger.error(e)

    # 个人风险分析
    risk_report = document.find('cisReport/personRiskStatInfo/stat')
    if risk_report is not None:
        risk = etree.tostring(risk_report, encoding='UTF-8')
        risk_dict = xmltodict.parse(risk, xml_attribs=False)
        person_risk = PersonRisk.query.filter_by(person_id=person.id).first()
        if person_risk is None:
            person_risk = PersonRisk(person=person)
        person_risk.judicial_case = risk_dict['stat']['alCount']
        person_risk.judicial_performed = risk_dict['stat']['zxCount']
        person_risk.judicial_blacklist = risk_dict['stat']['sxCount']
        person_risk.tax_performed = risk_dict['stat']['swCount']
        person_risk.tax_debt = risk_dict['stat']['cqggCount']
        person_risk.loan_expired = risk_dict['stat']['wdyqCount']
        try:
            db.session.add(person_risk)
            db.session.commit()
        except StatementError as e:
            logger.error(e)


if __name__ == '__main__':
    # app = create_app('testing')
    # app_context = app.app_context()
    # app_context.push()
    # db.create_all()
    # process_person_id_risk(test)
    pass
