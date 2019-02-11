# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Mon Feb 11 08:25:56 2019
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
        MainWindow.resize(713, 352)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.mdiArea = QtGui.QMdiArea(self.centralwidget)
        self.mdiArea.setViewMode(QtGui.QMdiArea.TabbedView)
        self.mdiArea.setDocumentMode(True)
        self.mdiArea.setTabsClosable(True)
        self.mdiArea.setTabsMovable(True)
        self.mdiArea.setObjectName(_fromUtf8("mdiArea"))
        self.gridLayout.addWidget(self.mdiArea, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 713, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMaster = QtGui.QMenu(self.menubar)
        self.menuMaster.setObjectName(_fromUtf8("menuMaster"))
        self.menuTransaksi = QtGui.QMenu(self.menubar)
        self.menuTransaksi.setObjectName(_fromUtf8("menuTransaksi"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionProduk = QtGui.QAction(MainWindow)
        self.actionProduk.setObjectName(_fromUtf8("actionProduk"))
        self.actionBarang = QtGui.QAction(MainWindow)
        self.actionBarang.setObjectName(_fromUtf8("actionBarang"))
        self.actionCompare = QtGui.QAction(MainWindow)
        self.actionCompare.setObjectName(_fromUtf8("actionCompare"))
        self.menuMaster.addAction(self.actionProduk)
        self.menuMaster.addAction(self.actionBarang)
        self.menuTransaksi.addAction(self.actionCompare)
        self.menubar.addAction(self.menuMaster.menuAction())
        self.menubar.addAction(self.menuTransaksi.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.menuMaster.setTitle(_translate("MainWindow", "Master", None))
        self.menuTransaksi.setTitle(_translate("MainWindow", "Transaksi", None))
        self.actionProduk.setText(_translate("MainWindow", "Produk", None))
        self.actionBarang.setText(_translate("MainWindow", "Barang", None))
        self.actionCompare.setText(_translate("MainWindow", "Compare", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

