#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# Author  : Jakcey1999
# Email   : 9516694 # qq.com
# Time    : 2019-03-22-022 下午 17:27
# File    : 编程题2.17计算BMI.py
# IDE     : PyCharm [Python 3.x]
# Code is far away from bugs with the god animal protecting.
  Life is short. You need Python 3.x

"""
# inche 英尺，pound 磅
height_inches, weight_pounds = eval(input("请分别输入身高（英尺）和体重（磅）："))

BMI = weight_pounds * 0.45359237 / ((height_inches * 0.0254)**2)

print("身高{:.2f}英尺，体重{:.2f}磅，BMI={:.4f}".format(
    height_inches, weight_pounds, BMI))
