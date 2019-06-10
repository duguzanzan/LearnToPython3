#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-06-10 10:37
# @Author  : zan
# @File    : Lesson26.py
# @Title   : 协程


'在generator中，我们不但可以用过for循环来迭代，还可以不断调用next()函数获取有yield语句返回的下一个值'

'python的yeild不但可以返回一个值，也可以接受调用者发出的参数'

def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER]Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n += 1
        print('[PRODUCER]Producing %s' % n)
        r = c.send(n)
        print('[PRODUCER]Consumer return %s' % r)
    c.close()

c = consumer()
produce(c)

'''
1.首先调用c.send(None)启动生成器
2.然后通过c.send(n)切换到consumer执行
3.consumer通过yield拿到传值，处理，又通过yield将结果返回
4.produce拿到consumer处理的结果，继续生产
5.produce决定不生产了，通过c.close()关不consumer
整个流程无锁，又一个线程执行，称为‘协程’
'''











