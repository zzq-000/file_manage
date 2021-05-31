import random
import tkinter.messagebox
from tkinter import *
from tkinter import ttk
import login
import disk


class mainwindow():

    def reback(self):
        self.initface.destroy()
        login.login(self.root)

    def print(self):
        x = self.tree1.get_children()
        # self.num.
        lb = Label(self.initface, text=str(self.disk.left), fg='green')
        lb.grid(row=2, column=8, padx=5)
        for i in x:
            self.tree1.delete(i)
        for i in range(len(self.disk.empty)):
            self.disk.empty[i].id = i
            self.tree1.insert("", i, text=" ", values=(
                " " + str(self.disk.empty[i].id), " " + str(self.disk.empty[i].begin),
                " " + str(self.disk.empty[i].length)))
        self.tree1.pack(side=LEFT)

        x = self.tree2.get_children()
        for i in x:
            self.tree2.delete(i)
        for i in range(len(self.disk.FCB)):
            content = ''
            for j in self.disk.FCB[i].index:
                content += str(j) + " "
            self.tree2.insert("", i, text=" ", values=(
                " " + str(self.disk.FCB[i].id), " " + str(self.disk.FCB[i].size) + 'KB', " " + content))
        self.tree2.pack(side=RIGHT)

        return

    def allocate(self):
        id = str(self.e1.get())
        size = float(self.e2.get())
        flag = self.disk.allocate(id, size)
        if flag:
            tkinter.messagebox.showinfo('提示', '分配成功')
        else:
            tkinter.messagebox.showinfo('提示', '分配失败')
        self.print()

    def recycle(self):
        id = str(self.e3.get())
        flag = self.disk.recycle(id)
        if flag:
            tkinter.messagebox.showinfo('提示', '回收成功')
        else:
            tkinter.messagebox.showinfo('提示', '回收失败')
        self.print()

    def randombuild(self):
        num = int(self.e4.get())
        count = 0
        for i in range(num):
            size = random.randint(2, 10) + random.uniform(0, 1)
            size = float(format(size, '.1f'))
            if not self.disk.allocate(str(i + 1) + '.txt', size):
                tkinter.messagebox.showinfo("警告", "只生成" + str(count) + "个文件")
                return
            count += 1
        tkinter.messagebox.showinfo("提示", str(num) + "个随机文件已生成")
        self.print()
        return

    def specdelete(self):
        for i in self.disk.FCB:
            s=i.id
            name=s.split('.')[0]
            if int(name)%2==1:
                self.disk.recycle(s)
        tkinter.messagebox.showinfo("提示","删除成功")
        self.print()
        return

    def __init__(self, master):
        self.root = master
        self.root.title('管理')
        self.initface = Frame(self.root, )
        self.initface.pack()
        self.disk = disk.Disk()
        lb = Label(self.initface, text='创建文件:')
        lb.grid(row=2, column=1, padx=5)
        lb = Label(self.initface, text='文件名')
        lb.grid(row=1, column=2, padx=5)
        lb = Label(self.initface, text='大小')
        lb.grid(row=1, column=3, padx=5)
        self.e1 = Entry(self.initface, width=14)
        self.e1.grid(row=2, column=2, padx=5)
        self.e2 = Entry(self.initface, width=14)
        self.e2.grid(row=2, column=3, padx=5)
        btnsure = Button(self.initface, text='确认', fg='black', font=('黑体', 9), command=self.allocate)
        btnsure.grid(row=2, column=4, padx=5)

        lb = Label(self.initface, text='删除文件:')
        lb.grid(row=3, column=1, padx=5)
        self.e3 = Entry(self.initface, width=14)
        self.e3.grid(row=3, column=2, padx=5, pady=5)
        btnsure = Button(self.initface, text='确认', fg='black', font=('黑体', 9), command=self.recycle)
        btnsure.grid(row=3, column=4, padx=5)

        lb = Label(self.initface, text='=======================================')
        lb.grid(row=4, column=2, columnspan=3, padx=5)

        lb = Label(self.initface, text='批量创建文件数:')
        lb.grid(row=6, column=1, padx=5)
        self.e4 = Entry(self.initface, width=14)
        self.e4.grid(row=6, column=2, padx=5, pady=5)
        btnsure = Button(self.initface, text='批量生成文件', fg='black', font=('黑体', 9), command=self.randombuild)
        btnsure.grid(row=6, column=3, padx=5)

        btnsure = Button(self.initface, text='批量删除部分文件', fg='red', font=('黑体', 9), command=self.specdelete)
        btnsure.grid(row=6, column=4, padx=5)

        lb = Label(self.initface, text='总空闲块数:')
        lb.grid(row=2, column=7, padx=5)
        lb=Label(self.initface, text=str(self.disk.left),fg='green')
        lb.grid(row=2, column=8, padx=5)


        columns = (("序号", "第一个空闲盘块号", "空闲盘块数"))
        self.tree1 = ttk.Treeview(self.root, height=18, show="headings", columns=columns)  # #创建表格对象
        self.tree1.column("序号", width=130)  # #设置列
        self.tree1.column("第一个空闲盘块号", width=200)
        self.tree1.column("空闲盘块数", width=130)
        self.tree1.heading("序号", text="序号")  # #设置显示的表头名
        self.tree1.heading("第一个空闲盘块号", text="第一个空闲盘块号")
        self.tree1.heading("空闲盘块数", text="空闲盘块数")

        columns = (("文件名", "大小", "所处磁盘块号"))
        self.tree2 = ttk.Treeview(self.root, height=18, show="headings", columns=columns)  # #创建表格对象
        self.tree2.column("文件名", width=110)  # #设置列
        self.tree2.column("大小", width=100)
        self.tree2.column("所处磁盘块号", width=250)
        self.tree2.heading("文件名", text="文件名")  # #设置显示的表头名
        self.tree2.heading("所处磁盘块号", text="所处磁盘块号")
        self.tree2.heading("大小", text="大小")
        self.print()
