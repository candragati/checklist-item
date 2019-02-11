from PyQt4 import QtGui, QtCore
import sys
from raw_ui import reportInput_ui
from myDB import eksekusi, joss

h  = ("Kode","Nama","Qty", "Harga", "Total")

class Main(QtGui.QDialog, reportInput_ui.Ui_Dialog):
    def __init__(self,parent = None, kodeProduk = None):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        self.aksi()
        self.isiUsaha()
        self.isiItem()
        self.tableWidget.setColumnCount(len(h))
        self.tableWidget.setHorizontalHeaderLabels(h)        
        self.normal()
        if kodeProduk != None:
            self.comboBoxUsaha.setCurrentIndex(self.comboBoxUsaha.findText(kodeProduk))
            self.comboBoxUsaha.setEnabled(False)
            self.CBUsahaEnter()

        else:
            self.comboBoxUsaha.setFocus()       

    def normal(self):
        self.tableWidget.setRowCount(0)            
        self.lineEditQty.setText('1')
        self.lineEditTotal.setText('0')
        self.lineEditHargaJual.setText('0')
        self.lineEditProfit.setText('0')

    def aksi(self):
        self.comboBoxUsaha.currentIndexChanged.connect(self.namaUsaha)
        self.comboBoxItem.currentIndexChanged.connect(self.namaItem)
        QtGui.QShortcut(QtGui.QKeySequence("Return"),self.comboBoxUsaha, self.CBUsahaEnter, context = QtCore.Qt.WidgetShortcut)
        QtGui.QShortcut(QtGui.QKeySequence("Enter"), self.comboBoxUsaha, self.CBUsahaEnter, context = QtCore.Qt.WidgetShortcut)
        QtGui.QShortcut(QtGui.QKeySequence("Return"),self.comboBoxItem, self.CBItemEnter, context = QtCore.Qt.WidgetShortcut)
        QtGui.QShortcut(QtGui.QKeySequence("Enter"), self.comboBoxItem, self.CBItemEnter, context = QtCore.Qt.WidgetShortcut)
        QtGui.QShortcut(QtGui.QKeySequence("Delete"), self.tableWidget, self.hapusBaris, context = QtCore.Qt.WidgetShortcut)
        self.lineEditQty.textEdited.connect(self.onQtyEdit)
        self.lineEditHargaJual.textEdited.connect(self.onHJEdit)
        self.lineEditQty.returnPressed.connect(self.onQtyEnter)
        self.pushButton.pressed.connect(self.onInput)
        self.pushButtonBatal.pressed.connect(self.onClose)
        self.pushButtonSimpan.pressed.connect(self.onSimpan)
        self.pushButtonSimpan.setShortcut("Ctrl+S")
        self.lineEditHargaJual.returnPressed.connect(self.onHargaJualEnter)

    def hapusBaris(self):
        r = self.tableWidget.currentRow()
        self.tableWidget.removeRow(r)
        self.hitung()
        self.hitungProfit()

    def onHargaJualEnter(self):
        self.pushButtonSimpan.setFocus()

    def onSimpan(self):
        kodeProduk = self.comboBoxUsaha.currentText()
        total = float(self.lineEditTotal.text().replace(',',''))
        hargaJual = float(self.lineEditHargaJual.text().replace(',',''))
        r = self.tableWidget.rowCount()
        if r != 0:
            try:
                if self.pushButtonSimpan.text() == 'Simpan':
                    sql = "INSERT INTO report (kodeProduk, hargaTotal, hargaJual) VALUES ('%s','%s','%s')"%(
                    kodeProduk, total, hargaJual)
                else:
                    sqlh = "DELETE FROM reportDetail WHERE kodeProduk = '%s'"%kodeProduk
                    joss(sqlh)
                    sql = "UPDATE report SET hargaTotal='%s', hargaJual='%s' WHERE kodeProduk = '%s'"%(
                    total, hargaJual, kodeProduk)
                joss(sql)

                for i in range(r):
                    kodeItem = self.tableWidget.item(i,0).text()
                    qty = float(self.tableWidget.item(i,2).text().replace(',',''))
                    harga = float(self.tableWidget.item(i,3).text().replace(',',''))
                    total = float(self.tableWidget.item(i,4).text().replace(',',''))
                    sqld = "INSERT INTO reportDetail (kodeProduk, kodeItem, qty, harga, subtotal) VALUES ('%s','%s','%s','%s','%s')"%(
                    kodeProduk, kodeItem, qty, harga, total)
                    joss(sqld)
            except Exception,e:
                QtGui.QMessageBox.warning(self,"Perhatian!","Tidak dapat menyimpan\n%s"%e)
            else:
                QtGui.QMessageBox.information(self,"Perhatian!","Data sudah disimpan!")
                self.onClose()
        else:
            QtGui.QMessageBox.warning(self,"Perhatian!","Tidak ada data yang akan disimpan")

    def onClose(self):
        self.close()

    def onInput(self):
        kode_pro  = str(self.comboBoxItem.currentText())
        nama = str(self.lineEditNamaItem.text())
        qty = str(self.lineEditQty.text().replace(',',''))    
        harga = str(self.lineEditHarga.text())
        total = format(float(harga.replace(',',''))*float(qty),',.2f')
        teks = (kode_pro, nama, qty, harga, total)
        sama = 0
        n = self.tableWidget.rowCount()
        for i in range(n):
            item = self.tableWidget.item(i, 0)
            if item is not None:
                if kode_pro == item.text():
                    sama = 1
                    baris = i+1

        if sama == 1:
            QtGui.QMessageBox.warning(self, "Perhatian", "Kode %s sudah ada yang sama di baris %i!" % (kode_pro,baris))
            self.tableWidget.setFocus()
            self.tableWidget.selectRow(baris-1)
        else:
            self.tableWidget.insertRow(n)        
            for i in range(len(teks)):                        
                item = QtGui.QTableWidgetItem()
                item.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                item.setToolTip(str(teks[i]))
                item.setText(str(teks[i]))
                self.tableWidget.setItem(n,i,item)
            self.hitung()
            self.hitungProfit()
        self.comboBoxItem.setEnabled(True)
        self.comboBoxItem.setFocus()
        self.pushButton.setEnabled(False)
        self.lineEditQty.setEnabled(False)
        self.lineEditQty.setText('1')

            

    def hitung(self):
        r = self.tableWidget.rowCount()
        total = 0
        for i in range(r):
            self.tableWidget.item(i, 2).setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
            self.tableWidget.item(i, 3).setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
            self.tableWidget.item(i, 4).setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
            harga = float(self.tableWidget.item(i,4).text().replace(',',''))
            total += harga
        self.lineEditTotal.setText(format(total,',.0f'))
        self.tableWidget.resizeColumnsToContents()

    def isiItem(self):
        sql = "SELECT kode FROM barang"
        bar, jum = eksekusi(sql)
        for i in range(jum):
            self.comboBoxItem.addItem(bar[i][0])

    def namaItem(self):
        kode = self.comboBoxItem.currentText()
        sql = "SELECT nama, harga FROM barang WHERE kode = '%s'"%kode
        bar, jum = eksekusi(sql)
        self.lineEditNamaItem.setText(bar[0][0])
        self.lineEditHarga.setText(format(bar[0][1],',.2f'))


    def isiUsaha(self):
        sql = "SELECT kode FROM produk"
        bar, jum = eksekusi(sql)
        for i in range(jum):
            self.comboBoxUsaha.addItem(bar[i][0])

    def namaUsaha(self):
        kode = self.comboBoxUsaha.currentText()
        sql = "SELECT nama FROM produk WHERE kode = '%s'"%kode
        bar, jum = eksekusi(sql)
        self.lineEditNamaUsaha.setText(bar[0][0])

    def CBUsahaEnter(self):
        kode = self.comboBoxUsaha.currentText()
        sqld = "SELECT kodeItem, nama, qty, reportDetail.harga, subtotal FROM reportDetail,barang WHERE kodeProduk = '%s' AND kode = kodeItem"%kode
        bard, jumd = eksekusi(sqld)
        if jumd == 0:
            self.normal()
            self.comboBoxUsaha.setEnabled(False)            
        else:
            self.comboBoxUsaha.setEnabled(False)
            self.pushButtonSimpan.setText('Update')
            sql = "SELECT hargaTotal, hargaJual FROM report WHERE kodeProduk = '%s'"%kode
            bar, jum = eksekusi(sql)
            self.lineEditTotal.setText(format(bar[0][0],',.2f'))
            self.lineEditHargaJual.setText(format(bar[0][1],',.0f'))            
            self.tableWidget.setRowCount(jumd)
            for i in range(jumd):
                kodeItem = bard[i][0]
                nama = bard[i][1]
                qty = format(bard[i][2],',.2f')
                harga = format(bard[i][3],',.2f')
                subtotal = format(bard[i][4],',.2f')
                teks = (kodeItem, nama, qty, harga,subtotal)
                for c in range(len(teks)):
                    item = QtGui.QTableWidgetItem()
                    item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)                    
                    item.setToolTip(teks[c])
                    item.setText(teks[c])
                    self.tableWidget.setItem(i, c, item)
            self.hitung()
            self.hitungProfit()
        self.comboBoxItem.setEnabled(True)
        self.comboBoxItem.setFocus()

    def CBItemEnter(self):
        self.comboBoxItem.setEnabled(False)
        self.lineEditQty.selectAll()
        self.lineEditQty.setEnabled(True)
        self.lineEditQty.setFocus()

    def hitungProfit(self):
        total = float(str(self.lineEditTotal.text().replace(',','')))
        hargaJual = float(str(self.lineEditHargaJual.text().replace(',','')))
        profit = hargaJual - total
        self.lineEditProfit.setText(format(profit,',.0f'))

    def onHJEdit(self,item):
        try:
            self.lineEditHargaJual.setText(format(int(item), ',.0f'))       
            self.hitungProfit()     
        except Exception:
            a = item.replace(',', '')
            try:
                self.lineEditHargaJual.setText(format(int(a), ',.0f'))                
                self.hitungProfit()
            except Exception:                
                self.lineEditHargaJual.backspace()
                if str(self.lineEditHargaJual.text()) == "":
                    self.lineEditHargaJual.setText('0')
                self.hitungProfit()

    def onQtyEdit(self,item):
        try:
            self.lineEditQty.setText(format(int(item), ',.0f'))            
        except ValueError:
            a = item.replace(',', '')
            try:
                self.lineEditQty.setText(format(int(a), ',.0f'))                
            except:
                self.lineEditQty.backspace()
                if str(self.lineEditQty.text()) == "":
                    self.lineEditQty.setText('0')

    def onQtyEnter(self):
        self.pushButton.setEnabled(True)
        self.pushButton.setFocus()

    


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    form = Main()
    form.show()
    sys.exit(app.exec_())