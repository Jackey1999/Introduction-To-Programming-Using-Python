#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# Author  : Jakcey1999
# Email   : 9516694 # qq.com
# Time    : 2019-03-21-021 上午 0:11
# File    : 编程题2.10计算跑道长度.py
# IDE     : PyCharm [Python 3.x]
# Code is far away from bugs with the god animal protecting.
  Life is short. You need Python 3.x

"""
# 编程题2.10计算跑道长度

v = eval(input("请输入飞机的起飞速度，默认单位（米/秒） ："))
a = eval(input("请输入飞机的加速度，默认单位（米/秒^2） ："))

length = v**2 / (2 * a)

print("根据给定的参数，飞机起飞所需的最短跑道长度为 {} 米".format(length))
