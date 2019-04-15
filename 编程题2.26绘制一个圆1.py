#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# Author  : Jakcey1999
# Email   : 9516694 # qq.com
# Time    : 2019-03-24-024 下午 14:42
# File    : 编程题2.26绘制一个圆1.py
# IDE     : PyCharm [Python 3.x]
# Code is far away from bugs with the god animal protecting.
  Life is short. You need Python 3.x

"""
import turtle

x, y = eval(input("请输入圆心坐标(x,y)："))
radius = eval(input("请输入圆的半径："))

# 原点坐标
turtle.dot(3, "red")
turtle.write("原点 (0,0)", align="center", font=("Arial", 12, "normal"))

# 圆心坐标
turtle.penup()
turtle.goto(x, y)
turtle.pendown()

turtle.dot(3, "blue")
turtle.write(
    "圆心 ({:.2f},{:.2f})".format(
        x, y), align="center", font=(
            "Arial", 12, "normal"))

# 绘制圆形
turtle.pensize(2)
turtle.pencolor("blue")
turtle.right(90)
turtle.penup()
turtle.fd(radius)
turtle.pendown()

turtle.right(-90)
turtle.circle(radius)

# 计算面积
PI = 3.1415927
s = PI * radius * radius
turtle.penup()
turtle.goto(x, -y / 4)
turtle.pendown()
turtle.write(
    ("r = {:.2f}\ns = {:.2f}").format(
        radius, s), align="right", font=(
            "Arial", 12, "normal"))

turtle.hideturtle()

turtle.done()