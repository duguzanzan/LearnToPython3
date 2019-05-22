#!/usr/bin/env python3
# -*- conding: utf-8 -*-

__author__ = 'DeRozan'

'*****************线程与进程******************'

'多线程'
'Unix/Linux操作系统提供了一个fork()系统调用,非常特殊，此函数调用一次返回两次，父进程和子进程个返回一次'
'子进程永远返回0，父进程返回子进程的ID。子进程可以使用getppid()拿到父进程ID'

'''
import os
print('Process(%s)start...' % (os.getpid()))
# Only works on Unix/Linux/Mac
pid = os.fork()
if pid == 0:
    print('I am child process(%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I(%s) just created a child process(%s).' % (os.getpid(), pid))
'''



'multiprocessing'
'由于Python是跨平台的，自然也应该提供一个跨平台的多进程支持.'

'''
from multiprocessing import Process
import os

#子进程need to do
def run_proc(name):
    print('Run child process %s(%s)...' % (name, os.getpid()))

if __name__ == '__main__':
    print('Prarent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',)) #when create child process，only need pass in function name and parameters
    print('Child process will start.')
    p.start() #child process start
    p.join() #wait child process end and go to next
    print('Child process end.')
'''


'Pool'
'If must need a lot of child process, 可以使用进程池的方式批量创建子进程'
'''
from multiprocessing import Pool
import os,time,random

def long_time_task(name):
    print("Run task %s(%s)." % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print("Task %s run %0.2f seconds." % (name, (end - start)))

if __name__ == '__main__':
    print('Parent process %s' % os.getpid())
    p = Pool(9) #Pool的默认大小是CPU的核数，进程池内的子进程大于核数才能看到等待效果
    for i in range(10):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close() #调用close()之后就不能继续添加新的Process了
    p.join() #等待所有子进程执行完毕
    print('All subprocesses done.')
'''


'子进程'
'subprocess模块可以放我们非常方便的启动一个子进程，然后控制其输入和输出'
'''
import subprocess

>>> print('$ nslookup www.python.org')
>>> r = subprocess.call(['nslookup', 'www.python.org'])
>>> print('Exit code:', r)
$ nslookup www.python.org
Server:		192.168.1.253
Address:	192.168.1.253#53

Non-authoritative answer:
www.python.org	canonical name = dualstack.python.map.fastly.net.
Name:	dualstack.python.map.fastly.net
Address: 151.101.108.223

Exit code: 0
'''


'如果子进程需要输入，通过communicate()'
'''
>>> import subprocess

>>> print('$ nslookup')
>>> p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
>>> output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
>>> print(output.decode('utf-8'))
>>> print('Exit code:', p.returncode)
$ nslookup
Server:		192.168.1.253
Address:	192.168.1.253#53

Non-authoritative answer:
python.org	mail exchanger = 50 mail.python.org.

Authoritative answers can be found from:
mail.python.org	internet address = 188.166.95.178
mail.python.org	has AAAA address 2a03:b0c0:2:d0::71:1

Exit code: 0
'''

'进程间的通信'
'multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据'
from multiprocessing import Process, Queue
import os,time,random

#写数据进程执行的代码
def lz_write(q):
    print('Process to write:%s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

#读数据进程执行的代码
def lz_read(q):
    print('Process to read:%s' % os.getpid())
    while True:
        value = q.get()
        print('Get %s from queue.' % value)


if __name__ == '__main__':
    q = Queue()
    pw = Process(target=lz_write, args=(q,))
    pr = Process(target=lz_read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate() #pr进程里是死循环，无法等待其结束，只能强行终止























