#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QComboBox, QPushButton

class MainUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.ComboBoxProduct = QComboBox(self)
        self.ComboBoxProduct.move(20, 20)
        self.buttonAddLable = QPushButton("add", self)
        self.buttonAddLable.clicked.connect(self.AddLable)
        self.buttonAddLable.move(20, 50)

        self.ComboBoxProduct.addItem("1")
        self.ComboBoxProduct.addItem("2")
        self.setGeometry(20, 50, 600, 400)
        self.setWindowTitle('Explorer')

    def AddLable(self):
        print("Add Lable")
        self.buttonAddLable.move(100, 100)
        # self.button_1 = QPushButton("1", self)
        # self.button_1.move(50, 20)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainUI()
    ui.show()
    sys.exit(app.exec_())