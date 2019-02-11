# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'report.ui'
#
# Created: Sun Feb 10 22:10:43 2019
#      by: PyQt4 UI code generator 4.10.4
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
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tableWidgetUsaha = QtGui.QTableWidget(self.centralwidget)
        self.tableWidgetUsaha.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidgetUsaha.setTabKeyNavigation(False)
        self.tableWidgetUsaha.setAlternatingRowColors(True)
        self.tableWidgetUsaha.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableWidgetUsaha.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableWidgetUsaha.setObjectName(_fromUtf8("tableWidgetUsaha"))
        self.tableWidgetUsaha.setColumnCount(0)
        self.tableWidgetUsaha.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidgetUsaha, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.dockWidget = QtGui.QDockWidget(MainWindow)
        self.dockWidget.setMinimumSize(QtCore.QSize(800, 113))
        self.dockWidget.setObjectName(_fromUtf8("dockWidget"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.gridLayout_4 = QtGui.QGridLayout(self.dockWidgetContents)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.tableWidgetItem = QtGui.QTableWidget(self.dockWidgetContents)
        self.tableWidgetItem.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidgetItem.setTabKeyNavigation(False)
        self.tableWidgetItem.setAlternatingRowColors(True)
        self.tableWidgetItem.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableWidgetItem.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableWidgetItem.setObjectName(_fromUtf8("tableWidgetItem"))
        self.tableWidgetItem.setColumnCount(0)
        self.tableWidgetItem.setRowCount(0)
        self.gridLayout_3.addWidget(self.tableWidgetItem, 0, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget)
        self.actionTambah = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/DESIGN/icon/32x32/add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionTambah.setIcon(icon)
        self.actionTambah.setObjectName(_fromUtf8("actionTambah"))
        self.toolBar.addAction(self.actionTambah)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionTambah.setText(_translate("MainWindow", "Tambah", None))
        self.actionTambah.setShortcut(_translate("MainWindow", "Ctrl+N", None))

import icon_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

