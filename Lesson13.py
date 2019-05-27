#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-05-27 11:10
# @Author  : zan
# @File    : Lesson13.py
# @Title   : 常用内建模块

'datatime'

from datetime import datetime
'datetime模块中包含datetime类'

now = datetime.now()
print(now)
print(type(now))

dt = datetime(1993,1,18,12,10)#指定日期创建
print(dt)

'datetime转换为timestamp'
print(dt.timestamp())#727330200.0, 小数位表示毫秒数

t = 727330200.0
print(datetime.fromtimestamp(t))#1993-01-18 12:10:00，UTC+8:00时区
print(datetime.utcfromtimestamp(t))#1993-01-18 04:10:00, UTC+0:00时区

'str --> datetime'
cday = datetime.strptime('1993-1-18 12:10:42', '%Y-%m-%d %H:%M:%S')
print(cday)#1993-01-18 12:10:42

'datetime --> str'
print(now.strftime('%a, %b %d %H:%M'))#Mon, May 27 14:48


'datetime加减'
from datetime import timedelta

print(now)
print(now + timedelta(hours=10))
print(now - timedelta(days=1))
print(now + timedelta(days=5, hours=1))


'本地时间转换为UTC时间'
from datetime import timezone

tz_utc_8 = timezone(timedelta(hours=8))
print('line48:',datetime.now())

dt = now.replace(tzinfo=tz_utc_8)
print('line51:',dt)


'时区转换'
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print('line56:',utc_dt)

'astimezone()将转换时区为北京时间'
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print('line60:',bj_dt)

'astimezone()将bj_dt转换时区为东京时间'
tokyo_dt = bj_dt.astimezone(timezone(timedelta(hours=9)))
print('line64:',tokyo_dt)
'不是必须从UTC0:00时区转换到其他地区，任何带时区的datetime都可以正确转换'


'如果要存储datetime，最佳方式是将其转换为timestamp再存储，因为timestamp的值与时区完全无关'

#Practice
import re

def to_timestamp(dt_str, tz_str):

    array = re.match(r'UTC([\+|\-\d]+):(\d+)',tz_str)
    tz_utc_str = timezone(timedelta(hours=int(array.group(1))))
    date_dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S').replace(tzinfo=tz_utc_str)
    return date_dt.timestamp()

# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')















