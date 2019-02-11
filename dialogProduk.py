from PyQt4 import QtGui
from raw_ui import produk_ui
import sys,re
from myDB import joss,eksekusi
import myDB


class Main(QtGui.QDialog, produk_ui.Ui_Dialog):
    def __init__(self,parent = None, kode = None):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        self.aksi()       
        self.setWindowTitle("Tambah data produk")
        self.lineEditKode.setEnabled(True) 
        if kode != None:
            self.lineEditKode.setText(kode)
            self.onKodeEnter()

    def aksi(self):
        self.pushButtonSimpan.pressed.connect(self.onSimpan)
        self.lineEditKode.returnPressed.connect(self.onKodeEnter)
        self.lineEditNama.returnPressed.connect(self.onNamaEnter)
        self.pushButtonSimpan.setShortcut("Ctrl+S")

    def onNamaEnter(self):
        self.plainTextEdit.setEnabled(True)
        self.plainTextEdit.setFocus()
        self.pushButtonSimpan.setEnabled(True)

    def errorinput(self):
        QtGui.QMessageBox.warning(self,"Perhatian","Silahkan masukkan hanya huruf dan angka")

    def onKodeEnter(self):
        kode = str(self.lineEditKode.text()).upper()
        sql = "SELECT kode, nama, keterangan FROM produk WHERE kode = '%s'"%kode
        bar, jum = eksekusi(sql)
        if kode == "" or jum == 0:
            self.lineEditKode.setText("(menunggu...)")
            self.lineEditKode.setEnabled(False)
            self.lineEditNama.setEnabled(True)
            self.lineEditNama.setFocus()
        elif kode.isalnum()==False:
            self.errorinput()
        else:
            self.lineEditKode.setEnabled(False)
            self.lineEditNama.setEnabled(True)
            self.lineEditNama.setFocus()
            self.lineEditKode.setText(bar[0][0])
            self.lineEditNama.setText(bar[0][1])
            self.plainTextEdit.setPlainText(bar[0][2])

    def onSimpan(self):
        kode = str(self.lineEditKode.text())
        if kode == "(menunggu...)":
            self.buatKode()
            self.simpanLagi()            
        elif kode.isalnum()==False:
            self.errorinput()
            self.lineEditKode.setFocus()
        else:
            self.simpanLagi()

    def simpanLagi(self):
        kode = str(self.lineEditKode.text())
        nama = self.lineEditNama.text()
        keterangan = self.plainTextEdit.toPlainText()
        try:
            if self.lineEditKode.isEnabled()==False:
                joss("DELETE FROM produk WHERE kode = '%s'"%kode)
            sql = "INSERT INTO produk (kode,nama,keterangan) VALUES ('%s','%s','%s')"%(kode,nama,keterangan)            
            joss(sql)           
        except Exception,e:
            QtGui.QMessageBox.warning(self,"Perhatian!","Tidak dapat simpan data\n%s"%e)
        else:
            QtGui.QMessageBox.information(self,"information","Data berhasil disimpan")
        self.onClose()

    def buatKode(self):
        kode  = str(self.lineEditKode.text())
        nama = str(self.lineEditNama.text()).replace(" ","").replace("'","").upper()[:5]
        a=(re.sub('[, -:\".\']','',nama))                
        if self.lineEditKode.isEnabled():
            kode = kode
        else:
            sql = "SELECT kode FROM produk WHERE kode LIKE '%s%%'"%a
            bar, jum = eksekusi(sql)
            if jum == 0:
                self.lineEditKode.setText(a+str(1))
            else:
                self.lineEditKode.setText(a+str(jum+1))
        
    def onClose(self):
        self.close()

if __name__ == '__main__':
    app  = QtGui.QApplication(sys.argv)
    form = Main()
    form.show()
    sys.exit(app.exec_())