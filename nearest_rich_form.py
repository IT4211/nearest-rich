# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nearest_rich_form.ui'
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
        self.menuAnalysis = QtGui.QMenu(self.menubar)
        self.menuAnalysis.setObjectName(_fromUtf8("menuAnalysis"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
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
        self.listWidget_file = QtGui.QListWidget(self.dockWidgetContents_3)
        self.listWidget_file.setObjectName(_fromUtf8("listWidget_file"))
        self.gridLayout.addWidget(self.listWidget_file, 0, 0, 1, 1)
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
        self.textEdit_status = QtGui.QTextEdit(self.dockWidgetContents_4)
        self.textEdit_status.setReadOnly(True)
        self.textEdit_status.setObjectName(_fromUtf8("textEdit_status"))
        self.gridLayout_2.addWidget(self.textEdit_status, 0, 0, 1, 1)
        self.dockWidget_status.setWidget(self.dockWidgetContents_4)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dockWidget_status)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionOpen_Dir = QtGui.QAction(MainWindow)
        self.actionOpen_Dir.setObjectName(_fromUtf8("actionOpen_Dir"))
        self.actionSave_As = QtGui.QAction(MainWindow)
        self.actionSave_As.setObjectName(_fromUtf8("actionSave_As"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionStart_Analysis = QtGui.QAction(MainWindow)
        self.actionStart_Analysis.setObjectName(_fromUtf8("actionStart_Analysis"))
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionOpen_Dir)
        self.menuFile.addAction(self.actionSave_As)
        self.menuAnalysis.addAction(self.actionStart_Analysis)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAnalysis.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "nearest-rich", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuAnalysis.setTitle(_translate("MainWindow", "Analysis", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.dockWidget_filelist.setWindowTitle(_translate("MainWindow", "File list", None))
        self.dockWidget_status.setWindowTitle(_translate("MainWindow", "status", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))
        self.actionOpen_Dir.setText(_translate("MainWindow", "Open Dir", None))
        self.actionSave_As.setText(_translate("MainWindow", "Save As..", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionStart_Analysis.setText(_translate("MainWindow", "Start Analysis", None))

