#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#函数
#abs()
print('abs(12.56):', abs(12.56))
print('abs(-20):', abs(-20))
#max()
print('max(1, 2):', max(1, 2))
print('max(2, 3, 1, -5):', max(2, 3, 1, -5))
#数据转换
print('int(\'123\'):', int('123'))
print('int(12.56):', int(12.56))
print('str(123):', str(123))
print('str(-12.56):', str(-12.56))
print('bool(1):', bool(1))
print('bool(\'0\'):', bool('0'))
print('bool(\'\'):', bool(''))
#函数可以new一个新对象
a = abs
print('a = abs; a(-1):', a(-1))
#Practice
print('10进制转16进制:255->', str(hex(255)),',1000->', str(hex(1000)))

#定义函数
def my_abs(x):
	if x >= 0:
		return x;
	else:
		return -x;

print('自定义函数my_abs(-99):', my_abs(-99))

#如果想定义一个什么事也不做的空函数，可以用pass语句
def nop():
	pass

import math

def move(x, y, step, angle=0):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx, ny
x, y = move(100, 100, 60, math.pi / 6)
print(x, y)
r = move(100, 100, 60, math.pi / 6)
print(r)
#返回值是一个tuple！
#但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，
#所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。
#Pratice
m, n = (200, 100)
print('m:', m,',n:', n)

def quadratic(a, b, c):
	if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
		return TypeError('bad operand type')
	if b**2<4*a*c:
		print('there is no result')
	return (-b + math.sqrt(b**2 - 4*a*c))/(2*a), (-b - math.sqrt(b**2 - 4*a*c))/(2*a)
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))
if quadratic(2, 3, 1) != (-0.5, -1.0):
	print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
	print('测试失败')
else:
	print('测试成功')	


#关键字函数
def f1(a, b, c=0, *args, **kw):
	print('a = ', a, 'b = ', b, 'c = ', c, 'args = ', args, 'kw = ', kw)
def f2(a, b, c=0, *, d, **kw):
	print('a = ', a, 'b = ', b, 'c = ', c, 'd = ', d, 'kw = ', kw)
print(f1(1, 2, 3))
print(f1(1, 2, 3, 'a', 'b'))
print(f1(1, 2, 3, 'a', 'b', x = 99))
print(f2(1, 2, d = 99, ext = None))

#Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数
#默认参数一定要用不可变对象，否者有逻辑性错误
#*args是可变参数，args接收的是一个tuple
#**kw是关键字参数，kw接收的是一个dict

#Pratice
def product(*args):
	if len(args) == 0:
		raise TypeError('Please enter the right form')
	sum = 1
	for n in args:
		if not isinstance(n, (int, float)):
			raise TypeError('Please enter the right form')
		else:
			sum *= n
	return sum
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')


#递归函数
def fact(n):
	if n == 1:
		return 1;
	return n * fact(n - 1)

print(fact(5))
print(fact(10))

#Pratice 汉诺塔
def move(n, a, b, c):
	if n == 1:
		print(a, '-->', c)
	else:
		move(n-1, a, c, b)
		move(1, a, b, c)
		move(n-1, b, a, c)
print(move(3, 'A', 'B', 'C'))






