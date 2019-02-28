#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QWidget, QApplication, QHBoxLayout,
    QFrame, QSplitter, QStyleFactory)
from PyQt5.QtCore import Qt

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.hbox = QHBoxLayout(self)
        # 使用了一个样式框架，为了让框架组件之间的分割线看的明显。
        self.topleft = QFrame(self)
        self.topleft.setFrameShape(QFrame.StyledPanel)

        self.topRight = QFrame(self)
        self.topRight.setFrameShape(QFrame.StyledPanel)

        self.bottom = QFrame(self)
        self.bottom.setFrameShape(QFrame.StyledPanel)

        # 创建了一个分割框组件并且在这个分割框中添加进入两个框架组件。
        self.splitter1 = QSplitter(Qt.Horizontal)
        self.splitter1.addWidget(self.topleft)
        self.splitter1.addWidget(self.topRight)

        # 把第一个分割框添加进另一个分割框组件中。
        self.splitter2 = QSplitter(Qt.Vertical)
        self.splitter2.addWidget(self.splitter1)
        self.splitter2.addWidget(self.bottom)

        self.hbox.addWidget(self.splitter2)
        self.setLayout(self.hbox)


        self.setGeometry(20, 50, 600, 400)
        self.setWindowTitle('Splitter')
        self.show()

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())