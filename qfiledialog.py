# ----------------------------------------------------------------------------
# Nombre:       qfiledialog.py
# Autor:        Gabriel F
# GitHub:       https://github.com/gab98fra/
# Creado:       20 de Septiembre 2020
# Modificado:   20 de Septiembre 2020
# Copyright:    (c) 2020 by Gabriel F, 2020
# ----------------------------------------------------------------------------

from PyQt5.QtGui import QIcon, QFont 
from PyQt5.QtCore import Qt    
from PyQt5.QtWidgets import (QApplication, QDialog, QPushButton, QTextEdit, QLabel, QFileDialog)


import sys

"""
    Ejemplo de QFileDialog: Abrir y guardar un archivo txt

"""

class aplicacion(QDialog):

    def __init__(self):

        super().__init__()
        self.setWindowTitle("QFileDialog with PyQt5")
        self.setWindowIcon(QIcon("logo.png"))
        self.resize(500,600)
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint)
        self.initUI()

    def initUI(self):
    #Widgets

        label=QLabel("Abrir y guardar archivos txt", self)
        label.move(120, 20)

        pusbutton=QPushButton("Abrir un archivo", self)
        pusbutton.move(100,80)

        pusbutton1=QPushButton(self)
        pusbutton1.setText("Guardar un archivo")
        pusbutton1.move(300,80)

        self.textedit=QTextEdit(self)
        self.textedit.resize(460, 450)
        self.textedit.move(20, 120)

        #-------Funciones PushButton----------------
        pusbutton.clicked.connect(self.openFile)
        pusbutton1.clicked.connect(self.saveFile)

    def openFile(self):
    #Leer un archivo txt

        filename=QFileDialog.getOpenFileName(self, "Abrir archivo", "c:\\", "Archivos txt (*.txt)")

        if filename[0]:
        #Si existe directorio: c://users/documents/...

            #Abrir archivo
            f=open(filename[0], "r")

            with f:
                #Leer contenido del archivo
                data=f.read()
                #Imprimir la información del archivo
                self.textedit.setText(data)
    
    def saveFile(self):
    #Guardar archivo txt

        options=QFileDialog.Option()
        #Ventana distinta a la nativa
        options=QFileDialog.DontUseNativeDialog

        filesave, _ =QFileDialog.getSaveFileName(self, "Guardar archivo", "c:\\", "Archivos txt (*.txt)", options=options)

        #filesave ----> directorio

        f=open(filesave, 'w')
        with f:
            #Guardamos el archivo con la información de textedit
            f.write(self.textedit.toPlainText())#Indica texto plano

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    
    ventana = aplicacion()
    ventana.show()

    sys.exit(app.exec_())


