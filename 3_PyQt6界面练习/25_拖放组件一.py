﻿import sys

from PyQt6.QtWidgets import (QPushButton, QWidget,
                             QLineEdit, QApplication)


class Button(QPushButton):
    def __init__(self, title, parent):
        super().__init__(title, parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ingnore()

    def dropEvent(self, e):
        self.setText(e.mimeData().text())


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        edit = QLineEdit('', self)
        edit.setDragEnabled(True)
        edit.move(30, 65)

        button = Button('按钮', self)
        button.move(190, 65)

        self.setWindowTitle('简单的拖拽功能')
        self.setGeometry(300, 300, 300, 150)


def main():
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec()


if __name__ == '__main__':
    main()
