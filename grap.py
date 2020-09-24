# ----------------------------------------------------------------------------
# Nombre:       grap.py
# Autor:        Gabriel F
# GitHub:       https://github.com/gab98fra/
# Creado:       24 de Septiembre 2020
# Modificado:   24 de Septiembre 2020
# Copyright:    (c) 2020 by Gabriel F, 2020
# ----------------------------------------------------------------------------

"""
    Gráfica circular o de pastel

"""


from PyQt5.QtGui import QFont, QIcon, QPalette, QColor, QPainter
from PyQt5.QtCore import Qt, QTranslator, QLocale, QLibraryInfo, pyqtSlot
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice, QLegend
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QGridLayout, QVBoxLayout, QHBoxLayout,
                             QLabel, QComboBox, QSizePolicy, QCheckBox)

import sys

class window(QMainWindow):
#Ventana principal
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gráfico Circular o de pastel")
        self.setWindowIcon(QIcon("logo.png"))
        self.setMinimumSize(1200, 650)
        self.move(80,10)

        #Fuente
        font=QFont()
        font.setPointSize(9)
        self.setFont(font)

        #Objeto gráfico/Asignar a la ventana principal
        widget=widget_grafica()
        self.setCentralWidget(widget)


class widget_grafica(QWidget):
#widget - gráfica
    def __init__(self, parent=None):
        super(widget_grafica, self).__init__(parent)

        self.initUI()

    def initUI(self):
    
        #Panel valores -métodos ejecutados
        self.color_fondo = self.lista_color_fondo()
        self.animacion_grafica = self.lista_animacion()
        self.leyenda_grafica = self.lista_leyenda()
        self.marcador_grafica = self.lista_marcadores() 
        self.posicion_grafica=self.lista_posicion_leyenda()
        self.posicion_grafica = self.lista_posicion_leyenda()
        
        self.mostrar_ocultar_leyenda = QCheckBox("Mostrar etiqueta")

        #Panel- menú-Horizontal
        panel_widget = QHBoxLayout()
        panel_widget.addWidget(QLabel("Tema"))
        panel_widget.addWidget(self.color_fondo)
        panel_widget.addWidget(QLabel("Animación"))
        panel_widget.addWidget(self.animacion_grafica)
        panel_widget.addWidget(QLabel("Leyenda"))
        panel_widget.addWidget(self.leyenda_grafica)
        panel_widget.addWidget(QLabel("Marcador"))
        panel_widget.addWidget(self.marcador_grafica)
        panel_widget.addWidget(QLabel("Ubicación"))
        panel_widget.addWidget(self.posicion_grafica)
        panel_widget.addWidget(self.mostrar_ocultar_leyenda)
        panel_widget.addStretch()#Ajustar widgets

        #Contedor -Gráfica
        contenedor_grafica = QChartView(self.grafica_circular())
        contenedor_grafica.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        contenedor_grafica.setRenderHint(QPainter.Antialiasing, True)

        self.grafica = contenedor_grafica

        #Layout
        layout = QGridLayout()
        layout.addLayout(panel_widget,       1, 0, 1, 0)
        layout.addWidget(contenedor_grafica, 2, 0, 4, 0)

        self.setLayout(layout)

        #Funciones
        self.color_fondo.currentIndexChanged.connect(self.update_initUI)
        self.animacion_grafica.currentIndexChanged.connect(self.update_initUI)
        self.leyenda_grafica.currentIndexChanged.connect(self.update_initUI)
        self.marcador_grafica.currentIndexChanged.connect(self.update_initUI)
        self.posicion_grafica.currentIndexChanged.connect(self.update_initUI)
        self.mostrar_ocultar_leyenda.toggled.connect(self.update_initUI)

        #Valor predeterminado-mostrar leyenda gráfica
        self.mostrar_ocultar_leyenda.setChecked(True)
        
        self.update_initUI()

    def lista_color_fondo(self):
    #Lista de fondos

        lista_colores_fondo = QComboBox()

        lista_colores_fondo.addItem("Predeterminado", QChart.ChartThemeQt)
        lista_colores_fondo.addItem("Brillo", QChart.ChartThemeLight)
        lista_colores_fondo.addItem("Oscuro", QChart.ChartThemeDark)
        lista_colores_fondo.addItem("Azul Fuerte", QChart.ChartThemeBlueCerulean)
        lista_colores_fondo.addItem("Arena", QChart.ChartThemeBrownSand)
        lista_colores_fondo.addItem("Azul cielo", QChart.ChartThemeBlueNcs)
        lista_colores_fondo.addItem("Amarillo", QChart.ChartThemeHighContrast)
        lista_colores_fondo.addItem("Azul claro", QChart.ChartThemeBlueIcy)

        return lista_colores_fondo

    def lista_animacion(self):
    #Lista de animaciones
        animacionComboBox = QComboBox()

        animacionComboBox.addItem("No animaciones", QChart.NoAnimation)
        animacionComboBox.addItem("Animaciones GridAxis", QChart.GridAxisAnimations)
        animacionComboBox.addItem("Serie de animaciones", QChart.SeriesAnimations)
        animacionComboBox.addItem("Todas las animaciones", QChart.AllAnimations)

        return animacionComboBox

    def lista_leyenda(self):
    #Lista de leyendas

        leyendaComboBox = QComboBox()

        leyendaComboBox.addItem("No Leyenda", 0)
        leyendaComboBox.addItem("Leyenda superior", Qt.AlignTop)
        leyendaComboBox.addItem("Leyenda inferior", Qt.AlignBottom)
        leyendaComboBox.addItem("Leyenda izquierda", Qt.AlignLeft)
        leyendaComboBox.addItem("Leyenda derecha", Qt.AlignRight)

        return leyendaComboBox

    def lista_marcadores(self):
    #Lista de marcadores

        marcadorLeyendaComboBox = QComboBox()

        marcadorLeyendaComboBox.addItem("Predeterminado", QLegend.MarkerShapeDefault)
        marcadorLeyendaComboBox.addItem("Rectangular", QLegend.MarkerShapeRectangle)
        marcadorLeyendaComboBox.addItem("Circular", QLegend.MarkerShapeCircle)
        marcadorLeyendaComboBox.addItem("Determinado por la serie",QLegend.MarkerShapeFromSeries)

        return marcadorLeyendaComboBox

    def lista_posicion_leyenda(self):
    #Lista posiciones de leyenda

        posicionEtiquetaComboBox = QComboBox()

        posicionEtiquetaComboBox.addItem("Predeterminada", QPieSlice.LabelOutside)
        posicionEtiquetaComboBox.addItem("Interior horizontal",
                                         QPieSlice.LabelInsideHorizontal)
        posicionEtiquetaComboBox.addItem("Interior tangencial",
                                         QPieSlice.LabelInsideTangential)
        posicionEtiquetaComboBox.addItem("Interior normal",
                                         QPieSlice.LabelInsideNormal)

        return posicionEtiquetaComboBox

    def grafica_circular(self):
    #Gráfica circular
        
        #Grátfica
        grafica = QChart()
        grafica.setTitle("Segmento de categorías")

        datos = [("Abarrotes", 13.23), ("Nutrición", 15.2), ("Infántil", 8.42),
                       ("Cremería", 2.3), ("Cámara Fría", 6.4), ("Papelería", 2.344)]

        series = QPieSeries(grafica)

        for etiqueta, valor in datos:
            slice = series.append(etiqueta, valor)

        grafica.addSeries(series)
        grafica.createDefaultAxes()

        return grafica

    @pyqtSlot()

    def update_initUI(self):
    #Actualización tema_seleccionado-Interactivo

        #Valor seleccionado
        tema_seleccionado = self.color_fondo.itemData(self.color_fondo.currentIndex())

        if self.grafica.chart().theme() != tema_seleccionado:

            self.grafica.chart().setTheme(tema_seleccionado)
            #Paleta de colores
            paleta = self.window().palette()

            if tema_seleccionado == QChart.ChartThemeLight:
                paleta.setColor(QPalette.Window, QColor(0xf0f0f0))
                paleta.setColor(QPalette.WindowText, QColor(0x404044))

            elif tema_seleccionado == QChart.ChartThemeDark:
                paleta.setColor(QPalette.Window, QColor(0x121218))
                paleta.setColor(QPalette.WindowText, QColor(0xd6d6d6))

            elif tema_seleccionado == QChart.ChartThemeBlueCerulean:
                paleta.setColor(QPalette.Window, QColor(0x40434a))
                paleta.setColor(QPalette.WindowText, QColor(0xd6d6d6))

            elif tema_seleccionado == QChart.ChartThemeBrownSand:
                paleta.setColor(QPalette.Window, QColor(0x9e8965))
                paleta.setColor(QPalette.WindowText, QColor(0x404044))

            elif tema_seleccionado == QChart.ChartThemeBlueNcs:
                paleta.setColor(QPalette.Window, QColor(0x018bba))
                paleta.setColor(QPalette.WindowText, QColor(0x404044))

            elif tema_seleccionado == QChart.ChartThemeHighContrast:
                paleta.setColor(QPalette.Window, QColor(0xffab03))
                paleta.setColor(QPalette.WindowText, QColor(0x181818))

            elif tema_seleccionado == QChart.ChartThemeBlueIcy:
                paleta.setColor(QPalette.Window, QColor(0xcee7f0))
                paleta.setColor(QPalette.WindowText, QColor(0x404044))

            else:
                paleta.setColor(QPalette.Window, QColor(0xf0f0f0))
                paleta.setColor(QPalette.WindowText, QColor(0x404044))
            
            #Asignar el tema seleccionado
            self.window().setPalette(paleta)

        #-------------------Animación----------------------
        opciones = QChart.AnimationOptions(self.animacion_grafica.itemData(
            self.animacion_grafica.currentIndex()))

        if self.grafica.chart().animationOptions() != opciones:
            self.grafica.chart().setAnimationOptions(opciones)

        #-------------------Obtener leyenda----------------------

        leyenda = self.grafica.chart().legend()

        
        #-------------------leyenda grafica----------------------
        alineacion = self.leyenda_grafica.itemData(self.leyenda_grafica.currentIndex())

        if alineacion == 0:
            leyenda.hide()
        else:
            leyenda.setAlignment(Qt.Alignment(alineacion))
            leyenda.show()

        #-------------------marcador----------------------
        marcador = self.marcador_grafica.itemData(
            self.marcador_grafica.currentIndex()) 

        if leyenda != marcador:
            leyenda.setMarkerShape(marcador)

        #-------------------Posoción etiqueta----------------------
        posicionEtiqueta = self.posicion_grafica.itemData(
            self.posicion_grafica.currentIndex())
        self.grafica.chart().series()[0].setLabelsPosition(posicionEtiqueta)

        #-------------------Mostrar/Oculatar etiquta----------------------
        visibilidadEtiqueta = self.mostrar_ocultar_leyenda.isChecked()
        self.grafica.chart().series()[0].setLabelsVisible(visibilidadEtiqueta)


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