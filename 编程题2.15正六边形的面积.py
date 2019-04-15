#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# Author  : Jakcey1999
# Email   : 9516694 # qq.com
# Time    : 2019-03-22-022 下午 17:13
# File    : 编程题2.15正六边形的面积.py
# IDE     : PyCharm [Python 3.x]
# Code is far away from bugs with the god animal protecting.
  Life is short. You need Python 3.x

"""

# 编程题2.15正六边形的面积

s = eval(input("请输入正六边形的边长："))

area = (s**2) * 3 * (3**0.5) / 2

print("输入的边长 = {:.2f},正六边形的面积 = {:2f}".format(s, area))
