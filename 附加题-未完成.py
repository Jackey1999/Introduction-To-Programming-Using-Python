#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# Author  : Jakcey1999
# Email   : 9516694 # qq.com
# Time    : 2019-03-20-020 上午 10:22
# File    : 附加题-未完成.py
# IDE     : PyCharm [Python 3.x]
# Code is far away from bugs with the god animal protecting.
  Life is short. You need Python 3.x

"""
# 附加题，见微信图 2019-03-19  未完成，后补

import turtle

turtle.setup(500,500)
turtle.speed(1)
'''
# 内圈交错八角形
turtle.penup()
turtle.goto(-50,0)
turtle.pendown()

turtle.pencolor('#FF00FF')
for i in range(8):
    turtle.dot(10, 'red')  # 参数：直径，颜色
    turtle.forward(100)
    turtle.right(-135)
'''

# 中圈交错八角形
turtle.penup()
turtle.goto(-100,0)
turtle.pendown()

turtle.pencolor('#0000EE')
for i in range(8):
    turtle.dot(10, 'black')  # 参数：直径，颜色
    turtle.forward(200)
    turtle.right(-135)


turtle.hideturtle()         # 隐藏小海龟

turtle.done()