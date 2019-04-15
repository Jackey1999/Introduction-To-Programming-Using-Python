#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# Author  : Jakcey1999
# Email   : 9516694 # qq.com
# Time    : 2019-03-21-021 上午 10:41
# File    : 讲解format函数.py
# IDE     : PyCharm [Python 3.x]
# Code is far away from bugs with the god animal protecting.
  Life is short. You need Python 3.x

"""
# format() 函数文档：http://www.runoob.com/python/att-string-format.html

# format 函数可以接受不限个参数，位置可以不按顺序。

print("网站名称：{name},网址：{url}".format(name="菜鸟教程", url="http://www.runoob.com"))

# 使用位置进行填充
print("Hello,{}. My name is {}. How is going? ".format("Hialry", "Vergil"))
# Hello,Hialry. My name is Vergil. How's it going?

# 若格式中未指定填充位置，将会按序填充
print("{}  {}  {}  {}  {}  {}".format("1", "2", "3", "4", "5", "6"))
# 1  2  3  4  5  6

print("{0}  {1}  {3}  {5}  {2}  {4}".format("1", "2", "3", "4", "5", "6"))
# 1  2  4  6  3  5

# 使用关键字段进行填充
print(
    "I\'m {name1} ,and I miss u so much,{name2}.".format(
        name1="Vergil",
        name2="Hilary"))
# # I'm Vergil ,and I miss u so much,Hilary.

names = ['Hilary', 'Vergil', 'Nero']
places = ['Chengdu', 'Shijiazhuang', 'Tokyo']
print(
    "Hi {names[0]}.I am {names[1]} and this is {names[2]}.".format(
        names=names))
# Hi Hilary.I am Vergil and this is Nero.

print(
    "Three people:{0[0]},{0[1]},{0[2]} from three places:{1[0]},{1[1]},{1[2]}.".format(
        names,
        places))
# Three people:Hilary,Vergil,Nero from three places:Chengdu,Shijiazhuang,Tokyo.

# 进制转换
print("{0:b},{0:o},{1:d},{1:x}".format(256, 512))
# 100000000,400,512,200

# 逗号分隔
print("{:,}".format(123456789))
# 123,456,789


# 浮点数格式
print("{:+12.3f}".format(3.14159265358979))
# +3.142

# 对齐与填充, \n 换行符
print(
    "{:>010}\n".format(12),                 # 右对齐，填充0，宽度10
    "{:0>10}\n".format(12),                 # 填充0,右对齐，宽度10
    "{:x>10}\n".format(12),                 # 填充0,右对齐，宽度10
    "{:0<+12.3f}\n".format(-12.34567),      # 填充0，左对齐，保留+号，宽度12，保留3位小数
    "{:^10}\n".format(3)                    # 居中对齐，宽度10
)
'''
0000000012
 0000000012
 -12.34600000
     3   
'''
        # 以上 print 结果，第 2 行开始多了一个空格，原因未知
print("{:>010}".format(12))
print("{:0>5}".format(12))
print("{:x>6}".format(12))
print("{:x<6}".format(12))
print("{:x^6}".format(12))
print("{:0<+12.3f}".format(-12.34567))
print("{:^10}".format(3) )
'''
0000000012
00012
xxxx12
12xxxx
xx12xx
-12.34600000
    3   
'''

