#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'DeRozan'

'错误、调试和测试'

'Bug fix'

'高级语言通用的try...except...finally'
try:
    print('trying...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')

'Python的错误其实也是class，所有的错误类型都继承自BaseException'

'出错的时候，一定要分析错误的调用栈信息，才能定义错误的位置'


'记录错误'
'logging模块可以非常容易地记录错误信息'

'抛出错误'
'只有在必要的时候才定义我们自己的错误类型。' \
'如果可以选择Python已有的内置的错误类型（比如ValueError，TypeError），尽量使用Python内置的错误类型。'

'''
#Pratice 修复下列程序
from functools import reduce

def str2num(s):
    # return int(s) s可能是浮点数
    try:
        return int(s)
    except ValueError as e:
        return float(s)
    except Exception as e:
        print('Exception:', e)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()

'''


'调试'

'断言' '跟OC和Swift一样，写法和swift一模一样' '启动Python解释器时可以用-O参数来关闭assert,断言的开关“-O”是英文大写字母O，不是数字0。'
'''
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

def main():
    foo('0')
main()

'''

'logging' '不会抛出错误,可以输出到文件'

'''
import logging

n = int('0')
logging.info('n = %d' % n)
print(10 / n)
'''

'pdb'

'''
import pdb

n = int('0')
pdb.set_trace() # 运行到这里会自动暂停
print(10 / n)

'输入命令n可以单步执行代码'
'任何时候都可以输入命令p 变量名来查看变量'
'输入命令q结束调试，退出程序'
'''


'Make a Dict'
class Dict(dict):
    def __init__(self, **kw):
        super().__init__(**kw)
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)
    def __setattr__(self, key, value):
        self[key] = value

d = Dict(a = 1, b = 2)
print(d['a'])
print(d.b)

'Make a Tool for text Dict'
import unittest

class TextDict(unittest.TestCase):
    def  text_init(self): #以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1) # 断言函数返回的结果与1相等
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError): #期待抛出指定类型的Error
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError): #通过d.empty访问不存在的key时，我们期待抛出AttributeError
            value = d.empty

#Practice
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def get_grade(self):
        if self.score > 100 or self.score < 0:
            raise ValueError
        if self.score >= 60 and self.score < 80:
            return 'B'
        if self.score >= 80:
            return 'A'
        return 'C'


class TestStudent(unittest.TestCase):

    def test_80_to_100(self):
        s1 = Student('Bart', 80)
        s2 = Student('Lisa', 100)
        self.assertEqual(s1.get_grade(), 'A')
        self.assertEqual(s2.get_grade(), 'A')

    def test_60_to_80(self):
        s1 = Student('Bart', 60)
        s2 = Student('Lisa', 79)
        self.assertEqual(s1.get_grade(), 'B')
        self.assertEqual(s2.get_grade(), 'B')

    def test_0_to_60(self):
        s1 = Student('Bart', 0)
        s2 = Student('Lisa', 59)
        self.assertEqual(s1.get_grade(), 'C')
        self.assertEqual(s2.get_grade(), 'C')

    def test_invalid(self):
        s1 = Student('Bart', -1)
        s2 = Student('Lisa', 101)
        with self.assertRaises(ValueError):
            s1.get_grade()
        with self.assertRaises(ValueError):
            s2.get_grade()

# if __name__ == '__main__':
#     unittest.main()


'文档测试'


def fact(n):
    '''
    Calculate 1*2*...*n

    >>> fact(1)
    1
    >>> fact(10)
    3628800
    >>> fact(-1)
    Traceback (most recent call last):
      ...
    ValueError
    '''
    if n < 1:
        raise ValueError()
    if n == 1:
        return 1
    return n * fact(n - 1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()















