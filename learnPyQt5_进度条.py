#!usr/bin/python3
#-*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QProgressBar, QPushButton
from PyQt5.QtCore import QBasicTimer

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.buttonStart = QPushButton('开始', self)
        self.buttonStart.move(20, 50)
        self.buttonStart.clicked.connect(self.doAction)

        # 创建一个滑块条
        self.progressbar = QProgressBar(self)
        self.progressbar.setGeometry(120, 50, 200, 25)

        # 用定时器激活进度条
        self.timer = QBasicTimer()
        self.step = 0

        self.setGeometry(50, 50, 600, 400)
        self.setWindowTitle('QProgressBar')
        self.show()

    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            self.buttonStart.setText('Finished')
            return

        self.step = self.step + 1
        self.progressbar.setValue(self.step)

    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.buttonStart.setText('开始')
        else:
            # 调用了start()方法激活进度条。这个方法有两个参数：定时时间和接收定时器事件的对象。
            self.timer.start(10, self)
            self.buttonStart.setText('结束')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())