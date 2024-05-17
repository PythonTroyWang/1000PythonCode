import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import word2excel_util
import excel2word_util
import os


class MY_GUI:
    def __init__(self, window):
        self.window = window

    def set_init_window(self):
        global v_file, v_file_q, v_file_a, v_num, v_file_excel, v_q_random, v_s_random
        v_file = StringVar()
        v_file_q = StringVar()
        v_file_a = StringVar()
        v_num = StringVar(value='1')
        v_file_excel = StringVar()
        v_q_random = StringVar(value="0")
        v_s_random = StringVar(value="0")
        # 界面基础设置
        self.window.title('数据处理小工具')
        sw = self.window.winfo_screenwidth()
        sh = self.window.winfo_screenheight()
        width = 500
        height = 540
        x = (sw - width) / 2
        y = (sh - height) / 2
        self.window.geometry("%dx%d+%d+%d" % (width, height, x, y))
        self.window.maxsize(width, height)
        self.window.minsize(width, height)
        # 第一种情况界面元素
        Label(self.window, text='第一种情况：题目和答案在一个文档').grid(row=0, column=0, columnspan=2, pady=10)
        Entry(self.window, textvariable=v_file, width=55).grid(row=1, column=0, pady=2, padx=5, sticky=N+S)
        Button(self.window, text="导入整体文件", command=self.browse_click).grid(row=1, column=1, pady=2, sticky=N+S)
        Button(self.window, text="word转excel", command=self.do_click).grid(row=2, column=0, columnspan=2, pady=10)
        # 第二种情况界面元素
        Label(self.window, text='第二种情况：题目和答案是不同的文档').grid(row=3, column=0, columnspan=2, pady=10)
        Entry(self.window, textvariable=v_file_q, width=55).grid(row=4, column=0, pady=2, padx=5, sticky=N+S)
        Button(self.window, text="导入题目文件", command=self.browse_q_click).grid(row=4, column=1, pady=2, sticky=N+S)
        Entry(self.window, textvariable=v_file_a, width=55).grid(row=5, column=0, pady=2, padx=5, sticky=N+S)
        Button(self.window, text="导入答案文件", command=self.browse_a_click).grid(row=5, column=1, pady=2, sticky=N+S)
        Button(self.window, text="word转excel", command=self.do_2_click).grid(row=6, column=0, columnspan=2, pady=10)
        # 增加起始编号
        Label(self.window, text='起始编号设置').grid(row=7, column=0, pady=10, sticky=E)
        Entry(self.window, textvariable=v_num, width=10).grid(row=7, column=1, sticky=W)

        # Excel转Word
        Label(self.window, text='试题Excel文档转word文档').grid(row=8, column=0, columnspan=2, pady=10)
        Entry(self.window, textvariable=v_file_excel, width=55).grid(row=9, column=0, pady=2, padx=5, sticky=N + S)
        Button(self.window, text="导入数据文件", command=self.browse_excel_click).grid(row=9, column=1, pady=2, sticky=N + S)

        Checkbutton(self.window, text='题目顺序随机', variable=v_q_random).grid(row=10, column=0, pady=10, sticky=E)
        Checkbutton(self.window, text='题目选项随机', variable=v_s_random).grid(row=10, column=1, pady=10, sticky=W)

        Button(self.window, text="excel转word", command=self.do_excel_click).grid(row=11, column=0, columnspan=2, pady=10)

    @staticmethod
    def browse_click():
        file_path = filedialog.askopenfilename(title=u'导入文件', initialdir=(os.getcwd()), filetypes=[("Doc", "*.docx")])
        if len(file_path) > 0:
            v_file.set(file_path)

    @staticmethod
    def browse_q_click():
        file_path = filedialog.askopenfilename(title=u'导入题目文件', initialdir=(os.getcwd()), filetypes=[("Doc", "*.docx")])
        if len(file_path) > 0:
            v_file_q.set(file_path)

    @staticmethod
    def browse_a_click():
        file_path = filedialog.askopenfilename(title=u'导入答案文件', initialdir=(os.getcwd()), filetypes=[("Doc", "*.docx")])
        if len(file_path) > 0:
            v_file_a.set(file_path)

    @staticmethod
    def browse_excel_click():
        file_path = filedialog.askopenfilename(title=u'导入数据文件', initialdir=(os.getcwd()), filetypes=[("Excel", "*.xlsx")])
        if len(file_path) > 0:
            v_file_excel.set(file_path)

    @staticmethod
    def do_click():
        try:
            file_path = v_file.get()
            num = v_num.get()
            if len(file_path) == 0:
                messagebox.showinfo('提示', '请先导入文档')
            else:
                a, b = word2excel_util.word2excel_with_file(file_path, num)
                if b is not None:
                    messagebox.showinfo('提示', '处理异常，第%s条%s的格式似乎出错了，请检查一下' % (a, b))
                else:
                    messagebox.showinfo('提示', '处理完成，请到excel_result目录下查看文件')
                    os.system("start explorer " + os.getcwd() + os.sep + 'excel_result')
        except Exception:
            messagebox.showerror('提示', '请保证文档和标准示例中的格式一致！')

    @staticmethod
    def do_2_click():
        try:
            file_q_path = v_file_q.get()
            file_a_path = v_file_a.get()
            num = v_num.get()
            if len(file_q_path) == 0:
                messagebox.showinfo('提示', '请先导入题目文档')
            elif len(file_a_path) == 0:
                messagebox.showinfo('提示', '请先导入答案文档')
            else:
                a, b = word2excel_util.word2excel_with2file(file_q_path, file_a_path, num)
                if b is not None:
                    messagebox.showinfo('提示', '处理异常，第%s条%s的格式似乎出错了，请检查一下' % (a, b))
                else:
                    messagebox.showinfo('提示', '处理完成，请到excel_result目录下查看文件')
                    os.system("start explorer " + os.getcwd() + os.sep + 'excel_result')
        except Exception:
            messagebox.showerror('提示', '请保证文档和标准示例中的格式一致！')

    @staticmethod
    def do_excel_click():
        try:
            file_excel_path = v_file_excel.get()
            if len(file_excel_path) == 0:
                messagebox.showinfo('提示', '请先导入数据文档')
            else:
                q = v_q_random.get()
                s = v_s_random.get()
                excel2word_util.excel2word_with_file(file_excel_path, q, s)
                messagebox.showinfo('提示', '处理完成，请到word_result目录下查看文件')
                os.system("start explorer " + os.getcwd() + os.sep + 'word_result')
        except Exception as e:
            messagebox.showerror('提示', repr(e))


def start():
    window = tkinter.Tk()
    img_generate = MY_GUI(window)
    img_generate.set_init_window()
    window.mainloop()


start()
