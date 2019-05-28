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
from collections import ChainMap
import os, argparse

#构造缺省参数
defaults = {
    'color':'red',
    'user':'guest'
}

#构造命令行参数
parser = argparse.ArgumentParser()
parser.add_argument('-u','--user')
parser.add_argument('-c','--color')
namespace = parser.parse_args()
command_line_args = {k:v for k, v in vars(namespace).items() if v}

#组合成ChainMap:
combined = ChainMap(command_line_args,os.environ, defaults)

print('line111,color=%s' % combined['color'])
print('line112,user=%s' % combined['user'])

'当传入命令行参数时，优先使用命令行参数：'
'''
$ python3 Lesson14.py -u bob
color=red
user=bob
'''

'同时传入命令行参数和环境变量，命令行参数的优先级较高：'
'''
$ user=admin color=green python3 use_chainmap.py -u bob
color=green
user=bob
'''


'Counter'
'简单的计数器，统计字符出现个数'
from collections import  Counter

c = Counter()
# for ch in 'programming':
#     c[ch] = c[ch] + 1
c.update('programming')

print('line138:', c)
print('line139:',Counter('PROGRAMMING'))




















