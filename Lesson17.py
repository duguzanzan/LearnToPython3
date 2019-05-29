#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-05-29 16:36
# @Author  : zan
# @File    : Lesson17.py

'contextlib'

'''
with open(Users/zan/Developer/Python/test.txt,'r') as f:
    f.read()
'''
'任何对象，只要正确实现上下文管理，就可以使用with语句'

'实现上下文管理是通过_enter_ & _exit_ 这两个方法'
class Query(object):
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('Begin')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print('Error')
        else:
            print('End')

    def query(self):
        print('Query info about %s...' % self.name)

with Query('DeRozan') as q:
    q.query()


'contextmanger'
from contextlib import contextmanager
class Query(object):
    def __init__(self,name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)

@contextmanager
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q
    print('End')

with create_query('Bob') as q:
    q.query()

@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)

with tag('h1'):
    print('hello')
    print('word')

'代码执行顺序'
'1.with语句首先执行yield之前的语句，因此打印<h1>;' \
'2.yield调用会执行with语句内部所有语句，因此打印hello和world；' \
'3.最后执行yield之后的语句，因此打印</h1>'


'closing'
'如果对象没有实现上下文，可以用closing()来吧对象编程上下文对象'
from contextlib import closing
from urllib.request import urlopen

# with closing(urlopen('http://www.python.org')) as page:
#     for line in page:
#         print(line)

'''
closing也是一个经过@contextmanager装饰的generator，这个generator编写起来其实非常简单：
@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()
'''


'urllib'
'URL的功能'

'Get'
from urllib import request

with request.urlopen('http://itunes.apple.com/lookup?id=1151680849') as f:
    data = f.read()
    print('Status:',f.status,f.reason)
    for k, v in f.getheaders():
        print('%s:%s' % (k, v))
    print('Data:',data.decode('utf-8'))

'模拟iphone6去请求'
'''
req = request.Request('http://www.douban.com')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s:%s' % (k, v))
    print('Data:', f.read().decode('utf-8'))
'''

'Post'

from urllib import parse

'微博登录'
print('Login to weibo on...')
username = input('username:')
password = input('password:')
login_data = parse.urlencode([
    ('username', username),
    ('password', password),
    ('entry', 'mweibo'),
    ('client_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])

req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

with request.urlopen(req, data=login_data.encode('utf-8')) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))

#Practice
import json

def fetch_data(url):
    with request.urlopen(url) as f:
        print('Status:', f.status, f.reason)
        return json.loads(f.read().decode('utf-8'))

URL = 'https://api.szzy888.com/api/help/contact_list?clientip=127.0.0.1&source=2'
data = fetch_data(URL)
print(data)
assert data['data']['complain_tel'] == '021-60586264'
print('ok')















