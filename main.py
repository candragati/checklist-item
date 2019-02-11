from PyQt4 import QtGui
from raw_ui import main_ui
import barang
import produk
import report
import sys

class Main(QtGui.QMainWindow, main_ui.Ui_MainWindow):
    def __init__(self,parent  = None):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        self.aksi()
        self.showMaximized()

    def aksi(self):
        self.actionProduk.triggered.connect(self.onProduk)
        self.actionBarang.triggered.connect(self.onBarang)
        self.actionCompare.triggered.connect(self.onReport)

    def onReport(self):
        sub  = report.Main()
        self.mdiArea.addSubWindow(sub)
        sub.show()

    def onProduk(self):
        sub = produk.Main()
        self.mdiArea.addSubWindow(sub)
        sub.show()

    def onBarang(self):
        sub  = barang.Main()
        self.mdiArea.addSubWindow(sub)
        sub.show()


if __name__ == '__main__':
    app  = QtGui.QApplication(sys.argv)
    form = Main()
    form.show()
    sys.exit(app.exec_())
