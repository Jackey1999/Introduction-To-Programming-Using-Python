#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# Author  : Jakcey
# Email   : 9516694 # qq.com
# Time    : 2019-03-27 15:05
# File    : 编程题3.9工资表.py
# IDE     : PyCharm [Python 3.7]
# Code is far away from bugs with the god animal protecting.
  Life is short. You need Python 3.7

"""
name = input("Enter emplyee's name:")
hoursWorked = eval(input("Enter number of hours worked in a week:"))
payRate = eval(input("Enter hourly pay rate:"))
ftRate = eval(input("Enter federal tax withholding rate:"))
stRate = eval(input("Enter state tax withholding rate:"))

grossPay = hoursWorked * payRate

federalWithholding = hoursWorked * payRate * ftRate
stateWithholding = hoursWorked * payRate * stRate
totalDeduction = federalWithholding + stateWithholding

netPay = grossPay * (1 - ftRate - stRate)

print()
print(
    "Employee Name: {}\nHours Worked: {:.1f}\nPay Rate:${:.1f}\nGross Pay: ${:.1f}".format(
        name,
        hoursWorked,
        payRate,
        grossPay))

print()
print(
    "Decutions:\n  Federal Withholding (20.0%):${:.1f}\n  State Withholding (9.0%):${:.2f}\n  Total Deduction:${:.2f}".format(
        federalWithholding,
        stateWithholding,
        totalDeduction))

print()
print("Net Pay:$ {:.2f} ".format(netPay))
