import sys
import os
from PyQt5 import QtWidgets, QtCore, QtGui

class DynamicallyAddComponents(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ComponentsCounter = 0
        self.LineSet = {}
        self.initUI()

    def initUI(self):
        self.QHBox = QtWidgets.QHBoxLayout(self)
        self.QVBoxPushButton = QtWidgets.QVBoxLayout(self)
        self.PushGroup = QtWidgets.QButtonGroup(self)

        self.PushAdd = QtWidgets.QPushButton("增加一个控件", self)
        self.PushGroup.addButton(self.PushAdd)
        self.QHBox.addWidget(self.PushAdd)
        self.QHBox.addLayout(self.QVBoxPushButton)
        self.PushAdd.clicked.connect(self.AddComponents)
        self.PushGroup.buttonClicked[int].connect(self.ShowPushButtonText)
        
        self.resize(900, 600)
        self.setWindowTitle("动态添加控件")
        
    def AddComponents(self):
        # print(self.ComponentsCounter)
        self.PushX = QtWidgets.QPushButton(str(self.ComponentsCounter))
        self.PushGroup.addButton(self.PushX)
        self.QVBoxPushButton.addWidget(self.PushX)

        self.LineX = QtWidgets.QLineEdit(self)
        self.LineX.setText(str(self.ComponentsCounter))
        self.QVBoxPushButton.addWidget(self.LineX)
        self.LineX.textChanged[str].connect(self.ShowLineEditText)
        self.LineSet[str(self.ComponentsCounter)] = self.LineX
        self.ComponentsCounter += 1

    def ShowPushButtonText(self, ButtonID):
        # print(ButtonID)
        print(self.PushGroup.button(ButtonID).text())
        if self.PushGroup.button(ButtonID).text() in self.LineSet:
            print(self.LineSet[self.PushGroup.button(ButtonID).text()].text())

    def ShowLineEditText(self, LineText):
        print(LineText)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    test = DynamicallyAddComponents()
    test.show()
    sys.exit(app.exec_())