# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reportInput.ui'
#
# Created: Sun Feb 10 19:18:39 2019
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(622, 508)
        self.gridLayout_2 = QtGui.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tableWidget = QtGui.QTableWidget(Dialog)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 3, 0, 1, 2)
        self.label_4 = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 6, 0, 1, 1)
        self.lineEditProfit = QtGui.QLineEdit(Dialog)
        self.lineEditProfit.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEditProfit.setFont(font)
        self.lineEditProfit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEditProfit.setObjectName(_fromUtf8("lineEditProfit"))
        self.gridLayout.addWidget(self.lineEditProfit, 6, 1, 1, 1)
        self.comboBoxItem = QtGui.QComboBox(Dialog)
        self.comboBoxItem.setEnabled(False)
        self.comboBoxItem.setObjectName(_fromUtf8("comboBoxItem"))
        self.gridLayout.addWidget(self.comboBoxItem, 1, 0, 1, 1)
        self.lineEditNamaUsaha = QtGui.QLineEdit(Dialog)
        self.lineEditNamaUsaha.setEnabled(False)
        self.lineEditNamaUsaha.setObjectName(_fromUtf8("lineEditNamaUsaha"))
        self.gridLayout.addWidget(self.lineEditNamaUsaha, 0, 1, 1, 1)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setEnabled(False)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout_3.addWidget(self.pushButton, 0, 3, 1, 1)
        self.lineEditQty = QtGui.QLineEdit(Dialog)
        self.lineEditQty.setEnabled(False)
        self.lineEditQty.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEditQty.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEditQty.setObjectName(_fromUtf8("lineEditQty"))
        self.gridLayout_3.addWidget(self.lineEditQty, 0, 2, 1, 1)
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_3.addWidget(self.label, 0, 1, 1, 1)
        self.lineEditHarga = QtGui.QLineEdit(Dialog)
        self.lineEditHarga.setEnabled(False)
        self.lineEditHarga.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEditHarga.setObjectName(_fromUtf8("lineEditHarga"))
        self.gridLayout_3.addWidget(self.lineEditHarga, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 2, 1, 1, 1)
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.comboBoxUsaha = QtGui.QComboBox(Dialog)
        self.comboBoxUsaha.setObjectName(_fromUtf8("comboBoxUsaha"))
        self.gridLayout.addWidget(self.comboBoxUsaha, 0, 0, 1, 1)
        self.lineEditHargaJual = QtGui.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEditHargaJual.setFont(font)
        self.lineEditHargaJual.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEditHargaJual.setObjectName(_fromUtf8("lineEditHargaJual"))
        self.gridLayout.addWidget(self.lineEditHargaJual, 5, 1, 1, 1)
        self.label_3 = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)
        self.lineEditTotal = QtGui.QLineEdit(Dialog)
        self.lineEditTotal.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEditTotal.setFont(font)
        self.lineEditTotal.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEditTotal.setObjectName(_fromUtf8("lineEditTotal"))
        self.gridLayout.addWidget(self.lineEditTotal, 4, 1, 1, 1)
        self.label_2 = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)
        self.lineEditNamaItem = QtGui.QLineEdit(Dialog)
        self.lineEditNamaItem.setEnabled(False)
        self.lineEditNamaItem.setObjectName(_fromUtf8("lineEditNamaItem"))
        self.gridLayout.addWidget(self.lineEditNamaItem, 1, 1, 1, 1)
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.pushButtonSimpan = QtGui.QPushButton(Dialog)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/DESIGN/icon/32x32/disk.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonSimpan.setIcon(icon)
        self.pushButtonSimpan.setAutoDefault(False)
        self.pushButtonSimpan.setObjectName(_fromUtf8("pushButtonSimpan"))
        self.gridLayout_4.addWidget(self.pushButtonSimpan, 0, 1, 1, 1)
        self.pushButtonBatal = QtGui.QPushButton(Dialog)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/DESIGN/icon/32x32/cancel.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonBatal.setIcon(icon1)
        self.pushButtonBatal.setAutoDefault(False)
        self.pushButtonBatal.setObjectName(_fromUtf8("pushButtonBatal"))
        self.gridLayout_4.addWidget(self.pushButtonBatal, 0, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_4, 7, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label_4.setText(_translate("Dialog", "Profit", None))
        self.pushButton.setText(_translate("Dialog", "Input", None))
        self.label.setText(_translate("Dialog", "Qty", None))
        self.label_5.setText(_translate("Dialog", "Harga : ", None))
        self.label_3.setText(_translate("Dialog", "Harga Jual", None))
        self.label_2.setText(_translate("Dialog", "Total", None))
        self.pushButtonSimpan.setText(_translate("Dialog", "Simpan", None))
        self.pushButtonBatal.setText(_translate("Dialog", "Batal", None))

import icon_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

