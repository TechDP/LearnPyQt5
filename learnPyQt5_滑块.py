#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QSlider, QLabel, QApplication
from PyQt5.QtCore import Qt

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 创建一个横向滑块
        sld = QSlider(Qt.Horizontal, self)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setGeometry(30, 40, 100, 30)
        # 滑块连接到 changeValue 槽，传递 int 类型数据进去
        sld.valueChanged[int].connect(self.changeValue)

        self.label = QLabel(self)
        self.label.setText(str(0))
        self.label.setGeometry(160, 40, 80, 30)

        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('QSlider')
        self.show()


    def changeValue(self, value):
        # label 上显示滑块传递的值
        self.label.setText(str(value))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())