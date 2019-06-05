#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-06-05 14:57
# @Author  : zan
# @File    : Lesson24.py
# @Title   : SQL

'''
import sqlite3

connect = sqlite3.connect('test.db')

cursor = connect.cursor()

# cursor.execute('create table user(id varchar(20)primary key, name varchar(20))')

cursor.execute("insert into user (id, name) values ('2', 'Adam')")

cursor.close()

connect.commit()

connect.close()
'''

#Practice

'''
import os, sqlite3

db_file = os.path.join(os.path.dirname(__file__), 'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)

connect = sqlite3.connect(db_file)
cursor = connect.cursor()
cursor.execute('create table user(id varchar(20)primary key ,name varchar (20), score int)')
cursor.execute(r"insert into user values('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values('A-003', 'Lisa', 78)")
cursor.close()
connect.commit()
connect.close()

def get_score_in(low, high):
    connect = sqlite3.connect(db_file)
    cursor = connect.cursor()
    values = cursor.execute(r'select name from user where score > ? and score <= ? order by score', (low, high)).fetchall()
    cursor.close()
    connect.commit()
    connect.close()
    l = list(name[0] for name in values)
    print(values)
    return list(l)

assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)

print('Pass')

'''

'mysql'
'''
# 导入MySQL驱动:
>>> import mysql.connector
# 注意把password设为你的root口令:
>>> conn = mysql.connector.connect(user='root', password='password', database='test')
>>> cursor = conn.cursor()
# 创建user表:
>>> cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 插入一行记录，注意MySQL的占位符是%s:
>>> cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
>>> cursor.rowcount
1
# 提交事务:
>>> conn.commit()# 执行完sql之后要提交事务
>>> cursor.close()
# 运行查询:
>>> cursor = conn.cursor()
>>> cursor.execute('select * from user where id = %s', ('1',))#占位符使用%s
>>> values = cursor.fetchall()
>>> values
[('1', 'Michael')]
# 关闭Cursor和Connection:
>>> cursor.close()
True
>>> conn.close()
'''












