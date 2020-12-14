# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Kalypso(object):
    def setupUi(self, Kalypso):
        Kalypso.setObjectName("Kalypso")
        Kalypso.resize(728, 514)
        self.centralwidget = QtWidgets.QWidget(Kalypso)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setMaximumSize(QtCore.QSize(200, 16777215))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.openFilePushButton = QtWidgets.QPushButton(self.groupBox)
        self.openFilePushButton.setMaximumSize(QtCore.QSize(200, 16777215))
        self.openFilePushButton.setObjectName("openFilePushButton")
        self.verticalLayout.addWidget(self.openFilePushButton)
        self.uploadPushButton = QtWidgets.QPushButton(self.groupBox)
        self.uploadPushButton.setMaximumSize(QtCore.QSize(200, 16777215))
        self.uploadPushButton.setObjectName("uploadPushButton")
        self.verticalLayout.addWidget(self.uploadPushButton)
        self.cancelPushButton = QtWidgets.QPushButton(self.groupBox)
        self.cancelPushButton.setMaximumSize(QtCore.QSize(200, 16777215))
        self.cancelPushButton.setObjectName("cancelPushButton")
        self.verticalLayout.addWidget(self.cancelPushButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.previewLabel = QtWidgets.QLabel(self.groupBox)
        self.previewLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.previewLabel.setObjectName("previewLabel")
        self.verticalLayout.addWidget(self.previewLabel)
        self.graphicsView = QtWidgets.QGraphicsView(self.groupBox)
        self.graphicsView.setMaximumSize(QtCore.QSize(200, 16777215))
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)
        self.horizontalLayout.addWidget(self.groupBox)
        self.uploadedListWidget = QtWidgets.QListWidget(self.centralwidget)
        self.uploadedListWidget.setObjectName("uploadedListWidget")
        self.horizontalLayout.addWidget(self.uploadedListWidget)
        Kalypso.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Kalypso)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 728, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        Kalypso.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Kalypso)
        self.statusbar.setObjectName("statusbar")
        Kalypso.setStatusBar(self.statusbar)
        self.actionUpload = QtWidgets.QAction(Kalypso)
        self.actionUpload.setObjectName("actionUpload")
        self.actionSet_AuthCode = QtWidgets.QAction(Kalypso)
        self.actionSet_AuthCode.setObjectName("actionSet_AuthCode")
        self.menuFile.addAction(self.actionUpload)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSet_AuthCode)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(Kalypso)
        QtCore.QMetaObject.connectSlotsByName(Kalypso)

    def retranslateUi(self, Kalypso):
        _translate = QtCore.QCoreApplication.translate
        Kalypso.setWindowTitle(_translate("Kalypso", "Kalypso"))
        self.openFilePushButton.setText(_translate("Kalypso", "Open file"))
        self.uploadPushButton.setText(_translate("Kalypso", "Upload"))
        self.cancelPushButton.setText(_translate("Kalypso", "Cancel"))
        self.previewLabel.setText(_translate("Kalypso", "Preview"))
        self.menuFile.setTitle(_translate("Kalypso", "File"))
        self.actionUpload.setText(_translate("Kalypso", "Open file"))
        self.actionSet_AuthCode.setText(_translate("Kalypso", "Set AuthCode"))
