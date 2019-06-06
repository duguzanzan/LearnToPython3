#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-06-06 13:47
# @Author  : zan
# @File    : Lesson25_wsgi_hello.py

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]