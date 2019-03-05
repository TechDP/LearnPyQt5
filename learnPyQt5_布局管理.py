#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sys
import time
from PyQt5.QtWidgets import (QWidget, QLabel, QApplication,
    QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout, 
    QTextEdit, QLineEdit)

class Example(QWidget):
    def __init__(self):
        super().__init__()

        # print("show UI1")
        # self.initUI_1()
        # time.sleep(5)
        print("show UI2")
        self.initUI_2()
        # print("show UI3")
        # self.initUI_3()


    def initUI_1(self):
        # 创建 lable 放在固定位置
        label1 = QLabel('Zetcode', self)
        label1.move(15, 10)

        # 创建 lable 放在固定位置
        label2 = QLabel('tutorials', self)
        label2.move(35, 40)

        # 创建 lable 放在固定位置
        label3 = QLabel('for programmers', self)
        label3.move(55, 70)

        # 创建 PushButton 
        okButton = QPushButton('确定')
        # 创建 PushButton 
        cancelButton = QPushButton('取消')

        # 这里我们创建了一个水平箱布局，并且增加了一个拉伸因子和两个按钮。
        # 拉伸因子在两个按钮之前增加了一个可伸缩空间。
        # 这会将按钮推到窗口的右边。
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        # 为了创建必要的布局，我们把水平布局放置在垂直布局内。
        # 拉伸因子将把包含两个按钮的水平箱布局推到窗口的底边。
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        # 设置窗口主布局
        self.setLayout(vbox)

        self.setGeometry(2560/2, 100, 700, 500)
        self.setWindowTitle('Absolute')
        self.show()

    def initUI_2(self):
        # 实例化 QGridLayout 类， 并且把这个类设为应用窗口的布局
        grid = QGridLayout()
        self.setLayout(grid)

        # 定义按钮的名字
        names = ['cls', 'Bck', '', 'close',
                 '7',   '8',   '9', '/',
                 '4',   '5',    '6', '*']
        
        positions = [(i, j) for i in range(3) for j in range(4)]

        # 创建按钮
        for positions, name in zip(positions, names):
            if name == '':
                continue
            button = QPushButton(name)
            grid.addWidget(button, *positions)

        self.move(100, 150)
        self.setWindowTitle('Calculator')
        self.show()

    def initUI_3(self):
        # 创建三个标签
        title = QLabel('title')
        autor = QLabel('autor')
        review = QLabel('review')

        # 创建两个行文本框和文本框
        titleEdit = QLineEdit()
        autorEdit = QLineEdit()
        reviewEdit = QTextEdit()

        grid = QGridLayout()
        # 设置组件之间的行间距
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)

        grid.addWidget(autor, 2, 0)
        grid.addWidget(autorEdit, 2, 1)
        
        grid.addWidget(review, 3, 0)
        # 如果我们向网格布局中增加一个组件，我们可以提供组件的跨行和跨列参数。
        # 在这个例子中，我们让 reviewEdit 组件跨了5行。
        grid.addWidget(reviewEdit, 3, 1, 5, 1)

        self.setLayout(grid)

        self.setGeometry(300, 300, 700, 400)
        self.setWindowTitle('Review')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())