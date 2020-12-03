# ----------------------------------------------------------------------------
# Nombre:       browser.py
# Autor:        Gabriel F
# GitHub:       https://github.com/gab98fra/
# Creado:       07 de Noviembre 2020
# Modificado:   02 de Diciembre 2020
# Copyright:    (c) 2020 by Gabriel F, 2020
# ----------------------------------------------------------------------------

"""
    Browser sencillo permite visitar cualquier página web especificando la url

    Python 3.8.2
    PyQt 5.15.0
    PyQtWebEngine 5.15.1

"""

from PyQt5.QtGui import QIcon, QFont 
from PyQt5.QtCore import Qt, QUrl    
from PyQt5.QtWidgets import (QApplication, QWidget, QMessageBox, QGridLayout)
from PyQt5.QtWebEngineWidgets import QWebEngineView


import sys


class event_key(QWidget):

    def __init__(self):

        super().__init__()
        self.setWindowTitle("Browser by Gabriel F")
        self.setWindowIcon(QIcon("logo.png"))
        self.showMaximized()
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint)
        
        #Focus a la ventana
        self.setFocus()
        
        self.initUI()


    def initUI(self):
    #-------------------------------Widgets------------------------------
        
        layout=QGridLayout(self)


        #Variable por defecto
        default_url="https://webfomatica.com/"


        self.browser=QWebEngineView(self)
        self.browser.setGeometry(5,30, 700,700)
        self.browser.load(QUrl(default_url))
        self.browser.show()

        #Agregar al layout
        layout.addWidget(self.browser,   0, 0, 1, 1)#widget 

        #Agregar al layout de la clase
        self.setLayout(layout)

    
    def closeEvent(self, event):
    #Evento cerrar ventana

        close = QMessageBox(self)
        close.setWindowTitle("¡Cerrar ventana!")
        close.setIcon(QMessageBox.Question)
        close.setText("¿Estás seguro que desea salir de la ventana?   ")
        #Opciones
        botonSalir = close.addButton("Salir", QMessageBox.YesRole)
        botonCancelar = close.addButton("Cancelar", QMessageBox.NoRole)
                
        close.exec_()
                
        if close.clickedButton() == botonSalir:
            
            event.accept()

        else:
            
            event.ignore()

    

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    
    ventana = event_key()
    ventana.show()

    sys.exit(app.exec_())


