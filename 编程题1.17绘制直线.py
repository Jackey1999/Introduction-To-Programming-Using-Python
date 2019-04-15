#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# Author  : Jakcey1999
# Email   : 9516694 # qq.com
# Time    : 2019-03-20-020 上午 10:19
# File    : 编程题1.17.py
# IDE     : PyCharm [Python 3.x]
# Code is far away from bugs with the god animal protecting.
  Life is short. You need Python 3.x

"""


# 1.17，图 1-19b，绘制直线

import turtle

turtle.setup(500, 500)  # 设置窗口尺寸
turtle.speed(1)

turtle.penup()
turtle.goto(-39, 49)
turtle.write(turtle.pos())      # 在窗口上标注当前坐标，精度暂未学
turtle.pendown()

turtle.goto(50, -50)
turtle.write(turtle.pos())      # 在窗口上标注当前坐标，

# 简写turtle.ht(),隐藏海龟。若显示，可使用turtle.showturtle(),简写turtle.st()
turtle.hideturtle()

turtle.penup()                    # 签名，font 这里有坑，勿踩
turtle.goto(100, 200)
turtle.pendown()
turtle.write("Jackey1999", move=False,font=("Consolas", 16))
turtle.hideturtle()

turtle.done()