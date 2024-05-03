from PyQt6.QtWidgets import (QWidget, QPushButton,
                             QFrame, QApplication)
from PyQt6.QtGui import QColor
import sys


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.col = QColor(0, 0, 0)

        red_btn = QPushButton('红色', self)
        red_btn.setCheckable(True)
        red_btn.move(10, 10)
        red_btn.clicked[bool].connect(self.setColor)

        green_btn = QPushButton('绿色', self)
        green_btn.setCheckable(True)
        green_btn.move(10, 60)
        green_btn.clicked[bool].connect(self.setColor)

        blue_btn = QPushButton('蓝色', self)
        blue_btn.setCheckable(True)
        blue_btn.move(10, 110)
        blue_btn.clicked[bool].connect(self.setColor)

        self.square = QFrame(self)
        self.square.setGeometry(150, 20, 100, 100)
        self.square.setStyleSheet("QWidget {background-color: %s}" % self.col.name())

        self.setGeometry(300, 300, 300, 250)
        self.setWindowTitle('Toggle button')
        self.show()

    def setColor(self, pressed):
        source = self.sender()
        if pressed:
            val = 255
        else:
            val = 0
        if source.text() == "红色":
            self.col.setRed(val)
        elif source.text() == "绿色":
            self.col.setGreen(val)
        else:
            self.col.setBlue(val)
        self.square.setStyleSheet("QFrame {background-color: %s}" % self.col.name())


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
