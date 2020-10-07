# ----------------------------------------------------------------------------
# Nombre:       widget.py
# Autor:        Gabriel F
# GitHub:       https://github.com/gab98fra/
# Creado:       04 de Septiembre 2020
# Modificado:   06 de Octubre 2020
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
                             QLabel, QPushButton,  QComboBox, QTreeWidget, QMessageBox)

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

        #Objeto widget/Asignar a la ventana principal
        widget=widget1()
        self.setCentralWidget(widget)

class widget1(QWidget):
#widget

  def __init__(self,  parent=None):
    super(widget1, self).__init__(parent)

    self.initUI()

  def initUI(self):
  #----------------------Widgets-----------------------------

    #Variables   -  método (retorna combobox con valores)
    combobox_periodo=self.combobox_list_1()
    combobox_categoria=self.combobox_list_2()
    combobox_subcategoria=self.combobox_list_3()
    combobox_marca=self.combobox_list_4()
        
    #-------Objeto: QTreWidget-------------------
    self.table_user=QTreeWidget()
    self.table_user.setHeaderLabels(("Usuario", "Pass", "Nombre", "Apellido", "Fecha de Nacimiento"))
    
    #Formato
    self.model=self.table_user.model()

    for indice, ancho in enumerate((110, 150, 150, 160), start=0):
            self.model.setHeaderData(indice, Qt.Horizontal, Qt.AlignCenter, Qt.TextAlignmentRole)
            self.table_user.setColumnWidth(indice, ancho)

    self.table_user.setAlternatingRowColors(True)
    
    #----------Layout vertical para label y combobox--------
    vertical_layout=QVBoxLayout()
    vertical_layout.addWidget(QLabel("Seleccionar periodo"))
    vertical_layout.addWidget(combobox_periodo)
    vertical_layout.addWidget(QLabel("Seleccionar categoría"))
    vertical_layout.addWidget(combobox_categoria)
    vertical_layout.addWidget(QLabel("Seleccionar subcategoría"))
    vertical_layout.addWidget(combobox_subcategoria)
    vertical_layout.addWidget(QLabel("Seleccionar marca"))
    vertical_layout.addWidget(combobox_marca)
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
    combobox_periodo.currentIndexChanged.connect(self.message)
    combobox_categoria.currentIndexChanged.connect(self.message)
    combobox_subcategoria.currentIndexChanged.connect(self.message)
    combobox_marca.currentIndexChanged.connect(self.message)
    
  def message(self):

        msg=QMessageBox(self)
        msg.setWindowTitle("Mensaje")
        msg.setText("Es un mensaje")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

  def combobox_list_1(self):
    
    list_combobox=QComboBox()

    list_combobox.addItem("Periodo 1")
    list_combobox.addItem("Periodo 2")
    list_combobox.addItem("Periodo 3")
    
    return list_combobox

  def combobox_list_2(self):
    
    list_combobox=QComboBox()

    list_combobox.addItem("Categoría 1")
    list_combobox.addItem("Categoría 2")
    list_combobox.addItem("Categoría 3")
    
    return list_combobox

  def combobox_list_3(self):
    
    list_combobox=QComboBox()

    list_combobox.addItem("Subcategoría 1")
    list_combobox.addItem("Subcategoría 2")
    list_combobox.addItem("Subcategoría 3")
    
    return list_combobox

  def combobox_list_4(self):
    
    list_combobox=QComboBox()

    list_combobox.addItem("Marca 1")
    list_combobox.addItem("Marca 2")
    list_combobox.addItem("Marca 3")
    
    return list_combobox
    

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