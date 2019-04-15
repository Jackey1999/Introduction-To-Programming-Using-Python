#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# Author  : Jakcey1999
# Email   : jackey1999 # foxmail.com
# Time    : 2019-03-20-020 上午 10:14
# File    : 编程题1.7.py
# IDE     : PyCharm [Python 3.x]
# Code is far away from bugs with the god animal protecting.
  Life is short. You need Python 3.x

"""

# 1.7
# pi=
max = 11            # max为分支项中的最大数
sum = 0
i = 0
for i in range(1 + max // 2):
    sum = sum + 4 * 1 * ((-1)**i) / (1 + i * 2)
    i = i + 1
print(sum)