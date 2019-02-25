#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit,
    QInputDialog, QApplication, QFrame, QColorDialog, 
    QVBoxLayout, QSizePolicy, QLabel, QFontDialog, 
    QAction, QFileDialog, QTextEdit, QMainWindow)
from PyQt5.QtGui import QColor, QIcon

class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        
        # 创建一个按钮
        self.button1 = QPushButton('Dialog', self)
        self.button1.move(20, 20)
        # 点击时连接到 showDialog()
        self.button1.clicked.connect(self.showDialog)

        # 创建一个文本框
        self.le = QLineEdit(self)
        self.le.move(130, 20)

        # 初始化 QtGuiQFrame 组件的背景颜色
        col = QColor(0, 0, 0)
        # 创建一个按钮连接 showDialogSetColor()
        self.buttonSetColor = QPushButton('Set coler', self)
        self.buttonSetColor.move(20, 100)
        self.buttonSetColor.clicked.connect(self.showDialogSetColor)

        # 创建一个颜色框
        self.frm = QFrame(self)
        self.frm.setStyleSheet("QWidget { background-color: %s }" % col.name())
        self.frm.setGeometry(130, 100, 100, 100)

        vbox = QVBoxLayout()
        self.buttonSetFont = QPushButton('Set Font', self)
        self.buttonSetFont.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.buttonSetFont.move(20, 250)
        self.buttonSetFont.clicked.connect(self.showDialogSetFont)
        vbox.addWidget(self.buttonSetFont)

        self.label1 = QLabel('Knowledge only matters', self)
        self.label1.move(130, 250)
        
        self.textEdit1 = QTextEdit()
        self.setCentralWidget(self.textEdit1)
        self.statusBar()

        openFile = QAction(QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+o')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialogOpenFile)

        menuber = self.menuBar()
        fileMenu = menuber.addMenu('&File')
        fileMenu.addAction(openFile)
        
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('Input dialog')
        self.show()

    def showDialog(self):
        # 设置对话框的标题和提示语
        # 这一行会显示一个输入对话框。
        # 第一个字符串参数是对话框的标题，
        # 第二个字符串参数是对话框内的消息文本。
        # 对话框返回输入的文本内容和一个布尔值。
        # 如果我们点击了Ok按钮，布尔值就是true，反之布尔值是false
        # （注：也只有按下Ok按钮时，返回的文本内容才会有值）。
        text, ok = QInputDialog.getText(self, 'Input Dialog', 
            'Enter your name:')
        
        # 如果点 ok ，设置 le 的内容为输入内容
        if ok:
            self.le.setText(str(text))

    def showDialogSetColor(self):
        # 弹出颜色选择框
        col = QColorDialog.getColor()
        if col.isValid():
            # 设置颜色框的颜色
            self.frm.setStyleSheet("QWidget { background-color: %s }" % col.name())

    def showDialogSetFont(self):
        # 在这儿我们弹出一个字体对话框。
        # getFont()方法返回字体名字和布尔值。
        # 如果用户点击了OK，布尔值为True；否则为False。
        font, ok = QFontDialog.getFont()
        if ok:
            self.label1.setFont(font)

    def showDialogOpenFile(self):
        # 弹出文件选择框。
        # 第一个字符串参数是getOpenFileName()方法的标题。
        # 第二个字符串参数指定了对话框的工作目录。默认的，文件过滤器设置成All files (*)。
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')

        if fname[0]:
            f = open(fname[0], 'r')

            with f:
                data = f.read()
                self.textEdit1.setText(data)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())