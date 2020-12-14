# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Kalypso(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("Kalypso")
        self.resize(728, 514)
        self.centralwidget = QtWidgets.QWidget()
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
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 728, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar()
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.actionUpload = QtWidgets.QAction()
        self.actionUpload.setObjectName("actionUpload")
        self.actionSet_AuthCode = QtWidgets.QAction()
        self.actionSet_AuthCode.setObjectName("actionSet_AuthCode")
        self.menuFile.addAction(self.actionUpload)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSet_AuthCode)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Kalypso", "Kalypso"))
        self.openFilePushButton.setText(_translate("Kalypso", "Open file"))
        self.uploadPushButton.setText(_translate("Kalypso", "Upload"))
        self.cancelPushButton.setText(_translate("Kalypso", "Cancel"))
        self.previewLabel.setText(_translate("Kalypso", "Preview"))
        self.menuFile.setTitle(_translate("Kalypso", "File"))
        self.actionUpload.setText(_translate("Kalypso", "Open file"))
        self.actionSet_AuthCode.setText(_translate("Kalypso", "Set AuthCode"))

    # def closeEvent(self, a0: QtGui.QCloseEvent) -> None: