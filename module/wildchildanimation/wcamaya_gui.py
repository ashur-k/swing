# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\DEV\Github\wca-maya/gui/forms/wca-tools/form.ui'
#
# Created: Wed Jan 20 00:41:18 2021
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WcaMayaDialog(object):
    
    def setupUi(self, WcaMayaDialog):
        WcaMayaDialog.setObjectName("WcaMayaDialog")
        WcaMayaDialog.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(WcaMayaDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.connectionLayout = QtWidgets.QHBoxLayout()
        self.connectionLayout.setObjectName("connectionLayout")
        self.pushButtonConnection = QtWidgets.QPushButton(WcaMayaDialog)
        self.pushButtonConnection.setObjectName("pushButtonConnection")
        self.connectionLayout.addWidget(self.pushButtonConnection)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.connectionLayout.addItem(spacerItem)
        self.labelProject = QtWidgets.QLabel(WcaMayaDialog)
        self.labelProject.setObjectName("labelProject")
        self.connectionLayout.addWidget(self.labelProject)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.connectionLayout.addItem(spacerItem1)
        self.comboBoxProject = QtWidgets.QComboBox(WcaMayaDialog)
        self.comboBoxProject.setObjectName("comboBoxProject")
        self.connectionLayout.addWidget(self.comboBoxProject)
        self.verticalLayout.addLayout(self.connectionLayout)
        self.shotLayout = QtWidgets.QVBoxLayout()
        self.shotLayout.setObjectName("shotLayout")
        self.labelShot = QtWidgets.QLabel(WcaMayaDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelShot.sizePolicy().hasHeightForWidth())
        self.labelShot.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.labelShot.setFont(font)
        self.labelShot.setObjectName("labelShot")
        self.shotLayout.addWidget(self.labelShot)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(WcaMayaDialog)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.comboBoxEpisode = QtWidgets.QComboBox(WcaMayaDialog)
        self.comboBoxEpisode.setObjectName("comboBoxEpisode")
        self.horizontalLayout_2.addWidget(self.comboBoxEpisode)
        self.label_2 = QtWidgets.QLabel(WcaMayaDialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.comboBoxSequence = QtWidgets.QComboBox(WcaMayaDialog)
        self.comboBoxSequence.setObjectName("comboBoxSequence")
        self.horizontalLayout_2.addWidget(self.comboBoxSequence)
        self.shotLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.shotLayout)
        self.assetLayout = QtWidgets.QVBoxLayout()
        self.assetLayout.setObjectName("assetLayout")
        self.label = QtWidgets.QLabel(WcaMayaDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.assetLayout.addWidget(self.label)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(WcaMayaDialog)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.comboBoxAssetEpisode = QtWidgets.QComboBox(WcaMayaDialog)
        self.comboBoxAssetEpisode.setObjectName("comboBoxAssetEpisode")
        self.horizontalLayout_3.addWidget(self.comboBoxAssetEpisode)
        self.label_5 = QtWidgets.QLabel(WcaMayaDialog)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.comboBoxAssetType = QtWidgets.QComboBox(WcaMayaDialog)
        self.comboBoxAssetType.setObjectName("comboBoxAssetType")
        self.horizontalLayout_3.addWidget(self.comboBoxAssetType)
        self.assetLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.assetLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.textEdit = QtWidgets.QTextEdit(WcaMayaDialog)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout_4.addWidget(self.textEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonDownload = QtWidgets.QPushButton(WcaMayaDialog)
        self.pushButtonDownload.setObjectName("pushButtonDownload")
        self.horizontalLayout.addWidget(self.pushButtonDownload)
        self.pushButtonExport = QtWidgets.QPushButton(WcaMayaDialog)
        self.pushButtonExport.setObjectName("pushButtonExport")
        self.horizontalLayout.addWidget(self.pushButtonExport)
        self.pushButtonEditorial = QtWidgets.QPushButton(WcaMayaDialog)
        self.pushButtonEditorial.setObjectName("pushButtonEditorial")
        self.horizontalLayout.addWidget(self.pushButtonEditorial)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(WcaMayaDialog)
        QtCore.QMetaObject.connectSlotsByName(WcaMayaDialog)

    def retranslateUi(self, WcaMayaDialog):
        WcaMayaDialog.setWindowTitle(QtWidgets.QApplication.translate("WcaMayaDialog", "WCA_Tools", None, -1))
        self.pushButtonConnection.setText(QtWidgets.QApplication.translate("WcaMayaDialog", "Logon", None, -1))
        self.labelProject.setText(QtWidgets.QApplication.translate("WcaMayaDialog", "Project", None, -1))
        self.labelShot.setText(QtWidgets.QApplication.translate("WcaMayaDialog", "Shot", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("WcaMayaDialog", "Episode", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("WcaMayaDialog", "Sequence", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("WcaMayaDialog", "Asset", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("WcaMayaDialog", "Episode", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("WcaMayaDialog", "Asset Type", None, -1))
        self.pushButtonDownload.setText(QtWidgets.QApplication.translate("WcaMayaDialog", "Download", None, -1))
        self.pushButtonExport.setText(QtWidgets.QApplication.translate("WcaMayaDialog", "Export/Playblast", None, -1))
        self.pushButtonEditorial.setText(QtWidgets.QApplication.translate("WcaMayaDialog", "Open Editorial", None, -1))
