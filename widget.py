# ----------------------------------------------------------------------------
# Nombre:       widget.py
# Autor:        Gabriel F
# GitHub:       https://github.com/gab98fra/
# Creado:       04 de Septiembre 2020
# Modificado:   05 de Octubre 2020
# Copyright:    (c) 2020 by Gabriel F, 2020
# ----------------------------------------------------------------------------

"""
    Ventana con los widgets más comunes para un desarrollar GUI

    Python 3.8.2
    PyQt 5.15.0

"""


from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt, QTranslator, QLocale, QLibraryInfo
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
        
    #-------Objeto: Qtable-------------------
    self.table_user=QTreeWidget()
    #Campos de la tabla
    self.table_user.setHeaderLabels(("Usuario", "Pass", "Nombre", "Apellido", "Fecha de Nacimiento"))
    
    #Formato
    self.model=self.table_user.model()

    for indice, ancho in enumerate((110, 150, 150, 160), start=0):
            self.model.setHeaderData(indice, Qt.Horizontal, Qt.AlignCenter, Qt.TextAlignmentRole)
            self.table_user.setColumnWidth(indice, ancho)

    self.table_user.setAlternatingRowColors(True)
    
    #-------------Combobox------------------
    combobox1=QComboBox()
    combobox1.addItem("Periodo 1")
    combobox1.addItem("Periodo 2")
    combobox2=QComboBox()
    combobox2.addItem("Categoría 1")
    combobox2.addItem("Categoría 2")
    combobox3=QComboBox()
    combobox3.addItem("Sub-categoría 1")
    combobox3.addItem("Sub-categoría 1")
    combobox4=QComboBox()
    combobox4.addItem("Marca 1")
    combobox4.addItem("Marca 2")
    
    #----------Objeto Layout vertical para combobox--------
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

    #----------Objeto Layout vertical para QPushButton--------
    horizontal_layout=QHBoxLayout()
    horizontal_layout.addWidget(QPushButton("Descargar"))
    horizontal_layout.addWidget(QPushButton("Imprimir"))
    horizontal_layout.addWidget(QPushButton("Limpiar"))
    horizontal_layout.addStretch()

    #---------Objeto - Layout-----------------
    gridLayout1=QGridLayout()
    #Agregar al gridlayout1
    gridLayout1.addLayout(vertical_layout,   0, 0, 2, 1)#layout, (row, col)
    gridLayout1.addLayout(horizontal_layout, 0, 1, 1, 1)
    gridLayout1.addWidget(self.table_user,   1, 1, 1, 1)#widget 

    #Asignar al layout clase widget
    self.setLayout(gridLayout1)

    #--------------Eventos combobox----------------------------------------
    combobox1.currentIndexChanged.connect(self.message)
    combobox2.currentIndexChanged.connect(self.message)
    combobox3.currentIndexChanged.connect(self.message)
    combobox4.currentIndexChanged.connect(self.message)
    
  def message(self):

        msg=QMessageBox(self)
        msg.setWindowTitle("Mensaje")
        msg.setText("Es un mensaje")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

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