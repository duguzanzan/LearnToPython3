#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-05-31 17:50
# @Author  : zan
# @File    : Lesson20.py
# @Title   : 常用的三方模块

'requests'

import requests

# r = requests.get('https://www.douban.com/')
# print(r.status_code)
# print(r.text)

r = requests.get('http://canal.stockstar.com/Base/V_BS_STK_STAR_GUIDENCE/full=2&sort=DECLAREDATE%20desc&encoding=utf8&limit=20')
print('line17:', r.url)
print('line18:', r.encoding)
print('line19:', r.content)
print('line20:', r.json())













