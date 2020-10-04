# ----------------------------------------------------------------------------
# Nombre:       key.py
# Autor:        Gabriel F
# GitHub:       https://github.com/gab98fra/
# Creado:       03 de Septiembre 2020
# Modificado:   04 de Septiembre 2020
# Copyright:    (c) 2020 by Gabriel F, 2020
# ----------------------------------------------------------------------------

"""
    Evento: keyPressEvent y closeEvent

    Python 3.8.2
    PyQt 5.15.0

"""

from PyQt5.QtGui import QIcon, QFont 
from PyQt5.QtCore import Qt    
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLineEdit, QLabel, QMessageBox)


import sys


class event_key(QWidget):

    def __init__(self):

        super().__init__()
        self.setWindowTitle("Eventos PyQt5 by Gabriel F")
        self.setWindowIcon(QIcon("logo.png"))
        self.resize(400,400)
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint)
        
        #Focus a la ventana
        self.setFocus()
        
        self.initUI()


    def initUI(self):
    #-------------------------------Widgets------------------------------
        
        
        self.line_edit1=QLineEdit(self)
        self.line_edit1.move(80, 80)
        

        botton1=QPushButton("Asignar Focus a lineEdit" ,self)
        botton1.move(50, 30) 

        botton2=QPushButton("Asignar Focus a la ventana" ,self)
        botton2.move(200, 30) 
        
        self.label1=QLabel("Escriba cualquier letra en el teclado: ", self)
        self.label1.resize(350, 20)
        self.label1.move(80, 250)
        
        #Evento kepressevent en widgets personalizados
        self.line_edit1.keyPressEvent=self.keypressevent_lineedit

        #Eventos pushbutton
        botton1.clicked.connect(self.line_edit1.setFocus)#Focus a line_Edit1
        
    def keyPressEvent(self, event):
    #Evento asginada a la ventana

        #Obetener información del teclado
        press=event.text()

        self.label1.setText('Tecla presionado en la ventana: {0} '.format(press))

    def keypressevent_lineedit(self, event):
    #Evento asignada a la ventana
    #    
        #Obtener información del teclado
        press=event.text()
        self.label1.setText('Tecla presionado en line_edit:  {0} '.format(press))

    def closeEvent(self, event):
    #Evento cerrar ventana

        close = QMessageBox(self)
        close.setWindowTitle("¡Cerrar ventana!")
        close.setIcon(QMessageBox.Question)
        close.setText("¿Estás seguro que desea salir Ventana?   ")
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


