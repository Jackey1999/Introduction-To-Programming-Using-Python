#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# Author  : Jakcey1999
# Email   : 9516694 # qq.com
# Time    : 2019-03-20-020 上午 10:21
# File    : 编程题1.18.py
# IDE     : PyCharm [Python 3.x]
# Code is far away from bugs with the god animal protecting.
  Life is short. You need Python 3.x

"""

# 1.18，图 1-19c，绘制五角星
import turtle

turtle.setup(500, 500)  # 设置窗口尺寸
turtle.speed(1)         # 调整绘图速度，便于观察+调教代码

turtle.penup()                    # 签名，font 这里有坑，勿踩
turtle.goto(100, 200)
turtle.pendown()
turtle.write("Jackey1999", move=False,font=("Consolas", 16))

turtle.penup()          # 调整起点位置
turtle.goto(0, 100)
turtle.pendown()

turtle.right(72)        # 调整海龟朝向

for i in range(5):
    turtle.fd(200)
    turtle.right(144)

turtle.setheading(72)       # 调整海龟朝向

turtle.done()