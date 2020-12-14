# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'authcode_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AuthCode(object):
    def setupUi(self, AuthCode):
        AuthCode.setObjectName("AuthCode")
        AuthCode.resize(395, 132)
        self.centralwidget = QtWidgets.QWidget(AuthCode)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.authCodeLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.authCodeLineEdit.setObjectName("authCodeLineEdit")
        self.verticalLayout.addWidget(self.authCodeLineEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.okPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.okPushButton.setObjectName("okPushButton")
        self.horizontalLayout.addWidget(self.okPushButton)
        self.cancelPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelPushButton.setObjectName("cancelPushButton")
        self.horizontalLayout.addWidget(self.cancelPushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        AuthCode.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AuthCode)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 395, 23))
        self.menubar.setObjectName("menubar")
        AuthCode.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AuthCode)
        self.statusbar.setObjectName("statusbar")
        AuthCode.setStatusBar(self.statusbar)

        self.retranslateUi(AuthCode)
        QtCore.QMetaObject.connectSlotsByName(AuthCode)

    def retranslateUi(self, AuthCode):
        _translate = QtCore.QCoreApplication.translate
        AuthCode.setWindowTitle(_translate("AuthCode", "AuthCode"))
        self.label.setText(_translate("AuthCode", "Input Auth Code Below"))
        self.okPushButton.setText(_translate("AuthCode", "OK"))
        self.cancelPushButton.setText(_translate("AuthCode", "Cancel"))
