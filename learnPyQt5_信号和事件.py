#！/usr/bin/python3
#-*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication,
    QLCDNumber, QSlider, QVBoxLayout, QPushButton)
from PyQt5.QtCore import Qt, pyqtSignal, QObject

# 信号使用了 pyqtSignal() 方法创建，并且成为外部类 Communicate 类的属性。
class Communicate(QObject):
    closeApp = pyqtSignal()

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 创建一个 LCD 显示模块
        lcd = QLCDNumber(self)
        # 创建一个水平滑块
        sld = QSlider(Qt.Horizontal, self)
        # 滑块的最小值是10
        sld.setMinimum(10)
        # 滑块的最大值是1000
        sld.setMaximum(1000)
        # 滑块的步长 TODO: 不好用……
        sld.setSingleStep(5)

        # 创建按钮
        button1 = QPushButton('button1', self)
        button1.move(30, 30)

        # 创建按钮
        button2 = QPushButton('button2', self)
        button2.move(130, 130)

        # 按钮点击后连接的槽
        button1.clicked.connect(self.buttonClicked)
        button2.clicked.connect(self.buttonClicked)

        # 创建左下角的状态栏
        self.statusBar()

        vbox = QVBoxLayout()
        # 把 LCD 显示模块和水平滑块添加到 widget 中
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        # valueChanged信号和 LCD 数字显示的 display 槽链接在一起
        sld.valueChanged.connect(lcd.display)

        # 把自定义的 closeApp 信号连接到 QMainWindow 的 close() 槽上。
        self.c = Communicate()
        self.c.closeApp.connect(self.close)
        
        self.setGeometry(1300, 200, 700, 400)
        self.setWindowTitle('Signaal & slot')
        self.show()

    # 重写 keyPressEvent 事件处理函数，按下 Esc 按键时，程序终止
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

    def buttonClicked(self):
        # 可以获取信号发出的信号源是哪一个
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + 'was pressed')

    # 重写 mousePressEvent 方法，
    # 当我们在窗口上点击一下鼠标，closeApp信号会被发射。应用中断。
    def mousePressEvent(self, event):
        self.c.closeApp.emit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())