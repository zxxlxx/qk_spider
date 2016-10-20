# -*- coding: utf-8 -*-
import yaml
import os


def config():
    basedir = os.path.abspath(os.path.dirname(__file__))
    stream = open(basedir + '/config.yml', 'r', encoding='utf8')
    configuration = yaml.load(stream)
    return configuration

config = config()

