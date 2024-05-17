import os
from tkinter import messagebox

import tkinter
from tkinter import *
import windnd
import util


class MY_GUI:
    def __init__(self, window):
        self.window = window

    def set_init_window(self):
        global v_path
        v_path = StringVar(value="请将待处理的PDF文件夹拖放进来")
        self.window.title('PDF处理工具')
        sw = self.window.winfo_screenwidth()
        sh = self.window.winfo_screenheight()
        x = (sw - 500) / 2
        y = (sh - 450) / 2
        self.window.geometry("%dx%d+%d+%d" % (500, 450, x, y))
        self.window.maxsize(500, 450)
        self.window.minsize(500, 450)
        drag_frame = Frame(self.window, width=480, height=200, bd=3, relief=GROOVE, bg='lightgrey',
                           takefocus=True).grid(row=0,
                                                columnspan=3,
                                                padx=10,
                                                pady=(10, 20))
        Label(drag_frame, textvariable=v_path, bg='lightgrey').grid(row=0, columnspan=3)
        Button(self.window, text="生成文件", command=self.generate_file_click).grid(row=6, columnspan=3, pady=10)

        windnd.hook_dropfiles(self.window, dragged_file, force_unicode='utf-8')

    @staticmethod
    def generate_file_click():
        file_path = v_path.get()
        print(file_path)
        if os.path.isfile(file_path):
            messagebox.showinfo('提示', '请拖放文件夹而不是文件')
        elif file_path == "请将待处理的PDF文件夹拖放进来":
            messagebox.showinfo('提示', '请检查是否拖放了数据文件夹')
        else:
            pdf_files = util.get_file(file_path)
            for pdf_file in pdf_files:
                util.parse(pdf_file)
            messagebox.showinfo('提示', '处理完成，请到result目录下查看文件')
            os.system("start explorer " + os.getcwd() + os.sep + 'result')


def dragged_file(files):
    v_path.set(files[0])


def start():
    window = tkinter.Tk()
    img_generate = MY_GUI(window)
    img_generate.set_init_window()
    window.mainloop()


start()
