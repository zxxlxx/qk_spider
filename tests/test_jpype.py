# -*- coding: utf-8 -*-
import jpype

import os

jvm_path = jpype.getDefaultJVMPath()
basedir = os.path.abspath(os.path.dirname(__file__))
jar_path = basedir + '\\upaclient.jar'
jvmArg = "-Djava.class.path=" + jar_path

jpype.startJVM(jvm_path, "-ea")

try:
    if jpype.isJVMStartexd():
        jpype.shutdownJVM()
    jpype.startJVM(jvm_path, '-ea', jvmArg)
except InterruptedError as e:
    print(e)

ta = jpype.JPackage('upa.client').UPAClient
upa = ta()
z_result = upa.setDevelopmentId("FCA0WKKJOBUEJUFAI0BVRKQBJNEPJEJQ")
print(z_result)