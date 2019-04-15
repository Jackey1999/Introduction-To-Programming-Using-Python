#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# Author  : Jakcey1999
# Email   : 9516694 # qq.com
# Time    : 2019-03-20-020 上午 11:17
# File    : 讲解time库.py
# IDE     : PyCharm [Python 3.x]
# Code is far away from bugs with the god animal protecting.
  Life is short. You need Python 3.x

"""
# time库，时间的计算
import time
mytimes=time.time()
print(mytimes)

# mytimes=3691

seconds=int(mytimes) % 60                                 # 秒，取模，表示现在第几秒
hours=int(mytimes) // 3600                                # 小时，取整，表示已过去多少小时
minutes=int(mytimes) // 60
minutes=(minutes - seconds) // 60
# minutes = ((int(mytimes) - int(mytimes) // 3600 * 3600) -seconds) // 60
# # 表示已过去多少分钟
days=hours // 24
hours=hours % 24
print('自从1970年到现在，已过去:', days, '天', hours, '小时', minutes, '分', seconds, '秒')