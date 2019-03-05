#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QComboBox, QPushButton, QGridLayout, QWidget

class MainUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.ComboBoxProduct = QComboBox(self)
        
        self.buttonAddLable = QPushButton("add", self)
        self.buttonAddLable.clicked.connect(self.AddLable)
        self.button2 = QPushButton("2", self)
        self.button3 = QPushButton("3", self)
        
        self.grid.addWidget(self.ComboBoxProduct, 1, 1)
        self.grid.addWidget(self.buttonAddLable, 1, 3)
        self.grid.addWidget(self.button3, 2, 2)
        self.grid.addWidget(self.button2, 2, 3)
        self.grid.setHorizontalSpacing(20)
        self.grid.setVerticalSpacing(10)
        self.grid.setContentsMargins(0, 0, 0, 0)
        self.ComboBoxProduct.addItem("1")
        self.ComboBoxProduct.addItem("2")
        self.setGeometry(20, 50, 600, 400)
        self.setWindowTitle('Explorer')

    def AddLable(self):
        print("Add Lable")
        self.buttonAddLable.move(100, 100)
        self.button_1 = QPushButton("1", self)
        self.grid.addWidget(self.button_1, 2, 1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainUI()
    ui.show()
    sys.exit(app.exec_())