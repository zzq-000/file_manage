import tkinter.messagebox


import tkinter.messagebox

import mainwindow
from mainwindow import *


class base():
    def __init__(self, master):
        self.root = master
        self.root.title('主菜单')
        self.root.geometry('1000x500+400+200')
    #    login(self.root)
        mainwindow(self.root)


class login():
    username = 'admin'
    serect = '123'

    def log_in(self):
        if self.usr.get() == self.username and self.ser.get() == self.serect:
            self.initface.destroy()
            tkinter.messagebox.showinfo('欢迎', '登录成功')
            mainwindow(self.root)
        else:
            tkinter.messagebox.showinfo('警告', '用户名或密码错误')

    def __init__(self, master):
        self.root = master
        self.root.title('Login')
        self.initface = Frame(self.root, )
        self.initface.grid()

        Lb1 = Label(self.initface, text='用户名', width=3, height=3, fg='black', font=('黑体', 10))
        Lb1.grid(row=4, column=2, ipadx=30, ipady=5)
        self.usr = Entry(self.initface)
        self.usr.grid(row=4, column=3, padx=10, pady=10)
        Lb2 = Label(self.initface, text='密码', width=3, height=3, fg='black', font=('黑体', 10))
        Lb2.grid(row=5, column=2, ipadx=30, ipady=5)
        self.ser = Entry(self.initface, show='*')
        self.ser.grid(row=5, column=3, padx=10, pady=10)

        btnlogin = Button(self.initface, text='登录', fg='black', font=('黑体', 9), command=self.log_in)
        btnfog = Button(self.initface, text='忘记密码?', fg='black', font=('黑体', 9))
        btnlogin.grid(row=6, column=3, sticky=W, ipadx=10)
        btnfog.grid(row=6, column=3, sticky=E)