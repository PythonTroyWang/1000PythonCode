import sys
from PyQt6.QtWidgets import QWidget, QToolTip, QPushButton, QApplication, QMessageBox
from PyQt6.QtGui import QFont


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        QToolTip.setFont(QFont('微软雅黑', 10))

        self.setToolTip('这是窗口的<b>QWidget</b>组件提醒框')

        btn = QPushButton('Quit', self)
        btn.clicked.connect(QApplication.instance().quit)
        btn.setToolTip('这个是按钮的<b>QPushButton</b>组件提醒框')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        self.resize(350, 250)
        self.center()
        self.setWindowTitle('Tooltips')
        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, '消息', '确定要退出吗？',
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                     QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self):

        qr = self.frameGeometry()
        print(qr)
        cp = self.screen().availableGeometry().center()
        print(cp)

        qr.moveCenter(cp)
        self.move(qr.topLeft())

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
