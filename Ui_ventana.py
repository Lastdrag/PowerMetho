# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\nesto\Documents\yo\prograa\PowerMetho\ventana.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(742, 542)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 150, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.exportarCvs = QtWidgets.QPushButton(self.centralwidget)
        self.exportarCvs.setGeometry(QtCore.QRect(600, 150, 93, 28))
        self.exportarCvs.setObjectName("exportarCvs")
        self.ValoresAleatorios = QtWidgets.QRadioButton(self.centralwidget)
        self.ValoresAleatorios.setGeometry(QtCore.QRect(40, 40, 261, 20))
        self.ValoresAleatorios.setObjectName("ValoresAleatorios")
        self.ValoresSeparadosComas = QtWidgets.QRadioButton(self.centralwidget)
        self.ValoresSeparadosComas.setGeometry(QtCore.QRect(40, 70, 261, 20))
        self.ValoresSeparadosComas.setObjectName("ValoresSeparadosComas")
        self.TamanoMatriz = QtWidgets.QTextBrowser(self.centralwidget)
        self.TamanoMatriz.setGeometry(QtCore.QRect(570, 30, 71, 21))
        self.TamanoMatriz.setObjectName("TamanoMatriz")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 10, 161, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(420, 30, 131, 16))
        self.label_2.setObjectName("label_2")
        self.NumeroDeinteracciones = QtWidgets.QTextBrowser(self.centralwidget)
        self.NumeroDeinteracciones.setGeometry(QtCore.QRect(210, 110, 71, 21))
        self.NumeroDeinteracciones.setObjectName("NumeroDeinteracciones")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 110, 161, 16))
        self.label_3.setObjectName("label_3")
        self.CargarDoc = QtWidgets.QPushButton(self.centralwidget)
        self.CargarDoc.setGeometry(QtCore.QRect(420, 70, 93, 28))
        self.CargarDoc.setObjectName("CargarDoc")
        self.MuestraNombreDoc = QtWidgets.QTextBrowser(self.centralwidget)
        self.MuestraNombreDoc.setGeometry(QtCore.QRect(520, 70, 181, 21))
        self.MuestraNombreDoc.setObjectName("MuestraNombreDoc")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "ejecutar"))
        self.exportarCvs.setText(_translate("MainWindow", "exportar csv"))
        self.ValoresAleatorios.setText(_translate("MainWindow", "      Random Stochastic Matrix"))
        self.ValoresSeparadosComas.setText(_translate("MainWindow", "Comma Separeted Valudes (CSV) File"))
        self.label.setText(_translate("MainWindow", "Selec matrix source"))
        self.label_2.setText(_translate("MainWindow", "Square matrix  Size"))
        self.label_3.setText(_translate("MainWindow", "Number for Interaccion"))
        self.CargarDoc.setText(_translate("MainWindow", "Open file"))
