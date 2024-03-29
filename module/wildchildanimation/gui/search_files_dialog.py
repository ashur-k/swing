# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'search_files_dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from wildchildanimation.gui.swing_utils import fakestr

class Ui_SearchFilesDialog(object):
    def setupUi(self, SearchFilesDialog):
        if not SearchFilesDialog.objectName():
            SearchFilesDialog.setObjectName(u"SearchFilesDialog")
        SearchFilesDialog.setEnabled(True)
        SearchFilesDialog.resize(655, 226)
        SearchFilesDialog.setSizeGripEnabled(True)
        self.verticalLayout = QVBoxLayout(SearchFilesDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.labelSearch = QLabel(SearchFilesDialog)
        self.labelSearch.setObjectName(u"labelSearch")

        self.horizontalLayout_6.addWidget(self.labelSearch)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.textEdit = QTextEdit(SearchFilesDialog)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout.addWidget(self.textEdit)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButtonSearch = QPushButton(SearchFilesDialog)
        self.pushButtonSearch.setObjectName(u"pushButtonSearch")
        self.pushButtonSearch.setAutoDefault(True)

        self.horizontalLayout_4.addWidget(self.pushButtonSearch)

        self.progressBar = QProgressBar(SearchFilesDialog)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMaximum(1)
        self.progressBar.setValue(-1)

        self.horizontalLayout_4.addWidget(self.progressBar)

        self.pushButtonCancel = QPushButton(SearchFilesDialog)
        self.pushButtonCancel.setObjectName(u"pushButtonCancel")
        self.pushButtonCancel.setAutoDefault(False)

        self.horizontalLayout_4.addWidget(self.pushButtonCancel)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.retranslateUi(SearchFilesDialog)

        self.pushButtonSearch.setDefault(True)


        QMetaObject.connectSlotsByName(SearchFilesDialog)
    # setupUi

    def retranslateUi(self, SearchFilesDialog):
        SearchFilesDialog.setWindowTitle(fakestr(u"Search for files", None))
        self.labelSearch.setText(fakestr(u"Enter a comma separated list of file names or partial file names to search for ", None))
        self.pushButtonSearch.setText(fakestr(u"Search", None))
#if QT_CONFIG(shortcut)
        self.pushButtonSearch.setShortcut(fakestr(u"Ctrl+Return", None))
#endif // QT_CONFIG(shortcut)
        self.pushButtonCancel.setText(fakestr(u"Close", None))
    # retranslateUi

