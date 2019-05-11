#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#高级特性

#切片
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
#取list的前三个元素
print(L[:3]) #这里的3是索引3，但是不包含索引3的元素
#从索引1开始取到索引3的元素
print(L[1:3])
#取倒数两个元素
print(L[-2:])

L = list(range(100))
#前10个
print(L[:10])
#后10个
print(L[-10:])
#前10个数，每两个取一个
print(L[:10:2])
#所有的数，每5个取一个
print(L[::5])

#tuple也是不可变的list，切片之后仍是tuple
print((0, 1, 2, 3, 4, 5)[:3])

#字符串'xxx'也可以看成是一种list
print('ABCDEFG'[:3])
print('ABCDEFG'[::2])

#Pratice
def trim(s):
	while s != '' and s[0] == ' ':
		s = s[1:]
	while s != '' and s[-1] == ' ':
		s = s[:-1]
	return s

if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')


#迭代 Iteration
#只要是可迭代对象，无论有无下标，都可以迭代，比如字典
d = {'a' : 1, 'b' : 2, 'c' : 3}

#打印key
for key in d:
	print(key)
#打印value
for value in d.values():
	print(value)

#字符串也是迭代对象
for ch in 'ABCDEFG':
	print(ch)

#通过collections模块的Iterable类型判断是否可迭代
from collections import Iterable
print('str是否可迭代:', isinstance('abc', Iterable))
print('list是否可迭代:', isinstance([1,2,3], Iterable))
print('整数是否可迭代:', isinstance(123, Iterable))

#Python内置的enumerate函数可以把一个list变成索引-元素对
for i, value in enumerate(['A', 'B', 'C']):
	print(i, value)
for x, y in [(1, 1)]:
	pass

#Pratice

def findMinAndMax(L):
	if len(L) == 0:
		return (None,None)
	a = L[0]
	b = L[0]
	for x in L:
		if x < a:
			a = x
		if x > b:
			b = x
	return (a, b)

if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')

#列表生成式
#列表生成式是Python内置的非常简单却强大的可以从来创建list的生成式
print(list(range(1, 11)))

#生成【1*1, 2*2, 3*3, ..., 10*10]
L = []
for x in range(1,11):
	L.append(x * x)
print(L)
#anthor
print([x * x for x in range(1, 11)])

#for循环后面加上if判断
print([x * x for x in range(1, 11) if x % 2 == 0])#筛选出仅偶数的平方

#两层循环
print([m + n for m in 'ABC' for n in 'XYZ'])

#运用列表生成式，可以写出非常简洁的代码
#一行代码生成所有文件和目录名
import os #导入os模块
print([d for d in os.listdir('.')]) #os.listdir可以列出文件和目录


#for循环可以同时使用两个甚至多个变量，比如dictionary的items()可以同时迭代key和value
d = {'x' : 'A', 'y' : 'B', 'z' : 'C'}
for k, v in d.items():
	print(k, '=', v)
#列表生成式写法
print([k + '=' + v for k, v in d.items()])

L = ('Hello', 'World', 'Apple', 'NBA')
#将tuple中的字符串变成小写
print([s.lower() for s in L])
#完善列表式
L = ('Hello', 'World', 100, 'Apple', 'NBA', 200)
print([s.lower() for s in L if isinstance(s, str)])

#Practice
L1 = ('Hello', 'World', 26, 'Apple', 'NBA', None)
print([s.lower() for s in L1 if isinstance(s, str)])


#生成器 generator
g = (x * x for x in range(10))
print(g)
#区别仅在于最外层的[]和(),g是一个generator
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
# print(next(g))
#generator保存的是算法，每次调用next(g),就是计算出g的下一个元素的值，直到最后一个元素，没有更多元素时，抛出StopIteration的错误


#斐波拉切数列
def fib(max):
	n, a, b, = 0, 0, 1
	while n < max:
		print(b)
		a , b = b, a + b
		n = n + 1
	return 'done'
print(fib(10))


#generator的函数，在每次调用next()的时候，遇到yield语句或者是回
def odd():
	print('step 1')
	yield 1
	print('step 2')
	yield 3
	print('step 3')
	yield 5
o = odd()
print(next(o))
print(next(o))
print(next(o))
# print(next(o))






































