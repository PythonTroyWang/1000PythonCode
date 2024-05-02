import sys
from PyQt6.QtWidgets import QMainWindow, QPushButton, QApplication


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        btn1 = QPushButton('按钮1', self)
        btn1.move(30, 50)

        btn2 = QPushButton('按钮2', self)
        btn2.move(150, 50)

        btn1.clicked.connect(lambda: self.button_clicked(btn1))
        btn2.clicked.connect(lambda: self.button_clicked(btn2))

        self.statusBar()

        self.setGeometry(300, 300, 450, 350)
        self.setWindowTitle('Event sender')
        self.show()

    def button_clicked(self, button):
        msg = f'{button.text()} 被点击了'
        self.statusBar().showMessage(msg)


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
