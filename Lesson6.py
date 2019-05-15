#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'a test module'

__author__ = 'DeRozan Liu'

import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello, world!')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if  __name__ == '__main__':
    test()

'作用域'
def _private_1(name):
    return 'Hello, %s' % name
def _private_2(name):
    return  'Hi, %s' % name
def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)
print(greeting('Derozan'))
print(greeting('Zan'))

#类似_xxx和__xxx这样的函数或者变量都是非公开的(private)

#类和实例
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grage(self):
        if  self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

bart = Student('Bart1 Simpson', 60)
bart.name = 'Bart Simpson'
print(bart.name)

bart1 = Student('Bart1 Simpson', 90)
print(bart1.name,bart1.score)

#数据封装
def print_score(std):
    print('%s: %s' % (std.name, std.score))
print_score(bart1)

bart1.print_score()

print(bart.name, bart.get_grage())
print(bart1.name, bart1.get_grage())


#访问限制
'如果让内部属性不被外部访问，可以把属性的名称前面加两个下划线__，在Python中，' \
'实例的变量名如果以__开头，就变成了一个私有变量(private)'
class Student1(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')
bart2 = Student1('DeRozan', 59)
#print(bart2.__name) #AttributeError: 'Student1' object has no attribute '__name'

print(bart2.get_name())

bart2.set_score(100)
print(bart2.get_score())


#Pratice
class Student2(object):
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        self.__gender = gender

bart = Student2('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')

#继承和多态
class Animal(object):
    def run(self):
        print('Animal is running...')
class Dog(Animal):
    def run(self):
        print('Dog is running...')
    def eat(self):
        print('Eating meat...')
class Cat(Animal):
    pass
d = Dog()
print(d.run())
c = Cat()
print(c.run())

print(isinstance(d, Dog))
print(isinstance(d, Animal))

'多态'
def run_twice(animal):
    animal.run()
    animal.run()
print(run_twice(Animal()))
print(run_twice(Dog()))

'获取对象信息'
print(type(123))
print(type('str'))
print(type(None))

print(type(123) == type(456))
print(type(123)== int)
print(type('abc') == type('123'))

'判断一个对象是否是函数'
import types
def fn():
    pass

print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)

print(type(lambda x: x) == types.LambdaType)
print(type(x for x in range(10)) == types.GeneratorType)


'使用isinstance()'
'对于class的继承关系，使用type()很不方便'

'能用type()判断的基本类型也可以使用isintance()判断'
print('isinstance(\'a\', str):', isinstance('a', str))
print('isinstance(123, int):', isinstance(123, int))
print('isinstance(b\'a\', bytes):',isinstance(b'a', bytes))

'判断一个变量是否是某个类型中的一种'
print('isinstance([1, 2, 3], (list, tuple)):', isinstance([1, 2, 3], (list, tuple)))
print('isinstance((1, 2, 3), (list, tuple)):', isinstance((1, 2, 3), (list, tuple)))

'使用dir()函数可以获得一个对象的所有属性和方法'
print(dir('ABC'))
print('ABC'.__len__())

class MyDog(object):
    def __len__(self):
        return 100
dog = MyDog()
print(len(dog))

class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x
obj = MyObject()
print(obj.power())

print(hasattr(obj, 'x')) #是否有属性‘x’
print(obj.x)
print(hasattr(obj, 'y'))
setattr(obj, 'y', 19) #设置一个属性‘y’
print(hasattr(obj, 'y'))
print(obj.y)

# getattr(obj, 'z')
# Traceback (most recent call last):
#   File "/Users/zan/Developer/Python/Lesson6.py", line 211, in <module>
#     getattr(obj, 'z')
# AttributeError: 'MyObject' object has no attribute 'z'

fn = getattr(obj, 'power') #获取属性‘power’赋值给fn
print(fn())
print(type(fn))

'实例属性和类属性'
class Student3(object):
    name = 'Student'
s = Student3()
print(s.name) #打印name属性，因为实例没有name属性，所以会继续查找class的name属性
print(Student3.name)
s.name = 'Michael'
print(s.name) #实例属性优先于类属性
del s.name #删除实例的name属性
print(s.name)

#Pratice
'为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加'
class Student4(object):
    count = 0
    def __init__(self, name):
        self.name = name
        Student4.count +=1

if Student4.count != 0:
    print('测试失败!')
else:
    bart = Student4('Bart')
    if Student4.count != 1:
        print('测试失败!')
    else:
        lisa = Student4('Bart')
        if Student4.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student4.count)
            print('测试通过!')






