#! /usr/bin/python
# -*- coding: utf-8 -*-

import logging
import os
import sys
try:
    import jpype
except ImportError:
    pass

jvm_path = jpype.getDefaultJVMPath()
basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
jar_path = basedir + '/spiderJar.jar'
jvmArg = "-Djava.class.path=" + jar_path


def start_jvm():
    try:
        if jpype.isJVMStarted():
            jpype.shutdownJVM()
        jpype.startJVM(jvm_path, '-ea', jvmArg)
        if not jpype.isThreadAttachedToJVM():
            jpype.attachThreadToJVM()
    except InterruptedError as e:
        logging.debug("JVM启动失败{}", e)


def stop_jvm():
    jpype.shutdownJVM()
