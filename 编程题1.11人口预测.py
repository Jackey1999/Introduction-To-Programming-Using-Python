#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# Author  : Jakcey1999
# Email   : 9516694 # qq.com
# Time    : 2019-03-20-020 上午 10:15
# File    : 编程题1.11.py
# IDE     : PyCharm [Python 3.x]
# Code is far away from bugs with the god animal protecting.
  Life is short. You need Python 3.x

"""

# 1.11
born_one_year = 365 * (24 * 3600 // 7)           # 每年出生人口
dead_one_year = 365 * (24 * 3600 // 13)          # 每年死亡人口
immigration = 365 * (24 * 3600 // 45)            # 每年移民人口
Now_population = 3120324986                      # 当前人口

i = 1
for i in range(5):
    Total_population = Now_population + i * \
        (born_one_year - dead_one_year + immigration)           # Pycharm中自动换行，以 \ 表示
    i = i + 1
    print('接下来第{}年，人口是{}人。'.format(i, Total_population))