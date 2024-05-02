from PyQt6.QtWidgets import (QMainWindow, QTextEdit,
                             QFileDialog, QApplication)
from PyQt6.QtGui import QIcon, QAction
from pathlib import Path
import sys


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        open_file = QAction('打开', self)
        open_file.setShortcut('Ctrl+O')
        open_file.setStatusTip('打开一个新文件')
        open_file.triggered.connect(self.show_dialog)

        menubar = self.menuBar()
        file_menu = menubar.addMenu('文件')
        file_menu.addAction(open_file)

        self.setGeometry(300, 300, 550, 450)
        self.setWindowTitle('文件对话框')
        self.show()

    def show_dialog(self):
        home_dir = str(Path.home())
        print(home_dir)
        fname = QFileDialog.getOpenFileName(self, '打开文件', home_dir)
        if fname[0]:
            with open(fname[0], 'r') as f:
                data = f.read()
                self.textEdit.setText(data)

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
