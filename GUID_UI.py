# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUID.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(464, 170)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 129, 16))
        self.label.setObjectName("label")
        self.ConversionGUIDButton = QtWidgets.QPushButton(self.centralwidget)
        self.ConversionGUIDButton.setGeometry(QtCore.QRect(280, 40, 111, 31))
        self.ConversionGUIDButton.setObjectName("ConversionGUIDButton")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 40, 261, 31))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.Number = QtWidgets.QSpinBox(self.centralwidget)
        self.Number.setGeometry(QtCore.QRect(140, 10, 71, 19))
        self.Number.setMinimum(1)
        self.Number.setProperty("value", 1)
        self.Number.setObjectName("Number")
        self.GenGUIDButton = QtWidgets.QPushButton(self.centralwidget)
        self.GenGUIDButton.setGeometry(QtCore.QRect(220, 10, 171, 20))
        self.GenGUIDButton.setObjectName("GenGUIDButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 464, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GUID"))
        self.label.setText(_translate("MainWindow", "Number of GUID generate:"))
        self.ConversionGUIDButton.setText(_translate("MainWindow", "Conversion GUID"))
        self.GenGUIDButton.setText(_translate("MainWindow", "Generate GUID"))