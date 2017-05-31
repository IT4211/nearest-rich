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
from SQLiteDB import *
from matplotlibwidgetFile import SelectablePoint
from nearest_rich_form import *
from open_option_form import *
from rich_view_form import *
from richlibrary import *
import diskimage

# 디버깅 관련 메시지 출력
import cgitb
cgitb.enable(format='text')

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class OpenOption(QtGui.QDialog):
    def __init__(self, parent = None):
        super(OpenOption, self).__init__(parent)

        self.ui_opt = Ui_Open_Option()
        self.ui_opt.setupUi(self)
        self.ui_opt.pushButton_OK.clicked.connect(self.ok)
        self.ui_opt.pushButton_CANCEL.clicked.connect(self.cancel)
        self.exts = [self.ui_opt.radioButton_exe,
               self.ui_opt.radioButton_dll,
               self.ui_opt.radioButton_sys,
               self.ui_opt.radioButton_lib]
        # Default
        self.exts[0].setChecked(True)
        self.opt = None

    def ok(self):
        for ext in self.exts:
            if ext.isChecked():
                self.opt = ext.text()
        self.close()

    def cancel(self):
        self.close()

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

    def _Open(self):

        self.diskImg = QtGui.QFileDialog.getOpenFileName(self, "Open disk image file")
        # 디스크 이미지를 선택하지 않고 창을 닫거나 확인을 누른 경우
        if self.diskImg is None:
            return
        else:
            #img = str(self.diskImg)
            #pass
            img = unicode(self.diskImg)
            if img == u'':
                return
        # 정확히 디스크 이미지 파일을 지정했는지 검사
        #
        self.ui.textEdit_status.insertPlainText(img + _fromUtf8(" 디스크 이미지 파일 탐색 중...\n"))
        # 옵션 다이얼로그
        self.imgOption = OpenOption()
        self.imgOption.exec_()
        # 옵션을 선택하지 않고 닫거나 취소 버튼을 누른 경우 예외 처리
        ext = self.imgOption.opt
        if ext is None:
            return
        # 지정한 옵션에 맞는 cfg 파일 생성

        # 디스크 이미지가 존재하는 경로에 추출한 파일을 저장할 디렉토리 생성
        imgPath = os.path.split(img)[0]
        outDir = os.path.join(imgPath, 'output')
        os.mkdir(outDir)
        case = diskimage.tsk(img)
        try:
            case.LoadImage()                    # 디스크 이미지를 로드
        except Exception as e:
            self._WarningMessage(u"디스크 이미지를 로드할 수 없습니다.")
            self.ui.textEdit_status.insertPlainText(img + _fromUtf8(" 디스크 이미지 파일을 읽어들일 수 없습니다.\n"))
            self.ui.textEdit_status.insertPlainText(_fromUtf8("[-]ERROR: " + str(e) + "\n"))
            os.rmdir(outDir)
            return
        case.SetConf()                      # 조건 값을 읽어들임
        imgDir = case.OpenDirectory('/')    # 디스크 탐색을 시작, 시작 디렉토리를 지정
        case.ListDirectory(imgDir, [], [])  # 조건에 맞는 목록을 구함
        case.ExtractDirectoryEntry(False)   # 파일을 추출
        del case

        try:
            fileNames = os.listdir(outDir)
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
                filePath = os.path.join(outDir, fileName)

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
                except Exception as e:
                    self.ui.textEdit_status.insertPlainText(_fromUtf8(fileName + " 파일을 읽는 도중 오류가 발생하였습니다.\n"))
                    self.ui.textEdit_status.insertPlainText(_fromUtf8("[-]ERROR: " + str(e) + "\n"))
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

        self.x = [1, 2, 3, 4, 5, 6]
        x = self.x
        self.y = [1, 2, 3, 4, 5, 6]
        y = self.y
        self.labels = ['1', '2', '3', '4', '5', '6']
        labels = self.labels

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
        self.dbPath = QtGui.QFileDialog.getSaveFileName(self, "Save file as...", filter="db(*.db)")
        dbPath = unicode(self.dbPath) # 한글 인코딩 처리
        self.ui.textEdit_status.insertPlainText(_fromUtf8("데이터베이스 생성 중...\n"))

        db = sqlite_db(dbPath)
        db.create_sqlite()

        rowCount = self.ui.tableWidget_file.rowCount()
        for i in range(0, rowCount):
            fName = self.ui.tableWidget_file.item(i, 0)
            fPath = self.ui.tableWidget_file.item(i, 2)
            f = open(unicode(fPath.text()), 'rb')
            rd = f.read()
            md5 = hashlib.md5()
            md5.update(rd)
            hexmd5 = md5.hexdigest()
            md5value = str(hexmd5.upper())
            sha1 = hashlib.sha1()
            sha1.update(rd)
            hexsha1 = sha1.hexdigest()
            sha1value = str(hexsha1.upper())
            mcv = self.ui.tableWidget_file.item(i, 3)
            pid = self.ui.tableWidget_file.item(i, 4)
            cnt = self.ui.tableWidget_file.item(i, 5)
            db.insert_sqlite(fName.text(), fPath.text(), md5value, sha1value, mcv.text(), cnt.text(), pid.text())

        self.ui.textEdit_status.insertPlainText(_fromUtf8("데이터베이스 생성 완료\n"))

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
            if rh['err'] is not 0:
                e = err2str(rh['err'])
                raise Exception(e)
        except Exception as e:
            self._WarningMessage(str(e))
        else:
            # 파일 오픈해서 Rich Header 파싱 후 새로운 Dialog에서 출력
            # Modeless Dialogs
            rich_view = QtGui.QDialog(self)
            rich_view.ui = Ui_Dialog_rich_view()
            rich_view.ui.setupUi(rich_view)
            rich_view.setAttribute(QtCore.Qt.WA_DeleteOnClose)

            for cmpid in rh['cmpids']:
                mcv = cmpid['mcv']
                cnt = cmpid['cnt']
                pid = cmpid['pid']
                rowPosition = rich_view.ui.tableWidget_rich_view.rowCount()
                rich_view.ui.tableWidget_rich_view.insertRow(rowPosition)
                rich_view.ui.tableWidget_rich_view.setItem(rowPosition, 0, QtGui.QTableWidgetItem(str(mcv)))
                rich_view.ui.tableWidget_rich_view.setItem(rowPosition, 1, QtGui.QTableWidgetItem(str(cnt)))
                rich_view.ui.tableWidget_rich_view.setItem(rowPosition, 2, QtGui.QTableWidgetItem(str(pid)))

            rich_view.show()

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