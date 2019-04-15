#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# Author  : Jakcey1999
# Email   : 9516694 # qq.com
# Time    : 2019-03-20-020 下午 23:05
# File    : 编程题2.8计算能量.py
# IDE     : PyCharm [Python 3.x]
# Code is far away from bugs with the god animal protecting.
  Life is short. You need Python 3.x

"""
# 编程题2.8计算能量

# 输入 水的重量
waterWeight = eval(input("请输入水的重量/千克："))

# 输入 水的初始温度
waterInitalTemp = eval(input("请输入水的初始温度/摄氏度："))

# 输入 水加热后的温度
waterFinalTemp = eval(input("请输入水加热后的温度/摄氏度："))

# 计算能量
Q = waterWeight * (waterFinalTemp - waterInitalTemp) * 4184

# 输出结果
print("按输入要求计算，加热所需能量为：", Q, " 焦耳")
