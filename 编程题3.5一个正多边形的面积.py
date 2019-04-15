#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# Author  : Jakcey
# Email   : 9516694 # qq.com
# Time    : 2019-03-27 14:19
# File    : 编程题3.5一个正多边形的面积.py
# IDE     : PyCharm [Python 3.7]
# Code is far away from bugs with the god animal protecting.
  Life is short. You need Python 3.7

"""

import math

n, s = eval(input("请分别输入正多边形的边数n，边长s："))

area = n * math.pow(s, 2) / (4 * math.tan(math.pi / n))

print("边长{},正{}边形的面积是 {:.2f}".format(s,n,area))
