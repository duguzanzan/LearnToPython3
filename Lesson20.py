#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-05-31 17:50
# @Author  : zan
# @File    : Lesson20.py
# @Title   : 常用的三方模块

'requests'

import requests

# r = requests.get('https://www.douban.com/')
# print(r.status_code)
# print(r.text)

# r = requests.get('http://canal.stockstar.com/Base/V_BS_STK_STAR_GUIDENCE/full=2&sort=DECLAREDATE%20desc&encoding=utf8&limit=20')
# print('line17:', r.url)
# print('line18:', r.encoding)
# print('line19:', r.content)
# print('line20:', r.json())
#
# r = requests.post('https://api.szzy888.com/api/user/login', data={'username': '18337151126', 'password': 'abc123', 'source': '2', 'clientip': '127.0.0.1'})
# print('line23:', r.json())


'chardet'
import chardet

print('line29:', chardet.detect(b'Hello, world!'))

data = '大碗宽面，鸡你太美，雨女无瓜'.encode('gbk')
print('line32', chardet.detect(data))

data = '最怕空气突然安静，最怕朋友突然的关心'.encode('utf-8')
print('line35:', chardet.detect(data))

data = '最新の主要ニュース'.encode('euc-jp')
print('line38:', chardet.detect(data))


'psutil'
'process and system utilities'

import psutil

print('line46:CPU逻辑数量', psutil.cpu_count())
print('line47:CPU物理数量', psutil.cpu_count(False))
'2说明是双核超线程, 4则是4核非超线程'

'统计CPU的用户／系统／空闲时间：'
print('line51:', psutil.cpu_times())

'CPU的使用率'
# for x in range(10):
#     print(psutil.cpu_times_percent(interval=1,percpu=True))

'获取物理内存信息'
print('line58:', psutil.virtual_memory())

'获取交换内存信息'
print('line61:', psutil.swap_memory())

'获取磁盘信息'
print('line64:', psutil.disk_partitions())

'获取磁盘使用情况'
print('line67:', psutil.disk_usage('/'))

'获取磁盘IO'
print('line70:', psutil.disk_io_counters())


'获取网络信息'
print('line74:', psutil.net_io_counters()) # 获取网络读写字节／包的个数

print('line76:', psutil.net_if_addrs())# 获取网络接口信息

print('line78:', psutil.net_if_stats())# 获取网络接口状态

# print('line80:', psutil.net_connections()) # 获取网络连接状态


'获取进程信息'
print('line84:', psutil.pids())# 所有进程ID

p = psutil.Process(7060)# 获取指定进程ID=3776，其实就是当前Python交互环境
print('line87:', p.name())# 进程名称
print('line88:', p.exe())# 进程exe路径
print('line89:', p.cwd()) # 进程工作目录
print('line90:', p.cmdline())# 进程启动的命令行
print('line91:', p.ppid())# 父进程ID
print('line92:', p.parent())# 父进程
print('line93:', p.children())# 子进程列表
print('line94:', p.status())# 进程状态
print('line95:', p.username())# 进程用户名
print('line96:', p.create_time())# 进程创建时间
print('line97:', p.terminal())# 进程终端
print('line98:', p.cpu_times)# 进程使用CPU时间
print('line99:', p.memory_info())# 进程使用的内存
print('line100:', p.open_files())# 进程打开的文件
print('line101:', p.connections())# 进程相关网络连接
print('line102:', p.num_threads())# 进程的线程数量
print('line103:', p.threads())# 所有的线程信息
print('line104:', p.environ())# 进程环境变量
# print('line105:', p.terminal())# 结束进程










