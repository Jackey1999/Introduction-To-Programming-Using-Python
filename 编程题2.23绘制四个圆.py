#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# Author  : Jakcey1999
# Email   : 9516694 # qq.com
# Time    : 2019-03-24-024 下午 14:37
# File    : 编程题2.23绘制四个圆.py
# IDE     : PyCharm [Python 3.x]
# Code is far away from bugs with the god animal protecting.
  Life is short. You need Python 3.x

"""
import turtle

radius = eval(input("请输入圆的半径："))

turtle.pensize(2)           # 设定画笔粗细

turtle.circle(radius)       # 第一个圆圈

turtle.penup()              # 第二个圆圈
turtle.goto(radius * (-2), 0)
turtle.pendown()
turtle.circle(radius)

turtle.penup()              # 第三个圆圈
turtle.goto(radius * (-2), radius * (-2))
turtle.pendown()
turtle.circle(radius)

turtle.penup()              # 第四个圆圈
turtle.goto(0, radius * (-2))
turtle.pendown()
turtle.circle(radius)

turtle.penup()
turtle.goto(radius, 0)
turtle.pendown()
turtle.hideturtle()

turtle.write("半径 = {:.0f} ".format(radius), font=("宋体", 16, "normal"))

turtle.done()