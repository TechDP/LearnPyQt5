#!usr/bin/python3
#-*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QComboBox, QLabel

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.lable_Sysctrl = QLabel('Ubuntu', self)

        self.combox_Sysctrl = QComboBox(self)
        self.combox_Sysctrl.addItem('Ubuntu')
        self.combox_Sysctrl.addItem('Arch')
        self.combox_Sysctrl.addItem('Debian')
        self.combox_Sysctrl.addItem('Gentoo')

        self.combox_Sysctrl.move(50, 50)
        self.lable_Sysctrl.move(50, 150)
        self.combox_Sysctrl.activated[str].connect(self.onActive)

        self.setGeometry(20, 50, 600, 400)
        self.setWindowTitle('Combox')
        self.show()

    def onActive(self, text):
        self.lable_Sysctrl.setText(text)
        self.lable_Sysctrl.adjustSize()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())