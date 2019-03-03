#!usr/bin/python3
#-*- coding:utf-8 -*-

from PyQt5 import QtCore 
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton, QCheckBox
import sys 

class CustWidget( QWidget ): 
    def __init__(self, parent=None): 
        super(CustWidget, self).__init__(parent) 
        self.okButton = QPushButton("OK", self) 
        self.checkbox = QCheckBox("set title", self)
        #使用setObjectName设置对象名称 
        self.okButton.setObjectName("okButton") 
        self.checkbox.setObjectName("checkbox")
        layout = QHBoxLayout() 
        layout.addWidget(self.okButton) 
        layout.addWidget(self.checkbox)
        self.setLayout(layout) 
        QtCore.QMetaObject.connectSlotsByName(self) 
        
    @QtCore.pyqtSlot() 
    def on_okButton_clicked(self): 
        print( "单击了OK按钮") 

    @QtCore.pyqtSlot(int)
    def on_checkbox_stateChanged(self, state):
        print("checkbox的状态时%d"%state)
        
if __name__ == "__main__": 
    app = QApplication(sys.argv) 
    win = CustWidget() 
    win.show() 
    app.exec_()