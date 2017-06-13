# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\L.SeonHo\Documents\GitHub\nearest-rich\open_option_form.ui'
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

class Ui_Open_Option(object):
    def setupUi(self, Open_Option):
        Open_Option.setObjectName(_fromUtf8("Open_Option"))
        Open_Option.resize(261, 243)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Open_Option.sizePolicy().hasHeightForWidth())
        Open_Option.setSizePolicy(sizePolicy)
        Open_Option.setMinimumSize(QtCore.QSize(261, 243))
        Open_Option.setMaximumSize(QtCore.QSize(261, 243))
        self.groupBox_extenstion = QtGui.QGroupBox(Open_Option)
        self.groupBox_extenstion.setGeometry(QtCore.QRect(20, 20, 221, 161))
        self.groupBox_extenstion.setObjectName(_fromUtf8("groupBox_extenstion"))
        self.radioButton_lib = QtGui.QRadioButton(self.groupBox_extenstion)
        self.radioButton_lib.setGeometry(QtCore.QRect(30, 120, 181, 16))
        self.radioButton_lib.setObjectName(_fromUtf8("radioButton_lib"))
        self.radioButton_exe = QtGui.QRadioButton(self.groupBox_extenstion)
        self.radioButton_exe.setGeometry(QtCore.QRect(30, 30, 181, 16))
        self.radioButton_exe.setObjectName(_fromUtf8("radioButton_exe"))
        self.radioButton_dll = QtGui.QRadioButton(self.groupBox_extenstion)
        self.radioButton_dll.setGeometry(QtCore.QRect(30, 60, 181, 16))
        self.radioButton_dll.setObjectName(_fromUtf8("radioButton_dll"))
        self.radioButton_sys = QtGui.QRadioButton(self.groupBox_extenstion)
        self.radioButton_sys.setGeometry(QtCore.QRect(30, 90, 181, 16))
        self.radioButton_sys.setObjectName(_fromUtf8("radioButton_sys"))
        self.pushButton_OK = QtGui.QPushButton(Open_Option)
        self.pushButton_OK.setGeometry(QtCore.QRect(20, 190, 101, 31))
        self.pushButton_OK.setObjectName(_fromUtf8("pushButton_OK"))
        self.pushButton_CANCEL = QtGui.QPushButton(Open_Option)
        self.pushButton_CANCEL.setGeometry(QtCore.QRect(140, 190, 101, 31))
        self.pushButton_CANCEL.setObjectName(_fromUtf8("pushButton_CANCEL"))

        self.retranslateUi(Open_Option)
        QtCore.QMetaObject.connectSlotsByName(Open_Option)

    def retranslateUi(self, Open_Option):
        Open_Option.setWindowTitle(_translate("Open_Option", "Diskimage Option", None))
        self.groupBox_extenstion.setTitle(_translate("Open_Option", "File extension", None))
        self.radioButton_lib.setText(_translate("Open_Option", "lib (Static Library)", None))
        self.radioButton_exe.setText(_translate("Open_Option", "exe (PE File Format)", None))
        self.radioButton_dll.setText(_translate("Open_Option", "dll (Dynamic Link Library)", None))
        self.radioButton_sys.setText(_translate("Open_Option", "sys (System File)", None))
        self.pushButton_OK.setText(_translate("Open_Option", "OK", None))
        self.pushButton_CANCEL.setText(_translate("Open_Option", "Cancel", None))

