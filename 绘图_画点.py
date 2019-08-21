# -*- coding: utf-8 -*-

"""
PyQt5 tutorial

In the example, we draw randomly 1000 red points
on the window.

author: py40.com
last edited: 2017年3月
"""
import sys, random
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Points')
        self.show()

    # 改变窗口大小时，会进入paintEvent事件
    # 每次我们改变窗口的大小,生成一个 paint event 事件。我们得到的当前窗口的大小size。我们使用窗口的大小来分配点在窗口的客户区。
    def paintEvent(self, e):
        print("paint event in")
        qp = QPainter()
        qp.begin(self)
        self.drawPoints(qp)
        qp.end()

    def drawPoints(self, qp):
        qp.setPen(Qt.red)
        size = self.size()

        for i in range(1000):
            x = random.randint(1, size.width() - 1)
            y = random.randint(1, size.height() - 1)
            qp.drawPoint(x, y)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())