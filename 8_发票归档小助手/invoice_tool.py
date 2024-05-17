from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog, messagebox

from utils.network_util import get_mac_address
from utils.work_util import sendReq
import requests
import json
import os
from configparser import RawConfigParser
import threading


class MainPage(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        self.label_company_name = self.label_company_name(self)
        self.input_company_name = self.input_company_name(self)
        self.label_select_output = self.label_select_output(self)
        self.label_select_input = self.label_select_input(self)
        self.button_do = self.button_do(self)

        self.input_select_input = self.input_select_input(self)
        self.button_select_input = self.button_select_input(self)
        self.input_select_output = self.input_select_output(self)
        self.button_select_output = self.button_select_output(self)

    def __win(self):
        self.title("快档通——瞬时批量归档，轻松秒查，贴心发票助手")
        global var_company_name, var_input_folder, var_output_folder
        var_company_name = StringVar()
        var_input_folder = StringVar()
        var_output_folder = StringVar()
        # 设置窗口大小、居中
        width = 600
        height = 500
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        self.resizable(width=False, height=False)
        self.status_bar = Label(self, text="快档通 v1.0 @copyright 聚诚财税 客服微信：TechXL", anchor=CENTER)
        self.status_bar.pack(side=BOTTOM, fill=BOTH, pady=10)

    @staticmethod
    def label_company_name(parent):
        label = Label(parent, text="①请填写公司名称：", anchor="w", )
        label.place(x=75, y=100, width=150, height=30)
        return label

    @staticmethod
    def input_company_name(parent):
        ipt = Entry(parent, textvariable=var_company_name, )
        ipt.place(x=210, y=100, width=330, height=30)
        return ipt

    @staticmethod
    def label_select_input(parent):
        label = Label(parent, text="②请选择此文件夹：(将税务系统直接下载的文件解压后放到同一个文件夹内)", anchor="w", )
        label.place(x=75, y=161, width=470, height=30)
        return label

    @staticmethod
    def input_select_input(parent):
        ipt = Entry(parent, textvariable=var_input_folder, )
        ipt.place(x=75, y=212, width=365, height=30)
        return ipt

    @staticmethod
    def button_select_input(parent):
        btn = Button(parent, command=input_select_click, text="选择", takefocus=False, )
        btn.place(x=461, y=212, width=80, height=30)
        return btn

    @staticmethod
    def label_select_output(parent):
        label = Label(parent, text="③请选择要保存的文件夹：", anchor="w", )
        label.place(x=75, y=268, width=470, height=30)
        return label

    @staticmethod
    def input_select_output(parent):
        ipt = Entry(parent, textvariable=var_output_folder)
        ipt.place(x=75, y=322, width=365, height=30)
        return ipt

    @staticmethod
    def button_select_output(parent):
        btn = Button(parent, command=output_select_click, text="选择", takefocus=False, )
        btn.place(x=461, y=322, width=80, height=30)
        return btn

    def button_do(self, parent):
        btn = Button(parent, command=lambda: thread_it(start_execute, self.button_do, ), text="开始执行", takefocus=False, )
        btn.place(x=251, y=394, width=100, height=30)
        return btn


def thread_it(func, *args):
    # 创建
    t = threading.Thread(target=func, args=args)
    # 守护 !!!
    t.setDaemon(True)
    # 启动
    t.start()


def input_select_click():
    source_path = filedialog.askdirectory(title='请选择待整理的发票目录')
    var_input_folder.set(source_path)


def output_select_click():
    source_path = filedialog.askdirectory(title='请选择要保存的目录')
    var_output_folder.set(source_path)


def start_execute(btn):
    company_name = var_company_name.get().strip()
    input_folder = var_input_folder.get()
    output_folder = var_output_folder.get()

    if company_name == "":
        messagebox.showinfo("提示信息", "请填写公司名称")
        return
    if input_folder == "":
        messagebox.showinfo("提示信息", "请选择待整理的发票目录")
        return
    if output_folder == "":
        messagebox.showinfo("提示信息", "请选择要保存的目录")
        return

    output_path = output_folder + '/' + company_name
    try:
        if os.path.exists(output_path + f'/{company_name}数电发票数据统计.xlsx'):
            os.remove(output_path + f'/{company_name}数电发票数据统计.xlsx')
    except PermissionError:
        messagebox.showinfo("提示信息", f"请先关闭您正在打开的{company_name}的发票数据统计文档，否则无法生成新的统计文档")
        return

    btn['state'] = DISABLED
    sendReq(input_folder, output_path, company_name)

    messagebox.showinfo(title="提示", message="文件已归档完成，自动打开文件夹")
    output_path = output_path.replace('/', '\\')
    os.system("start explorer " + output_path)

    var_company_name.set('')
    var_input_folder.set('')
    var_output_folder.set('')

    btn['state'] = ACTIVE


class WinMainPage(MainPage):
    def __init__(self):
        super().__init__()


class LicensePage(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        self.label_license = self.label_license(self)
        self.input_license = self.input_license(self)
        self.button_license_submit = self.button_license_submit(self)

    def __win(self):
        self.title("快档通---许可证授权界面")
        global var_input_license
        var_input_license = StringVar()
        # 设置窗口大小、居中
        width = 400
        height = 150
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        self.resizable(width=False, height=False)

    @staticmethod
    def label_license(parent):
        label = Label(parent, text="请输入授权码：", anchor="w", )
        label.place(x=30, y=30, width=100, height=30)
        return label

    @staticmethod
    def input_license(parent):
        ipt = Entry(parent, textvariable=var_input_license, )
        ipt.place(x=135, y=30, width=220, height=30)
        return ipt

    @staticmethod
    def button_license_submit(parent):
        btn = Button(parent, command=submit_license, text="授权", takefocus=False, )
        btn.place(x=150, y=80, width=100, height=30)
        return btn


def submit_license():
    input_license = var_input_license.get()
    if input_license == "":
        messagebox.showinfo("信息提示", "请输入授权许可证码！")
        return
    data_submit = {
        'license': input_license,
        'mac_address': get_mac_address()
    }
    headers_submit = {'Content-Type': 'application/json'}
    url_submit = "远程服务端接地址"
    response_submit = requests.post(url=url_submit, headers=headers_submit, data=json.dumps(data_submit)).text
    response_data_submit = json.loads(response_submit)
    if response_data_submit['code'] == 200:
        if response_data_submit['data'] == "0":
            messagebox.showinfo("信息提示", "您的软件已成功激活！")
            # 添加配置许可证
            add_config_license(input_license)
            # 跳转主界面
            winLicensePage.destroy()
            my_main_page = MainPage()
            my_main_page.mainloop()
        if response_data_submit['data'] == "1":
            messagebox.showinfo("信息提示", "您使用的授权许可证已被使用，请使用新的授权许可证进行软件激活！")
        if response_data_submit['data'] == "2":
            messagebox.showinfo("信息提示", "您的授权许可证不正确！")
    else:
        messagebox.showinfo("网络错误，请联网激活软件！")


def add_config_license(input_license):
    # 创建一个ConfigParser对象
    config_submit = RawConfigParser()
    # 读取ini文件内容
    config_submit.read('config.ini')
    # 获取ini文件中的数据
    section_license = 'license'
    option_key = 'key'
    config_submit.set(section_license, option_key, input_license)
    with open(file_path, 'w') as config_file:
        config_submit.write(config_file)


class WinLicensePage(LicensePage):
    def __init__(self):
        super().__init__()


def create_new_config():
    config_new = RawConfigParser()
    config_new.read('config.ini')
    section_new = 'license'
    option_new = 'key'
    if section_new not in config_new.sections():
        config_new.add_section(section_new)
    config_new.set(section_new, option_new, "")
    with open(file_path, 'w') as file:
        config_new.write(file)


def get_config_license():
    config_check = RawConfigParser()
    # 读取ini文件内容
    config_check.read('config.ini')
    # 获取ini文件中的数据
    section = 'license'
    option = 'key'
    return config_check.get(section, option)


if __name__ == "__main__":
    key = ""
    file_path = "config.ini"
    if not os.path.exists(file_path):
        create_new_config()
        winLicensePage = WinLicensePage()
        winLicensePage.mainloop()
    else:
        key = get_config_license()
        data = {
            'license': key,
            'mac_address': get_mac_address()
        }
        headers = {'Content-Type': 'application/json'}
        url = "远程服务端接地址"
        response = requests.post(url=url, headers=headers, data=json.dumps(data)).text
        print(response)
        response_data = json.loads(response)
        if response_data['code'] == 200 and response_data['data'] == "0":
            winMainPage = MainPage()
            winMainPage.mainloop()
        else:
            winLicensePage = WinLicensePage()
            winLicensePage.mainloop()
