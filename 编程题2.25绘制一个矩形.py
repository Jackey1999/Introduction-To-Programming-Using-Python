#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# Author  : Jakcey1999
# Email   : 9516694 # qq.com
# Time    : 2019-03-24-024 下午 14:41
# File    : 编程题2.25绘制一个矩形.py
# IDE     : PyCharm [Python 3.x]
# Code is far away from bugs with the god animal protecting.
  Life is short. You need Python 3.x

"""
import turtle
x, y = eval(input("请输入矩形的中心点："))
a, b = eval(input("请输入矩形的长和宽："))

# 显示原点坐标
turtle.dot(5, "red")
turtle.write(
    "原点 ({},{})".format(
        0, 0), align="center", font=(
            "Arial", 12, "normal"))

# 显示矩形中心点坐标
turtle.penup()
turtle.goto(x, y)
turtle.pendown()
turtle.dot(5, "blue")
turtle.write(
    "矩形中心点 ({},{})".format(
        x, y), align="center", font=(
            "Arial", 12, "normal"))

# 绘制矩形
turtle.penup()
turtle.goto(x + a / 2, y + b / 2)
turtle.pendown()

turtle.fd(-a)
turtle.right(90)
turtle.fd(b)
turtle.right(-90)
turtle.fd(a)
turtle.right(-90)
turtle.fd(b)

# 隐藏小海龟
turtle.hideturtle()

turtle.done()