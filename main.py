import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QHeaderView
from ui.ui import Ui_MainWindow
import ui.resources as resources
from pathlib import Path
import shutil
from PyQt6.QtGui import QShortcut
from misc.database import *
from misc.helper import PandasModel
from misc.info import EssentialData

type_properties = EssentialData.TypeProperties

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.type_select.addItems(list(type_properties.keys()))
        self.type_select.setCurrentIndex(0)
        #init all_files
        self.storage = FileManager()

        #Disables the exportButton
        self.exportButton.setEnabled(False)

        #init statusbar
        self.statusbar.showMessage("Welcome Back!")

        #Connects
        self.addButton.clicked.connect(self.add_survey_file)  #function for adding survey
        self.templateButton.clicked.connect(self.generate_template)  #function for generating template
        self.newDataBaseButton.clicked.connect(self.create_database)  #function for creating database
        self.deleteSurveyButton.clicked.connect(self.delete_survey)  #function for deleting survey
        self.exportButton.clicked.connect(self.export_database)

        self.pcefButton.clicked.connect(self.load_pcef)
        self.capacityButton.clicked.connect(self.load_capacity) 

        #Actions
        self.delete_key = QShortcut("Delete", self)
        self.delete_key.activated.connect(self.delete_survey)

        #Events
        self.ingest_data_list.currentTextChanged.connect(self.enable_export)
    
    def load_pcef(self):
        try:
            open_path, selected_filter = QFileDialog.getOpenFileName(self,
                                                    caption="Open PCEF",
                                                    directory="",
                                                    filter="Excel Files (*.xlsx *.xls)")
            if open_path:
                df = pd.read_excel(open_path).transpose()
                tableModel = PandasModel(df)
                self.pcefTable.setModel(tableModel)
                self.pcefTable.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
                self.pcefTable.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
                self.pcefTable.horizontalHeader().setVisible(False)
                self.storage.add_pcef(open_path)
        
        except FileNotFoundError:
            QMessageBox.critical(self, "Error", "No file selected")
            self.statusbar.showMessage("No file selected")
            return None
        
        self.statusbar.showMessage("PCEF loaded successfully")
    
    def load_capacity(self):
        try:
            open_path, selected_filter = QFileDialog.getOpenFileName(self,
                                                    caption="Open Capacity File",
                                                    directory="",
                                                    filter="Excel Files (*.xlsx *.xls)")
            if open_path:
                df = pd.read_excel(open_path).transpose()
                tableModel = PandasModel(df)
                self.capacityTable.setModel(tableModel)
                self.capacityTable.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
                self.capacityTable.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
                self.capacityTable.horizontalHeader().setVisible(False)
                self.storage.add_capacity(open_path)

        except FileNotFoundError:
            QMessageBox.critical(self, "Error", "No file selected")
            self.statusbar.showMessage("No file selected")
            return None
        
        self.statusbar.showMessage("Capcity loaded successfully")
    
    
    def enable_export(self):
        self.pcefButton.setEnabled(True)
        self.exportButton.setEnabled(True)

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
        
        #Generates the Capacity Template
        headers = ['Approach', 'No of Lanes', 'Capacity per Lane', 'Alias']
        current_type = self.get_current_type()
        if current_type == "4LI":
            data = ["North", "South", "East", "West"]
        elif current_type == "3LI":
            data = ["North", "West", "East"]
        elif current_type == "MB":
            data = ["North", "South"]
        else:
            QMessageBox.critical(self, "Error", "Survey Type not supported")
            return False
        
        capacity_path = os.path.join(Path(folder_path), 'Capacity Template.xlsx')
        df = pd.DataFrame({header: [] for header in headers})
        df['Approach'] = data
        df.to_excel(capacity_path, index=False)
        return True

    def get_current_type(self):
        return type_properties[self.type_select.currentText()]['type']
    
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
                try:
                    valid = file_check(file, type_properties[self.type_select.currentText()]['type'])
                    if valid == False:
                        QMessageBox.critical(self, "Error", f"Invalid file. {file} is not a valid file. Will skip file.")
                        continue
                except ValueError:  #Error Handling if the survey type is not supported
                    QMessageBox.critical(self, "Error", f"Invalid file. {file} is not a valid file. Will skip file.")
                
                #Adds the file to the list (only the basefile without prefixes)
                self.storage.quick_append(file, type_properties[self.type_select.currentText()]['type'])
                self.ingest_data_list.clear()
                self.ingest_data_list.addItems(self.storage.get_storage()['display_name'])
            self.statusbar.showMessage(f"Added {len(filenames)} files")
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

    def export_database(self):
        """
        Exports the database based on the selected survey type.

        Retrieves the current survey type from the type_select dropdown menu, 
        then uses the corresponding schema to generate the database. The user 
        is prompted to select a location to save the database. If a location is 
        selected, the database is created and a success message is displayed in 
        the status bar. If no location is selected, an error message is displayed.

        The database is exported with all the surveys in the storage. For each 
        survey, the function will call the corresponding database function to 
        insert the data into the database. If the survey type is not supported, 
        an error message is displayed.

        Parameters:
            None

        Returns:
            None
        """

        current_type = type_properties[self.type_select.currentText()]['type']
        schema = type_properties[self.type_select.currentText()]["schema"]

        out_path, selected_filer = QFileDialog.getSaveFileName(
            self, "New Database", "", "SQLite Database (*.db)"
        )

        generate_database(schema, out_path)

        all_surveys = self.storage.get_storage()['path']
        
        for survey in all_surveys:
            if (current_type == '4LI'):
                fourleg_intersection_to_db(survey, out_path)
            elif (current_type == '3LI'):
                threeleg_intersection_to_db(survey, out_path)
            elif (current_type == 'MB'):
                midblock_to_db(survey, out_path)
            # TODO: Add spot speed
            # if (current_type == 'SSS'):
            #     spot_speed_to_db(survey, out_path)
            else:
                QMessageBox(
                    QMessageBox.Icon.Critical,
                    "Error",
                    f"Survey Type Currently Unavailable: {current_type}",QMessageBox.StandardButton.Ok
                ).exec()

                self.statusbar.showMessage(f"Survey Type Currently Unavailable: {current_type}")
                return None
            
        self.statusbar.showMessage(f"Database created successfully: {out_path}")

        #Adds the PCEF data to the database
        pcef_to_db(self.storage.get_storage()['pcef'], out_path)

        #Adds the Capacity data to the database
        if (current_type == '4LI') or (current_type == '3LI') or (current_type == 'MB'):
            capacity_to_db(self.storage.get_storage()['capacity'], out_path)



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()
    app.exec()