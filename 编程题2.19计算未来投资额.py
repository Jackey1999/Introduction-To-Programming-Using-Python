#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# Author  : Jakcey1999
# Email   : 9516694 # qq.com
# Time    : 2019-03-22-022 下午 19:28
# File    : 编程题2.19计算未来投资额.py
# IDE     : PyCharm [Python 3.x]
# Code is far away from bugs with the god animal protecting.
  Life is short. You need Python 3.x

"""

amount, rate, years = eval(input("请分别输入投资金额/元，年化利率/%，投资期限/年："))

accumulateAmount = amount * (1 + rate / 100 / 12)**(years * 12)

print("未来投资总额 = {:.2f} 元".format(accumulateAmount))
