# ----------------------------------------------------------------------------
# Nombre:       slots.py
# Autor:        Gabriel F
# GitHub:       https://github.com/gab98fra/
# Creado:       03 de Septiembre 2020
# Modificado:   04 de Septiembre 2020
# Copyright:    (c) 2020 by Gabriel F, 2020
# ----------------------------------------------------------------------------

"""
    Eventos y Focus PyQt5 
    Eventos: mousePressEvent y  clicked
    
    Python 3.8.2
    PyQt 5.15.0

"""

from PyQt5.QtGui import QIcon, QFont 
from PyQt5.QtCore import Qt    
from PyQt5.QtWidgets import (QApplication, QDialog, QPushButton, QLineEdit, QLabel, QMessageBox)


import sys


class slots(QDialog):

    def __init__(self):

        super().__init__()
        self.setWindowTitle("Eventos PyQt5 by Gabriel F")
        self.setWindowIcon(QIcon("logo.png"))
        self.resize(400,400)
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint)
        
        
        self.initUI()

    def initUI(self):
    #-------------------------------Widgets------------------------------

        label1=QLabel("User: ", self)
        label1.move(80, 40)#col, row
        self.lineedit1=QLineEdit(self)
        self.lineedit1.move(180, 40)

        label2=QLabel("Pasword: ", self)
        label2.move(80, 80)
        self.lineedit2=QLineEdit(self)
        self.lineedit2.move(180, 80)

        label3=QLabel("New Pasword: ", self)
        label3.move(80, 120)
        self.lineedit3=QLineEdit(self)
        self.lineedit3.move(180, 120)

        label4=QLabel("Dar click aquí y colocar Focus en lineedit2: ", self)
        label4.resize(150, 20)
        label4.move(80, 160)

        label5=QLabel("Presionar Enter en teclado: ", self)
        label5.resize(150, 20)
        label5.move(80, 200)

        self.pusbutton1=QPushButton("Aceptar", self)
        self.pusbutton1.move(120,350)

        self.pusbutton2=QPushButton(self)
        self.pusbutton2.setText("Cancelar y Salir ")
        self.pusbutton2.move(220,350)

    
        #-------Eventos: mousePressEvent----------------
        label4.mousePressEvent=self.click_label

        #-------Eventos: clicked----------------
        self.pusbutton1.clicked.connect(self.click_aceptar)
        self.pusbutton2.clicked.connect(self.close)

    def click_label(self, event):
        
        self.message("MousePressEvent", "Realizó click en Label y Focus se encuentra en lineedit2")
        self.lineedit2.setFocus()

    def click_aceptar(self):

        self.message("Clicked", "Realizó click en el botón Aceptar y Focus se encuentra en botón: Cancelar y Salir")
        self.pusbutton2.setFocus()


    def message(self, title, m):
    #Ventana mensaje

        msg=QMessageBox(self)
        msg.setWindowTitle(title)
        msg.setText(m)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    
    ventana = slots()
    ventana.show()

    sys.exit(app.exec_())


