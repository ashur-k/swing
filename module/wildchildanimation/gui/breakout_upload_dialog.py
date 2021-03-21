# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'breakout_upload_dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_BreakoutUploadDialog(object):
    def setupUi(self, BreakoutUploadDialog):
        if not BreakoutUploadDialog.objectName():
            BreakoutUploadDialog.setObjectName(u"BreakoutUploadDialog")
        BreakoutUploadDialog.setEnabled(True)
        BreakoutUploadDialog.resize(614, 468)
        self.verticalLayout = QVBoxLayout(BreakoutUploadDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayoutProject = QHBoxLayout()
        self.horizontalLayoutProject.setObjectName(u"horizontalLayoutProject")
        self.verticalLayoutProject = QVBoxLayout()
        self.verticalLayoutProject.setObjectName(u"verticalLayoutProject")
        self.horizontalLayoutEpisodeSequence = QHBoxLayout()
        self.horizontalLayoutEpisodeSequence.setObjectName(u"horizontalLayoutEpisodeSequence")
        self.checkBoxSequence = QCheckBox(BreakoutUploadDialog)
        self.checkBoxSequence.setObjectName(u"checkBoxSequence")
        self.checkBoxSequence.setMinimumSize(QSize(100, 0))
        self.checkBoxSequence.setChecked(True)

        self.horizontalLayoutEpisodeSequence.addWidget(self.checkBoxSequence)

        self.comboBoxSequence = QComboBox(BreakoutUploadDialog)
        self.comboBoxSequence.setObjectName(u"comboBoxSequence")
        self.comboBoxSequence.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxSequence.sizePolicy().hasHeightForWidth())
        self.comboBoxSequence.setSizePolicy(sizePolicy)
        self.comboBoxSequence.setMinimumSize(QSize(200, 0))
        self.comboBoxSequence.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayoutEpisodeSequence.addWidget(self.comboBoxSequence)


        self.verticalLayoutProject.addLayout(self.horizontalLayoutEpisodeSequence)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labelPlayblastFolder = QLabel(BreakoutUploadDialog)
        self.labelPlayblastFolder.setObjectName(u"labelPlayblastFolder")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.labelPlayblastFolder.sizePolicy().hasHeightForWidth())
        self.labelPlayblastFolder.setSizePolicy(sizePolicy1)
        self.labelPlayblastFolder.setMinimumSize(QSize(100, 0))
        self.labelPlayblastFolder.setMaximumSize(QSize(60, 16777215))
        font = QFont()
        font.setBold(False)
        font.setWeight(50)
        self.labelPlayblastFolder.setFont(font)
        self.labelPlayblastFolder.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.labelPlayblastFolder)

        self.lineEditPlayblastFolder = QLineEdit(BreakoutUploadDialog)
        self.lineEditPlayblastFolder.setObjectName(u"lineEditPlayblastFolder")

        self.horizontalLayout.addWidget(self.lineEditPlayblastFolder)

        self.toolButtonSelectPlayblasts = QToolButton(BreakoutUploadDialog)
        self.toolButtonSelectPlayblasts.setObjectName(u"toolButtonSelectPlayblasts")

        self.horizontalLayout.addWidget(self.toolButtonSelectPlayblasts)


        self.verticalLayoutProject.addLayout(self.horizontalLayout)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.labelProjectsFolder = QLabel(BreakoutUploadDialog)
        self.labelProjectsFolder.setObjectName(u"labelProjectsFolder")
        sizePolicy1.setHeightForWidth(self.labelProjectsFolder.sizePolicy().hasHeightForWidth())
        self.labelProjectsFolder.setSizePolicy(sizePolicy1)
        self.labelProjectsFolder.setMinimumSize(QSize(100, 0))
        self.labelProjectsFolder.setMaximumSize(QSize(60, 16777215))
        self.labelProjectsFolder.setFont(font)
        self.labelProjectsFolder.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.labelProjectsFolder)

        self.lineEditProjectsFolder = QLineEdit(BreakoutUploadDialog)
        self.lineEditProjectsFolder.setObjectName(u"lineEditProjectsFolder")

        self.horizontalLayout_6.addWidget(self.lineEditProjectsFolder)

        self.toolButtonSelectProjects = QToolButton(BreakoutUploadDialog)
        self.toolButtonSelectProjects.setObjectName(u"toolButtonSelectProjects")

        self.horizontalLayout_6.addWidget(self.toolButtonSelectProjects)


        self.verticalLayoutProject.addLayout(self.horizontalLayout_6)


        self.horizontalLayoutProject.addLayout(self.verticalLayoutProject)


        self.verticalLayout.addLayout(self.horizontalLayoutProject)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.tableView = QTableView(BreakoutUploadDialog)
        self.tableView.setObjectName(u"tableView")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(10)
        sizePolicy2.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy2)
        self.tableView.setSizeIncrement(QSize(0, 0))
        font1 = QFont()
        font1.setPointSize(9)
        self.tableView.setFont(font1)
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView.setWordWrap(False)

        self.horizontalLayout_3.addWidget(self.tableView)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButtonScan = QPushButton(BreakoutUploadDialog)
        self.pushButtonScan.setObjectName(u"pushButtonScan")

        self.horizontalLayout_4.addWidget(self.pushButtonScan)

        self.pushButtonCreate = QPushButton(BreakoutUploadDialog)
        self.pushButtonCreate.setObjectName(u"pushButtonCreate")

        self.horizontalLayout_4.addWidget(self.pushButtonCreate)

        self.progressBar = QProgressBar(BreakoutUploadDialog)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMaximum(1)
        self.progressBar.setValue(-1)

        self.horizontalLayout_4.addWidget(self.progressBar)

        self.pushButtonCancel = QPushButton(BreakoutUploadDialog)
        self.pushButtonCancel.setObjectName(u"pushButtonCancel")
        self.pushButtonCancel.setAutoDefault(False)

        self.horizontalLayout_4.addWidget(self.pushButtonCancel)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.lineEdit = QLineEdit(BreakoutUploadDialog)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout.addWidget(self.lineEdit)


        self.retranslateUi(BreakoutUploadDialog)

        QMetaObject.connectSlotsByName(BreakoutUploadDialog)
    # setupUi

    def retranslateUi(self, BreakoutUploadDialog):
        BreakoutUploadDialog.setWindowTitle(QCoreApplication.translate("BreakoutUploadDialog", u"Upload Layout Sequence", None))
