#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# Author  : Jakcey1999
# Email   : 9516694 # qq.com
# Time    : 2019-03-20-020 下午 13:07
# File    : 讲解2.6交换赋值.py
# IDE     : PyCharm [Python 3.x]
# Code is far away from bugs with the god animal protecting.
  Life is short. You need Python 3.x

"""
# 交换赋值

# 引入中间变量

x = 1
y = 2
temp = x
x = y
y = temp
print(x, "  ", y)

# 交换赋值的高级用法
a = 3
b = 4
a, b = b, a  # swap x with y
print(a, "  ", b)


# 2.7 定名常量

PI = 3.14159    # 通常用大写来定义常量

