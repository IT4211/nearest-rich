# -*- coding: utf-8 -*-
"""
@Author : Lee Seonho (horensic)
@E-mail : horensic@gmail.co.kr
"""

import sys
from PyQt4 import QtGui, QtCore
from nearest_rich_form import *
import header_parser

class NearestRich(QtGui.QMainWindow):

    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def DrawBubbleChart(self):
        pass


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    Nearest_Rich = NearestRich()
    Nearest_Rich.show()
    app.exec_()

