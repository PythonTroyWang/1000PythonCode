import sys

from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import QMainWindow, QApplication, QMenu, QTextEdit


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.statusbar = self.statusBar()
        self.statusbar.showMessage('Ready')

        exit_act = QAction(QIcon('exit.png'), '&退出', self)
        exit_act.setShortcut('Ctrl+Q')
        exit_act.setStatusTip('Exit application')
        exit_act.triggered.connect(QApplication.instance().quit)

        new_act1 = QAction('&新建A文件', self)
        new_act1.setShortcut('Ctrl+N1')
        new_act1.setStatusTip('新建A文件')

        new_act2 = QAction('&新建B文件', self)
        new_act2.setShortcut('Ctrl+N2')
        new_act2.setStatusTip('新建B文件')

        open_act = QAction('&打开文件', self)
        open_act.setShortcut('Ctrl+O')
        open_act.setStatusTip('打开文件')

        imp_menu = QMenu('新建文件', self)
        imp_menu.addAction(new_act1)
        imp_menu.addAction(new_act2)

        view_state_act = QAction('状态栏可视', self, checkable=True)
        view_state_act.setStatusTip('状态栏可视')
        view_state_act.setChecked(True)
        view_state_act.triggered.connect(self.toggleMenu)

        menubar = self.menuBar()
        file_menu = menubar.addMenu('&File')
        viewMenu = menubar.addMenu('&View')
        file_menu.addMenu(imp_menu)
        file_menu.addAction(open_act)
        file_menu.addAction(exit_act)
        viewMenu.addAction(view_state_act)

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exit_act)

        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('菜单和状态栏')
        self.show()

    def toggleMenu(self, state):

        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()

    def contextMenuEvent(self, event):

        cmenu = QMenu(self)
        new_act = cmenu.addAction('new')
        open_act = cmenu.addAction('open')
        quit_act = cmenu.addAction('quit')
        action = cmenu.exec(self.mapToGlobal(event.pos()))

        if action == quit_act:
            QApplication.instance().quit()

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
