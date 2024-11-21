import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from ui.ui import Ui_MainWindow
import ui.resources as resources
from pathlib import Path
import shutil
from PyQt6.QtCore import QAbstractTableModel, Qt
from PyQt6.QtGui import QShortcut
from misc.database import generate_database, FileManager, file_check
import openpyxl as xl

class TableModel(QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            return self._data[index.row()][index.column()]
    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)
    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data[0])

type_properties = {
    "TVC: 4-Leg Intersection": {
        "template": Path(r"bin/essential data/4-Leg Template.xlsx"),
        "type": "4LI",
        "schema": Path(r"bin/database_format/tvc_schema.json")
    },
    "TVC: 3-Leg Intersection": {
        "template": Path(r"bin/essential data/3-Leg Template.xlsx"),
        "type": "3LI",
        "schema": Path(r"bin/database_format/tvc_schema.json")
    },
    "TVC: Midblock": {
        "template": Path(r"bin/essential data/Midblock Template.xlsx"),
        "type": "MB",
        "schema": Path(r"bin/database_format/tvc_schema.json")
    },
    "Spot Speed": {
        "template": Path(r"bin/essential data/Spot Speed Template.xlsx"),
        "type": "Spot Speed",
        "schema": Path(r"bin/database_format/sss_schema.json")
    }
}

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        
        super().__init__()
        
        self.setupUi(self)

        
        self.type_select.addItems(list(type_properties.keys()))
        self.type_select.setCurrentIndex(0)
        #init all_files
        self.storage = FileManager()

        #Disables the pcef and run button
        self.pcefButton.setEnabled(False)
        self.exportButton.setEnabled(False)

        #init statusbar
        self.statusbar.showMessage("Welcome Back!")

        #Connects
        self.addButton.clicked.connect(self.add_survey_file)  #function for adding survey
        self.templateButton.clicked.connect(self.generate_template)  #function for generating template
        self.newDataBaseButton.clicked.connect(self.create_database)  #function for creating database
        self.deleteSurveyButton.clicked.connect(self.delete_survey)  #function for deleting survey

        #Actions
        self.delete_key = QShortcut("Delete", self)
        self.delete_key.activated.connect(self.delete_survey)


    def generate_template(self):
        """
        Generates a template for the selected survey type in the specified folder.

        Returns:
            bool: True if the template was generated successfully, False otherwise.
        """
        
        current_survey = self.type_select.currentText()
        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder", "", QFileDialog.Option.ShowDirsOnly)
        
        #Checks if there is a template available for the selected survey type
        try:
            template = type_properties[current_survey]["template"]
            pcef = os.path.join(os.getcwd(),'bin\essential data\PCEF.xlsx')
            shutil.copy(template, Path(folder_path))
            shutil.copy(pcef, Path(folder_path))
            self.statusbar.showMessage(f"Template generated successfully: {folder_path}")
            print(f"Template generated successfully: {folder_path}")

        except FileNotFoundError:   #File not found
            print("File not found")
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Critical)
            msg.setText("File not found")
            msg.setInformativeText("Please reinstall the program or contact the development team")
            msg.setWindowTitle("Error")
            msg.exec()

            return False
        
        return True

    def add_survey_file(self):
        """
        Opens a file dialog for the user to select one or more survey files.

        Parameters:
            None

        Returns:
            None
        """
        caption = "Open Survey File"
        initial_dir = ""
        filter = "Excel Files (*.xlsx *.xls)"
        try:
            filenames, selected_filter = QFileDialog.getOpenFileNames(self, 
                                                    caption=caption,
                                                    directory=initial_dir,
                                                    filter=filter)
            for file in filenames:
                valid = file_check(file, type_properties[self.type_select.currentText()]['type'])
                if valid == False:
                    QMessageBox.critical(self, "Error", f"Invalid file. {file} is not a valid file. Will skip file.")
                    continue

                #Adds the file to the list (only the basefile without prefixes)
                self.storage.quick_append(file, type_properties[self.type_select.currentText()]['type'])
                self.ingest_data_list.clear()
                self.ingest_data_list.addItems(self.storage.get_storage()['display_name'])
                
        except FileNotFoundError:
            QMessageBox.critical(self, "Error", "No file selected")
        
    def delete_survey(self):
        """
        Deletes a survey file from the list of survey files.

        Parameters:
            None

        Returns:
            None
        """
        if self.ingest_data_list.count() == 0:
            return None
        index = self.ingest_data_list.currentRow()
        self.storage.quick_remove(index)
        self.ingest_data_list.clear()
        self.ingest_data_list.addItems(self.storage.get_storage()['display_name'])

    def create_database(self):
        """
        Creates a new SQLite database based on the selected survey type.

        Retrieves the current survey type from the type_select dropdown menu, 
        then uses the corresponding schema to generate the database. The user 
        is prompted to select a location to save the database. If a location is 
        selected, the database is created and a success message is displayed in 
        the status bar. If no location is selected, an error message is displayed.

        Parameters:
            None

        Returns:
            None
        """
        survey_type = self.type_select.currentText()

        schema = type_properties[survey_type]["schema"]
        try:
            out_path, selected_filer = QFileDialog.getSaveFileName(
                self, "New Database", "", "SQLite Database (*.db)"
            )
        except FileNotFoundError:
            QMessageBox.critical(self, "Error", "No file selected")
        
        generate_database(schema, out_path)
        self.statusbar.showMessage(f"Database created successfully: {out_path}")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()
    app.exec()

