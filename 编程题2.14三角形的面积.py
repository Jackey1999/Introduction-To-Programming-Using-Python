#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# Author  : Jakcey1999
# Email   : 9516694 # qq.com
# Time    : 2019-03-22-022 下午 16:34
# File    : 编程题2.14三角形的面积.py
# IDE     : PyCharm [Python 3.x]
# Code is far away from bugs with the god animal protecting.
  Life is short. You need Python 3.x

"""
# 编程题2.14三角形的面积

x1, y1 = eval(input("请输入 A 点的坐标 x1,y1 : "))
x2, y2 = eval(input("请输入 B 点的坐标 x2,y2 : "))
x3, y3 = eval(input("请输入 C 点的坐标 x3,y3 : "))

side1 = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
side2 = ((x3 - x2)**2 + (y3 - y2)**2)**0.5
side3 = ((x1 - x3)**2 + (y1 - y3)**2)**0.5

s = (side1 + side2 + side3) / 2
area = (s * (s - side1) * (s - side2) * (s - side3))**0.5       # 面积计算公式

print("三条边的长度分别为：{:.2f} {:.2f} {:.2f}".format(side1, side2, side3))
print("三角形的面积为：{:.2f}".format(area))

# 三角形面积在线计算器：https://zh.numberempire.com/arbitrary_triangle_calculator.php
