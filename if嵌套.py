#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# Author  : Jakcey1999
# Email   : 9516694 # qq.com
# Time    : 2019-03-28-028 上午 0:03
# File    : if嵌套.py
# IDE     : PyCharm [Python 3.x]
# Code is far away from bugs with the god animal protecting.
  Life is short. You need Python 3.x

"""
name = input("please input name:")
age = eval(input("please input age:"))
height = eval(input("please input height:"))
star = input("please input star:")
pos = input("please input pos:")
# 陈梦奇，北京，年龄，身高，星座

if pos != "北京":
    print("地址不符合，淘汰")
else:
    if age <= 40:
        print("年龄不符合，淘汰")
    else:
        if height <= 170:
            print("身高不符合，淘汰")
        else:
            if star != "天蝎座":
                print("星座不符合，淘汰")
            else:
                print("符合要求", name)
