#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# Author  : Jakcey1999
# Email   : 9516694 # qq.com
# Time    : 2019-03-24-024 下午 14:51
# File    : 三角形面积.py
# IDE     : PyCharm [Python 3.x]
# Code is far away from bugs with the god animal protecting.
  Life is short. You need Python 3.x

"""
import turtle
import math

data = eval(input("qin shuru :"))


area = 5 * data * data / math.tan(math.pi / 5) / 4

turtle.circle(data, steps=5)
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.write(str(area))

turtle.done()
