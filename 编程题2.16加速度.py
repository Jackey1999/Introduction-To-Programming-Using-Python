#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# Author  : Jakcey1999
# Email   : 9516694 # qq.com
# Time    : 2019-03-22-022 下午 17:20
# File    : 编程题2.16加速度.py
# IDE     : PyCharm [Python 3.x]
# Code is far away from bugs with the god animal protecting.
  Life is short. You need Python 3.x

"""
# 编程题2.16加速度
v0, v1, t = eval(input("请分别输入初始速度（米/秒）、末速度（米/秒）、时间（秒）："))

a = (v1 - v0) / t

print("平均加速度为: {:.2f} 米/秒^2".format(a))
