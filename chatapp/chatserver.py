# -*- coding: utf-8 -*-
# Muhsin Hameed
# Form implementation generated from reading ui file 'chatserver.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(130, 20, 131, 16))
        self.label.setObjectName("label")
        self.textEditMessages = QtWidgets.QTextEdit(Dialog)
        self.textEditMessages.setGeometry(QtCore.QRect(60, 60, 281, 151))
        self.textEditMessages.setObjectName("textEditMessages")
        self.lineEditMessages = QtWidgets.QLineEdit(Dialog)
        self.lineEditMessages.setGeometry(QtCore.QRect(32, 240, 231, 31))
        self.lineEditMessages.setObjectName("lineEditMessages")
        self.pushButtonSend = QtWidgets.QPushButton(Dialog)
        self.pushButtonSend.setGeometry(QtCore.QRect(290, 230, 93, 28))
        self.pushButtonSend.setObjectName("pushButtonSend")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Muhsin\'s Server"))
        self.pushButtonSend.setText(_translate("Dialog", "Send"))
