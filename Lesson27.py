#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-06-10 11:03
# @Author  : zan
# @File    : Lesson27.py
# @Title   : asyncio/async/await

'asyncio是Python3.4引入的标准库'
'asyncio的编程模式就是一个消息循环，从模块中获取一个EventLoop的引用，然后把需要执行的协程扔进EvenLoop中执行，就实现了异步IO'

'''
import asyncio

@asyncio.coroutine#把一个generator标记为coroutine类型,就可以扔到EventLoop中执行
def hello():
    print('Hello,world!')
    #异步调用asyncio.sleep(1)
    r = yield from asyncio.sleep(1)#yield from语法可以让我们方便的调用另一个generator
    print('Hello again!')

# 获取Eventloop
loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(hello())
loop.close()
'''

'''
asyncio.sleep()也是一个coroutine,所以线程不会等待asyncio.sleep(),而是直接中断并执行下一个消息循环
当asyncio.sleep()返回时，线程就可以从yield from拿到返回值，然后接着执行下一个语句
把asyncio.sleep(1)看成一个耗时1秒的IO操作，在此期间，主线程并未等待，而是去执行EventLoop中其他可以执行的coroutine
'''


'''
import threading
import asyncio

@asyncio.coroutine
def hello():
    print('Hello world!(%s)' % threading.current_thread())
    yield from asyncio.sleep(1)
    print('Hello again!(%s)' % threading.current_thread())

loop = asyncio.get_event_loop()
tasks = [hello(),hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
'''

'''
Hello world!(<_MainThread(MainThread, started 4484511168)>)
Hello world!(<_MainThread(MainThread, started 4484511168)>)
Hello again!(<_MainThread(MainThread, started 4484511168)>)
Hello again!(<_MainThread(MainThread, started 4484511168)>)
多个coroutine可以由一个线程并发执行
'''

'异步网络连接'
'''
import asyncio

@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    writer.close()

loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
'''

'为了简化并更好的标识异步IO，从Python3.5开始引入新的语法，async和await'
'1.把@asyncio.coroutine 替换成 async'
'2.把yield from 替换成 await'

# import asyncio
#
# async def hello():
#     print('Hello,world!')
#     r = await asyncio.sleep(1)
#     print('Hello again!')
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(hello())
# loop.close()

import asyncio

async def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = await connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    await writer.drain()
    while True:
        line = await reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    writer.close()

loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()


















