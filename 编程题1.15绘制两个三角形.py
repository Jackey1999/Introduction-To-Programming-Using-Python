#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# Author  : Jakcey1999
# Email   : 9516694 # qq.com
# Time    : 2019-03-20-020 上午 10:18
# File    : 编程题1.15.py
# IDE     : PyCharm [Python 3.x]
# Code is far away from bugs with the god animal protecting.
  Life is short. You need Python 3.x

"""


# 1.15，图 1-18d，绘制两个三角形

import turtle

turtle.setup(500, 500)  # 设置窗口尺寸

turtle.right(60)        # 绘制下方三角形
turtle.fd(200)

turtle.right(120)
turtle.fd(200)

turtle.right(120)
turtle.fd(200)

turtle.fd(200)          # 绘制上方三角形

turtle.right(-120)
turtle.fd(200)

turtle.right(-120)
turtle.fd(200)

turtle.penup()                    # 签名，font 这里有坑，勿踩
turtle.goto(100, 200)
turtle.pendown()
turtle.write("Jackey1999", move=False,font=("Consolas", 16))
turtle.hideturtle()

turtle.done()  # 运行结束不退出 turtle 绘图窗口