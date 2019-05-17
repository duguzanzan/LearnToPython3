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
















