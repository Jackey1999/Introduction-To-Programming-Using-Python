#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# Author  : Jakcey1999
# Email   : 9516694 # qq.com
# Time    : 2019-03-24-024 下午 15:15
# File    : 随机字符.py
# IDE     : PyCharm [Python 3.x]
# Code is far away from bugs with the god animal protecting.
  Life is short. You need Python 3.x

"""

# 3.3.7

import time

timesdata=time.time()
print(timesdata)
timesdata=int(timesdata)
print(timesdata)
timesdata=timesdata%26         # 余数0-25
timesdata2=timesdata%60

print("%",timesdata)

# print((ord('A')))
print(chr(ord('A')+timesdata))
print((ord('Z')))
