#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
function 1:
try:
    f = open('/Users/zan/Developer/Python/test.txt', 'r')
    print(f.read())
finally:
    if f:
        f.close()
'''

'''
function 2:
with open('/Users/zan/Developer/Python/test.txt', 'r') as f:
    print(f.read())
'''

'''
read()会一次性读取文件的全部内容
read(size)方法，每次最多读取size个字节的内容
readline()可以每次读取一行内容
readlines()一次读取所有内容并按行返回list
***如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便
for line in f.readlines():
    print(line.strip()) # 把末尾的'\n'删掉
'''

'file-like Object'
'像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object.'
'StringIO 就是在内存中创建的file-like Object，用作临时缓存'


'二进制文件'
'要读取二进制文件，比如图片、视频等等，用‘rb’模式打开文件'

'''
>>> f = open('/Users/zan/Developer/Python/test.png', 'rb')
>>> print(f.read())
b'\x89PNG\r\n\x1a\n\x00\x00\x00\r...' #十六进制表示的字节
'''


'字符编码'
'''
>>> f = open('/Users/zan/Developer/Python/test.txt', encoding='gbk',errors='ignore') #errors可以设置忽略文本编码错误
>>> print(f.read())
'''

'写文件'
" 'w'或者'wb'表示写文本文件或写二进制文件: "
'''
>>> f = open('/Users/zan/Developer/Python/test.txt', 'w')
>>> f.write('Hello, DeRozan')
>>> f.close()
'''
'你可以反复调用write()来写入文件，但是务必要调用f.close()来关闭文件。' \
'当我们写文件时，操作系统往往不会立刻把数据写入磁盘，而是放到内存缓存起来，空闲的时候再慢慢写入。' \
'只有调用close()方法时，操作系统才保证把没有写入的数据全部写入磁盘。' \
'忘记调用close()的后果是数据可能只写了一部分到磁盘，剩下的丢失了。所以，还是用with语句来得保险'
with open('/Users/zan/Developer/Python/test.txt', 'a') as f:
    f.write('Hello,world!\n')
'以\'w\'模式写入文件时，如果文件已存在，会直接覆盖（相当于删掉后新写入一个文件）。' \
    '如果我们希望追加到文件末尾怎么办？可以传入\'a\'以追加（append）模式写入。'

#Practice
'''
fpath = r'/Users/zan/Developer/Python/h5text1.html'
with open(fpath, 'r') as f:
    s = f.read()
    print(s)
'''


'StringIO'
'内存中读写str'
'''
>>> from io import StringIO
>>> f = StringIO()
>>> f.write('hello')
5
>>> f.write(' ')
1
>>> f.write('liuzan')
6
>>> print(f.getvalue())
hello liuzan
'''

'''
>>> p = StringIO('Hi\nHello\nGoodbye')
>>> while True:
...    s = p.readline()
...    if s == '':
...        break
...    print(s.strip())
    
Hi
Hello
Goodbye
'''

'BytesIO'
'StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO'

'''
>>> from io import BytesIO
>>> b = BytesIO()
>>> b.write('中文'.encode('utf-8'))
6
>>> print(b.getvalue())
b'\xe4\xb8\xad\xe6\x96\x87'
'''

'和StringIO类似，可以用一个bytes初始化BytesIO，然后，像读文件一样读取'
'''
>>> r = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
>>> r.read()
b'\xe4\xb8\xad\xe6\x96\x87's
'''


'操作文件和目录'

'''
>>>import os
>>>os.name  # 操作系统类型
'posix' #如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统

'要获取详细的系统信息，可以调用uname()函数：'
>>> os.uname()
posix.uname_result(sysname='Darwin', nodename='192.168.0.103', release='18.5.0', version='Darwin Kernel Version 18.5.0: Mon Mar 11 20:40:32 PDT 2019; root:xnu-4903.251.3~3/RELEASE_X86_64', machine='x86_64')

'********** 注意uname()函数在Windows上不提供，也就是说，os模块的某些函数是跟操作系统相关的。**********'
'''

'环境变量'
'''
'在操作系统中定义的环境变量，全部保存在os.environ这个变量中'
>>> os.environ
environ({'PATH': '/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin', 'PYDEVD_LOAD_VALUES_ASYNC': 'True', 'LOGNAME': 'zan', 'PYCHARM_MATPLOTLIB_INDEX': '0', 'XPC_SERVICE_NAME': 'com.jetbrains.pycharm.32312', 'PWD': '/Users/zan/Developer/Python', 'PYCHARM_HOSTED': '1', 'PYCHARM_DISPLAY_PORT': '64877', 'PYCHARM_MATPLOTLIB_INTERACTIVE': 'true', 'PYTHONPATH': '/Applications/PyCharm.app/Contents/helpers/pycharm_matplotlib_backend:/Applications/PyCharm.app/Contents/helpers/pycharm_display:/Applications/PyCharm.app/Contents/helpers/third_party/thriftpy:/Applications/PyCharm.app/Contents/helpers/pydev', 'SHELL': '/bin/zsh', 'PAGER': 'less', 'LSCOLORS': 'Gxfxcxdxbxegedabagacad', 'PYTHONIOENCODING': 'UTF-8', 'OLDPWD': '/Applications/PyCharm.app/Contents/bin', 'USER': 'zan', 'ZSH': '/Users/zan/.oh-my-zsh', 'IPYTHONENABLE': 'True', 'TMPDIR': '/var/folders/_b/_8n97t6x6p5g04s52wdbx2v40000gn/T/', 'SSH_AUTH_SOCK': '/private/tmp/com.apple.launchd.GRF5pkflLi/Listeners', 'XPC_FLAGS': '0x0', 'PYTHONUNBUFFERED': '1', '__CF_USER_TEXT_ENCODING': '0x1F5:0x19:0x34', 'Apple_PubSub_Socket_Render': '/private/tmp/com.apple.launchd.eKG4SmI7uS/Render', 'LESS': '-R', 'LC_CTYPE': 'zh_CN.UTF-8', 'HOME': '/Users/zan', '__PYVENV_LAUNCHER__': '/usr/local/bin/python3.7'})

