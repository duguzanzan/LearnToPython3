#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-05-30 10:54
# @Author  : zan
# @File    : Lesson18.py
# @Title   : XML & HTML

'XML'

'DOM VS SAX'
'DOM把整个XML读入内存，解析为数，因此内存大，解析慢，但可任意遍历数的节点'
'SAX是流模式，边读边解析，占用内存小，解析快，但需要自己处理事件'

'Python中使用SAX，非常简洁'
'事件：start_element,end_element,char_data'

from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

    def end_element(self, name):
        print('sax:end_element: %s' % name)

    def char_data(self, text):
        print('sax:char_data: %s' % text)

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)


'HTMLParser'

from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    def handle_data(self, data):
        print(data)

    def handle_comment(self, data):
        print('<!--', data, '-->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)

parser = MyHTMLParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')

'feed()方法可以多次调用'

#Practice
from html.parser import HTMLParser
# from html.entities import name2codepoint
from urllib import request
import re

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super(MyHTMLParser,self).__init__()
        self.__parsedata='' # 设置一个空的标志位

    def handle_starttag(self, tag, attrs):
        if ('class', 'event-title') in attrs:
            self.__parsedata = 'name'  # 通过属性判断如果该标签是我们要找的标签，设置标志位
        if tag == 'time':
            self.__parsedata = 'time'
        if ('class', 'say-no-more') in attrs:
            self.__parsedata = 'year'
        if ('class', 'event-location') in attrs:
            self.__parsedata = 'location'

    def handle_endtag(self, tag):
        self.__parsedata = ''# 在HTML 标签结束时，把标志位清空

    def handle_data(self, data):
        if self.__parsedata == 'name':
            print('会议名称:%s' % data) # 通过标志位判断，输出打印标签内容

        if self.__parsedata == 'time':
            print('会议时间:%s' % data)

        if self.__parsedata == 'year':
            if re.match(r'\s\d{4}', data): # 因为后面还有两组 say-no-more 后面的data却不是年份信息,所以用正则检测一下
                print('会议年份:%s' % data.strip())

        if self.__parsedata == 'location':
            print('会议地点:%s' % data)
            print('----------------------------------')

parser = MyHTMLParser()

URL = 'https://www.python.org/events/python-events/'

with request.urlopen(URL, timeout=15) as f:  # 打开网页并取到数据
    data = f.read()
parser.feed(data.decode('utf-8'))





