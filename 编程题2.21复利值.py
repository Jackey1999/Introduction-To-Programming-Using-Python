#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# Author  : Jakcey1999
# Email   : 9516694 # qq.com
# Time    : 2019-03-22-022 下午 19:40
# File    : 编程题2.21复利值.py
# IDE     : PyCharm [Python 3.x]
# Code is far away from bugs with the god animal protecting.
  Life is short. You need Python 3.x

"""

manthly_saving_amount = eval(input("请输入每月存款金额/元："))

i = 6
rate_month = 1 + 0.00417

sum = 0
for x in range(i):
    sum = (manthly_saving_amount + sum) * rate_month

print(sum)
