#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# Author  : Jakcey1999
# Email   : 9516694 # qq.com
# Time    : 2019-03-27-027 下午 23:55
# File    : 指令翻译系统.py
# IDE     : PyCharm [Python 3.x]
# Code is far away from bugs with the god animal protecting.
  Life is short. You need Python 3.x

"""
# cmd: tasklisk 输出命令清单

import os
cmdstr=input("输入指令：")
if cmdstr=="记事本":
    os.system("notepad")
elif cmdstr=="计算器":
    os.system("calc")
elif cmdstr=="进程":
    os.system("tasklist")
elif cmdstr=="IP地址":
    os.system("ipconfig")
elif cmdstr=="重启":
    os.system("shutdown -r -t 20000")
elif cmdstr=="关机":
    os.system("shutdown -s -t 200")
else:
    print("其他指令，还没有翻译")