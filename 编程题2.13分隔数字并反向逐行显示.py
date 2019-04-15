#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# Author  : Jakcey1999
# Email   : 9516694 # qq.com
# Time    : 2019-03-21-021 下午 12:52
# File    : 编程题2.13分隔数字并反向逐行显示.py
# IDE     : PyCharm [Python 3.x]
# Code is far away from bugs with the god animal protecting.
  Life is short. You need Python 3.x

"""

x = eval(input("请输入4位整数："))
y = str(x)                          # 必须先转为 str 类型
print(y[::-1])


'''
本题答案运用 "切片+print" 的方法

参考：
range(stop)
举例，list=(range(10))，输出: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

range(start, stop[, step])
举例，list(range(0, 30, 5))，输出：[0, 5, 10, 15, 20, 25]

解释 s[i:j:k] 是，从i 到j，步长 k，－ 表示倒叙

'''

# 笔记参考1：https://blog.csdn.net/evan123mg/article/details/49232089
# 笔记参考2：https://www.cnblogs.com/ifantastic/archive/2013/04/15/3021845.html