from PyQt6.QtWidgets import QWidget, QCheckBox, QApplication
from PyQt6.QtCore import Qt
import sys


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        cb = QCheckBox('展示标题', self)
        cb.move(20, 20)
        cb.toggle()
        cb.stateChanged.connect(self.change_title)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('复选框')
        self.show()

    def change_title(self, state):
        if state == Qt.CheckState.Checked.value:
            self.setWindowTitle('复选框练习')
        else:
            self.setWindowTitle('空')

def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()