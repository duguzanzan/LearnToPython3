#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-06-03 17:33
# @Author  : zan
# @File    : Lesson21.py
# @Title   : 图形界面

from tkinter import *
import tkinter.messagebox as messagebox


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        # self.helloLabel = Label(self, text='Hello, world!')
        # self.helloLabel.pack()
        self.nameInput = Entry(self)
        self.nameInput.pack()
        # self.quitButton = Button(self, text='Quit', command=self.quit)
        # self.quitButton.pack()
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message', 'Hello, %s' % name)

# app = Application()
# app.master.title('Hello World')
# app.mainloop()

# 导入turtle包的所有内容:
from turtle import *

'画个方块'
'''
#设置笔的宽度
width(4)

forward(100)
right(90)

pencolor('green')
forward(100)
right(90)

pencolor('red')
forward(100)
right(90)

pencolor('blue')
forward(100)
right(90)


done()# 调用done()使得窗口等待被关闭，否则将立刻关闭窗口:
'''

'五角星'
'''
def drawStar(x, y):
    pu()
    goto(x, y)
    pd()
    seth(0)
    for i in range(5):
        fd(40)
        rt(144)

for x in range(0,250, 50):
    drawStar(x, 0)

done()
'''

'分叉树'
# 设置色彩模式是RGB:
colormode(255)

lt(90)

lv = 14
l = 120
s = 45

width(lv)

# 初始化RGB颜色:
r = 0
g = 0
b = 0
pencolor(r, g, b)

penup()
bk(l)
pendown()
fd(l)

def draw_tree(l, level):
    global r, g, b
    # save the current pen width
    w = width()

    # narrow the pen width
    width(w * 3.0 / 4.0)
    # set color:
    r = r + 1
    g = g + 2
    b = b + 3
    pencolor(r % 200, g % 200, b % 200)

    l = 3.0 / 4.0 * l

    lt(s)
    fd(l)

    if level < lv:
        draw_tree(l, level + 1)
    bk(l)
    rt(2 * s)
    fd(l)

    if level < lv:
        draw_tree(l, level + 1)
    bk(l)
    lt(s)

    # restore the previous pen width
    width(w)

speed("fastest")

draw_tree(l, 4)

done()

















