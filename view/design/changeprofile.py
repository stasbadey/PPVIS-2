# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view/design/changeprofile.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_choose(object):
    def setupUi(self, choose):
        choose.setObjectName("choose")
        choose.resize(190, 192)
        choose.setStyleSheet("background-color: rgb(255, 197, 192);\n"
"color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(choose)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("color: rgb(0, 0, 0);")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText("Логин")
        self.lineEdit.setStyleSheet("color: rgb(0, 0, 0);")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setPlaceholderText("Пароль")
        self.lineEdit_2.setStyleSheet("color: rgb(0, 0, 0);")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_2.addWidget(self.line_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setPlaceholderText("Повторный ввод пароля")
        self.lineEdit_3.setStyleSheet("color: rgb(0, 0, 0);")
        self.verticalLayout_2.addWidget(self.lineEdit_3)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_2.addWidget(self.line_4)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setStyleSheet("background-color: rgb(0, 156, 255);")
        self.pushButton.setObjectName("pushButton_7")
        self.verticalLayout_2.addWidget(self.pushButton)
        choose.setCentralWidget(self.centralwidget)

        self.retranslateUi(choose)
        QtCore.QMetaObject.connectSlotsByName(choose)

    def retranslateUi(self, choose):
        _translate = QtCore.QCoreApplication.translate
        choose.setWindowTitle(_translate("choose", "MainWindow"))
        self.label.setText(_translate("choose", "    Изменение данных профиля"))
        self.pushButton.setText(_translate("choose", "Подтвердить"))
