#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'DeRozan Liu'

'面向对象高级编程'

'使用__slots__'

class Student(object):
    pass
s = Student()
s.name = 'DeRozan'
print(s.name)

def set_age(self, age):
    self.age = age

from types import MethodType

s.set_age = MethodType(set_age, s) #给实例绑定一个方法
s.set_age(25)
print(s.age) # 25

s2 = Student()
# s2.set_age(25)
# Traceback (most recent call last):
#   File "/Users/zan/Developer/Python/Lesson7.py", line 26, in <module>
#     s2.set_age(25)
# AttributeError: 'Student' object has no attribute 'set_age'
# 对另一个实例是不起作用的

'给所有实例都绑定方法'
def set_score(self, score):
    self.score = score
Student.set_score = set_score

s.set_score(100)
print(s.score) #100

s2.set_score(99)
print(s2.score) #99

'如果只允许Student实例添加name和age属性，Python在定义class的时候使用__slots__变量'
class Student1(object):
    __slots__ = ('name', 'age') #用tuple定义允许绑定的属性名称

s3 = Student1()
s3.name = 'DeRozan'
s3.age = 26
# s3.score = 99
# Traceback (most recent call last):
#   File "/Users/zan/Developer/Python/Lesson7.py", line 51, in <module>
#     s3.score = 99
# AttributeError: 'Student1' object has no attribute 'score'

class GraduateStudent(Student1):
    pass
g = GraduateStudent()
g.score = 9999
print(g.score) #__slots__定义的属性仅对当前类实例起作用，对于继承的子类没有作用


#使用@property,(*???感觉好像Object-C和Swift的合体)
class Student2(object):
    def get_score(self):
        return self._score
    def set_score(self, score):
        if not isinstance(score, (int, float)):
            raise ValueError('score must be an integer or float!')
        if score < 0 or score > 100:
            raise ValueError('score must between 0 - 100!')
        self._score = score
s2 = Student2()
s2.set_score(99)

'进化版'
class Student3(object):
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self, score):
        if not isinstance(score, (int, float)):
            raise ValueError('score must be an inteager or float!')
        if score < 0 or score > 100:
            raise  ValueError('score must between 0 - 100!')
        self._score = score
    @property
    def birth(self):
        return  self._birth
    @birth.setter
    def birth(self, value):
        self._birth = value
    @property
    def age(self):
        return self._age
s3 = Student3()
s3.score = 99.5
print(s3.score)
s3.birth = '1993-1-18'
print(s3.birth)
# s3.age = 26
# print(s3.age)
# Traceback (most recent call last):
#   File "/Users/zan/Developer/Python/Lesson7.py", line 103, in <module>
#     s3.age = 26
# AttributeError: can't set attribute
#只定义getter方法，不定义setter方法就是一个只读属性


#Pratice
class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('value must be inteager or float!')
        if value < 0:
            raise ValueError('value must be bigger than 0!')
        self._width = value
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('value must be inteager or float!')
        if value < 0:
            raise ValueError('value must be bigger than 0!')
        self._height = value
    @property
    def resolution(self):
        self._resolution = self._width * self._height
        return self._resolution
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')

'多重继承'
class Animal(object):
    pass

#大类
class Mammal(object):
    pass
class Bird(object):
    pass

#功能
class Runnable(object):
    def run(self):
        print('Running...')
class Flyable(object):
    def fly(self):
        print('Flying...')

#各种动物
class Dog(Mammal, Runnable):
    pass
class Bat(Mammal, Flyable):
    pass
class Parrot(Bird, Flyable):
    pass
class Ostrich(Bird, Runnable):
    pass


'定义类'
'形如__xxx__的变量或者函数名可能在Python中有着特殊用途'

'__str__'
class Student4(object):
    def __init__(self, name):
        self._name = name
    def __str__(self):
        return 'Student object (name: %s)' % self._name
print(Student4('DeRozan'))

