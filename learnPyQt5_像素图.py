#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QHBoxLayout
from PyQt5.QtGui import QPixmap

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout(self)
        # 创建QPixmap对象。该对象构造方法传入一个文件的名字作为参数。
        pixmap = QPixmap('test.png')

        # 我们把像素图对象设置给标签，从而通过标签来显示像素图。
        lablePixmap = QLabel(self)
        lablePixmap.setPixmap(pixmap)
        

        hbox.addWidget(lablePixmap)
        self.setLayout(hbox)
        

        self.setGeometry(30, 30, 600, 400)
        self.setWindowTitle('QPixmap')
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())