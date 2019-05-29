#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-05-29 14:24
# @Author  : zan
# @File    : Lesson16.py
# @Title   : 常用的内建模块

'itertools'
'提供了非常有用的用于操作迭代对象的函数'

import itertools

'''
natuals = itertools.count(1)
for n in natuals:
    print(n)#打印自然数序列
'''

'''
cs = itertools.cycle('ABC')
for c in cs:
    print(c)#无线循环打印字符，字符串也是一种序列
...
'A'
'B'
'C'
'A'
'B'
'C'
...
'''

'''
ns = itertools.repeat('ABC',3)#负责把第一个元素无限重复下去，如果给了第二元素，就限定了重复次数
for n in ns:
    print(n)
...
ABC
ABC
ABC
...
'''

natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x<=10,natuals)
print('line46:',list(ns))
print('line47:', ns)
'takewhile()可以通过条件判断来截取出一个有限序列'

'chain()'
for c in itertools.chain('ABC','XYZ'):
    print('line52:', c)

'groupby()'
'把相邻的重复的元素跳出来放在一起'
for key,group in itertools.groupby('AAABBBCCAAA'):
    print('line57:', key, list(group))

for key, group in itertools.groupby('AaaBbBCcaAa', lambda x:x.upper()):
    print('line60:', key, list(group))

#Practice
def pi(N):
    '计算pi的值'
    #step 1:创建一个奇数序列：1，3，5，9...
    natuals = itertools.count(1,2)
    #step 2: 取出序列的前N项：1，3，5，7，9...2*N-1.
    ns = itertools.takewhile(lambda x: x<=(2 * N - 1),natuals)
    #step 3: 添加正负符号并用4除：4/1,-4/3,4/5,-4/7,4/9...
    pm = list(ns)
    result = list(map(lambda x: float(4 / x * 1 if pm.index(x) % 2 == 0 else 4 / x * -1), pm))
    #step 4: 求和
    return sum(result)

print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')












