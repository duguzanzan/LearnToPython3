#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-05-29 16:36
# @Author  : zan
# @File    : Lesson17.py

'contextlib'

'''
with open(Users/zan/Developer/Python/test.txt,'r') as f:
    f.read()
'''
'任何对象，只要正确实现上下文管理，就可以使用with语句'

'实现上下文管理是通过_enter_ & _exit_ 这两个方法'
class Query(object):
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('Begin')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print('Error')
        else:
            print('End')

    def query(self):
        print('Query info about %s...' % self.name)

with Query('DeRozan') as q:
    q.query()


'contextmanger'
from contextlib import contextmanager
class Query(object):
    def __init__(self,name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)

@contextmanager
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q
    print('End')

with create_query('Bob') as q:
    q.query()

@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)

with tag('h1'):
    print('hello')
    print('word')

'代码执行顺序'
'1.with语句首先执行yield之前的语句，因此打印<h1>;' \
'2.yield调用会执行with语句内部所有语句，因此打印hello和world；' \
'3.最后执行yield之后的语句，因此打印</h1>'


'closing'
'如果对象没有实现上下文，可以用closing()来吧对象编程上下文对象'
from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('http://www.python.org')) as page:
    for line in page:
        print(line)

'''
closing也是一个经过@contextmanager装饰的generator，这个generator编写起来其实非常简单：
@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()
'''
