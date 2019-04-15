#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# Author  : Jakcey1999
# Email   : 9516694 # qq.com
# Time    : 2019-03-20-020 上午 10:16
# File    : 编程题1.12.py
# IDE     : PyCharm [Python 3.x]
# Code is far away from bugs with the god animal protecting.
  Life is short. You need Python 3.x

"""

# 1.12，图 1-18a，绘制正方形

import turtle

turtle.setup(500, 500)       # 设置窗口尺寸

turtle.penup()
turtle.goto(100, 100)
turtle.pendown()

for i in range(4):
    turtle.right(90)
    turtle.fd(200)

turtle.penup()
turtle.goto(-100, 0)
turtle.pendown()
turtle.fd(200)

turtle.penup()
turtle.goto(0, -100)
turtle.pendown()
turtle.right(-90)
turtle.fd(100)

turtle.penup()
turtle.goto(0, 100)
turtle.pendown()
turtle.right(180)
turtle.fd(100)

turtle.penup()                    # 签名，font 这里有坑，勿踩
turtle.goto(100, 200)
turtle.pendown()
turtle.write("Jackey1999", move=False,font=("Consolas", 16))
turtle.hideturtle()

turtle.done()               # 运行结束不退出 turtle 绘图窗口