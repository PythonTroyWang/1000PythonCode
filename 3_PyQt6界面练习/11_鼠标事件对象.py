import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QApplication, QGridLayout, QLabel


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        grid = QGridLayout()

        x = 0
        y = 0

        self.text = f'x = {x}, y = {y}'

        self.label = QLabel(self.text, self)
        grid.addWidget(self.label, 0, 0, Qt.AlignmentFlag.AlignTop)

        # 开启指针跟踪
        self.setMouseTracking(True)
        self.setLayout(grid)

        self.setGeometry(300, 300, 500, 400)
        self.setWindowTitle('事件对象')
        self.show()

    def mouseMoveEvent(self, e):
        x = int(e.position().x())
        y = int(e.position().y())
        text = f'x = {x}, y = {y}'
        self.label.setText(text)

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
