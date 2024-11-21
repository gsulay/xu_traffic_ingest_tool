# Form implementation generated from reading ui file './ui/draft ui.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(747, 679)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setStyleSheet("\n"
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
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.i_o_frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.i_o_frame.setStyleSheet("*{\n"
"background-color:rgb(16, 15, 15);\n"
"}\n"
"\n"
"QFrame#i_o_frame {\n"
"\n"
"    background-color:rgb(49, 42, 44);\n"
"    }\n"
"\n"
"QPushButton{\n"
"    color:rgba(255, 255, 255, 95);\n"
"    font: 15pt \"Futura\";\n"
"    padding-top:5px;\n"
"    padding-bottom:5px;\n"
"    margin-top:5px;\n"
"    background:rgba(0,0,0,30);\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background:rgba(0,0,0,50);\n"
"    }")
        self.i_o_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.i_o_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.i_o_frame.setObjectName("i_o_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.i_o_frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.prepareButton = QtWidgets.QPushButton(parent=self.i_o_frame)
        self.prepareButton.setObjectName("prepareButton")
        self.verticalLayout.addWidget(self.prepareButton)
        self.resultsButton = QtWidgets.QPushButton(parent=self.i_o_frame)
        self.resultsButton.setObjectName("resultsButton")
        self.verticalLayout.addWidget(self.resultsButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 2)
        self.verticalLayout.setStretch(3, 8)
        self.horizontalLayout.addWidget(self.i_o_frame)
        self.prepareWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.prepareWidget.setStyleSheet("QPushButton{\n"
"background-color: rgba(0,0,0,30);\n"
"color:rgb(190, 190, 190)\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(0,0,0,50);}")
        self.prepareWidget.setObjectName("prepareWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.prepareWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.logo_and_select = QtWidgets.QHBoxLayout()
        self.logo_and_select.setContentsMargins(10, -1, 10, -1)
        self.logo_and_select.setObjectName("logo_and_select")
        self.type_select = QtWidgets.QComboBox(parent=self.prepareWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.type_select.sizePolicy().hasHeightForWidth())
        self.type_select.setSizePolicy(sizePolicy)
        self.type_select.setObjectName("type_select")
        self.logo_and_select.addWidget(self.type_select)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.logo_and_select.addItem(spacerItem2)
        self.logo = QtWidgets.QLabel(parent=self.prepareWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setMinimumSize(QtCore.QSize(300, 100))
        self.logo.setMaximumSize(QtCore.QSize(300, 100))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap(":/ui/erc_logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.logo_and_select.addWidget(self.logo)
        self.logo_and_select.setStretch(0, 5)
        self.logo_and_select.setStretch(1, 3)
        self.verticalLayout_2.addLayout(self.logo_and_select)
        self.filesCapacitiesLayout = QtWidgets.QHBoxLayout()
        self.filesCapacitiesLayout.setObjectName("filesCapacitiesLayout")
        self.loadedFilesLayout = QtWidgets.QVBoxLayout()
        self.loadedFilesLayout.setObjectName("loadedFilesLayout")
        self.loadedFilesLabel = QtWidgets.QLabel(parent=self.prepareWidget)
        self.loadedFilesLabel.setObjectName("loadedFilesLabel")
        self.loadedFilesLayout.addWidget(self.loadedFilesLabel)
        self.ingest_data_list = QtWidgets.QListWidget(parent=self.prepareWidget)
        self.ingest_data_list.setObjectName("ingest_data_list")
        self.loadedFilesLayout.addWidget(self.ingest_data_list)
        self.filesCapacitiesLayout.addLayout(self.loadedFilesLayout)
        self.capacityFileLayout = QtWidgets.QVBoxLayout()
        self.capacityFileLayout.setObjectName("capacityFileLayout")
        self.roadCapacityLabel = QtWidgets.QLabel(parent=self.prepareWidget)
        self.roadCapacityLabel.setObjectName("roadCapacityLabel")
        self.capacityFileLayout.addWidget(self.roadCapacityLabel)
        self.capacityTable = QtWidgets.QListWidget(parent=self.prepareWidget)
        self.capacityTable.setObjectName("capacityTable")
        self.capacityFileLayout.addWidget(self.capacityTable)
        self.filesCapacitiesLayout.addLayout(self.capacityFileLayout)
        self.verticalLayout_2.addLayout(self.filesCapacitiesLayout)
        self.propertiesLabel = QtWidgets.QLabel(parent=self.prepareWidget)
        self.propertiesLabel.setObjectName("propertiesLabel")
        self.verticalLayout_2.addWidget(self.propertiesLabel)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.properties_view = QtWidgets.QTableWidget(parent=self.prepareWidget)
        self.properties_view.setObjectName("properties_view")
        self.properties_view.setColumnCount(0)
        self.properties_view.setRowCount(0)
        self.horizontalLayout_3.addWidget(self.properties_view)
        self.propertiesLayout = QtWidgets.QVBoxLayout()
        self.propertiesLayout.setObjectName("propertiesLayout")
        self.pcefButton = QtWidgets.QPushButton(parent=self.prepareWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pcefButton.sizePolicy().hasHeightForWidth())
        self.pcefButton.setSizePolicy(sizePolicy)
        self.pcefButton.setObjectName("pcefButton")
        self.propertiesLayout.addWidget(self.pcefButton)
        self.capacityButton = QtWidgets.QPushButton(parent=self.prepareWidget)
        self.capacityButton.setObjectName("capacityButton")
        self.propertiesLayout.addWidget(self.capacityButton)
        self.horizontalLayout_3.addLayout(self.propertiesLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.button_controls = QtWidgets.QHBoxLayout()
        self.button_controls.setObjectName("button_controls")
        self.templateButton = QtWidgets.QPushButton(parent=self.prepareWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.templateButton.sizePolicy().hasHeightForWidth())
        self.templateButton.setSizePolicy(sizePolicy)
        self.templateButton.setObjectName("templateButton")
        self.button_controls.addWidget(self.templateButton)
        self.line_2 = QtWidgets.QFrame(parent=self.prepareWidget)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_2.setObjectName("line_2")
        self.button_controls.addWidget(self.line_2)
        self.newDataBaseButton = QtWidgets.QPushButton(parent=self.prepareWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newDataBaseButton.sizePolicy().hasHeightForWidth())
        self.newDataBaseButton.setSizePolicy(sizePolicy)
        self.newDataBaseButton.setObjectName("newDataBaseButton")
        self.button_controls.addWidget(self.newDataBaseButton)
        self.line_3 = QtWidgets.QFrame(parent=self.prepareWidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.button_controls.addWidget(self.line_3)
        self.addButton = QtWidgets.QPushButton(parent=self.prepareWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addButton.sizePolicy().hasHeightForWidth())
        self.addButton.setSizePolicy(sizePolicy)
        self.addButton.setObjectName("addButton")
        self.button_controls.addWidget(self.addButton)
        self.deleteSurveyButton = QtWidgets.QPushButton(parent=self.prepareWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deleteSurveyButton.sizePolicy().hasHeightForWidth())
        self.deleteSurveyButton.setSizePolicy(sizePolicy)
        self.deleteSurveyButton.setObjectName("deleteSurveyButton")
        self.button_controls.addWidget(self.deleteSurveyButton)
        self.line_4 = QtWidgets.QFrame(parent=self.prepareWidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_4.setObjectName("line_4")
        self.button_controls.addWidget(self.line_4)
        self.exportButton = QtWidgets.QPushButton(parent=self.prepareWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exportButton.sizePolicy().hasHeightForWidth())
        self.exportButton.setSizePolicy(sizePolicy)
        self.exportButton.setObjectName("exportButton")
        self.button_controls.addWidget(self.exportButton)
        self.verticalLayout_2.addLayout(self.button_controls)
        self.line = QtWidgets.QFrame(parent=self.prepareWidget)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.filesPreview = QtWidgets.QLabel(parent=self.prepareWidget)
        self.filesPreview.setObjectName("filesPreview")
        self.verticalLayout_2.addWidget(self.filesPreview)
        self.preview = QtWidgets.QHBoxLayout()
        self.preview.setObjectName("preview")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.savePreviewButton = QtWidgets.QPushButton(parent=self.prepareWidget)
        self.savePreviewButton.setObjectName("savePreviewButton")
        self.verticalLayout_3.addWidget(self.savePreviewButton)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)
        self.verticalLayout_3.setStretch(1, 1)
        self.verticalLayout_3.setStretch(2, 8)
        self.preview.addLayout(self.verticalLayout_3)
        self.previewTable = QtWidgets.QTableWidget(parent=self.prepareWidget)
        self.previewTable.setObjectName("previewTable")
        self.previewTable.setColumnCount(0)
        self.previewTable.setRowCount(0)
        self.preview.addWidget(self.previewTable)
        self.preview.setStretch(1, 8)
        self.verticalLayout_2.addLayout(self.preview)
        self.verticalLayout_2.setStretch(1, 3)
        self.verticalLayout_2.setStretch(3, 1)
        self.verticalLayout_2.setStretch(5, 1)
        self.verticalLayout_2.setStretch(7, 2)
        self.horizontalLayout.addWidget(self.prepareWidget)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 9)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 747, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLoad_File_Ctrl_O = QtGui.QAction(parent=MainWindow)
        self.actionLoad_File_Ctrl_O.setObjectName("actionLoad_File_Ctrl_O")
        self.actionChange_Default_Template_Output = QtGui.QAction(parent=MainWindow)
        self.actionChange_Default_Template_Output.setObjectName("actionChange_Default_Template_Output")
        self.actionChange_HTML_Output = QtGui.QAction(parent=MainWindow)
        self.actionChange_HTML_Output.setObjectName("actionChange_HTML_Output")
        self.menuFile.addAction(self.actionLoad_File_Ctrl_O)
        self.menuFile.addAction(self.actionChange_Default_Template_Output)
        self.menuFile.addAction(self.actionChange_HTML_Output)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.prepareButton.setText(_translate("MainWindow", "Prepare"))
        self.resultsButton.setText(_translate("MainWindow", "Results"))
        self.type_select.setPlaceholderText(_translate("MainWindow", "[Select Analaysis Type]"))
        self.loadedFilesLabel.setText(_translate("MainWindow", "Loaded Files"))
        self.roadCapacityLabel.setText(_translate("MainWindow", "Road Capacities"))
        self.propertiesLabel.setText(_translate("MainWindow", "Properties:"))
        self.pcefButton.setText(_translate("MainWindow", "PCEF"))
        self.capacityButton.setText(_translate("MainWindow", "Capacity"))
        self.templateButton.setText(_translate("MainWindow", "Generate File Template"))
        self.newDataBaseButton.setText(_translate("MainWindow", "New Database"))
        self.addButton.setText(_translate("MainWindow", "Add Survey File"))
        self.deleteSurveyButton.setText(_translate("MainWindow", "Delete Survey File"))
        self.exportButton.setText(_translate("MainWindow", "Export to Database"))
        self.filesPreview.setText(_translate("MainWindow", "Properties View"))
        self.savePreviewButton.setText(_translate("MainWindow", "Load Project Details"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionLoad_File_Ctrl_O.setText(_translate("MainWindow", "Load File (Ctrl+O)"))
        self.actionChange_Default_Template_Output.setText(_translate("MainWindow", "Change Default Template Output"))
        self.actionChange_HTML_Output.setText(_translate("MainWindow", "Change HTML Output"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
