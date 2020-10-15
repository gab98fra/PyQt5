# ----------------------------------------------------------------------------
# Nombre:       export.py
# Autor:        Gabriel F
# GitHub:       https://github.com/gab98fra/
# Creado:       14 de Octubre 2020
# Modificado:   14 de Octubre 2020
# Copyright:    (c) 2020 by Gabriel F, 2020
# ----------------------------------------------------------------------------

"""

    El siguiente scrip permite mostrar datos en una tabla, realizar vista previa de los datos, exportar a pdf
    e imprimir

    Python 3.8.2
    PyQt 5.15.0

"""


from PyQt5.QtGui import QFont, QIcon, QTextDocument
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter, QPrintPreviewDialog
from PyQt5.QtCore import (Qt, QTranslator, QLocale, QLibraryInfo, QFileInfo, QTextCodec, QByteArray, QTranslator, 
                            QLocale, QLibraryInfo)
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QFileDialog, QToolBar, QGridLayout, QVBoxLayout, 
                             QHBoxLayout, QLabel, QPushButton,  QComboBox, QTreeWidget, QTreeWidgetItem, QMessageBox)

import sys

class window(QMainWindow):
#Ventana principal

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exportar e imprimir datos by Gabriel F")
        self.setWindowIcon(QIcon("logo.png"))
        self.setMinimumSize(800, 650)
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
        
        #Objeto document
        self.document=QTextDocument()

        #Qpusbutton
        button_data=QPushButton("Mostrar datos", self)
        button1=QPushButton("Vista Previa", self)
        button2=QPushButton("Imprimir", self)
        button3=QPushButton("Exportar", self)
        button4=QPushButton("Limpiar", self)

        #-------Objeto: QTreWidget-------------------
        self.table_user=QTreeWidget()
        self.table_user.setHeaderLabels(("Id_Usuario", "Mes", "Nombre", "Estatus", "Fecha de alta"))
        
        #Formato
        self.model=self.table_user.model()

        for indice, ancho in enumerate((110, 150, 150, 160), start=0):
                self.model.setHeaderData(indice, Qt.Horizontal, Qt.AlignCenter, Qt.TextAlignmentRole)
                self.table_user.setColumnWidth(indice, ancho)

        self.table_user.setAlternatingRowColors(True)


        #----------Objeto Layout vertical para QPushButton--------
        horizontal_layout=QHBoxLayout()
        horizontal_layout.addWidget(button_data)
        horizontal_layout.addWidget(button1)
        horizontal_layout.addWidget(button2)
        horizontal_layout.addWidget(button3)
        horizontal_layout.addWidget(button4)
        horizontal_layout.addStretch()

        #---------Objeto - Layout-----------------
        gridLayout1=QGridLayout()
        #Agregar al gridlayout1
        gridLayout1.addLayout(horizontal_layout, 0, 1, 1, 1)
        gridLayout1.addWidget(self.table_user,   1, 1, 1, 1)#widget 

        #Asignar al layout clase widget
        self.setLayout(gridLayout1)

        #--------------Eventos qpushbutton----------------------------------------
        button_data.clicked.connect(self.data)          #data
        button1.clicked.connect(self.view)              #var_view previa
        button2.clicked.connect(self.print_document)    #imprimir
        button3.clicked.connect(self.pdf_export)        #exportar
        button4.clicked.connect(self.clear)             #limpiar
        

    def clear(self):
    #Limpiar tabla/documento
        
        self.table_user.clear()
        self.document.clear()


    def data (self):
    #Mostrar datos y objeto document

        data = [("1", "March", "Arnt", "Disabled", "10/23/2010"),
            ("2", "April", "Louis", "Enabled", "09/05/2020"),
            ("3", "June", "Steve", "Disabled", "02/15/2001"),
            ("4", "October", "Marcus", "Enabled", "01/13/2002"),
            ("5", "December", "John", "Enabled", "12/28/2018"),
        
                ]

        #Limpiar tabla/documento
        self.table_user.clear()
        self.document.clear()


        html_dato =''
        item_widget=[]

        for d in data:
        #Imprimir datos en la tabla
            
            self.table_user.insertTopLevelItems(0,[QTreeWidgetItem(self.table_user, d)])    

            html_dato += "<tr> <td>%s</td> <td>%s</td> <td>%s</td> <td>%s</td>  <td>%s</td> </tr>" %d
            item_widget.append(QTreeWidgetItem((str(d[0]), d[1], d[2], d[3], d[3])))

        

        html="""
        <!DOCTYPE html>
        <html>
        <head>
        <meta charset="UTF-8">
        <style>
        h3 {
            font-family: Helvetica-Bold;
            text-align: center;
        }
        table {
            font-family: arial, sans-serif;
            border-collapse: collapse;
            width: 100%;
            }
        td {
            text-align: left;
            padding-top: 4px;
            padding-right: 6px;
            padding-bottom: 2px;
            padding-left: 6px;
        }
        th {
            text-align: left;
            padding: 4px;
            background-color: black;
            color: white;
        }
        tr:nth-child(even) {
                            background-color: #dddddd;
                        }
        </style>
        </head>
        <body>
        <h3>LISTADO DE USUARIOS<br/></h3>
        <table align="left" width="100%" cellspacing="0">
        <tr>
            <th>Id_Usuario</th>
            <th>Mes</th>
            <th>Nombre</th>
            <th>Estatus</th>
            <th>Fecha de alta</th>
        </tr>
        [DATA]
        </table>
        </body>
        </html>
        """.replace("[DATA]", html_dato)


        qbyte = QByteArray()
        qbyte.append(str(html))
        #Ajuste
        codec = QTextCodec.codecForHtml(qbyte)
        unistr = codec.toUnicode(qbyte)

        if Qt.mightBeRichText(unistr):
            self.document.setHtml(unistr)
        else:
            self.document.setPlainText(unistr)

    def view(self):
    #Vista previa

        if not self.document.isEmpty():

            impres = QPrinter(QPrinter.HighResolution)
                
            var_view = QPrintPreviewDialog(impres, self)
            var_view.setWindowTitle("Vista previa")
            var_view.setWindowFlags(Qt.Window)
            var_view.resize(800, 600)

            exportarPDF = var_view.findChildren(QToolBar)
            exportarPDF[0].addAction(QIcon("logo.png"), "Exportar a PDF", self.pdf_export)
                
            var_view.paintRequested.connect(self.visualizar) 
            var_view.exec_()
        
        else:
            QMessageBox.critical(self, "Atención", "No hay datos en la tabla ",
                                 QMessageBox.Ok)

    def visualizar(self, imp):

        self.document.print_(imp)

    
    def pdf_export(self):

        if not self.document.isEmpty():
            file1, _ = QFileDialog.getSaveFileName(self, "Exportar a PDF", "file",
                                                           "Archivos PDF (*.pdf);;All Files (*)",
                                                           options=QFileDialog.Options())

            if file1:
                
                impres = QPrinter(QPrinter.HighResolution)
                impres.setOutputFormat(QPrinter.PdfFormat)
                impres.setOutputFileName(file1)
                
                self.document.print_(impres)

                QMessageBox.information(self, "Finalizado", "Se exportó correctamente el archivo",
                                        QMessageBox.Ok)
        else:
            QMessageBox.critical(self, "Atención", "No hay datos en la tabla",
                                 QMessageBox.Ok)

    def print_document(self):

        if not self.document.isEmpty():
            impres = QPrinter(QPrinter.HighResolution)
            
            dlg = QPrintDialog(impres, self)
            dlg.setWindowTitle("Imprimir documento")

            if dlg.exec_() == QPrintDialog.Accepted:
                self.document.print_(impres)

            del dlg
        else:
            QMessageBox.critical(self, "Atención", "No hay datos en la tabla",
                                 QMessageBox.Ok)


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