>>> os.environ['PATH']
'/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin'

>>> os.environ.get('x', 'default')
'default'
'''


'操作文件和目录'

'''
# 查看当前目录的绝对路径:
>>> os.path.abspath('.')
'/Users/zan/Developer/Python'

# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
>>> os.path.join('/Users/zan/Developer/Python', 'testdir')
'/Users/zan/Developer/Python/testdir'

# 然后创建一个目录:
>>> os.mkdir('/Users/zan/Developer/Python/testdir')

# 然后删除一个目录:
>>> os.rmdir('/Users/zan/Developer/Python/testdir')

# 把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名:
>>> os.path.split('/Users/zan/Developer/Python/test.txt')
('/Users/zan/Developer/Python', 'test.txt')

#得到文件扩展名
>>> os.path.splitext('/Users/zan/Developer/Python/test.txt')
('/Users/zan/Developer/Python/test', '.txt')

# 对文件重命名:
>>> os.rename('test.txt', 'test.py')

# 删掉文件:
>>> os.remove('test.py')
'''

'''
# 列出当前目录下的所有目录:
>>> [x for x in os.listdir('.') if os.path.isdir(x)]
['__pycache__', '.git', '.idea']

# 列出所有的.py文件:
>>> [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
['Lesson9.py', 'Lesson8.py', 'Lesson3.py', 'Lesson7.py', 'Lesson6.py', 'Lesson2.py', 'Lesson5.py', 'Lesson1.py', 'Lesson4.py']

'''

#Practice
'利用os模块编写一个能实现dir -l输出的程序'
'''
import os,time

def time_format(x):
    return time.asctime(time.localtime(x))

def cmd_dir():
    path = os.path.abspath('.')
    dir_and_file = [x for x in os.listdir('.')]
    gettime = list(map(time_format,map(os.path.getatime,dir_and_file)))
    getsize = list(map(os.path.getsize,dir_and_file))
    n = 0
    while n < len(dir_and_file):
        print(gettime[n], '==>', getsize[n], '==>', dir_and_file[n])
        n += 1

def findstr(path,st):
    for x in os.listdir(path):
        if os.path.isdir(x):
            new_path = os.path.join(path,x)
            findstr(new_path,st)
        elif st in os.path.splitext(x)[0]:
            print("相关文件名:%s,相对路径:%s" % (x,os.path.relpath(path)))


if __name__ == '__main__':
    f = os.path.abspath('.')
    text = input("input:")
    findstr(f,text)

'''

'序列化'
'pickle模块实现序列化'

'''
>>> import pickle
>>> d = dict(name = 'Bob', age = 26, score = 90)
>>> pickle.dumps(d) #pickle.dumps()把任意对象序列化成一个bytes
    b'\x80\x03}q\x00(X\x04\x00\x00\x00nameq\x01X\x03\x00\x00\x00Bobq\x02X\x03\x00\x00\x00ageq\x03K\x1aX\x05\x00\x00\x00scoreq\x04KZu.'
>>> f = open('dump.txt', 'wb')
>>> pickle.dump(d, f) #pickle.dump()直接把对象序列化后写入一个file-like Object
>>> f.close()
>>> f = open('dump.txt', 'rb')
>>> d = pickle.load(f) #pickle.load()从一个file-like Object中直接反序列化出对象
>>> f.close()
>>> d
    {'name': 'Bob', 'age': 26, 'score': 90}
'''


'JSON'

'''
>>> import json
>>> json.dumps(d) #dumps()返回一个str,dump()把json写入一个file-like Object
'{"name": "Bob", "age": 26, "score": 90}'
'''

import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
    def student2dict(self):
        return {
            'name':self.name,
            'age':self.age,
            'score':self.score
        }

def Student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

s = Student('Bob',26,90)
print(json.dumps(s.student2dict()))
print(json.dumps(s, default=Student2dict))
print(json.dumps(s, default=lambda obj: obj.__dict__))
'因为通常class的实例都有一个__dict__属性，他就是一个dict'
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])
jsonStr = json.dumps(s, default=Student2dict)
print(json.loads(jsonStr, object_hook=dict2student))


#Practice
obj = dict(name = '小明', age = 20)
print(json.dumps(obj, ensure_ascii=True)) #汉字转为unicode编码


















