from PyQt5 import uic
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
import sqlite3


class Example(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.run()

    def run(self):
        con = sqlite3.connect('coffee.db')
        cur = con.cursor()
        res = list(cur.execute('SELECT * FROM coffee'))
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setHorizontalHeaderLabels([der[0] for der in cur.description])
        self.tableWidget.setRowCount(1)
        for i in range(len(res)):
            line = list(res[i])
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j in range(len(line)):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(line[j])))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
