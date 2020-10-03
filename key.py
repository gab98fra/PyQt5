# ----------------------------------------------------------------------------
# Nombre:       key.py
# Autor:        Gabriel F
# GitHub:       https://github.com/gab98fra/
# Creado:       03 de Septiembre 2020
# Modificado:   03 de Septiembre 2020
# Copyright:    (c) 2020 by Gabriel F, 2020
# ----------------------------------------------------------------------------

"""
    Evento: keyPressEvent

    Python 3.8.2
    PyQt 5.15.0

"""

from PyQt5.QtGui import QIcon, QFont 
from PyQt5.QtCore import Qt    
from PyQt5.QtWidgets import (QApplication, QDialog, QPushButton, QLineEdit, QLabel, QMessageBox)


import sys


class event_key(QDialog):

    def __init__(self):

        super().__init__()
        self.setWindowTitle("Eventos PyQt5")
        self.setWindowIcon(QIcon("logo.png"))
        self.resize(400,400)
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint)
        
        
        self.initUI()

    def initUI(self):
    #-------------------------------Widgets------------------------------
        

        self.label1=QLabel("Escriba cualquier letra en el teclado: ", self)
        self.label1.resize(150, 20)
        self.label1.move(80, 160)


    def keyPressEvent(self, event):
        
        press=event.text()
        self.label1.setText('Tecla presionado: '+ press )


if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    
    ventana = event_key()
    ventana.show()

    sys.exit(app.exec_())


