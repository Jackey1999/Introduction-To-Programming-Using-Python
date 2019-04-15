#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# Author  : Jakcey1999
# Email   : 9516694 # qq.com
# Time    : 2019-03-20-020 下午 14:02
# File    : 编程题2.5计算小费.py
# IDE     : PyCharm [Python 3.x]
# Code is far away from bugs with the god animal protecting.
  Life is short. You need Python 3.x

"""
# 参考答案：https://www.cnblogs.com/qiyuanjiejie/p/9569901.html

# 2.5



subtotal, gratuityRate = eval(
    input("Please input subtotal and gratuityRate:"))  # 输入：小计、酬金率
gratuity = subtotal * gratuityRate/100
total = subtotal * (1 + gratuityRate/100)

print(
    "subtotal:",            # 小计
    subtotal,
    " gratuityRate:",       # 酬金率
    gratuityRate,
    " gratuity:",           # 酬金
    gratuity,
    "total:",               # 总金额
    total)
