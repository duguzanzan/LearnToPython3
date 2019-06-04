#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-06-04 16:34
# @Author  : zan
# @File    : Lesson22_socket_client.py

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('127.0.0.1', 9999))

print(s.recv(1024).decode('utf-8'))

for data in [b'Michael', b'Tracy', b'Sarah', b'Adam']:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))

s.send(b'exit')
s.close()


'UDP'
'''
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据:
    s.sendto(data, ('127.0.0.1', 9999))
    # 接收数据:
    print(s.recv(1024).decode('utf-8'))
s.close()
'''




