#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'DeRozan'

'多线程'

'一个进程至少有一个线程，进程包含线程'
'Python的线程是真正的Posix Thread,而不是模拟出来的线程'
'Python提供了两个模块：_thread和threading,_thread是低级模块，threading是高级模块，对_thread进行了封装'
import time,threading

#新线程执行的代码:
# def loop():
#     print('thread %s is running...' % threading.current_thread().name)
#     n = 0
#     while n < 5:
#         n +=1
#         print('thread %s>>>%s' % (threading.current_thread().name, n))
#         time.sleep(1)
#     print('thread %s ended.' % threading.current_thread().name)
#
# print('thread %s is running...' % threading.current_thread().name)
# t = threading.Thread(target=loop, name='LoopThread')
# t.start()
# t.join()
# print('thread %s ended.' % threading.current_thread().name)
'''
thread MainThread is running...
thread LoopThread is running...
thread LoopThread>>>1
thread LoopThread>>>2
thread LoopThread>>>3
thread LoopThread>>>4
thread LoopThread>>>5
thread LoopThread ended.
thread MainThread ended.
'''

'Lock'
'多线程和多进程的最大不同在于，' \
'多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响（深拷贝）,' \
'多线程中，所有变量都是又所有线程共享，任何一个变量都可以被任何一个线程修改'

# balance = 0 #银行余额（过于真实，扎心）
# lock = threading.Lock() #创建一个锁
#
# def change_it(n):
#     #先存后取，结果应该是0
#     global balance
#     balance = balance + n
#     balance = balance - n
#
# def run_thread(n):
#     for i in range(100000000):
#         lock.acquire() #先获取锁
#         try:
#             change_it(n)
#         finally:
#             lock.release() #释放锁
#
# t1 = threading.Thread(target=run_thread, args=(5,))
# t2 = threading.Thread(target=run_thread, args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance)
'''
结果可能不为0
修改balance需要多条语句，而执行这几条语句时，线程可能中断，从而导致多个线程把同一个对象的内容改乱了
当多个线程同时执行lock.acquire()时，只有一个线程能成功获取锁，然后继续执行代码，其他线程就继续等待直到获得锁为止
获取锁不释放锁，就会形成死线程，所以用try...finally来确保一定会释放锁
'''

'多核CPU'
'GIL锁：Global Interpreter Lock'
'任何Python线程执行前，必须先获得GIL锁，然后每执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行'
'多线程在Python中只能交替执行，即使100个线程泡在100核的CPU上，也只能用到1核'

'要真正利用多核，除非重写一个GIL的解释器,或者用C、C++或Java扩展实现，但是就失去了Python简单易用的特点'
'也可通过多进程实现多核任务，每个进程都有自己的GIL锁'



'ThreadLocal'

#创建全局ThreadLocal对象
# local_school = threading.local() #loacl是一个dict
#
# def process_student():
#     #获取当前线程关联的student
#     std = local_school.student
#     print('Hello, %s(in %s)' % (std, threading.current_thread().name))
#
# def process_thread(name):
#     #绑定ThreadLocal的student
#     local_school.student = name
#     process_student()
#
# t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
# t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
# t1.start()
# t2.start()
# t1.join()
# t2.join()
'''
Hello, Alice(in Thread-A)
Hello, Bob(in Thread-B)
'''

'ThreadLocal变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰.' \
'ThreadLocal解决了参数在一个线程中各个函数之间传递的问题'


'进程 VS 线程'

'多进程优点'
'稳定性高,子进程崩溃，不影响主进程和其他子进程'

'多进程缺点'
'创建进程的代价大，在Unix/Linux系统下，有fork调用还行。' \
'操作系统同事运行的进程数也是有限的，在内存和CPU的限制下，几千个进程同事运行，操作系统连调度都是问题'

'多线程优点'
'通常情况下比多进程快一点儿，但是也快不到哪儿去'

'多线程缺点'
'任何一条线程挂掉，可能导致整个进程崩溃，因为所有线程共享进程的内存。所以稳定性不如多进程'


'线程切换'
'如果几千个任务同时进行，操作系统可能就主要忙着切换任务，根本没有时间去执行任务了' \
'这种情况最常见的就是硬盘狂响，点击窗口无反应，系统处于假死状态'


'计算密集型 VS IO密集型'

'计算密集型任务的特点就是进行大量计算,消耗CPU资源，任务越多，CPU切换任务时间增多，任务效率越低。' \
'代码效率至关重要，Python这样的脚本语言运行效率很低，不适合计算密集型，用C最好'

'涉及网络、磁盘IO的任务都是IO密集型，CPU消耗少，速度极快的C不如开发效率更高的Python'


'异步IO'



























