#!/usr/bin/env python3
# -*- conding: utf-8 -*-

__author__ = 'DeRozan'

from multiprocessing.managers import BaseManager
import time,sys,queue

#创建类似QueueManager
class QueueManager(BaseManager):
    pass

#由于这个QueueManager只能从网络上获取Queue，所以注册时只提供名字
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

#链接服务器,运行task_master的机器
server_addr = '127.0.0.1'
print('Connect to server %s...' % server_addr)

#端口和验证注意保持与task_master设置的完全一致
manager = QueueManager(address=(server_addr,5000),authkey=b'abc')

#从网络连接
manager.connect()

#获取Queue的对象
task = manager.get_task_queue()
result = manager.get_result_queue()

#从task队里取任务，并把结果写入result队列
for i in range(10):
    try:
        n = task.get(timeout=1)
        print('run task %d * %d...' % (n, n))
        r = '%d * %d = %d' % (n,n,n*n)
        time.sleep(1)
        result.put(r)
    except queue.Queue.Empty:
        print('task queue is empty.')

#处理结束
print('worker exit.')














