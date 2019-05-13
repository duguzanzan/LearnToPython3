#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#返回函数
#高阶函数除了可以接受函数参数外，还可以将函数作为结果值返回

def lazy_sum(*args):
	def sum():
		ax = 0
		for n in args:
			ax += n
		return ax
	return sum

f = lazy_sum(1,2,3,4,5,6,7,8,9)
print(f)
print(f())

print(lazy_sum(1,3,5,7,9) == lazy_sum(1,3,5,7,9))
#每次调用都返回一个新的函数，即使传入相同的参数

#闭包
def count():
	fs = []
	for i in range(1, 4):
		def f():
			return i * i
		fs.append(f)
	return fs
f1, f2, f3 = count()
print(f1(), f2(), f3())
#打印结果全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，他们所引用的变量已经变成了3
#########返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量############

def new_count():
	def f(j):
		def g():
			return j * j
		return g
	fs = []
	for i in range(1, 4):
		fs.append(f(i)) #f(i)立刻被执行，因此i的当前值被传入f()
	return fs
f4, f5, f6 = new_count()
print(f4(), f5(), f6())

#Pratice利用闭包返回一个计数器函数
def createCounter():
	n = 0
	def counter():
		nonlocal n # 使用外层变量
		n += 1
		return n
	return counter
# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')

#匿名函数
#因为函数没有名字，不必担心函数名冲突
#lambda x: x * x实际就是:
#def f(x):
#    return x * x
f = lambda x: x * x
print(f)
print(f(5))

#把匿名函数作为返回值返回
def build(x, y):
	return lambda: x * x + y * y
print(build(2, 4)())

#Practice
L = list(filter(lambda n: n % 2 == 1, range(1, 20)))
print(L)

#装饰器decorator
#函数对象有一个__name__属性，可以拿到函数的名字
def now():
	print('2019-5-13')
f = now
print(f())
print(now.__name__)
print(f.__name__)

def log(text):
	def decorator(func):
		def  wrapper(*args, **kw):
			print('%s %s():' % (text, func.__name__))
			return func(*args, **kw)
		return wrapper
	return decorator
	
@log('execute')
def printDate():
	print('2019-5-13')
print(printDate())
#@log放到now()函数的定义处，相当于执行了：printDate = log(printDate)
#log()是一个decorator

import time, functools
def metric(fn):
	@functools.wraps(fn)
	def wrapper(*args, **kw):
		start = time.time()
		result = fn(*args, **kw)
		stop = time.time() - start
		print('%s enecuted in %s ms' % (fn.__name__, stop * 1000))
		return result
	return fn

@metric
def fast(x, y):
	time.sleep(0.0012)
	return x + y

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')

#偏函数 Partial function
#int()函数提供了base参数，默认值为10.
print(int('12345', base=8))
print(int('12345', 16))

#定义一个int2()函数，实现二进制转换
def int2(x, base=2):
	return int(x, base)
print(int2('1000000'))
print(int2('1010101'))
print(int2('1000000', base=10))

#创建偏函数时，实际上可以接受函数对象、*args和**kw这3个参数
int8 = functools.partial(int, base=8) #相当于：kw = {'base': 8}  int('10010', **kw)
print(int8('10010'))

max2 = functools.partial(max, 10) #相当于args = (10, 5, 6, 7)  max(*args)
print(max2(5, 6, 7))

















