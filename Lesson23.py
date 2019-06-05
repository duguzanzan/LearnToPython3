#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-06-05 10:13
# @Author  : zan
# @File    : Lesson23.py

"Didn't finish this"

'Send email'
'''
from email.mime.text import MIMEText

msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')

from_addr = input('From:')
password = input('Password:')

to_addr = input('To:')

smtp_host = input('SMTP host:')

smtp_port = input('SMTP port:')

import smtplib

server = smtplib.SMTP(smtp_host, smtp_port)
server.set_debuglevel(debuglevel=1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
'''

'Get email'
import imaplib

email = input('Email:')
password = input('Password:')

imap_host = input('IMAP host:')
imap_port = input('IMAP port:')

server = imaplib.IMAP4_SSL(host=imap_host, port=imap_port)
server.login(email, password)
typ, dat, name = server.list()
print(dat)
server.close()





