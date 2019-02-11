# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'barang.ui'
#
# Created: Mon Feb 11 08:27:18 2019
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
        Dialog.resize(496, 297)
        self.gridLayout_2 = QtGui.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.lineEditNama = QtGui.QLineEdit(Dialog)
        self.lineEditNama.setEnabled(False)
        self.lineEditNama.setObjectName(_fromUtf8("lineEditNama"))
        self.gridLayout.addWidget(self.lineEditNama, 2, 1, 1, 1)
        self.lineEditModel = QtGui.QLineEdit(Dialog)
        self.lineEditModel.setEnabled(False)
        self.lineEditModel.setObjectName(_fromUtf8("lineEditModel"))
        self.gridLayout.addWidget(self.lineEditModel, 3, 1, 1, 1)
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 1)
        self.lineEditKelebihan = QtGui.QLineEdit(Dialog)
        self.lineEditKelebihan.setEnabled(False)
        self.lineEditKelebihan.setObjectName(_fromUtf8("lineEditKelebihan"))
        self.gridLayout.addWidget(self.lineEditKelebihan, 6, 1, 1, 1)
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 7, 0, 1, 1)
        self.lineEditKekurangan = QtGui.QLineEdit(Dialog)
        self.lineEditKekurangan.setEnabled(False)
        self.lineEditKekurangan.setObjectName(_fromUtf8("lineEditKekurangan"))
        self.gridLayout.addWidget(self.lineEditKekurangan, 7, 1, 1, 1)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.lineEditKode = QtGui.QLineEdit(Dialog)
        self.lineEditKode.setEnabled(False)
        self.lineEditKode.setObjectName(_fromUtf8("lineEditKode"))
        self.gridLayout_3.addWidget(self.lineEditKode, 0, 0, 1, 1)
        self.checkBox = QtGui.QCheckBox(Dialog)
        self.checkBox.setEnabled(False)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.gridLayout_3.addWidget(self.checkBox, 0, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 1, 1, 1, 1)
        self.pushButtonSimpan = QtGui.QPushButton(Dialog)
        self.pushButtonSimpan.setEnabled(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/DESIGN/icon/32x32/disk.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonSimpan.setIcon(icon)
        self.pushButtonSimpan.setAutoDefault(False)
        self.pushButtonSimpan.setObjectName(_fromUtf8("pushButtonSimpan"))
        self.gridLayout.addWidget(self.pushButtonSimpan, 8, 0, 1, 1)
        self.plainTextEdit = QtGui.QPlainTextEdit(Dialog)
        self.plainTextEdit.setEnabled(False)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.gridLayout.addWidget(self.plainTextEdit, 4, 1, 1, 1)
        self.lineEditHarga = QtGui.QLineEdit(Dialog)
        self.lineEditHarga.setEnabled(False)
        self.lineEditHarga.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEditHarga.setObjectName(_fromUtf8("lineEditHarga"))
        self.gridLayout.addWidget(self.lineEditHarga, 5, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.lineEditKode, self.lineEditNama)
        Dialog.setTabOrder(self.lineEditNama, self.lineEditModel)
        Dialog.setTabOrder(self.lineEditModel, self.plainTextEdit)
        Dialog.setTabOrder(self.plainTextEdit, self.lineEditHarga)
        Dialog.setTabOrder(self.lineEditHarga, self.lineEditKelebihan)
        Dialog.setTabOrder(self.lineEditKelebihan, self.lineEditKekurangan)
        Dialog.setTabOrder(self.lineEditKekurangan, self.pushButtonSimpan)
        Dialog.setTabOrder(self.pushButtonSimpan, self.checkBox)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Kode", None))
        self.label_2.setText(_translate("Dialog", "Model", None))
        self.label_7.setText(_translate("Dialog", "Nama", None))
        self.label_3.setText(_translate("Dialog", "Spesifikasi", None))
        self.label_4.setText(_translate("Dialog", "Harga", None))
        self.label_5.setText(_translate("Dialog", "Kelebihan", None))
        self.label_6.setText(_translate("Dialog", "Kekurangan", None))
        self.checkBox.setText(_translate("Dialog", "Ada", None))
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

