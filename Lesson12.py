#!/usr/bin/env python3
# -*- conding: utf-8 -*-

__author__ = 'DeRozan'

'正则表达式'
#用\d匹配一个数字，\w匹配一个字母, 用.可以匹配任意字符
#用*表示任意个字符，包括0个，用+表示至少一个字符，用?表示0或1个字符，用{n}表示n个字符
#\s可以匹配一个空格（也包括Tab等空白符）

#例子:\d{3}\s+\d{3,8}
#\d{3}表示匹配3个数字
#\s+表示至少有一个空格
#\d{3,8}表示3-8个数字

"特殊字符在正则表达式中，要用 \ 转义"

'要做到更精确的匹配，可以用[]表示范围'
'[0-9a-zA-Z\_]可以匹配一个数字、字母或者下划线'
'[0-9a-zA-Z\_]+可以匹配至少一个数字、字母或下划线，比如a100,0_Z,Py3000'
'[a-zA-Z\_][0-9a-zA-Z\_]*可以匹配有字母或下划线开头，后面接任意个由数字、字母或下划线的字符串，也就是合法变量'
'[a-zA-Z\_][0-9a-zA-Z\_]{0.19}匹配同上，只是精确到1-20个字符（前面1个字符，后面最多19个字符）'


'A|B可以匹配A或B，所以（P|p）ython可以匹配Python或者python'
'^表示行的开头，^\d表示必须以数字开头'
'$表示行的结束，\d$表示必须以数字结尾'


'Python提供re模块，包含所有正则表达式共更能'
'由于Python的字符串本身也用\转义，所以强烈建议使用r前缀'
# s = r'ABC\-001'
# print(s)

# import re
# >>> re.match(r'^\d{3}\-\d{3,8}$', '010-123456')
#     <re.Match object; span=(0, 10), match='010-123456'>
# >>>re.match(r'^\d{3}\-\d{3,8}$', '010 123456')
#
'如果匹配成功，返回一个Match对象,否则返回None'

'切割字符串'
#>>> re.split(r'\s+','ab c')
# ['ab', 'c']
#>>> re.split(r'[\s\,\;]+','a,b;;c    d')
# ['a', 'b', 'c', 'd']
'无论多少空格或者分号都可以正常分割，正则比字符串方法使用更加方便'

'分组'
# >>> m = re.match(r'^(\d{3})-(\d{3,8})$','010-12345')
# >>> m
#     <re.Match object; span=(0, 9), match='010-12345'>
# >>> m.group(0)
#     '010-12345'
# >>> m.group(1)
#     '010'
# >>> m.group(2)
#     '12345'
# >>> m.group(3)
#     Traceback (most recent call last):
#         File "<input>", line 1, in <module>
#     IndexError: no such group
# >>> m.groups()
#    ('010', '12345')
'提取子串，用()表示要提取的分组'

# >>> t = '19:05:30'
# >>> m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
# >>> m.groups()
#     ('19', '05', '30')
'识别合法时间的正则表达式'

'贪婪匹配'
# >>> re.match(r'(\d+)(0*)$','102300').groups()
#     ('102300', '')
# >>> re.match(r'(\d+?)(0*)$','102300').groups()
#     ('1023', '00')
'由于\d+采用了贪婪匹配，直接把后面的0全部匹配了'
'加个？就可以让\d+采用非贪婪匹配'


'编译'
'如果一个正则表达式要重复使用几千次，我们可以预编译正则表达式'
# 编译:
# >>> re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
# 使用：
# >>> re_telephone.match('010-12345').groups()
# ('010', '12345')
# >>> re_telephone.match('010-8086').groups()
# ('010', '8086')


#Practice

import re

'验证Email地址'
def is_valid_email(addr):
    return re.match(r'^\w+[0-9|a-z|A-Z|.]+@[\w|\d]+\.com$',addr)

assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')

'可以提取出名字的Email地址'
def name_of_email(addr):
    array = re.split(r'[\>\@]',addr.replace('<',''))
    return array[0]

assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')














