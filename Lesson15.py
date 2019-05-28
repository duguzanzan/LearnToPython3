#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-05-28 10:35
# @Author  : zan
# @File    : Lesson15.py
# @Title   : base64 & struct

'base64'

'Base64使用一种用64个字符来表达任意二进制数据的方法'
import base64

print('line12:', base64.b64encode(b'binary\x99string'))
print('line13:', base64.b64decode(b'YmluYXJ5mXN0cmluZw=='))

'由于URL中不能出现字符+和/,于是使用url_safe将其分别变为-和_'

print('line17:', base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print('line18:', base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print('line18:', base64.urlsafe_b64decode(b'abcd--__'))

def safe_base64_decode(s):
    while len(s) % 4:
        s += b'='
    return base64.b64decode(s)

assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')


'struct'
'struct的pack函数把任意数据类型转变成bytes'

import struct

print('line37:', struct.pack('>I',10240099))
##########"FUCK,一直把'>I'打成了'>|' "#############
'>表示字节顺序是big-endian,也就是网络序，I表示4字节无符号整数'

print('line40:', struct.unpack('>IH',b'\xf0\xf0\xf0\xf0\x80\x80'))
'H表示2字节无符号整数'

#'BM'表示Windows位图，'BA'表示OS/2位图;
# 一个4字节整数：表示位图大小；
# 一个4字节整数：保留位，始终为0；
# 一个4字节整数：实际图像的偏移量；
# 一个4字节整数：Header的字节数；
# 一个4字节整数：图像宽度；
# 一个4字节整数：图像高度；
# 一个2字节整数：始终为1；
# 一个2字节整数：颜色数。

bmp_data = base64.b64decode('Qk1oAgAAAAAAADYAAAAoAAAAHAAAAAoAAAABABAAAAAAADICAAASCwAAEgsAAAAAAAAAAAAA/3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9/AHwAfAB8AHwAfAB8AHwAfP9//3//fwB8AHwAfAB8/3//f/9/AHwAfAB8AHz/f/9//3//f/9//38AfAB8AHwAfAB8AHwAfAB8AHz/f/9//38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f/9//3//f/9/AHwAfP9//3//f/9//3//f/9//38AfAB8AHwAfAB8AHwAfP9//3//f/9/AHwAfP9//3//f/9//38AfAB8/3//f/9//3//f/9//3//fwB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f/9/AHz/f/9/AHwAfP9//38AfP9//3//f/9/AHwAfAB8AHwAfAB8AHwAfAB8/3//f/9/AHwAfP9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9/AHwAfAB8AHz/fwB8AHwAfAB8AHwAfAB8AHz/f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//38AAA==')

def bmp_info(data):

    array = struct.unpack('<ccIIIIIIHH',data[:30])
    return {
        'width': array[-4],
        'height': array[-3],
        'color': array[-1]
    }

bi = bmp_info(bmp_data)
assert bi['width'] == 28
assert bi['height'] == 10
assert bi['color'] == 16
print('ok')


'hashlib'
'摘要算法又称哈希算法、散列算法。它通过一个函数，把任意长度的数据转换为一个长度固定的数据串'
import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print('line78:', md5.hexdigest())
















