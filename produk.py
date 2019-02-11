from PyQt4 import QtGui
from raw_ui import tabel_ui
import sys
from myDB import eksekusi
import dialogProduk

h = (
    "Kode",
    "Nama",
    "Keterangan"
    )
class Main(QtGui.QMainWindow,tabel_ui.Ui_MainWindow):
    def __init__(self,parent = None):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle('Tabel Jenis produk')
        self.aksi()
        self.formNormal()
        self.isiTabel()

    def isiTabel(self):
        sql = "SELECT kode, nama, keterangan FROM produk"
        bar, jum = eksekusi(sql)
        self.tableWidget.setRowCount(jum)
        for data in range(jum):
            kode = bar[data][0]
            nama = bar[data][1]
            keterangan = bar[data][2]
            teks  = (kode, nama, keterangan)
            for i in range(len(teks)):
                item = QtGui.QTableWidgetItem()
                item.setText(str(teks[i]))
                self.tableWidget.setItem(data, i, item)
        self.warnaTabel()

    def formNormal(self):        
        self.tableWidget.setColumnCount(len(h))
        self.tableWidget.setHorizontalHeaderLabels(h)

    def aksi(self):
        self.actionTambah.triggered.connect(self.onTambahKlik)
        self.tableWidget.doubleClicked.connect(self.onTabelEdit)

    def onTabelEdit(self):
        r = self.tableWidget.currentRow()
        kode = self.tableWidget.item(r,0).text()
        app = dialogProduk.Main(kode = kode)
        app.exec_()
        self.isiTabel()

    def onTambahKlik(self):
        app = dialogProduk.Main()
        app.exec_()
        self.isiTabel()

    def warnaTabel(self):
        self.tableWidget.resizeColumnsToContents()    
    
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    form = Main()
    form.show()
    sys.exit(app.exec_())