#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QToolTip, 
    QPushButton, QMessageBox, QDesktopWidget)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置字体，字号
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>Qwidget</b> widget')
        # 设置按钮名称
        btn = QPushButton('Button', self)
        # # 点击按钮后的信号槽传递
        # btn.clicked.connect(QCoreApplication.instance().quit)
        # 鼠标放在按钮上的提示
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        # 按钮的大小
        btn.resize(btn.sizeHint())
        btn.move(50, 50)
        # 前两个参数是窗口运行时的坐标，后两个参数是窗口大小
        self.setGeometry(0, 100, 500, 220)
        # 设置窗口运行时在屏幕正中央打开
        self.center()
        # 窗口标题栏显示
        self.setWindowTitle("Simple")
        # 窗口栏左边的图标
        self.setWindowIcon(QIcon('web.png'))
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    # 关闭窗口时会调用这个处理方法，
    # 我们要重写这个方法，在关闭串口时让用户多次确认
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes |
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            reply = QMessageBox.question(self, 'Message',
            "sure? sure? sure?", QMessageBox.Yes |
            QMessageBox.No, QMessageBox.No)

            if reply == QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()
        else:
            event.ignore()

if __name__ == '__main__':
    # app = QApplication(sys.argv)
    # w = QWidget()
    # # 窗口的大小
    # w.resize(550, 150)
    # # 窗口打开时的坐标
    # w.move(0, 0)
    # # 窗口标题栏显示
    # w.setWindowTitle('Simple')
    # w.show()
    # sys.exit(app.exec_())

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())