#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# Author  : Jakcey1999
# Email   : 9516694 # qq.com
# Time    : 2019-03-20-020 下午 14:15
# File    : 编程题2.6整数拆解并求和.py
# IDE     : PyCharm [Python 3.x]
# Code is far away from bugs with the god animal protecting.
  Life is short. You need Python 3.x

"""

# 2.6

num = eval(input("请输入0-1000之间的整数:"))
# 9521
sum = num // 100 + (num % 100) // 10 + num % 10
print("sum=", sum)
