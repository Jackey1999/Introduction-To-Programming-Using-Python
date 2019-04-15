#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# Author  : Jakcey
# Email   : 9516694 # qq.com
# Time    : 2019-03-27 01:13
# File    : 编程题3.1一个五边形的面积.py
# IDE     : PyCharm [Python 3.7]
# Code is far away from bugs with the god animal protecting.
  Life is short. You need Python 3.7

"""
import turtle
import math

r = eval(input("请输入五边形的边长:"))

s = 2 * r * math.sin(math.pi / 5)
area = 5 * s * s / (4 * math.tan(math.pi / 5))

turtle.circle(r, 360, 5)
print("area=", round(area, 2))

turtle.done()
