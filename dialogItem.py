from PyQt4 import QtGui
from raw_ui import barang_ui
import sys,re
from myDB import joss,eksekusi
import myDB


class Main(QtGui.QDialog, barang_ui.Ui_Dialog):
    def __init__(self,parent = None, kode = None):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        self.aksi()
        self.setWindowTitle("Tambah data barang")
        self.lineEditKode.setEnabled(True) 
        if kode != None:
            self.lineEditKode.setText(kode)
            self.onKodeEnter()

    def aksi(self):
        self.lineEditHarga.textEdited.connect(self.onHargaEdit)
        self.pushButtonSimpan.pressed.connect(self.onSimpan)
        self.lineEditKode.returnPressed.connect(self.onKodeEnter)
        self.lineEditNama.returnPressed.connect(self.onNamaEnter)
        self.pushButtonSimpan.setShortcut("Ctrl+S")
        self.lineEditModel.returnPressed.connect(self.onModelEnter)
        self.lineEditHarga.returnPressed.connect(self.onHargaEnter)
        self.lineEditKelebihan.returnPressed.connect(self.onKelebihanEnter)
        self.lineEditKekurangan.returnPressed.connect(self.onKekuranganEnter)
    
    def onHargaEnter(self):
        self.lineEditKelebihan.setEnabled(True)
        self.lineEditKelebihan.setFocus()

    def onKelebihanEnter(self):
        self.lineEditKekurangan.setEnabled(True)
        self.lineEditKekurangan.setFocus()

    def onKekuranganEnter(self):
        self.pushButtonSimpan.setEnabled(True)
        self.pushButtonSimpan.setFocus()

    def onModelEnter(self):
        self.plainTextEdit.setEnabled(True)
        self.plainTextEdit.setFocus()
        self.lineEditHarga.setEnabled(True)

    def onNamaEnter(self):
        self.lineEditModel.setEnabled(True)
        self.lineEditModel.setFocus()
        self.checkBox.setEnabled(True)

    def onHargaEdit(self,item):
        try:
            self.lineEditHarga.setText(format(int(item), ',.0f'))            
        except ValueError:
            a = item.replace(',', '')
            try:
                self.lineEditHarga.setText(format(int(a), ',.0f'))                
            except:
                self.lineEditHarga.backspace()
                if str(self.lineEditHarga.text()) == "":
                    self.lineEditHarga.setText('0')

    def errorinput(self):
        QtGui.QMessageBox.warning(self,"Perhatian","Silahkan masukkan hanya huruf dan angka")

    def onKodeEnter(self):
        kode = str(self.lineEditKode.text()).upper()
        sql = "SELECT kode,nama,model,spesifikasi,harga,kelebihan,kekurangan,ada FROM barang WHERE kode = '%s'"%kode
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
            self.lineEditKode.setText(kode)
            self.lineEditNama.setText(bar[0][1])
            self.lineEditModel.setText(bar[0][2])
            self.plainTextEdit.setPlainText(bar[0][3])
            self.lineEditHarga.setText(format(bar[0][4],',.2f'))
            self.lineEditKelebihan.setText(bar[0][5])
            self.lineEditKekurangan.setText(bar[0][6])
            self.checkBox.setChecked(bar[0][7])

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
        nama = str(self.lineEditNama.text())
        model = str(self.lineEditModel.text()            )
        spesifikasi = self.plainTextEdit.toPlainText()
        harga = str(self.lineEditHarga.text().replace(',',''))
        kelebihan = str(self.lineEditKelebihan.text())
        kekurangan = str(self.lineEditKekurangan.text())
        if self.checkBox.isChecked():
            ada = 1
        else:
            ada = 0
        sql = "INSERT INTO barang (kode,nama,model, spesifikasi, harga, kelebihan, kekurangan,ada) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s')"%(
            kode, nama, model, spesifikasi, harga, kelebihan, kekurangan, ada)

        try:                        
            if self.lineEditKode.isEnabled()==False:
                joss("DELETE FROM barang WHERE kode = '%s'"%kode)
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
            sql = "SELECT kode FROM usaha WHERE kode LIKE '%s%%'"%a
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