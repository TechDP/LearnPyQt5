#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets, QtCore

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        self.layouttest()
        self.setWindowTitle("嵌套布局示例")
        self.resize(600, 400)
        
        
    def layouttest(self):
        
        self.gridLayoutModuleSelect = QtWidgets.QGridLayout()
        
        self.button1 = QtWidgets.QRadioButton(str(1), self)
        self.button2 = QtWidgets.QRadioButton(str(2), self)
        self.button3 = QtWidgets.QRadioButton(str(3), self)
        self.button4 = QtWidgets.QRadioButton(str(4), self)

        self.gridLayoutModuleSelect.addWidget(self.button1, 0, 0)
        self.gridLayoutModuleSelect.addWidget(self.button2, 0, 1)
        self.gridLayoutModuleSelect.addWidget(self.button3, 1, 0)
        self.gridLayoutModuleSelect.addWidget(self.button4, 1, 1)

        wwg = QtWidgets.QWidget(self)
        wl = QtWidgets.QHBoxLayout(wwg)
        wl.addLayout(self.gridLayoutModuleSelect)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

