# ----------------------------------------------------------------------------
# Nombre:       widget.py
# Autor:        Gabriel F
# GitHub:       https://github.com/gab98fra/
# Creado:       04 de Septiembre 2020
# Modificado:   05 de Octubre 2020
# Copyright:    (c) 2020 by Gabriel F, 2020
# ----------------------------------------------------------------------------

"""
    Ventana con los widgets más comunes para un desarrollo GUi

    Python 3.8.2
    PyQt 5.15.0

"""


from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt, QTranslator, QLocale, QLibraryInfo, pyqtSlot
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QGridLayout, QVBoxLayout, QHBoxLayout,
                             QLabel, QPushButton,  QComboBox, QSizePolicy, QCheckBox, QTreeWidget, QMessageBox)

import sys

class window(QMainWindow):
#Ventana principal
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Widgets más comunes by Gabriel F")
        self.setWindowIcon(QIcon("logo.png"))
        self.setMinimumSize(1200, 650)
        self.move(80,10)

        #Fuente
        font=QFont()
        font.setPointSize(9)
        self.setFont(font)


        #Objeto gráfico/Asignar a la ventana principal
        widget=widget1()
        self.setCentralWidget(widget)

class widget1(QWidget):
#widget

  def __init__(self,  parent=None):
    super(widget1, self).__init__(parent)

    self.initUI()

  def initUI(self):
  #Widgets

    #Variables-widget
    self.list_periodo=self.periodo()
        
    #Objeto: Qtable- numero de columnas/registros
    self.table_user=QTreeWidget()
    
    #Campos de la tabla
    

    #Combobox
    combobox1=QComboBox()
    combobox1.addItem("Hola")
    combobox1.addItem("Hola2")
    combobox2=QComboBox()
    combobox3=QComboBox()
    combobox4=QComboBox()
    
    #Layout vertical para combobox
    vertical_layout=QVBoxLayout()
    vertical_layout.addWidget(QLabel("Seleccionar periodo"))
    vertical_layout.addWidget(combobox1)
    vertical_layout.addWidget(QLabel("Seleccionar categoría"))
    vertical_layout.addWidget(combobox2)
    vertical_layout.addWidget(QLabel("Seleccionar subcategoría"))
    vertical_layout.addWidget(combobox3)
    vertical_layout.addWidget(QLabel("Seleccionar marca"))
    vertical_layout.addWidget(combobox4)
    vertical_layout.addStretch()#expandir

    horizontal_layout=QHBoxLayout()
    horizontal_layout.addWidget(QPushButton("Descargar"))
    horizontal_layout.addWidget(QPushButton("Imprimir"))
    horizontal_layout.addWidget(QPushButton("Limpiar"))
    horizontal_layout.addStretch()

    #Layout
    gridLayout1=QGridLayout()
    #Agregar al gridlayout1
    gridLayout1.addLayout(vertical_layout,   0, 0, 2, 1)#layout, (row, col)
    gridLayout1.addLayout(horizontal_layout, 0, 1, 1, 1)
    gridLayout1.addWidget(self.table_user,   1, 1, 1, 1)#widget 


    #Asignar al layout clase: widget
    self.setLayout(gridLayout1)

    #--------------Eventos combobox----------------------------------------
    combobox1.currentIndexChanged.connect(self.message)


    
  def message(self):

    print("Hola")

  def periodo(self):

      return 0
  


if __name__ == "__main__":
    
    #Inicio
    app = QApplication(sys.argv)

    #--------------Ajustes App-----------------    
    translate = QTranslator(app)#Traductor
    locale = QLocale.system().name()#Lugar
    path = QLibraryInfo.location(QLibraryInfo.TranslationsPath)#ruta traductor
    translate.load("qtbase_%s" % locale, path)
    app.installTranslator(translate)

    #Crear ventana principal
    window=window()
    window.show()

    #Fin
    sys.exit(app.exec_())