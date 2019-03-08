#!usr/bin/python3
#-*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QTableView, QVBoxLayout
from PyQt5.QtGui import QStandardItemModel, QStandardItem


class Table(QWidget):
    def __init__(self, arg = None):
        super(Table, self).__init__(arg)
        self.setWindowTitle("QTaleView表格视图控件示例")
        self.resize(600, 400)
        self.model = QStandardItemModel(4, 4)
        self.model.setHorizontalHeaderLabels(['标题1', '标题2', 'title3', 'title4'])

        for row in range(10):
            for column in range(10):
                # 可以比创建时传入的参数的个数多，
                # 如果比创建时传入的参数的个数少，会补充空白的
                item = QStandardItem("row %s, column %s"%(row, column))
                self.model.setItem(row, column, item)

        self.tableView = QTableView()
        self.tableView.setModel(self.model)
        
        dlgLayout = QVBoxLayout()
        dlgLayout.addWidget(self.tableView)
        self.setLayout(dlgLayout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    table = Table()
    table.show()
    sys.exit(app.exec_())
        