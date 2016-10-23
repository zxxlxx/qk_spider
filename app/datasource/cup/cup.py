# -*- coding: utf-8 -*-

import os
import jpype
from app.util.logger import logger


class ChinaUnionPay:
    """
    银联智策
    """
    def __init__(self):
        self.jvm_path = jpype.getDefaultJVMPath()
        basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        jar_path = basedir + '/pengyuan.jar'
        self.jvmArg = "-Djava.class.path=" + jar_path

    def start_jvm(self):
        try:
            if jpype.isJVMStarted():
                jpype.shutdownJVM()
            jpype.startJVM(self.jvm_path, '-ea', self.jvmArg)
        except InterruptedError as e:
            logger.debug("JVM启动失败{}", e)

    def stop_jvm(self):
        jpype.shutdownJVM()
