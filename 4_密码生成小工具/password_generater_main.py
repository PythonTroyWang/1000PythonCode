import string
import sys

from PyQt6.QtWidgets import QApplication, QDialog, QMessageBox
import password_generate
import random

import warnings
warnings.filterwarnings('ignore', category=DeprecationWarning)


class MyPasswordGenerate(password_generate.Ui_PasswordGenerate, QDialog):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.pushButton.clicked.connect(self.new_pwd)

    def new_pwd(self):
        site = self.lineEdit_site.text()
        if not site:
            QMessageBox.warning(self, '信息提示', '请输入网站名称')
            return
        text = []
        if self.checkBox_number.isChecked():
            text.append(string.digits * 2)

        if self.checkBox_upper.isChecked():
            text.append(string.ascii_uppercase * 2)

        if self.checkBox_lower.isChecked():
            text.append(string.ascii_lowercase * 2)

        if self.checkBox_puc.isChecked():
            text.append(string.punctuation * 2)
        if not text:
            text = (
                    string.digits
                    + string.ascii_lowercase
                    + string.ascii_uppercase
                    + string.punctuation
            )
        else:
            text = "".join(text)
        text = random.sample(list(text), 20)
        password = "".join(text)
        self.lineEdit_result.setText(password)

        with open('我的密码本.txt', 'a', encoding='utf8') as f:
            f.write(f'{site}\t{password}\n')

        QMessageBox.information(self, '信息提示', '密码生成成功！')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myPasswordGenerate = MyPasswordGenerate()
    sys.exit(app.exec())
