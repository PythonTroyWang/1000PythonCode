import threading
from tkinter import messagebox, StringVar, Tk, DISABLED, ACTIVE
from tkinter.ttk import *
from do_word import sendReq
import os
from configparser import RawConfigParser


class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        self.__setting()
        self.tk_input_url = self.input_url(self)
        self.tk_label_url = self.label_url(self)
        self.tk_label_cookie = self.label_cookie(self)
        self.tk_input_cookie = self.input_cookie(self)
        self.tk_button_word = self.button_word(self)

    def __win(self):
        self.title("数据采集小工具")
        # 设置窗口大小、居中
        width = 600
        height = 350
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        self.resizable(width=False, height=False)
        global g_url, g_cookie
        g_url = StringVar()
        g_cookie = StringVar()

    def __setting(self):
        self.config = RawConfigParser()
        self.config.read('config.ini', encoding='utf-8')
        cookie = self.config.get('cookie', 'cookie')
        if cookie is not None:
            g_cookie.set(cookie)

    def label_url(self, parent):
        label = Label(parent, text="①请输入链接：", anchor="center", )
        label.place(x=110, y=50, width=85, height=30)
        return label

    def input_url(self, parent):
        ipt = Entry(parent, textvariable=g_url, )
        ipt.place(x=110, y=100, width=380, height=30)
        return ipt

    def label_cookie(self, parent):
        label = Label(parent, text="②请填写Cookie：", anchor="center", )
        label.place(x=110, y=140, width=100, height=30)
        return label

    def input_cookie(self, parent):
        ipt = Entry(parent, textvariable=g_cookie, )
        ipt.place(x=110, y=182, width=380, height=30)
        return ipt

    def button_word(self, parent):
        btn = Button(parent, text="采集生成word文档", command=lambda: thread_it(do_click, self.tk_button_word, ),
                     takefocus=False, )
        btn.place(x=110, y=240, width=150, height=30)
        return btn


def thread_it(func, *args):
    # 创建
    t = threading.Thread(target=func, args=args)
    # 守护 !!!
    t.setDaemon(True)
    # 启动
    t.start()
    # 阻塞--卡死界面！
    # t.join()


def do_click(btn):
    url = g_url.get()
    if url == '':
        messagebox.showinfo('提示', '链接地址不能为空！')
        return
    if 'https://v.huatu.com/tiku/analysis' not in url:
        messagebox.showinfo('提示', '链接地址不正确！')
        return
    cookie = g_cookie.get()
    if cookie == '':
        messagebox.showinfo('提示', 'cookie值不能为空！')
        return
    btn['state'] = DISABLED
    messagebox.showinfo('提示', '开始执行，请稍等，操作完成后会有提示！')
    # 开始采集生产word文档
    result = sendReq(url, cookie)
    if result == 'error':
        messagebox.showerror('提示', '操作失败！')
    else:
        messagebox.showinfo('提示', '操作完成，请到output目录下查看文件')
        os.system("start explorer " + os.getcwd() + os.sep + 'output')
    btn['state'] = ACTIVE


def on_closing():
    config = RawConfigParser()
    config.read('config.ini', encoding='utf-8')
    config.set('cookie', 'cookie', g_cookie.get())

    with open('config.ini', 'w', encoding='utf-8') as f:
        config.write(f)  # 值写入配置文件
    win.destroy()


class Win(WinGUI):
    def __init__(self):
        super().__init__()


if __name__ == "__main__":
    win = Win()
    win.protocol('WM_DELETE_WINDOW', on_closing)
    win.mainloop()
