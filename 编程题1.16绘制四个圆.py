#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# Author  : Jakcey1999
# Email   : 9516694 # qq.com
# Time    : 2019-03-20-020 上午 10:18
# File    : 编程题1.16.py
# IDE     : PyCharm [Python 3.x]
# Code is far away from bugs with the god animal protecting.
  Life is short. You need Python 3.x

"""



# 1.16，图 1-19a，绘制四个圆

import turtle

turtle.setup(500, 500)  # 设置窗口尺寸

turtle.penup()          # 第一象限，圈1
turtle.goto(30, 30)
turtle.pendown()
turtle.circle(30)

turtle.penup()          # 第二象限，圈2
turtle.goto(-30, 30)
turtle.pendown()
turtle.circle(30)

turtle.penup()          # 第三象限，圈3
turtle.goto(-30, -30)
turtle.pendown()
turtle.circle(30)

turtle.penup()          # 第四象限，圈4
turtle.goto(30, -30)
turtle.pendown()
turtle.circle(30)

turtle.penup()                    # 签名，font 这里有坑，勿踩
turtle.goto(100, 200)
turtle.pendown()
turtle.write("Jackey1999", move=False,font=("Consolas", 16))
turtle.hideturtle()

turtle.done()