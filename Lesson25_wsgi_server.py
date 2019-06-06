#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-06-06 13:51
# @Author  : zan
# @File    : Lesson25_wsgi_server.py

from wsgiref.simple_server import make_server

from Lesson25_wsgi_hello import application

http = make_server('', 8000, application)

print('Sering HTTP on port 8000...')

http.serve_forever()