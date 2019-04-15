#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# Author  : Jakcey1999
# Email   : 9516694 # qq.com
# Time    : 2019-03-20-020 上午 11:12
# File    : 讲解10显示线段长度.py
# IDE     : PyCharm [Python 3.x]
# Code is far away from bugs with the god animal protecting.
  Life is short. You need Python 3.x

"""
import turtle

x1, y1 = eval(input('请输入x1,y1：'))
x2, y2 = eval(input('请输入x2,y2：'))

turtle.penup()
turtle.goto(x1, y1)
turtle.write(str(x1) + ',' + str(x2))
turtle.pendown()
turtle.goto(x2, y2)
turtle.write(str(x2) + ',' + str(y2))


turtle.goto((x1+x2)/2,(y1+y2)/2)
length=((x1-x2)**2+(y1-y2)**2)**0.5
turtle.write('长度='+str(length))

turtle.done()

