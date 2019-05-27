#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-05-27 17:02
# @Author  : zan
# @File    : Lesson14.py
# @Title   : collections

'集合'

'namedtuple'
from collections import namedtuple

Point = namedtuple('Point',['x','y'])
p = Point(1,2)
print('line15:',p.x)
print('line16:',p.y)

'namedtuple是一个函数，它用来创建一个自定义的tuple对象'
print('line19:',isinstance(p,Point))
print('line20:',isinstance(p,tuple))

Circle = namedtuple('Circle',['x','y','r'])


'deque'
from collections import deque

q = deque(['a', 'b', 'c'])
q.append('d')
q.appendleft('m')
print('line31:',q)
'deque除了实现list的append()和pop（)外，还支持appendleft()和popleft()'

'defaultdict'
'如果key不存在，defalutdict会返回一个默认值'
from collections import defaultdict

dd = defaultdict(lambda:'N/A')
dd['key1'] = 'abc'
print('line40:',dd['key1'])
print('line41:',dd['key2'])#key2不存在，返回默认值


'OrderedDict'
'可以保持key的顺序'
from collections import OrderedDict
d = dict([('a',1),('b',2),('c',3)])
print('line48:',d)
d['z'] = 1
d['y'] = 2
d['x'] = 3
print('line52:',d.keys())

od = OrderedDict([('a',1),('b',2),('c',3)])
print('line52:',od)
od['z'] = 1
od['y'] = 2
od['x'] = 3
print('line59:',od.keys())

'OrderedDict可以实现一个FIFO(先进先出)的dict'

class LastUpdatedOrderedDict(OrderedDict):
    def __init__(self,capacity):
        super(LastUpdatedOrderedDict,self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove',last)
        if containsKey:
            del self[key]
            print('set:',[key, value])
        else:
            print('add:',[key,value])
        OrderedDict.__setitem__(self, key, value)

luod = LastUpdatedOrderedDict(3)
luod['z'] = 1
luod['y'] = 2
luod['x'] = 3
print('line84:',luod)
luod['x'] = 'x'
print('line86:',luod)
luod['a'] = 'a'
print('line88:',luod)


'ChainMap'




















