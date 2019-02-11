from PyQt4 import QtGui, QtCore
from raw_ui import tabel_ui
import sys
from myDB import eksekusi
import dialogItem

h = (
    "Kode",
    "Nama",
    "Model",
    "Harga",
    "Ada"
    )
class Main(QtGui.QMainWindow,tabel_ui.Ui_MainWindow):
    def __init__(self,parent = None):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle('Tabel Barang')
        self.aksi()
        self.formNormal()
        self.isiTabel()

    def isiTabel(self):
        sql = "SELECT kode, nama, model, harga, ada FROM barang"
        bar, jum = eksekusi(sql)
        self.tableWidget.setRowCount(jum)
        for data in range(jum):
            kode = bar[data][0]
            nama = bar[data][1]
            model = bar[data][2]
            harga = format(bar[data][3],',.2f')
            if bar[data][4] == 1:
                ada = "Yes"
            else:
                ada = "-"

            teks  = (kode, nama, model, harga, ada)
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
        app = dialogItem.Main(kode = kode)
        app.exec_()
        self.isiTabel()

    def onTambahKlik(self):
        app = dialogItem.Main()
        app.exec_()
        self.isiTabel()

    def warnaTabel(self):
        r = self.tableWidget.rowCount()
        for i in range(r):
            self.tableWidget.item(i, 3).setTextAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.tableWidget.resizeColumnsToContents()
    
    
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    form = Main()
    form.show()
    sys.exit(app.exec_())