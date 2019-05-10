#!/usr/bin/env python3
# 为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释
# -*- coding: utf-8 -*-
# 为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码
print("Learn to Python3 In the short term")
print("中文测试正常")

# %运算符就是用来格式化字符串,在字符串内部，%s表示用字符串替换，%d表示用整数替换，有几个%?占位符，后面就跟几个变量或者值，顺序要对应好。
# 如果只有一个%?，括号可以省略
print('Hi,%s,you have $%d.' % ('Michael', 1000))
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

# Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
# len()函数可以获得list元素的个数
print(len(classmates))
# list[-1]可以取到最后一个元素，list[-len(list)]越界	
print(classmates[-1])
# 增 append可以元素添加到末尾
classmates.append('Adam')
print(classmates)
# 插入 insert可以把元素插入到指定位置
classmates.insert(1, 'Jack')
print(classmates)
# 删 pop可以删除末尾的元素
classmates.pop()
print(classmates)
# 删除指定位置元素 pop(i)
classmates.pop(1)
print(classmates)
# 把某一个元素替换成别的
classmates[1] = 'Sarah'
print(classmates)

# 另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改
t = (1,2)
print(t)
tu = ('a','b',['A','B'])
print(tu)

# 条件判断
age = 6
if age >= 18:
	print('your age is', age)
	print('you are adult')
elif age>= 6:
	print('your age is', age)
	print('you are teenager')
else:
	print('kid')

# s = input('birth:')
# birth = int(s)
# if birth < 2000:
# 	print('00前')
# else:
# 	print('00后')

height = 1.83
weitht = 96
bmi = weitht/height * height
if bmi < 18.5:
	print('过轻')
elif bmi < 25:
	print('正常')
elif bmi < 28:
	print('过重')
elif bmi < 32:
	print('肥胖')
else:
	print('严重肥胖')

# Cycle
sum = 0
for x in range(101):
	sum += x
print(sum)

sum = 0
n = 99
while n > 0:
	sum += n
	n -= 2
print(sum)

# Dictionary
d = {'Michael' : 95, 'Bob' : 75, 'Tracy' : 85}
print(d['Michael'])

d['Adam'] = 67
print(d)

#如果key不存在，dict就会报错：
#要避免key不存在的错误，有两种办法，一是通过in判断key是否存在：'Thomas' in d
#二是通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value：d.get('Thomas')
print(d.get('Thomas'))
print('Is Thomas in d?','Thomas' in d)
#注意：返回None的时候Python的交互环境不显示结果。

#要删除一个key，用pop(key)方法，对应的value也会从dict中删除：
d.pop('Bob')
print(d)

#请务必注意，dict内部存放的顺序和key放入的顺序是没有关系的。

#和list比较，dict有以下几个特点：
# 查找和插入的速度极快，不会随着key的增加而变慢；
# 需要占用大量的内存，内存浪费多。

# 而list相反：
# 查找和插入的时间随着元素的增加而增加；
# 占用空间小，浪费内存很少。
# 所以，dict是用空间来换取时间的一种方法。

#set 集合
#set和dict类似，也是一组key的集合，但不存储value.key不能重复
s = set([1,1,2,2,3,3])
print(s)

#add(key)
s.add(4)
print(s)

#remove(key)
s.remove(4)
print(s)

s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print('s1:', s1, ',s2:', s2)
# 两个set可以做数学意义上的交集、并集等操作：
print('s1 & s2:', s1 & s2)
print('s1 | s2:', s1 | s2)

#list
a = ['c', 'b', 'a']
# 对list进行操作，list内部的内容是会变化的
a.sort()
print('a:', a)

str = 'abc'
# 对于不可变对象操作, 会返回一个新的值
print('str.replace(\'a\',\'A\'):',str.replace('a', 'A'))
print('str:',str)
newStr = str.replace('a', 'A')
print(newStr)










