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

md5_section = hashlib.md5()
md5_section.update('how to use md5'.encode('utf-8'))
md5_section.update(' in python hashlib?'.encode(('utf-8')))
print('line83:', md5_section.hexdigest())
'分块多次调用update(),最后的结果是一样的'

'MD5生成结果是固定的128bit字节，通常用一个32位16进制字符串表示'
'SHA1的结果是160bit字节，通常用一个40位16进制字符串表示'
'比SHA1更安全的算法是SHA256和SHA512,不过越安全的算法不仅越慢，而且摘要长度越长'


'摘要算法应用'
db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}

def login(user,password):
    pw_md5 = hashlib.md5(password.encode('utf-8'))
    return pw_md5.hexdigest() == db[user]

assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')

'加盐'
'由于常用口令的MD5值很容易被计算出来，' \
'所以，要确保存储的用户口令不是那些被计算出来的常用口令的MD5,' \
'这一方法通过对原始口令加一个复杂字符串来实现，俗称加盐'

import random

def get_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.salt = ''.join([chr(random.randint(48,122)) for i in range(20)])
        self.password = get_md5(password + self.salt)

db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}

def login(username, password):
    user = db[username]
    return user.password == get_md5(password + user.salt)

assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')


'hmac'
import hmac

message = b'Hello,world!'
key = b'secret'
h = hmac.new(key,message,digestmod='MD5')
print('line151:', h.hexdigest())
'跟普通hash算法非常类似'
'需要穿key&message都是bytes类型'

def hmac_md5(key,s):
    return hmac.new(key.encode('utf-8'),s.encode('utf-8'),digestmod='MD5').hexdigest()

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.key = ''.join(chr(random.randint(48,122)) for i in range(20))
        self.password = hmac_md5(self.key,password)

db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}

def login(username,password):
    user = db[username]
    return user.password == hmac_md5(user.key,password)

assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')