'__iter__'
'如果一个类被用于for...in循环，类似list或tuple那样，必须实现__iter__()'
'__iter__()返回一个迭代对象，for循环不断的调用迭代对象的__next__()'
class Fib(object):
    def __init__(self):
        self._a,self._b = 0, 1
    def __iter__(self):
        return self
    def __next__(self):
        self._a, self._b = self._b, self._a + self._b
        if self._a > 100000:
            raise StopIteration()
        return self._a
    def __getitem__(self, item):
        if isinstance(item, int):
            # item是索引
            a, b = 1, 1
            for x in range(item):
                a, b = b, a + b
            return a
        if isinstance(item, slice):
            # item是切片
            start = item.start
            stop = item.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

for n in Fib():
    print(n)

'__getitem__'
'Fib实例虽然能作用于for循环，看起来像list，但是不能当list来使用'
'要想像list那样按照下标取元素，必须实现__getitem__()'
f = Fib()
print(f[5])

'list有切片方法，所以__getitem__要判断是否是切片'
print(f[:5])
'但是没有对step参数做处理,也没有对负数做处理,所以要实现真正的__getitem__有很多工作要做'


'__getattr__'
'调用类不存在的属性会报错，通过__getattr__()方法，动态返回一个属性'
class Student5(object):
    def __init__(self):
        self.name = 'DeRozan'
    def __getattr__(self, item):
        if item == 'score':
            return 99
        if item == 'age':
            return lambda : 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % item)
s5 = Student5()
print(s5.name)
print(s5.score)
print(s5.age())

class Chain(object):
    def __init__(self, path=''):
        self._path = path
    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))
    def __call__(self, name=''):
        return Chain('%s/%s' % (self._path, name))
    def __str__(self):
        return self._path
print(Chain().status.user.timeline.list)#'/status/user/timeline/list'
'这个方法写接口不错'

print(Chain().users('duguzanzan').repos)

'__call__'
'一个对象实例可以有自己的属性和方法，当我们的调用实例方法是，我们使用instance.method()'
'任何类，只需要调用一个__call__()方法，就可以进行对实例进行调用'
class Student6(object):
    def __init__(self, name):
        self._name = name
    def __call__(self):
        print('My name is %s' % self._name)
s6 = Student6('DeRozan')
print(s6())

'能被调用的对象就是一个Callable对象'
print(callable(Student6))
print(callable(max))
print(callable([1, 2, 3]))
print(callable(Chain))
print(callable(None))
print(callable('str'))


'枚举Enum'
from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name, member in Month._member_map_.items():
    print(name, '=>', member, ',', member.value)

from enum import  Enum, unique

@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

day1 = Weekday.Mon
print(day1)
print(Weekday.Tue)
print(Weekday['Wed'])
print(Weekday.Thu.value)
print(day1 == Weekday.Fri)
print(Weekday(6))
# print(Weekday(7))#ValueError: 7 is not a valid Weekday

#Pratice
class Gender(Enum):
    Male = 0
    Female = 1
class Student7(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
bart = Student7('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')


'使用元类'
'动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的'

'type'

class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s' % name)
h = Hello()
print(h.hello())
print(type(Hello))
print(type(h))

def fn(self, name='world'):
    print('Hello, %s' % name)
#创建Hello1 class
Hello1 = type('Hello1', (object,), dict(hello1 = fn))

h1 = Hello1()
print(h1.hello1())
print(type(Hello1))
print(type(h1))

'要创建一个class对象，type()函数依次传入3个参数：'
'class的名称；'
'继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；'
'class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。'


'metaclass'#元类

class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)
class MyList(list, metaclass=ListMetaclass):
    pass

L = MyList()
L.add(1)
print(L)

'ORM,Object Relational Mapping, 对象-关系映射'

'定义Field类，负责保存数据库表的字段名和字段类型'
class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type
    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__,self.name)

'在Field的基础上，定义各种类型的Field,like StringField, IntegerField'
class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100')

class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')

'最复杂部分ModelMetaclass'
class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return  type.__new__(cls, name, bases, attrs)
        print('Found Model; %s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings #保存属性和列的映射关系
        attrs['__table__'] = name #假设表名和类名一致
        return  type.__new__(cls, name, bases, attrs)

'基类'
class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'model' object has attribute '%s'" % key)
    def __setattr__(self, key, value):
        self[key] = value
    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.mappings.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr((self, k, None)))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))


class User(Model):
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

u = User(id = 12345, name = 'DeRozan', email = 'test@orm.org', password = 'my-pwd')
u.save()









