#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# Author  : Jakcey1999
# Email   : 9516694 # qq.com
# Time    : 2019-03-20-020 下午 22:30
# File    : 讲解2.14计算距离.py
# IDE     : PyCharm [Python 3.x]
# Code is far away from bugs with the god animal protecting.
  Life is short. You need Python 3.x

"""
# 讲解 2.14，程序清单 2-10
# turtle文档：https://www.rddoc.com/doc/Python/3.6.0/zh/library/turtle/#turtle.dot

import turtle

turtle.setup(500,500)

# 输入第一个点的坐标
x1, y1 = eval(input("Enter x1,y1 for Point 1:"))

# 输入第二个点的坐标
x2, y2 = eval(input("Enter x2,y2 for Point 2:"))

# Compute the distance
distance = ((x1 - x2)**2 + (y1 - y2)**2)**0.5

# print("The di#stance between the two points is: ", distance)

turtle.penup()
turtle.goto(x1,y1)
turtle.pendown()
turtle.write("Point 1")
turtle.goto(x2,y2)
turtle.write("Point 2")

turtle.penup()

turtle.goto((x1+x2)/2,(y1+y2)/2)
turtle.write(distance)

turtle.hideturtle()
turtle.dot(5,"#EE00EE")   # 绘制圆点

turtle.done()