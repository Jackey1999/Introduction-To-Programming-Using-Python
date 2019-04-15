#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# Author  : Jakcey1999
# Email   : 9516694 # qq.com
# Time    : 2019-03-22-022 下午 19:34
# File    : 编程题2.20计算利息.py
# IDE     : PyCharm [Python 3.x]
# Code is far away from bugs with the god animal protecting.
  Life is short. You need Python 3.x

"""

balance, rate_interest = eval(input("请分别输入差额（元）和年化利息（%）："))

interest = balance * (rate_interest / 1200)

print("The interest is {:.2f} ".format(interest))
