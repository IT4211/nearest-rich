# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\L.SeonHo\Documents\GitHub\nearest-rich\rich_view_form.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog_rich_view(object):
    def setupUi(self, Dialog_rich_view):
        Dialog_rich_view.setObjectName(_fromUtf8("Dialog_rich_view"))
        Dialog_rich_view.setWindowModality(QtCore.Qt.NonModal)
        Dialog_rich_view.resize(341, 300)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog_rich_view.sizePolicy().hasHeightForWidth())
        Dialog_rich_view.setSizePolicy(sizePolicy)
        Dialog_rich_view.setMinimumSize(QtCore.QSize(341, 300))
        Dialog_rich_view.setMaximumSize(QtCore.QSize(341, 300))
        Dialog_rich_view.setModal(False)
        self.tableWidget_rich_view = QtGui.QTableWidget(Dialog_rich_view)
        self.tableWidget_rich_view.setGeometry(QtCore.QRect(10, 10, 321, 281))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_rich_view.sizePolicy().hasHeightForWidth())
        self.tableWidget_rich_view.setSizePolicy(sizePolicy)
        self.tableWidget_rich_view.setMinimumSize(QtCore.QSize(10, 10))
        self.tableWidget_rich_view.setMaximumSize(QtCore.QSize(321, 281))
        self.tableWidget_rich_view.setAutoFillBackground(True)
        self.tableWidget_rich_view.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget_rich_view.setAlternatingRowColors(True)
        self.tableWidget_rich_view.setObjectName(_fromUtf8("tableWidget_rich_view"))
        self.tableWidget_rich_view.setColumnCount(3)
        self.tableWidget_rich_view.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_rich_view.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_rich_view.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_rich_view.setHorizontalHeaderItem(2, item)

        self.retranslateUi(Dialog_rich_view)
        QtCore.QMetaObject.connectSlotsByName(Dialog_rich_view)

    def retranslateUi(self, Dialog_rich_view):
        Dialog_rich_view.setWindowTitle(_translate("Dialog_rich_view", "Rich View", None))
        self.tableWidget_rich_view.setSortingEnabled(True)
        item = self.tableWidget_rich_view.horizontalHeaderItem(0)
        item.setText(_translate("Dialog_rich_view", "mCV", None))
        item = self.tableWidget_rich_view.horizontalHeaderItem(1)
        item.setText(_translate("Dialog_rich_view", "Count", None))
        item = self.tableWidget_rich_view.horizontalHeaderItem(2)
        item.setText(_translate("Dialog_rich_view", "ProdID", None))

