#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# Author  : Jakcey1999
# Email   : 9516694 # qq.com
# Time    : 2019-03-24-024 下午 14:41
# File    : 编程题2.24绘制4个正六边形.py
# IDE     : PyCharm [Python 3.x]
# Code is far away from bugs with the god animal protecting.
  Life is short. You need Python 3.x

"""
import turtle

turtle.screensize(500, 500)
turtle.pensize(2)
turtle.pencolor("red")

radius = eval(input("请输入圆的半径："))

turtle.penup()               # 第一个圆
turtle.forward(radius)
turtle.pendown()
turtle.circle(radius,360,6)

turtle.penup()               # 第二个圆
turtle.forward(radius * (-2))
turtle.pendown()
turtle.circle(radius,360,6)

turtle.penup()               # 第三个圆
turtle.right(90)
turtle.forward(radius * (2))
turtle.pendown()
turtle.right(-90)
turtle.circle(radius,360,6)

turtle.penup()               # 第四个圆
turtle.forward(radius * 2)
turtle.down()
turtle.circle(radius,360,6)

turtle.penup()               # 文字
turtle.goto(radius, radius)
turtle.down()
turtle.write("正六边形外切圆的半径 = {:.0f}".format(radius), font=("宋体", 16, "normal"))  # ...半径也可用int(radius)
turtle.hideturtle()

turtle.done()
