#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# Author  : Jakcey
# Email   : 9516694 # qq.com
# Time    : 2019-03-27 13:11
# File    : 编程题3.3面积估算.py
# IDE     : PyCharm [Python 3.7]
# Code is far away from bugs with the god animal protecting.
  Life is short. You need Python 3.7
  
"""


'''
地图网站 www.gps-data-team.com/map
68923,Atlanta NE in US,GPS Position: 99°24'18"W, 40°24'37"N for x1,y1
73073,Orlando OK in US,GPS Position: 97°24'29"W, 35°56'40"N for x2,y2
36033,Georgiana AL in US,GPS Position: 86°38'5"W, 31°37'28"N for x3,y3
78.11,Charlotte TX in US,GPS Position: 98°39'20"W, 28°48'51"N for x4,y4
'''

import math

# 经纬度坐标值，转化为数值形式
x1,y1=99.405,40.410
x2,y2=97.408,35.944
x3,y3=86.634,31.624
x4,y4=98.656,28.814

# 经纬度转化为弧度数
x1,y1= math.radians(x1),math.radians(y1)
x2,y2 = math.radians(x2),math.radians(y2)
x3,y3 = math.radians(x3),math.radians(y3)
x4,y4 = math.radians(x4),math.radians(y4)

radius = 6371.01

# 计算城市间距离

dAO=radius * math.acos(math.sin(x1) * math.sin(x2) +
                       math.cos(x1) * math.cos(x2) * math.cos(y1 - y2))

dAG=radius * math.acos(math.sin(x1) * math.sin(x3) +
                       math.cos(x1) * math.cos(x3) * math.cos(y1 - y3))

dAC=radius * math.acos(math.sin(x1) * math.sin(x4) +
                       math.cos(x1) * math.cos(x4) * math.cos(y1 - y4))

dOG=radius * math.acos(math.sin(x3) * math.sin(x2) +
                       math.cos(x3) * math.cos(x2) * math.cos(y3 - y2))

dCG=radius * math.acos(math.sin(x3) * math.sin(x4) +
                       math.cos(x3) * math.cos(x4) * math.cos(y3 - y4))

# 计算三角形的面积，PDF p63 面积公式
sAOG=(dAO+dAG+dOG)/2

sACG=(dAC+dAG+dCG)/2

areaAOG=math.sqrt(sAOG*(sAOG-dAG)*(sAOG-dAO)*(sAOG-dOG))

areaACG=math.sqrt(sACG*(sACG-dAG)*(sACG-dAC)*(sACG-dCG))

areaTotal=areaAOG+areaACG

# 输出结果
print("areaTotal = ",areaTotal)



