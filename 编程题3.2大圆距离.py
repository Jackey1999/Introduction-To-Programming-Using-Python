#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# Author  : Jakcey
# Email   : 9516694 # qq.com
# Time    : 2019-03-27 01:34
# File    : 编程题3.2大圆距离.py
# IDE     : PyCharm [Python 3.7]
# Code is far away from bugs with the god animal protecting.
  Life is short. You need Python 3.7

"""
import math

x1, y1 = eval(input("请输入地球上A点的经纬度 x1,y1:"))
x2, y2 = eval(input("请输入地球上B点的经纬度 x2,y2:"))

radius = 6371.01

# 使用math.radians()将度数转化为弧度数
x1 = math.radians(x1)
y1 = math.radians(y1)
x2 = math.radians(x2)
y2 = math.radians(y2)

d = radius * math.acos(math.sin(x1) * math.sin(x2) +
                       math.cos(x1) * math.cos(x2) * math.cos(y1 - y2))

print("The distance between the two points is {:.2f} km".format(d))
