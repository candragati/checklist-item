from PyQt4 import QtGui, QtCore
import sys
from raw_ui import report_ui
import reportInput
from myDB import eksekusi,joss

h1 = ("Kode","Nama","Harga Total", "Harga Jual")
h2 = ("Kode","Nama","Qty","Harga","Subtotal")
class Main(QtGui.QMainWindow, report_ui.Ui_MainWindow):
    def __init__(self,parent = None):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        self.aksi()
        self.setWindowTitle("Laporan")
        self.tableWidgetUsaha.setColumnCount(len(h1))
        self.tableWidgetUsaha.setHorizontalHeaderLabels(h1)
        self.tableWidgetItem.setColumnCount(len(h2))
        self.tableWidgetItem.setHorizontalHeaderLabels(h2)
        self.isiTabel()
        self.warnaTabel()

    def warnaTabel(self):
        r = self.tableWidgetUsaha.rowCount()
        for i in range(r):
            self.tableWidgetUsaha.item(i, 2).setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
            self.tableWidgetUsaha.item(i, 3).setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)            
        self.tableWidgetUsaha.resizeColumnsToContents()

    def warnaTabelItem(self):
        r2 = self.tableWidgetItem.rowCount()
        for i in range(r2):
            self.tableWidgetItem.item(i, 2).setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
            self.tableWidgetItem.item(i, 3).setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)            
            self.tableWidgetItem.item(i, 4).setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.tableWidgetItem.resizeColumnsToContents()

    def isiTabel(self):
        sql = "SELECT kodeProduk, nama, hargaTotal, hargaJual FROM report, produk WHERE kodeProduk = kode"
        bar, jum = eksekusi(sql)
        self.tableWidgetUsaha.setRowCount(jum)
        for i in range(jum):
            kodeItem = bar[i][0]
            nama = bar[i][1]
            hargaTotal = format(bar[i][2],',.2f')
            hargaJual = format(bar[i][3],',.2f')
            
            teks = (kodeItem, nama, hargaTotal, hargaJual)
            for c in range(len(teks)):
                item = QtGui.QTableWidgetItem()
                item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)                    
                item.setToolTip(teks[c])
                item.setText(teks[c])
                self.tableWidgetUsaha.setItem(i, c, item)
        self.warnaTabel()

    def aksi(self):
        self.actionTambah.triggered.connect(self.onTambah)
        self.tableWidgetUsaha.itemClicked.connect(self.onTabelKlik)
        self.tableWidgetUsaha.itemSelectionChanged.connect(self.onTabelKlik)
        self.tableWidgetUsaha.doubleClicked.connect(self.onTabelEdit)

    def onTabelEdit(self):
        r = self.tableWidgetUsaha.currentRow()
        kodeProduk = self.tableWidgetUsaha.item(r,0).text()
        app = reportInput.Main(kodeProduk = kodeProduk)
        app.exec_()
        self.isiTabel()
        self.onTabelKlik()


    def onTabelKlik(self):
        r = self.tableWidgetUsaha.currentRow()
        kodeProduk = self.tableWidgetUsaha.item(r,0).text()
        sql  = "SELECT kodeItem, barang.nama, qty, reportDetail.harga, Subtotal FROM reportDetail,barang WHERE kodeProduk = '%s' AND kode = kodeItem"%kodeProduk
        bar, jum  = eksekusi(sql)
        self.tableWidgetItem.setRowCount(jum)
        for i in range(jum):
            kodeItem = bar[i][0]
            nama = bar[i][1]
            qty = format(bar[i][2],',.2f')
            harga = format(bar[i][3],',.2f')
            subtotal = format(bar[i][4],',.2f')
            
            teks = (kodeItem, nama, qty, harga, subtotal)
            for c in range(len(teks)):
                item = QtGui.QTableWidgetItem()
                item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)                    
                item.setToolTip(teks[c])
                item.setText(teks[c])
                self.tableWidgetItem.setItem(i, c, item)
        self.warnaTabelItem()


    def onTambah(self):
        app = reportInput.Main()
        app.exec_()
        self.isiTabel()
        self.onTabelKlik()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    form = Main()
    form.show()
    sys.exit(app.exec_())