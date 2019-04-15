#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# Author  : Jakcey1999
# Email   : 9516694 # qq.com
# Time    : 2019-03-21-021 上午 0:17
# File    : 编程题2.11投资额.py
# IDE     : PyCharm [Python 3.x]
# Code is far away from bugs with the god animal protecting.
  Life is short. You need Python 3.x

"""
# 编程题2.11投资额

finalMoney = eval(input("请用户输入最终金额/元： "))
rateYear = eval(input("请用户输入年利率/%： "))
years = eval(input("请用户输入年数/年："))

rateMonth = (rateYear / 12) / 100
months = years * 12

initialMoney = finalMoney / ((1 + rateMonth)**months)      # initialMoney 初始金额

print("初始投资金额 = ", initialMoney)
