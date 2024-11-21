# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'draft ui.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QListWidget, QListWidgetItem,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import design_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(925, 854)
        self.actionLoad_File_Ctrl_O = QAction(MainWindow)
        self.actionLoad_File_Ctrl_O.setObjectName(u"actionLoad_File_Ctrl_O")
        self.actionChange_Default_Template_Output = QAction(MainWindow)
        self.actionChange_Default_Template_Output.setObjectName(u"actionChange_Default_Template_Output")
        self.actionChange_HTML_Output = QAction(MainWindow)
        self.actionChange_HTML_Output.setObjectName(u"actionChange_HTML_Output")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"\n"
"\n"
"\n"
"QWidget#centralwidget{\n"
"background-color: rgb(66, 57, 61);\n"
"}\n"
"\n"
"QTableWidget, QComboBox, QListWidget, QColumnView{\n"
"background-color:rgba(16, 15, 15, 95);\n"
"color:white;\n"
"}\n"
"\n"
"QComboBox{\n"
"margin-top:30%;\n"
"margin-bottom:30%;\n"
"padding:10px;\n"
"}\n"
"\n"
"\n"
"QLabel{\n"
"color:white}\n"
"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.i_o_frame = QFrame(self.centralwidget)
        self.i_o_frame.setObjectName(u"i_o_frame")
        self.i_o_frame.setStyleSheet(u"*{\n"
"background-color:rgb(16, 15, 15);\n"
"}\n"
"\n"
"QFrame#i_o_frame {\n"
"\n"
"	background-color:rgb(49, 42, 44);\n"
"	}\n"
"\n"
"QPushButton{\n"
"	color:rgba(255, 255, 255, 95);\n"
"	font: 15pt \"Futura\";\n"
"	padding-top:5px;\n"
"	padding-bottom:5px;\n"
"	margin-top:5px;\n"
"	background:rgba(0,0,0,30);\n"
"	}\n"
"\n"
"QPushButton:hover {\n"
"	background:rgba(0,0,0,50);\n"
"	}")
        self.i_o_frame.setFrameShape(QFrame.StyledPanel)
        self.i_o_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.i_o_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.prepareButton = QPushButton(self.i_o_frame)
        self.prepareButton.setObjectName(u"prepareButton")

        self.verticalLayout.addWidget(self.prepareButton)

        self.resultsButton = QPushButton(self.i_o_frame)
        self.resultsButton.setObjectName(u"resultsButton")

        self.verticalLayout.addWidget(self.resultsButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 2)
        self.verticalLayout.setStretch(3, 8)

        self.horizontalLayout.addWidget(self.i_o_frame)

        self.prepareWidget = QWidget(self.centralwidget)
        self.prepareWidget.setObjectName(u"prepareWidget")
        self.prepareWidget.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0,0,0,30);\n"
