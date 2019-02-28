#!usr/bin/python3
#-*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QApplication

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.lable_line = QLabel(self)
        self.lineEdit1 = QLineEdit(self)
        self.lineEdit1.move(20, 20)
        self.lable_line.move(20, 50)

        self.lineEdit1.textChanged[str].connect(self.onChanged)

        self.setGeometry(20, 50, 600, 400)
        self.setWindowTitle('Single LineEdit')
        self.show()

    def onChanged(self, text):
        self.lable_line.setText(text)
        self.lable_line.adjustSize()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())