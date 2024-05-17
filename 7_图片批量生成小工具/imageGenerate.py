import os
from tkinter import messagebox

import pandas as pd
import tkinter
from tkinter import *
import image_tool
import threading
import windnd


class MY_GUI:
    def __init__(self, window):
        self.window = window

    def set_init_window(self):
        # 定义变量
        global v_show, v_product_gupiao, v_product_paiwei, v_path, v_trend, v_publish_text
        v_show = StringVar(value="0")
        v_product_gupiao = StringVar(value="0")
        v_product_paiwei = StringVar(value="0")
        v_path = StringVar(value="请将数据文件夹拖放进来")
        v_trend = IntVar()
        v_publish_text = StringVar(value="")
        # 窗口组件及布局
        self.window.title('图片自动生成工具')
        sw = self.window.winfo_screenwidth()
        sh = self.window.winfo_screenheight()
        x = (sw - 500) / 2
        y = (sh - 450) / 2
        self.window.geometry("%dx%d+%d+%d" % (500, 450, x, y))
        self.window.maxsize(500, 450)
        self.window.minsize(500, 450)
        drag_frame = Frame(self.window, width=480, height=130, bd=3, relief=GROOVE, bg='lightgrey',
                           takefocus=True).grid(row=0,
                                                columnspan=3,
                                                padx=10,
                                                pady=(10, 20))
        Label(drag_frame, textvariable=v_path, bg='lightgrey').grid(row=0, columnspan=3)

        # add data input
        Label(self.window, text='大盘趋势：').grid(row=1, column=0, pady=10)
        Radiobutton(self.window, text='向上', variable=v_trend, value=0).grid(row=1, column=1, pady=10)
        Radiobutton(self.window, text='向下', variable=v_trend, value=1).grid(row=1, column=2, pady=10)
        Label(self.window, text='版权发布文本：（日期使用{date}的方式加入到文本的需要位置）').grid(row=2, columnspan=3, pady=10)
        Entry(self.window, width=65, textvariable=v_publish_text).grid(row=3, columnspan=3, pady=10)

        Checkbutton(self.window, text='展示图', variable=v_show).grid(row=4, column=0, pady=10)
        Checkbutton(self.window, text='商品图-股票代码', variable=v_product_gupiao).grid(row=4, column=1, pady=10)
        Checkbutton(self.window, text='商品图-排位', variable=v_product_paiwei).grid(row=4, column=2, pady=10)
        Button(self.window, text="生成图片", command=self.generate_img_click).grid(row=5, columnspan=3, pady=10)
        Button(self.window, text="生成文件", command=self.generate_file_click).grid(row=6, columnspan=3, pady=10)

        # add drag function
        windnd.hook_dropfiles(self.window, dragged_file, force_unicode='utf-8')

    def generate_file_click(self):
        file_path = v_path.get()
        if os.path.isfile(file_path):
            messagebox.showinfo('提示', '请拖放数据文件夹：（务必包含动态数据和文字固化两个数据文件）')
        elif file_path == "请将数据文件夹拖放进来":
            messagebox.showinfo('提示', '请检查是否拖放了数据文件夹')
        else:
            messagebox.showinfo('提示', '程序已经开始生成文件，请去result目录下查看结果')
            self.export_file(file_path)

    def export_file(self, path):
        path = v_path.get()
        trend = ''
        if v_trend.get() == 0:
            trend = '向上'
        else:
            trend = '向下'
        try:
            df1 = pd.read_excel(os.path.join(path, '文字固化.xls'), converters={u'代码': str})
        except Exception:
            df1 = pd.read_excel(os.path.join(path, '文字固化.xlsx'), engine='openpyxl', converters={u'代码': str})
        try:
            df2 = pd.read_excel(os.path.join(path, '动态数据.xls'), converters={u'代码': str})
        except Exception:
            df2 = pd.read_excel(os.path.join(path, '动态数据.xlsx'), engine='openpyxl', converters={u'代码': str})

        # 修改代码格式
        df1['代码'] = df1['代码'].astype(str)
        df2['代码'] = df2['代码'].astype(str)

        public_text = v_publish_text.get()
        text = public_text.replace('{date}', df2['日期'][0].strftime('%Y%m%d'))
        # 取合并的数据
        df3 = df1.append(df2)
        # 取不相交的数据
        df3.drop_duplicates(subset='代码', keep=False, inplace=True)

        # 对动态数据进行排序
        df2 = df2.sort_values('BB-H', ascending=False)
        # 取相交数据
        ret = pd.merge(df2, df1, how='inner', on='代码')
        # 整理列
        ret['日期'] = ret['日期'].iat[0].strftime('%Y%m%d')
        ret.drop('名称_y', axis=1, inplace=True)
        ret.rename(columns={'名称_x': '名称'}, inplace=True)
        ret['大盘趋势'] = trend
        ret['版权发布文本'] = text

        df3.drop('地区', axis=1, inplace=True)
        df3.drop('细分行业', axis=1, inplace=True)
        df3.drop('流通股(亿)', axis=1, inplace=True)
        df3.drop('上市日期', axis=1, inplace=True)
        df3.drop('换手%', axis=1, inplace=True)
        df3.drop('现价', axis=1, inplace=True)
        df3.drop('日期', axis=1, inplace=True)
        df3.drop('BB-T', axis=1, inplace=True)
        df3.drop('BB-H', axis=1, inplace=True)
        df3.drop('排 T', axis=1, inplace=True)
        df3.drop('排 H', axis=1, inplace=True)
        df3.drop('派息', axis=1, inplace=True)

        writer = pd.ExcelWriter('./result/文件/output.xls')
        ret.to_excel(writer, index=0, sheet_name='根据股票代码匹配到的数据')
        df3.to_excel(writer, index=0, sheet_name='股票代码完全不匹配的数据')
        writer.save()

    def generate_img_click(self):
        file_path = v_path.get()
        if os.path.isfile(file_path):
            messagebox.showinfo('提示', '请拖放数据文件夹：（务必包含动态数据和文字固化两个数据文件）')
        elif file_path == "请将数据文件夹拖放进来":
            messagebox.showinfo('提示', '请检查是否拖放了数据文件夹')
        elif v_show.get() == '0' and v_product_gupiao.get() == '0' and v_product_paiwei.get() == '0':
            messagebox.showinfo('提示', '请至少选择一项分类进行输出')
        else:
            messagebox.showinfo('提示', '程序已经开始生成图片，请去result目录下查看结果')
            if v_show.get() == '1':
                self.image_generate_show(file_path)
            if v_product_gupiao.get() == '1':
                self.image_generate_product(file_path, 0)
            if v_product_paiwei.get() == '1':
                self.image_generate_product(file_path, 1)

    def image_generate_show(self, path):
        public_text = v_publish_text.get()
        try:
            df1 = pd.read_excel(os.path.join(path, '文字固化.xls'), converters={u'代码': str})
        except Exception:
            df1 = pd.read_excel(os.path.join(path, '文字固化.xlsx'), engine='openpyxl', converters={u'代码': str})
        try:
            df2 = pd.read_excel(os.path.join(path, '动态数据.xls'), converters={u'代码': str})
        except Exception:
            df2 = pd.read_excel(os.path.join(path, '动态数据.xlsx'), engine='openpyxl', converters={u'代码': str})

        text = public_text.replace('{date}', df2['日期'][0].strftime('%Y%m%d'))

        # 修改代码格式
        df1['代码'] = df1['代码'].astype(str)
        df2['代码'] = df2['代码'].astype(str)

        # 对动态数据进行排序
        df2 = df2.sort_values('BB-H', ascending=False)
        # 取相交数据
        ret = pd.merge(df2, df1, how='inner', on='代码')

        # 循环处理数据（参数：1、每行数据，2、日期）
        for item in ret.iterrows():
            t1 = threading.Thread(target=image_tool.img_generate, args=(item, text,))
            t1.start()

    def image_generate_product(self, path, name):
        trend = ''
        if v_trend.get() == 0:
            trend = '向上'
        else:
            trend = '向下'
        public_text = v_publish_text.get()
        try:
            df1 = pd.read_excel(os.path.join(path, '文字固化.xls'), converters={u'代码': str})
        except Exception:
            df1 = pd.read_excel(os.path.join(path, '文字固化.xlsx'), engine='openpyxl', converters={u'代码': str})
        try:
            df2 = pd.read_excel(os.path.join(path, '动态数据.xls'), converters={u'代码': str})
        except Exception:
            df2 = pd.read_excel(os.path.join(path, '动态数据.xlsx'), engine='openpyxl', converters={u'代码': str})

        # 修改代码格式
        df1['代码'] = df1['代码'].astype(str)
        df2['代码'] = df2['代码'].astype(str)
        text = public_text.replace('{date}', df2['日期'][0].strftime('%Y%m%d'))
        # 取四个比较值
        contrast_array = [df2.query("代码 == '1A0003'")['BB-T'].iat[0], df2.query("代码 == '1A0001'")['BB-T'].iat[0],
                          df2.query("代码 == '399006'")['BB-T'].iat[0], df2.query("代码 == '399003'")['BB-T'].iat[0]]
        # 对动态数据进行排序
        df2 = df2.sort_values('BB-H', ascending=False)
        # 取相交数据
        ret = pd.merge(df2, df1, how='inner', on='代码')
        # 循环处理数据（参数：1、每行数据，2、比对值, 3、排序号，4、日期，5、保存文件名称方式）
        i = 1
        for item in ret.iterrows():
            t2 = threading.Thread(target=image_tool.img_generate2, args=(item, contrast_array, i, text, name, trend,))
            t2.start()
            i += 1


def dragged_file(files):
    v_path.set(files[0])


def start():
    window = tkinter.Tk()
    img_generate = MY_GUI(window)
    img_generate.set_init_window()
    window.mainloop()


start()
