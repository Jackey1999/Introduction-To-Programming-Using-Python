#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# Author  : Jakcey1999
# Email   : 9516694 # qq.com
# Time    : 2019-03-20-020 上午 10:21
# File    : 编程题1.19.py
# IDE     : PyCharm [Python 3.x]
# Code is far away from bugs with the god animal protecting.
  Life is short. You need Python 3.x

"""

# 1.19，图 1-20a，绘制多边形

import turtle

turtle.setup(500, 500)          # 设置窗口尺寸
turtle.speed(1)                 # 调整绘图速度，便于调教代码

turtle.penup()                  # 设置起始坐标
turtle.right(60)
turtle.forward(150)
turtle.pendown()

turtle.setheading(30)
turtle.circle(150, 360, 6)        # 使用内切多边形的画法

turtle.hideturtle()               # 隐藏海龟

turtle.penup()                    # 签名，font 这里有坑，勿踩
turtle.goto(100, 200)
turtle.pendown()
turtle.write("Jackey1999", font=("Consolas", 16))

turtle.done()