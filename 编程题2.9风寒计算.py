#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# Author  : Jakcey1999
# Email   : 9516694 # qq.com
# Time    : 2019-03-20-020 下午 23:13
# File    : 编程题2.9风寒计算.py
# IDE     : PyCharm [Python 3.x]
# Code is far away from bugs with the god animal protecting.
  Life is short. You need Python 3.x

"""
# 编程题2.9风寒计算

tA = eval(input("请输入室外华氏温度，低于-58 或 高于 41： "))
if tA <= -58 and tA >= 41:
    print("ERROR:室外华氏温度 tA 输入错误，请重新输入！")
    exit()                                                      # 报错，并退出运行


v = eval(input("请输入高于 2 里/小时的室外风速： "))
if v < 2:
    print("ERROR:室外风速输入错误，请重新输入！")
    exit()                                                      # 报错，并退出运行


tWc = 35.74 + 0.6215 * tA - 35.75 * v**0.16 + 0.4275 * tA * v**0.16

print("当前风寒温度 = {:5f}".format(float(tWc)))                           # 将 tWc 参数传入{}
