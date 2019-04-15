#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# Author  : Jakcey1999
# Email   : 9516694 # qq.com
# Time    : 2019-03-20-020 下午 14:31
# File    : 编程题2.6整数拆解并求和进阶版.py
# IDE     : PyCharm [Python 3.x]
# Code is far away from bugs with the god animal protecting.
  Life is short. You need Python 3.x

"""
# 2.6

input_number = eval(input("请输入一个正整数:"))
input_number = str(input_number)                  # 必须先转化为字符串形式
sum = 0
for digit in input_number:                      # digit在字符串中
    sum += int(digit)
print(sum)
