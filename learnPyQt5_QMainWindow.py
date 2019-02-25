#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QApplication, QAction, qApp
from PyQt5.QtGui import QIcon

class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建一个 TextEdit在中央显示
        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

        # 创建一个有指定图标和文本为 "Exit"的标签
        exitAction = QAction(QIcon('exit.png'), '&Exit', self)
        # 快捷键TODO: 快捷键功能暂时不好用
        exitAction.setShortcut('Ctrl + Q')
        # 当鼠标指向该菜单项时，状态提示信息
        exitAction.setStatusTip('Exit application')
        # 当我们选中特定的动作，一个触发信号会被发射。信号连接到QApplication组件的quit()方法。这样就中断了应用。
        exitAction.triggered.connect(qApp.quit)

        # 创建工具栏TODO: 传进去的参数有什么作用？，将QtGui.QMainWindow的quit()方法连接到了触发信号上。
        self.toolbar = self.addToolBar('Exit3')
        self.toolbar.addAction(exitAction)

        # 创建一个菜单栏（左下角显示），默认显示为 "Ready"
        self.statusBar().showMessage('Ready')
        # 创建一个菜单栏
        menubar = self.menuBar()
        # 创建一个 "file"菜单
        fileMenu = menubar.addMenu('&file')
        # 把退出动作添加到 "file"菜单中
        fileMenu.addAction(exitAction)
        # 再添加一个 "save"菜单
        saveMenu = menubar.addMenu('&save')
        
        self.setGeometry(100, 100, 500, 540)
        self.setWindowTitle("Simple")
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    test = Example()
    sys.exit(app.exec_())
