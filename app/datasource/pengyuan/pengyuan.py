# -*- coding: utf-8 -*-

import os
from suds.client import Client
from suds import WebFault
import logging

basedir = os.path.abspath(os.path.dirname(__file__))
stream = open(basedir + '/id_test.xml', 'r')

logging.basicConfig(level=logging.INFO)
logging.getLogger('suds.client').setLevel(logging.DEBUG)

URL = "http://www.pycredit.com:9001/services/WebServiceSingleQuery?wsdl"

USER_NAME = 'qkwsquery'
PASSWORD = 'qW+06PsdwM+y1fjeH7w3vw=='

client = Client(URL)

client.set_options(port='WebServiceSingleQuery')
result = client.service.queryReport(USER_NAME, PASSWORD, stream, 'xml')
print(result)