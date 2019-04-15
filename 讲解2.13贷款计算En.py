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
# Enter annual interest rate as apercetage
annualInterestRate = eval(input("Enter annual interest rate,e.g.,7.25:"))           # 请输入年化利率
monthlyInterestRate = annualInterestRate / 1200

# Enter number of years
numberOfYears = eval(input("Enter number of years as an integer,e.g.,5:"))          # 请输入还款年限


# Enter loan amout
loanAmount = eval(input("Enter loan amount,e.g.,120000.95:"))                       # 请输入贷款总额

# Calculate payment
monthlyPayment = loanAmount * monthlyInterestRate / \
    (1 - 1 / (1 + monthlyInterestRate)**(numberOfYears * 12))
totalPayment = monthlyPayment * numberOfYears * 12


# Display results
print()
print("The monthly payment is", int(monthlyPayment * 100) / 100)                    # 输出，月供
print("The total payment is", int(totalPayment * 100) / 100)                        # 输出，总还款金额
