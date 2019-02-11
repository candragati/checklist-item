# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'produk.ui'
#
# Created: Mon Feb 11 08:27:29 2019
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
        Dialog.resize(496, 224)
        self.gridLayout_2 = QtGui.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lineEditNama = QtGui.QLineEdit(Dialog)
        self.lineEditNama.setEnabled(False)
        self.lineEditNama.setObjectName(_fromUtf8("lineEditNama"))
        self.gridLayout.addWidget(self.lineEditNama, 2, 1, 1, 1)
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)
        self.label_8 = QtGui.QLabel(Dialog)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 3, 0, 1, 1)
        self.pushButtonSimpan = QtGui.QPushButton(Dialog)
        self.pushButtonSimpan.setEnabled(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/DESIGN/icon/32x32/disk.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonSimpan.setIcon(icon)
        self.pushButtonSimpan.setAutoDefault(False)
        self.pushButtonSimpan.setObjectName(_fromUtf8("pushButtonSimpan"))
        self.gridLayout.addWidget(self.pushButtonSimpan, 4, 0, 1, 1)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.lineEditKode = QtGui.QLineEdit(Dialog)
        self.lineEditKode.setEnabled(False)
        self.lineEditKode.setObjectName(_fromUtf8("lineEditKode"))
        self.gridLayout_3.addWidget(self.lineEditKode, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 1, 1, 1, 1)
        self.plainTextEdit = QtGui.QPlainTextEdit(Dialog)
        self.plainTextEdit.setEnabled(False)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.gridLayout.addWidget(self.plainTextEdit, 3, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.lineEditKode, self.lineEditNama)
        Dialog.setTabOrder(self.lineEditNama, self.plainTextEdit)
        Dialog.setTabOrder(self.plainTextEdit, self.pushButtonSimpan)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Kode", None))
        self.label_7.setText(_translate("Dialog", "Nama Produk", None))
        self.label_8.setText(_translate("Dialog", "Keterangan", None))
        self.pushButtonSimpan.setText(_translate("Dialog", "Simpan", None))

import icon_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

