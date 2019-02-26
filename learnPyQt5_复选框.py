#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QCheckBox
from PyQt5.QtCore import Qt

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建一个复选框
        checkbox = QCheckBox('Show Title', self)
        checkbox.move(20, 20)
        # 复选框信号连接到 changeTitle 槽
        checkbox.stateChanged.connect(self.changeTitle)
        # 如果执行下面的代码，复选框默认情况是被选中的，同时信号会发送给槽
        checkbox.toggle()
        

        self.setGeometry(100, 100, 500, 400)
        self.setWindowTitle('Show Title')
        self.show()

    def changeTitle(self, state):
        # 判断复选框是否被选勾选
        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
            print('check box')
        else:
            self.setWindowTitle('check toggle')
            print('delet check box')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