#if QT_CONFIG(tooltip)
        BreakoutUploadDialog.setToolTip(QCoreApplication.translate("BreakoutUploadDialog", u"Select playblast and project file directories to upload as Layout", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxSequence.setText(QCoreApplication.translate("BreakoutUploadDialog", u"Sequence", None))
        self.labelPlayblastFolder.setText(QCoreApplication.translate("BreakoutUploadDialog", u"Playblasts", None))
#if QT_CONFIG(tooltip)
        self.lineEditPlayblastFolder.setToolTip(QCoreApplication.translate("BreakoutUploadDialog", u"Select a directory containing media files ###ABC_###", None))
#endif // QT_CONFIG(tooltip)
        self.toolButtonSelectPlayblasts.setText(QCoreApplication.translate("BreakoutUploadDialog", u"...", None))
        self.labelProjectsFolder.setText(QCoreApplication.translate("BreakoutUploadDialog", u"Projects", None))
#if QT_CONFIG(tooltip)
        self.lineEditProjectsFolder.setToolTip(QCoreApplication.translate("BreakoutUploadDialog", u"Select a directory containing project files ###ABC_###", None))
#endif // QT_CONFIG(tooltip)
        self.toolButtonSelectProjects.setText(QCoreApplication.translate("BreakoutUploadDialog", u"...", None))
        self.pushButtonScan.setText(QCoreApplication.translate("BreakoutUploadDialog", u"Scan Folders", None))
        self.pushButtonCreate.setText(QCoreApplication.translate("BreakoutUploadDialog", u"Create Shots", None))
        self.pushButtonCancel.setText(QCoreApplication.translate("BreakoutUploadDialog", u"Close", None))
    # retranslateUi
