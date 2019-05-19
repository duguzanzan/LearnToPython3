#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
function 1:
try:
    f = open('/Users/zan/Developer/Python/test.txt', 'r')
    print(f.read())
finally:
    if f:
        f.close()
'''

'''
function 2:
with open('/Users/zan/Developer/Python/test.txt', 'r') as f:
    print(f.read())
'''

'''
read()会一次性读取文件的全部内容
read(size)方法，每次最多读取size个字节的内容
readline()可以每次读取一行内容
readlines()一次读取所有内容并按行返回list
***如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便
for line in f.readlines():
    print(line.strip()) # 把末尾的'\n'删掉
'''

'file-like Object'

























