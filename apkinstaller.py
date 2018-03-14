#!/usr/bin/python

import sys
import os
import re

# sys.argv 用于存储传递给 python 脚本的参数
# 脚本名：    sys.argv[0]
# 参数1：     sys.argv[1]
# 参数2：     sys.argv[2]
argslen = len(sys.argv)

# 判断是否指定了要安装的 apk 包路径
if argslen == 1:
    print "Usage: apkinstaller.py [APK_FILE]"
    print "Install apk to your mobile"
    sys.exit(0)

# 获取到 apk 包路径
apk_path = sys.argv[1]

# 判断 apk 文件是否存在
if not os.path.exists(apk_path):
    print apk_path + " : no such apk file"
    sys.exit(0)

# 截取到 apk 文件名
apk_file = re.findall(".*/(.+\.apk)", apk_path)[0]

print
print 'installing ' + apk_file
print

# python 调用 shell 脚本进行安装
os.system('adb push ' + apk_path + ' /data/local/tmp/' + apk_file)
os.system('adb shell pm install -r /data/local/tmp/' + apk_file)
