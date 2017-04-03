# -*- coding: utf-8 -*-
"""
@Author : Lee Seonho (horensic)
@E-mail : horensic@gmail.co.kr
"""

import os, sys
from PyQt4 import QtGui, QtCore
from Logging import ForensicLog
from nearest_rich_form import *
from richheader import RichHeader

import cgitb
cgitb.enable(format='text')

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class NearestRich(QtGui.QMainWindow):

    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionOpen.triggered.connect(self._Open)
        self.ui.actionOpen_Dir.triggered.connect(self._OpenDir)
        self.ui.actionStart_Analysis.triggered.connect(self._StartAnalysis)
        self.ui.listWidget_file.itemDoubleClicked.connect(self.ItemClicked)

    def _DrawChart(self):
        pass

    def _Open(self):
        self.diskImg = QtGui.QFileDialog.getOpenFileName(self, "Open disk image file")
        # 디스크 이미지를 선택하지 않고 창을 닫는 경우
        if self.diskImg is None:
            return

    def _OpenDir(self):
        # PE 파일 세트가 존재하는 디렉토리 경로
        self.directory = QtGui.QFileDialog.getExistingDirectory(self, "Select directory")
        self.ui.textEdit_status.insertPlainText(_fromUtf8(self.directory + " 디렉토리 탐색 중...\n"))
        # 디렉토리를 선택하지 않고 창을 닫는 경우
        if self.directory is None:
            return
        fileNames = os.listdir(self.directory)
        # 이전에 있던 목록을 지움
        self.ui.listWidget_file.clear()
        for fileName in fileNames:
            filePath = os.path.join(str(self.directory), fileName)

            # TODO: 나중에 옵션으로 recursive하게 탐색하게 할 것인지 지정
            # 파일 목록 중 디렉토리가 존재하는 경우 continue
            if os.path.isdir(filePath):
                continue

            try:
                fp = open(filePath, 'r')
                mzSignature = fp.read(2)

                if mzSignature == 'MZ': # 0x4D5A
                    self.ui.listWidget_file.addItem(fileName)
                else:
                    pass
            except:
                oLog.writeLog("ERROR", "File Read Failure: " + fileName)
                exit(0)
            else:
                fp.close()
        fileCount = self.ui.listWidget_file.count()
        self.ui.textEdit_status.insertPlainText(_fromUtf8("분석 대상 파일 " + str(fileCount) + "개를 모두 읽어들였습니다.\n"))

    def _StartAnalysis(self):
        pass

    def ItemClicked(self, item):
        print item.text()
        pass

    def _WarningMessage(self, msg):
        print "[Warning] ", msg
        wmsg = QtGui.QMessageBox()
        wmsg.setIcon(QtGui.QMessageBox.Warning)
        wmsg.setText(msg)
        wmsg.setWindowTitle("Warning")
        wmsg.setStandardButtons(QtGui.QMessageBox.Ok)
        wmsg.exec_()


if __name__ == "__main__":

    logPath = os.path.join(os.getcwd(), "nearest_rich.log")
    oLog = ForensicLog(logPath)

    oLog.writeLog("INFO", "Nearest Rich Started")

    app = QtGui.QApplication(sys.argv)
    Nearest_Rich = NearestRich()
    Nearest_Rich.show()
    del oLog
    app.exec_()