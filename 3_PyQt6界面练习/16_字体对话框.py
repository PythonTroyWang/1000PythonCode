from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QPushButton,
                             QSizePolicy, QLabel, QFontDialog, QApplication)
import sys


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        btn = QPushButton('打开字体对话框', self)
        btn.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        btn.move(20, 20)

        btn.clicked.connect(self.show_dialog)

        self.lbl = QLabel('知识就是力量', self)
        self.lbl.move(130, 20)

        self.setGeometry(300, 300, 450, 350)
        self.setWindowTitle('字体对话框')
        self.show()

    def show_dialog(self):
        font, ok = QFontDialog.getFont()

        if ok:
            self.lbl.setFont(font)


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
