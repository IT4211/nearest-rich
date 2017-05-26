# -*- coding: utf8 -*-
"""
@Author : Seonho Lee (horensic)
@E-mail : horensic@gmail.co.kr
"""

import os
import csv
import hashlib
from PyQt4 import QtGui, QtCore
from Logging import ForensicLog
from matplotlibwidgetFile import SelectablePoint
from nearest_rich_form import *
from open_option_form import *
from richlibrary import *
import diskimage

import random

# 디버깅 관련 메시지 출력
import cgitb
cgitb.enable(format='text')

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class open_option(QtGui.QDialog):
    def __init__(self, parent = None):
        super(open_option, self).__init__(parent)

        self.ui_opt = Ui_Open_Option()
        self.ui_opt.setupUi(self)
        self.ui_opt.pushButton_OK.clicked.connect(self.ok)
        self.ui_opt.pushButton_CANCEL.clicked.connect(self.cancel)

    def ok(self):
        pass

    def cancel(self):
        return

class NearestRich(QtGui.QMainWindow):

    def __init__(self, parent = None):

        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionOpen.triggered.connect(self._Open)
        self.ui.actionOpen_Dir.triggered.connect(self._OpenDir)
        self.ui.actionStart_Analysis.triggered.connect(self._StartAnalysis)
        self.ui.actionExport_CSV.triggered.connect(self._ExportCSV)
        self.ui.actionExport_SQLiteDB.triggered.connect(self._ExportSQLiteDB)
        self.header = self.ui.tableWidget_file.horizontalHeader()
        self.header.setResizeMode(1, QtGui.QHeaderView.ResizeToContents)
        self.header.setResizeMode(2, QtGui.QHeaderView.ResizeToContents)
        self.header.setResizeMode(3, QtGui.QHeaderView.ResizeToContents)
        self.ui.tableWidget_file.cellDoubleClicked.connect(self.ItemClicked)
        # TODO: dock을 실수로 꺼버린 경우 다시 켤 수 있도록 View 메뉴 만들 것!

    def _DrawChart(self):
        pass

    def _Open(self):

        self.diskImg = QtGui.QFileDialog.getOpenFileName(self, "Open disk image file")
        # 디스크 이미지를 선택하지 않고 창을 닫거나 확인을 누른 경우
        if self.diskImg is None:
            return
        else:
            img = unicode(self.diskImg)
            if img == u'':
                return
        self.ui.textEdit_status.insertPlainText(img + _fromUtf8(" 디스크 이미지 파일 탐색 중...\n"))
        # 옵션 다이얼로그


        # 디스크 이미지가 존재하는 경로에 추출한 파일을 저장할 디렉토리 생성
        imgPath = os.path.split(img)[0]
        os.mkdir(os.path.join(imgPath, 'extract_file'))
        case = diskimage.tsk(img)
        #case.extract_directory_entry()
        del case

        try:
            fileNames = os.listdir(imgPath)
        except WindowsError as e:
            self._WarningMessage(str(e))
            exit(-1)
        else:
            # 테이블 비우기
            rowCount = self.ui.tableWidget_file.rowCount()
            while rowCount:
                self.ui.tableWidget_file.removeRow(rowCount - 1)
                rowCount -= 1

            for fileName in fileNames:
                filePath = os.path.join(imgPath, fileName)

                # 파일 목록 중 디렉토리가 존재하는 경우 continue
                if os.path.isdir(filePath):
                    continue
                try:
                    fp = open(filePath, 'r')
                    mzSignature = fp.read(2)

                    if mzSignature == 'MZ': # 0x4D5A
                        self.rowPosition = self.ui.tableWidget_file.rowCount()
                        self.ui.tableWidget_file.insertRow(self.rowPosition)
                        self.ui.tableWidget_file.setItem(self.rowPosition, 0, QtGui.QTableWidgetItem(_fromUtf8(fileName)))
                        self.ui.tableWidget_file.setItem(self.rowPosition, 2, QtGui.QTableWidgetItem(_fromUtf8(filePath)))
                    else:
                        pass
                except:
                    self.ui.textEdit_status.insertPlainText(_fromUtf8(fileName + " 파일을 읽는 도중 오류가 발생하였습니다.\n"))
                    exit(-1)
                else:
                    fp.close()
            fileCount = self.ui.tableWidget_file.rowCount()
            self.ui.textEdit_status.insertPlainText(_fromUtf8("분석 대상 파일 " + str(fileCount) + "개를 모두 읽어들였습니다.\n"))

    def _OpenDir(self):
        # PE 파일 세트가 존재하는 디렉토리 경로
        self.directory = QtGui.QFileDialog.getExistingDirectory(self, "Select directory")
        dir = unicode(self.directory) # 한글 인코딩 처리
        # 디렉토리를 선택하지 않고 창을 닫는 경우
        if self.directory is None or self.directory == u'':
            return
        self.ui.textEdit_status.insertPlainText(dir + _fromUtf8(" 디렉토리 탐색 중...\n"))
        try:
            fileNames = os.listdir(dir)
        except WindowsError as e:
            self._WarningMessage(str(e))
            exit(-1)
        else:
            # 테이블 비우기
            rowCount = self.ui.tableWidget_file.rowCount()
            while rowCount:
                self.ui.tableWidget_file.removeRow(rowCount - 1)
                rowCount -= 1

            for fileName in fileNames:
                filePath = os.path.join(dir, fileName)

                # TODO: 나중에 옵션으로 recursive하게 탐색하게 할 것인지 지정
                # 파일 목록 중 디렉토리가 존재하는 경우 continue
                if os.path.isdir(filePath):
                    continue
                try:
                    fp = open(filePath, 'r')
                    mzSignature = fp.read(2)

                    if mzSignature == 'MZ': # 0x4D5A
                        self.rowPosition = self.ui.tableWidget_file.rowCount()
                        self.ui.tableWidget_file.insertRow(self.rowPosition)
                        self.ui.tableWidget_file.setItem(self.rowPosition, 0, QtGui.QTableWidgetItem(_fromUtf8(fileName)))
                        self.ui.tableWidget_file.setItem(self.rowPosition, 2, QtGui.QTableWidgetItem(_fromUtf8(filePath)))
                        # 마지막 compid 파싱
                        mCV, ProdID, Count = self._ParseRich(filePath)
                        self.ui.tableWidget_file.setItem(self.rowPosition, 3, QtGui.QTableWidgetItem(str(mCV)))
                        self.ui.tableWidget_file.setItem(self.rowPosition, 4, QtGui.QTableWidgetItem(str(ProdID)))
                        self.ui.tableWidget_file.setItem(self.rowPosition, 5, QtGui.QTableWidgetItem(str(Count)))
                    else:
                        pass
                except IOError as e:
                    self.ui.textEdit_status.insertPlainText(_fromUtf8(str(fileName) + " 파일을 읽는 도중 오류가 발생하였습니다.\n"))
                    self.ui.textEdit_status.insertPlainText(_fromUtf8("[-]ERROR: " + str(e) + "\n"))
                    #return
                else:
                    fp.close()
            fileCount = self.ui.tableWidget_file.rowCount()
            self.ui.textEdit_status.insertPlainText(_fromUtf8("분석 대상 파일 " + str(fileCount) + "개를 모두 읽어들였습니다.\n"))

    def _StartAnalysis(self):
        self.ui.widget_matplotlib.canvas.axes.clear()

        x = [1, 1.2, 3, 4, 5, 6]
        y = [1, 1.2, 3, 4, 5, 6]
        labels = ['1', '2', '3', '4', '5', '6']

        self.sp = [SelectablePoint((x[i], y[i]), labels[i], self.ui.widget_matplotlib.canvas.fig) for i in range(len(x))]
        for i in range(len(x)):
            self.ui.widget_matplotlib.canvas.axes.add_artist(self.sp[i].point)

        self.ui.widget_matplotlib.canvas.draw()

    def _ExportCSV(self):
        self.csvPath = QtGui.QFileDialog.getSaveFileName(self, "Save file as...", filter="CSV(*.csv)")
        csvPath = unicode(self.csvPath) # 한글 인코딩 처리
        self.ui.textEdit_status.insertPlainText(_fromUtf8("CSV 파일 쓰는 중...\n"))
        with open(csvPath, 'wb') as csvStream:
            writer = csv.writer(csvStream, delimiter = ',', quoting = csv.QUOTE_ALL)
            writer.writerow(('Filename', 'Hash(MD5)', 'Hash(SHA-1)', 'Compids'))
            for row in range(self.ui.tableWidget_file.rowCount()):
                rowData = []
                fileNameItem = self.ui.tableWidget_file.item(row, 0)
                fileNameItem = unicode(fileNameItem.text())
                rowData.append(fileNameItem)
                filePathItem = self.ui.tableWidget_file.item(row, 2)
                filePathItem = unicode(filePathItem.text())
                try:
                    fItem = open(filePathItem, 'rb')
                except IOError as e:
                    self._WarningMessage(str(e))
                else:
                    try:
                        rdItem = fItem.read()
                    except IOError as e:
                        fItem.close()
                        self._WarningMessage(str(e))
                    else:
                        oMD5Hash = hashlib.md5()
                        oMD5Hash.update(rdItem)
                        hexMD5 = oMD5Hash.hexdigest()
                        MD5HashValue = hexMD5.upper()
                        rowData.append(MD5HashValue)

                        oSHA1Hash = hashlib.sha1()
                        oSHA1Hash.update(rdItem)
                        hexSHA1 = oSHA1Hash.hexdigest()
                        SHA1HashValue = hexSHA1.upper()
                        rowData.append(SHA1HashValue)

                    fItem.close()

                    rh = parse(filePathItem)
                    rowData.append(rh['cmpids'])

                writer.writerow(rowData)
        self.ui.textEdit_status.insertPlainText(_fromUtf8("CSV 파일 쓰기 완료\n"))

    def _ExportSQLiteDB(self):
        pass

    def _ParseRich(self, filepath):
        try:
            rh = parse(filepath)
            if rh['err'] is not 0:
                e = err2str(rh['err'])
                raise Exception(e)
        except Exception as e:
            self.ui.textEdit_status.insertPlainText(_fromUtf8(str(filepath) + "파일의 Rich 헤더를 읽는 도중 오류가 발생하였습니다.\n"))
            self.ui.textEdit_status.insertPlainText(_fromUtf8("[-]ERROR: " + str(e) + "\n"))
            return '-', '-', '-'
        else:
            lastCompid = rh['cmpids'][-1]
            mcv = lastCompid['mcv']
            cnt = lastCompid['cnt']
            pid = lastCompid['pid']
            del rh
            return mcv, pid, cnt

    @QtCore.pyqtSlot(int, int)
    def ItemClicked(self, row, col):
        item = self.ui.tableWidget_file.item(row, 2)
        itemPath = unicode(item.text()) # QString : u'\u####\u####' 형태로 저장되어 있는 상황
        itemPath = unicode(itemPath) # unicode() 처리를 2번 해줌으로써 한글 인코딩 처리
        try:
            rh = parse(itemPath)
            if type(rh) is not "dict":
                raise Exception

        except Exception as e:
            #print str(e)
            self._WarningMessage(str(e))
        else:
            print rh['cmpids']
            # 파일 오픈해서 Rich Header 파싱 후
            # 새로운 Dialog에서 출력
            """
            self.rich_view = rich_view()
            self.rich_view.set~~~
            self.rich_view.exec_()
            """

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