"color:rgb(190, 190, 190)\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(0,0,0,50);}")
        self.verticalLayout_2 = QVBoxLayout(self.prepareWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.logo_and_select = QHBoxLayout()
        self.logo_and_select.setObjectName(u"logo_and_select")
        self.logo_and_select.setContentsMargins(10, -1, 10, -1)
        self.type_select = QComboBox(self.prepareWidget)
        self.type_select.setObjectName(u"type_select")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.type_select.sizePolicy().hasHeightForWidth())
        self.type_select.setSizePolicy(sizePolicy)

        self.logo_and_select.addWidget(self.type_select)

        self.hspacer_logo = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.logo_and_select.addItem(self.hspacer_logo)

        self.logo = QLabel(self.prepareWidget)
        self.logo.setObjectName(u"logo")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy1)
        self.logo.setMinimumSize(QSize(300, 100))
        self.logo.setMaximumSize(QSize(300, 100))
        self.logo.setPixmap(QPixmap(u":/ui/erc_logo.png"))
        self.logo.setScaledContents(True)

        self.logo_and_select.addWidget(self.logo)

        self.logo_and_select.setStretch(0, 5)
        self.logo_and_select.setStretch(1, 3)

        self.verticalLayout_2.addLayout(self.logo_and_select)

        self.loadedFilesLabel = QLabel(self.prepareWidget)
        self.loadedFilesLabel.setObjectName(u"loadedFilesLabel")

        self.verticalLayout_2.addWidget(self.loadedFilesLabel)

        self.ingest_data_list = QListWidget(self.prepareWidget)
        self.ingest_data_list.setObjectName(u"ingest_data_list")

        self.verticalLayout_2.addWidget(self.ingest_data_list)

        self.propertiesLabel = QLabel(self.prepareWidget)
        self.propertiesLabel.setObjectName(u"propertiesLabel")

        self.verticalLayout_2.addWidget(self.propertiesLabel)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, 0, -1)
        self.properties_view = QTableWidget(self.prepareWidget)
        self.properties_view.setObjectName(u"properties_view")

        self.horizontalLayout_3.addWidget(self.properties_view)

        self.propertiesLayout = QVBoxLayout()
        self.propertiesLayout.setObjectName(u"propertiesLayout")
        self.pcefButton = QPushButton(self.prepareWidget)
        self.pcefButton.setObjectName(u"pcefButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pcefButton.sizePolicy().hasHeightForWidth())
        self.pcefButton.setSizePolicy(sizePolicy2)

        self.propertiesLayout.addWidget(self.pcefButton)

        self.capacityButton = QPushButton(self.prepareWidget)
        self.capacityButton.setObjectName(u"capacityButton")

        self.propertiesLayout.addWidget(self.capacityButton)


        self.horizontalLayout_3.addLayout(self.propertiesLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.button_controls = QHBoxLayout()
        self.button_controls.setObjectName(u"button_controls")
        self.templateButton = QPushButton(self.prepareWidget)
        self.templateButton.setObjectName(u"templateButton")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.templateButton.sizePolicy().hasHeightForWidth())
        self.templateButton.setSizePolicy(sizePolicy3)

        self.button_controls.addWidget(self.templateButton)

        self.line_2 = QFrame(self.prepareWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_2.setFrameShape(QFrame.Shape.VLine)

        self.button_controls.addWidget(self.line_2)

        self.newDataBaseButton = QPushButton(self.prepareWidget)
        self.newDataBaseButton.setObjectName(u"newDataBaseButton")
        sizePolicy1.setHeightForWidth(self.newDataBaseButton.sizePolicy().hasHeightForWidth())
        self.newDataBaseButton.setSizePolicy(sizePolicy1)

        self.button_controls.addWidget(self.newDataBaseButton)

        self.loadDataBaseButton = QPushButton(self.prepareWidget)
        self.loadDataBaseButton.setObjectName(u"loadDataBaseButton")
        sizePolicy3.setHeightForWidth(self.loadDataBaseButton.sizePolicy().hasHeightForWidth())
        self.loadDataBaseButton.setSizePolicy(sizePolicy3)

        self.button_controls.addWidget(self.loadDataBaseButton)

        self.line_3 = QFrame(self.prepareWidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.button_controls.addWidget(self.line_3)

        self.addButton = QPushButton(self.prepareWidget)
        self.addButton.setObjectName(u"addButton")
        sizePolicy1.setHeightForWidth(self.addButton.sizePolicy().hasHeightForWidth())
        self.addButton.setSizePolicy(sizePolicy1)

        self.button_controls.addWidget(self.addButton)

        self.exportButton = QPushButton(self.prepareWidget)
        self.exportButton.setObjectName(u"exportButton")
        sizePolicy3.setHeightForWidth(self.exportButton.sizePolicy().hasHeightForWidth())
        self.exportButton.setSizePolicy(sizePolicy3)

        self.button_controls.addWidget(self.exportButton)


        self.verticalLayout_2.addLayout(self.button_controls)

        self.line = QFrame(self.prepareWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.filesPreview = QLabel(self.prepareWidget)
        self.filesPreview.setObjectName(u"filesPreview")

        self.verticalLayout_2.addWidget(self.filesPreview)

        self.preview = QHBoxLayout()
        self.preview.setObjectName(u"preview")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.savePreviewButton = QPushButton(self.prepareWidget)
        self.savePreviewButton.setObjectName(u"savePreviewButton")

        self.verticalLayout_3.addWidget(self.savePreviewButton)

        self.modifyPreviewButton = QPushButton(self.prepareWidget)
        self.modifyPreviewButton.setObjectName(u"modifyPreviewButton")

        self.verticalLayout_3.addWidget(self.modifyPreviewButton)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 1)
        self.verticalLayout_3.setStretch(2, 8)

        self.preview.addLayout(self.verticalLayout_3)

        self.previewTable = QTableWidget(self.prepareWidget)
        self.previewTable.setObjectName(u"previewTable")

        self.preview.addWidget(self.previewTable)

        self.preview.setStretch(0, 1)
        self.preview.setStretch(1, 8)

        self.verticalLayout_2.addLayout(self.preview)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(2, 5)
        self.verticalLayout_2.setStretch(4, 2)
        self.verticalLayout_2.setStretch(5, 1)
        self.verticalLayout_2.setStretch(8, 5)

        self.horizontalLayout.addWidget(self.prepareWidget)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 9)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 925, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionLoad_File_Ctrl_O)
        self.menuFile.addAction(self.actionChange_Default_Template_Output)
        self.menuFile.addAction(self.actionChange_HTML_Output)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionLoad_File_Ctrl_O.setText(QCoreApplication.translate("MainWindow", u"Load File (Ctrl+O)", None))
        self.actionChange_Default_Template_Output.setText(QCoreApplication.translate("MainWindow", u"Change Default Template Output", None))
        self.actionChange_HTML_Output.setText(QCoreApplication.translate("MainWindow", u"Change HTML Output", None))
        self.prepareButton.setText(QCoreApplication.translate("MainWindow", u"Prepare", None))
        self.resultsButton.setText(QCoreApplication.translate("MainWindow", u"Results", None))
        self.type_select.setPlaceholderText(QCoreApplication.translate("MainWindow", u"[Select Analaysis Type]", None))
        self.logo.setText("")
        self.loadedFilesLabel.setText(QCoreApplication.translate("MainWindow", u"Loaded Files", None))
        self.propertiesLabel.setText(QCoreApplication.translate("MainWindow", u"Properties:", None))
        self.pcefButton.setText(QCoreApplication.translate("MainWindow", u"PCEF", None))
        self.capacityButton.setText(QCoreApplication.translate("MainWindow", u"Capacity", None))
        self.templateButton.setText(QCoreApplication.translate("MainWindow", u"Generate File Template", None))
        self.newDataBaseButton.setText(QCoreApplication.translate("MainWindow", u"New Database", None))
        self.loadDataBaseButton.setText(QCoreApplication.translate("MainWindow", u"Load Database", None))
        self.addButton.setText(QCoreApplication.translate("MainWindow", u"Add Survey File", None))
        self.exportButton.setText(QCoreApplication.translate("MainWindow", u"Export to Database", None))
        self.filesPreview.setText(QCoreApplication.translate("MainWindow", u"File Preview", None))
        self.savePreviewButton.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.modifyPreviewButton.setText(QCoreApplication.translate("MainWindow", u"Modify", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

