#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# Author  : Jakcey
# Email   : 9516694 # qq.com
# Time    : 2019-03-27 14:43
# File    : 编程题3.7大写的随机字符.py
# IDE     : PyCharm [Python 3.7]
# Code is far away from bugs with the god animal protecting.
  Life is short. You need Python 3.7

"""

# 大写的随机字符，对应的数字65~90

import time

a = int(time.time()) % 26 + 65
b = int(time.time()) % 26 + 97

print(chr(a))   # 随机大写
print(chr(b))   # 随机小写
