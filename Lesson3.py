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
#可以看到，odd不是普通函数，而是generator，在执行过程中，遇到yield就中断，下次又继续执行。执行3次yield后，已经没有yield可以执行了，所以，第4次调用next(o)就报错。
while True:
	try:
		x = next(o)
	except StopIteration as e:
		print('Generator return value:', e.value)
		break
	else:
		pass
	finally:
		pass

#Pratice杨辉三角形
def triangles():
	L = [1]
	while True:
		yield L
		L = [L[i] + L[i + 1] for i in range(len(L) - 1)]
		L.insert(0, 1)
		L.append(1)

n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')

#迭代器
#可以使用isinstance()判断一个对象是否是Iterable对象
from collections.abc import Iterable
print('isinstance([], Iterable):', isinstance([], Iterable))	
print('isinstance({}, Iterable):', isinstance({}, Iterable))
print('isinstance(\'abc\', Iterable):', isinstance('abc', Iterable))
print('isinstance((x for x in range(10)), Iterable):', isinstance((x for x in range(10)), Iterable))
print('isinstance(100, Iterable):', isinstance(100, Iterable))

#可以被next()函数调用并不断返回下一个值的对象成为迭代器：Iterator

from collections.abc import Iterator
print('isinstance((x for x in range(10)), Iterator):', isinstance((x for x in range(10)), Iterator))
print('isinstance([], Iterator):', isinstance([], Iterator))
print('isinstance({}, Iterator):', isinstance({}, Iterator))
print('isinstance(\'abc\', Iterator):', isinstance('abc', Iterator))

#使用iter()函数可以将Iterable变成Iterator
print('isinstance(iter([]), Iterator):', isinstance(iter([]), Iterator))
print('isinstance(iter(\'abc\'), Iterator):',isinstance(iter('abc'), Iterator))

#因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据直到没有数据时抛出StopIteration错误。
#可以把这个数据流看做一个有序序列，但是不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时才会计算
#Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可以那样做的



































