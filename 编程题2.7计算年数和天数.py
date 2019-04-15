#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# Author  : Jakcey1999
# Email   : 9516694 # qq.com
# Time    : 2019-03-20-020 下午 15:26
# File    : 编程题2.7计算年数和天数.py
# IDE     : PyCharm [Python 3.x]
# Code is far away from bugs with the god animal protecting.
  Life is short. You need Python 3.x

"""
# 2.7 计算年数和天数

minutes = eval(input("请输入分钟数,例如 10000000 ："))

hours = minutes // 60
days = hours // 24
years = days // 365
remainDays = days % 365

print("转化后，显示为", years, " 年，", remainDays, " 天")
