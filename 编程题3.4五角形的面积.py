#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# Author  : Jakcey
# Email   : 9516694 # qq.com
# Time    : 2019-03-27 14:14
# File    : 编程题3.4五角形的面积.py
# IDE     : PyCharm [Python 3.7]
# Code is far away from bugs with the god animal protecting.
  Life is short. You need Python 3.7

"""

import math

s = eval(input("请输入五角形的边长 s = "))

area = 5 * math.pow(s, 2) / (4 * math.tan(math.pi / 5))

print("area = ", area)               # 注意 / 符号后面 ()，否则计算次序会错
