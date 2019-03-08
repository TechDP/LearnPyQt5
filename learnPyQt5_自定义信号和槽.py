#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import QObject, pyqtSignal

class QTypeSignal(QObject):
    # 生成一个信号
    sendmsg = pyqtSignal(object)

    def __init__(self):
        super().__init__()

    def run(self):
        # 发射信号的实现
        self.sendmsg.emit('Hello Pyqt5')

class QTypeSlot(QObject):
    def __init__(self):
        super().__init__()

    def get(self, msg):
        # 槽函数的实现
        print("QSlot get msg =>" + msg)
    
if __name__ == "__main__":
    send = QTypeSignal()
    slot = QTypeSlot()
    print("把信号绑定到槽上")
    # 绑定信号和槽
    send.sendmsg.connect(slot.get)
    send.run()

    print("解绑信号和槽")
    # 解绑信号和槽
    send.sendmsg.disconnect(slot.get)
    send.run()