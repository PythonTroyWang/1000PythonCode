import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel


def main():
    app = QApplication(sys.argv)

    # 创建主窗口
    window = QMainWindow()
    window.setWindowTitle('Hello PyQt6')
    window.setGeometry(100, 100, 400, 200)

    # 在窗口中添加标签
    label = QLabel('Hello PyQt6', window)
    label.move(50, 50)

    # 显示窗口
    window.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()
