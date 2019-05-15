#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#函数式编程 --Functional Programming
#高阶函数--Higher-order function
#abs = 10
#abs(-10)
#Traceback(most recent call last):
#File "<stdin>", line 1, in <module>
#TypeError: 'int' object is not callable
#因为abs指向10后，就变成整数了
#注：由于abs函数实际上定义在import builtins模块中的，所有要让修改abs变量的指向在其他模块中生效
#要用import builtins; builtins.abs = 10

#传入函数
def add(x, y, f = abs):
	return f(x) + f(y)

print(add(-5, 6, abs))

def f(x):
	return x * x
r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))
#map()作为高阶函数，把运算规则抽象化
print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

from functools import reduce
#reduce(f,[x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
#reduce必须接受两个参数，如果作用于一个序列，会把结果和序列的下个一个元素累计计算
print(reduce(add, [1, 3, 5, 7, 9]))
#求和可以使用sum(),无需动用reduce

def fn(x, y):
	return x * 10 + y
print(reduce(fn, [1, 3, 5, 7, 9]))

def char2num(s):
	digits = {'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9}
	return digits[s]
print(reduce(fn, map(char2num, '13579')))

#简化函数
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def charToNum(s):
	return DIGITS[s]
def strToInt(s):
	return reduce(lambda x, y: x * 10 + y, map(charToNum, s))
print(strToInt('13579'))
#lambda函数 understand

#Pratice
def normalize(name):
	return name[0].upper() + name[1:].lower()
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

def prod(L):
	def mul(x, y):
		return x * y
	return reduce(mul, L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

def str2float(s):
	a,b = s.split('.')
	return reduce(lambda x, y: x * 10 + y, map(charToNum, a)) + reduce(lambda x, y: x * 10 + y, map(charToNum, b)) / pow(10, len(b))
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')

#Python内建的filter()函数用于过滤序列

#删除list中的偶数
def is_odd(n):
	return n % 2 == 1
print(list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

#删除list中的空字符串
def not_empty(s):
	return s and s.strip()
print(list(filter(not_empty, ['A', '', 'B', None, 'C', '   '])))


def _odd_iter():
	n = 1
	while True:
		n += 2
		yield n
def _not_divisible(n):
	return lambda x: x % n > 0
def primes():
	yield 2
	it = _odd_iter() #初始化序列
	while True:
		n = next(it) #返回序列的第一个数
		yield n
		it = filter(_not_divisible(n), it)

#打印1000以内的素数R
for n in primes():
	if n < 1000:
		print(n)
	else:
		break


#Pratice
def is_palindrome(n):
	return n == int(str(n)[::-1])
# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')

#排序算法
#Python内置sorted()函数可以对list进行排序
print(sorted([36, 5, -12, 9, -21]))

#可以接受一个key函数来实现自定义的排序
#按照绝对值大小排序
print(sorted([36, 5, -12, 9, -21], key=abs))

#对字符串排序
print(sorted(['bob', 'about', 'Zoo', 'Credit']))

#Pratice
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
#对上述列表分别按照名字排序
def by_name(t):
	return t[0]
L1 = sorted(L, key=by_name)
print(L1)
#按照成绩从高到低排序
def by_score(t):
	return -t[-1]
L2 = sorted(L, key=by_score)
print(L2)



























