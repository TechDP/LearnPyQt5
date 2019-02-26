#/usr/bin/python3
#-*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QFrame, QApplication
from PyQt5.QtGui import QColor

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.col = QColor(0, 0, 0)
        # 要创建切换按钮，就要创建QPushButton，
        # 并且调用setCheckable()方法让它可被选中。
        RedButton = QPushButton('Red', self)
        RedButton.setCheckable(True)
        RedButton.move(20, 20)
        # 把 clicked 信号连接到我们定义的方法上。我们使用 clicked 信号来操作布尔值。
        RedButton.clicked[bool].connect(self.setColor)

        GreenButton = QPushButton('Green', self)
        GreenButton.setCheckable(True)
        GreenButton.move(20, 60)
        GreenButton.clicked[bool].connect(self.setColor)

        BlueButton = QPushButton('Blue', self)
        BlueButton.setCheckable(True)
        BlueButton.move(20, 100)
        BlueButton.clicked[bool].connect(self.setColor)

        self.square = QFrame(self)
        self.square.setGeometry(150, 20, 100, 100)
        self.square.setStyleSheet("QWidget { background-color: %s }" % self.col.name())

        self.setGeometry(300, 300, 500, 400)
        self.setWindowTitle('Toggle button')
        self.show()

    def setColor(self, pressed):
        # 获得发生状态切换的按钮
        source = self.sender()

        if pressed:
            val = 255
        else:
            val = 0

        # 获取产生信号的信号源
        if source.text() == 'Red':
            self.col.setRed(val)
            print("set color Red")
        elif source.text() == 'Green':
            self.col.setGreen(val)
            print("set color Green")
        else:
            self.col.setBlue(val)
            print("set color Blue")

        self.square.setStyleSheet("QFrame { background-color: %s }" % self.col.name())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())