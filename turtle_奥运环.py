#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# Author  : Jakcey1999
# Email   : jackey1999 # foxmail.com
# Time    : 2019-03-18-018 下午 18:25
# File    : 奥运环.py
# IDE     : PyCharm [Python 3.x]
# Code is far away from bugs with the god animal protecting.
  Life is short. You need Python 3.x

"""
import turtle

turtle.setup(700,600)

turtle.width(10)
turtle.speed(0)     # 速度最快

# 绘制篮圈
turtle.color('blue')
turtle.circle(100)

# 绘制红圈
turtle.penup()
turtle.goto(-200, 0)
turtle.pendown()
turtle.color('black')
turtle.circle(100)

# 绘制黄圈
turtle.penup()
turtle.goto(200, 0)
turtle.pendown()
turtle.color('red')
turtle.circle(100)

# 绘制
turtle.penup()
turtle.goto(-100, -100)
turtle.pendown()
turtle.color('yellow')
turtle.circle(100)

# 绘制
turtle.penup()
turtle.goto(100, -100)
turtle.pendown()
turtle.color('green')
turtle.circle(100)

# 其他设置
turtle.penup()
turtle.goto(230, 230)
turtle.color('black')
turtle.write("Jackey1999", True, align="center", font=('宋体', 20, 'normal'))
turtle.hideturtle()

turtle.done()           # 程序继续执行
