# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\L.SeonHo\Documents\GitHub\nearest-rich\nearest_rich_form.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1051, 693)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1051, 693))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.widget_matplotlib = QtGui.QWidget(self.centralwidget)
        self.widget_matplotlib.setGeometry(QtCore.QRect(10, 10, 761, 481))
        self.widget_matplotlib.setObjectName(_fromUtf8("widget_matplotlib"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1051, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget_filelist = QtGui.QDockWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget_filelist.sizePolicy().hasHeightForWidth())
        self.dockWidget_filelist.setSizePolicy(sizePolicy)
        self.dockWidget_filelist.setObjectName(_fromUtf8("dockWidget_filelist"))
        self.dockWidgetContents_3 = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidgetContents_3.sizePolicy().hasHeightForWidth())
        self.dockWidgetContents_3.setSizePolicy(sizePolicy)
        self.dockWidgetContents_3.setObjectName(_fromUtf8("dockWidgetContents_3"))
        self.gridLayout = QtGui.QGridLayout(self.dockWidgetContents_3)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.listWidget = QtGui.QListWidget(self.dockWidgetContents_3)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.gridLayout.addWidget(self.listWidget, 0, 0, 1, 1)
        self.dockWidget_filelist.setWidget(self.dockWidgetContents_3)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget_filelist)
        self.dockWidget_status = QtGui.QDockWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget_status.sizePolicy().hasHeightForWidth())
        self.dockWidget_status.setSizePolicy(sizePolicy)
        self.dockWidget_status.setObjectName(_fromUtf8("dockWidget_status"))
        self.dockWidgetContents_4 = QtGui.QWidget()
        self.dockWidgetContents_4.setObjectName(_fromUtf8("dockWidgetContents_4"))
        self.gridLayout_2 = QtGui.QGridLayout(self.dockWidgetContents_4)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.dockWidgetContents_4)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.gridLayout_2.addWidget(self.plainTextEdit, 0, 0, 1, 1)
        self.dockWidget_status.setWidget(self.dockWidgetContents_4)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dockWidget_status)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "nearest-rich", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.dockWidget_filelist.setWindowTitle(_translate("MainWindow", "File list", None))
        self.dockWidget_status.setWindowTitle(_translate("MainWindow", "status", None))

