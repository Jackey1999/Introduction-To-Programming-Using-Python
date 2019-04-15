#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# Author  : Jakcey1999
# Email   : 9516694 # qq.com
# Time    : 2019-03-20-020 下午 22:06
# File    : 讲解2.13贷款计算En.py
# IDE     : PyCharm [Python 3.x]
# Code is far away from bugs with the god animal protecting.
  Life is short. You need Python 3.x

"""
# 输入年化贷款利率
annualInterestRate = eval(input("请输入年化贷款利率/%，如 7.15："))           # 请输入年化利率
monthlyInterestRate = annualInterestRate / 1200

# 输入贷款年限
numberOfYears = eval(input("请输入贷款年限/年，如 5 ："))          # 请输入还款年限


# 输入贷款总额
loanAmount = eval(input("请输入贷款总额/元，如 1200000 ："))                       # 请输入贷款总额

# Calculate payment
monthlyPayment = loanAmount * monthlyInterestRate / \
    (1 - 1 / (1 + monthlyInterestRate)**(numberOfYears * 12))
totalPayment = monthlyPayment * numberOfYears * 12


# 输出结果
print()
print("月均还款额/元：", int(monthlyPayment * 100) / 100)                    # 输出，月供
print("还款总额/元：", int(totalPayment * 100) / 100)                        # 输出，总还款金额
