# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'connection_dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from wildchildanimation.gui.swing_utils import fakestr
class Ui_ConnectionDialog(object):
    def setupUi(self, ConnectionDialog):
        if not ConnectionDialog.objectName():
            ConnectionDialog.setObjectName(u"ConnectionDialog")
        ConnectionDialog.resize(413, 356)
        self.verticalLayout = QVBoxLayout(ConnectionDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_9 = QLabel(ConnectionDialog)
        self.label_9.setObjectName(u"label_9")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)

        self.verticalLayout.addWidget(self.label_9)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labelServer = QLabel(ConnectionDialog)
        self.labelServer.setObjectName(u"labelServer")
        self.labelServer.setMinimumSize(QSize(120, 0))

        self.horizontalLayout.addWidget(self.labelServer)

        self.lineEditServer = QLineEdit(ConnectionDialog)
        self.lineEditServer.setObjectName(u"lineEditServer")

        self.horizontalLayout.addWidget(self.lineEditServer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.labelEmail = QLabel(ConnectionDialog)
        self.labelEmail.setObjectName(u"labelEmail")
        self.labelEmail.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_2.addWidget(self.labelEmail)

        self.lineEditEmail = QLineEdit(ConnectionDialog)
        self.lineEditEmail.setObjectName(u"lineEditEmail")

        self.horizontalLayout_2.addWidget(self.lineEditEmail)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(ConnectionDialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_3.addWidget(self.label_3)

        self.lineEditPassword = QLineEdit(ConnectionDialog)
        self.lineEditPassword.setObjectName(u"lineEditPassword")
        self.lineEditPassword.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_3.addWidget(self.lineEditPassword)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.label_10 = QLabel(ConnectionDialog)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)

        self.verticalLayout.addWidget(self.label_10)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(ConnectionDialog)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_4.addWidget(self.label)

        self.lineEditProjectsFolder = QLineEdit(ConnectionDialog)
        self.lineEditProjectsFolder.setObjectName(u"lineEditProjectsFolder")

        self.horizontalLayout_4.addWidget(self.lineEditProjectsFolder)

        self.toolButtonProjectsFolder = QToolButton(ConnectionDialog)
        self.toolButtonProjectsFolder.setObjectName(u"toolButtonProjectsFolder")

        self.horizontalLayout_4.addWidget(self.toolButtonProjectsFolder)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.verticalSpacer = QSpacerItem(20, 19, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label_6 = QLabel(ConnectionDialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.verticalLayout.addWidget(self.label_6)

        self.label_7 = QLabel(ConnectionDialog)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout.addWidget(self.label_7)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_2 = QLabel(ConnectionDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_5.addWidget(self.label_2)

        self.lineEditFfmpegBin = QLineEdit(ConnectionDialog)
        self.lineEditFfmpegBin.setObjectName(u"lineEditFfmpegBin")

        self.horizontalLayout_5.addWidget(self.lineEditFfmpegBin)

        self.toolButtonFfmpegBin = QToolButton(ConnectionDialog)
        self.toolButtonFfmpegBin.setObjectName(u"toolButtonFfmpegBin")

        self.horizontalLayout_5.addWidget(self.toolButtonFfmpegBin)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_4 = QLabel(ConnectionDialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_6.addWidget(self.label_4)

        self.lineEditFfprobeBin = QLineEdit(ConnectionDialog)
        self.lineEditFfprobeBin.setObjectName(u"lineEditFfprobeBin")

        self.horizontalLayout_6.addWidget(self.lineEditFfprobeBin)

        self.toolButtonFfprobeBin = QToolButton(ConnectionDialog)
        self.toolButtonFfprobeBin.setObjectName(u"toolButtonFfprobeBin")

        self.horizontalLayout_6.addWidget(self.toolButtonFfprobeBin)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.label_8 = QLabel(ConnectionDialog)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout.addWidget(self.label_8)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_5 = QLabel(ConnectionDialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_7.addWidget(self.label_5)

        self.lineEdit7zBinary = QLineEdit(ConnectionDialog)
        self.lineEdit7zBinary.setObjectName(u"lineEdit7zBinary")

        self.horizontalLayout_7.addWidget(self.lineEdit7zBinary)

        self.toolButton7zSelect = QToolButton(ConnectionDialog)
        self.toolButton7zSelect.setObjectName(u"toolButton7zSelect")

        self.horizontalLayout_7.addWidget(self.toolButton7zSelect)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.buttonBox = QDialogButtonBox(ConnectionDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(ConnectionDialog)
        self.buttonBox.accepted.connect(ConnectionDialog.accept)
        self.buttonBox.rejected.connect(ConnectionDialog.reject)

        QMetaObject.connectSlotsByName(ConnectionDialog)
    # setupUi

    def retranslateUi(self, ConnectionDialog):
        ConnectionDialog.setWindowTitle(fakestr(u"Dialog", None))
        self.label_9.setText(fakestr(u"Treehouse:", None))
        self.labelServer.setText(fakestr(u"Server", None))
#if QT_CONFIG(tooltip)
        self.lineEditServer.setToolTip(fakestr(u"Server URL - https://example.wildchildanimation.com", None))
#endif // QT_CONFIG(tooltip)
        self.labelEmail.setText(fakestr(u"Email", None))
#if QT_CONFIG(tooltip)
        self.lineEditEmail.setToolTip(fakestr(u"Logon email address", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(fakestr(u"Password", None))
#if QT_CONFIG(tooltip)
        self.lineEditPassword.setToolTip(fakestr(u"Logon password", None))
#endif // QT_CONFIG(tooltip)
        self.label_10.setText(fakestr(u"Storage:", None))
        self.label.setText(fakestr(u"Projects Folder", None))
#if QT_CONFIG(tooltip)
        self.lineEditProjectsFolder.setToolTip(fakestr(u"<html><head/><body><p>Root directory for projects</p><p><br/></p><p>Shots will be downloaded to:</p><p><span style=\" font-weight:600;\">root/project/assets</span></p><p><br/></p><p>Assets will be downloaded to: </p><p><span style=\" font-weight:600;\">root/project/assets</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.toolButtonProjectsFolder.setText(fakestr(u"...", None))
        self.label_6.setText(fakestr(u"Applications:", None))
        self.label_7.setText(fakestr(u"ffmpeg - video encoding", None))
        self.label_2.setText(fakestr(u"ffmpeg binary", None))
#if QT_CONFIG(tooltip)
        self.lineEditFfmpegBin.setToolTip(fakestr(u"<html><head/><body><p>Location of ffmpeg executable, usually something like </p><p><br/></p><p>C:\\ffmpeg\\ffmpeg-20200831-4a11a6f-win64-static\\bin\\ffmpeg.exe</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.toolButtonFfmpegBin.setText(fakestr(u"...", None))
        self.label_4.setText(fakestr(u"ffprobe binary", None))
#if QT_CONFIG(tooltip)
        self.lineEditFfprobeBin.setToolTip(fakestr(u"<html><head/><body><p>Location of ffmpeg executable, usually something like </p><p><br/></p><p>C:\\ffmpeg\\ffmpeg-20200831-4a11a6f-win64-static\\bin\\ffmpeg.exe</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.toolButtonFfprobeBin.setText(fakestr(u"...", None))
        self.label_8.setText(fakestr(u"7zip - compress and extract archive", None))
        self.label_5.setText(fakestr(u"7zip binary", None))
#if QT_CONFIG(tooltip)
        self.lineEdit7zBinary.setToolTip(fakestr(u"<html><head/><body><p>Location of ffmpeg executable, usually something like </p><p><br/></p><p>C:\\ffmpeg\\ffmpeg-20200831-4a11a6f-win64-static\\bin\\ffmpeg.exe</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton7zSelect.setText(fakestr(u"...", None))
    # retranslateUi

