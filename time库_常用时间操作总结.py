#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# Author  : Jakcey1999
# Email   : 9516694 # qq.com
# Time    : 2019-03-20-020 下午 15:40
# File    : time库_常用时间操作总结.py
# IDE     : PyCharm [Python 3.x]
# Code is far away from bugs with the god animal protecting.
  Life is short. You need Python 3.x

"""
# 来源： https://blog.csdn.net/ppdyhappy/article/details/78175547

# time库 中文文档：https://www.rddoc.com/doc/Python/3.6.0/zh/library/time/#time.time


import time     # 导入 module

a=time.time()                   # 查看当前时间
# 1553068069.3334055

ISOTIMEFORMAT='%Y-%m-%d %X %a'          # 设置时间格式,按需自定义格式

d1=time.strftime(ISOTIMEFORMAT,time.localtime())     # 根据设定的时间格式，解析当前的时间
# 2019-03-20 15:50:37 Wek

d2=time.ctime()

b=time.localtime()                      # 返回当前时区的时间
# time.struct_time(tm_year=2019, tm_mon=3, tm_mday=20, tm_hour=15, tm_min=47, tm_sec=17, tm_wday=2, tm_yday=79, tm_isdst=0)

c=time.gmtime()                          # 返回 0 时区的时间
# time.struct_time(tm_year=2019, tm_mon=3, tm_mday=20, tm_hour=7, tm_min=48, tm_sec=12, tm_wday=2, tm_yday=79, tm_isdst=0)



e=time.timezone  # 查看时区。这是秒值，为当前时区和 0 时区相差的描述，-28800=-8*3600，即为东八区

f=time.asctime()    # Wed Mar 20 16:08:17 2019

g=time.clock()  # 第一次调用，返回程序的运行时间；第二次调用，返回据前次调用的时间差。

k=time.sleep(1)    # 线程延迟指定时间，单位：秒 time.sleep(secs)

g1=time.clock()

print(e)

