"""
File       : app_list_panel.py
Author     : Fluffy Flower (Martin Wylde)
Contact    :
    Email   - martincw1989@gmail.com
    Telegram- @FluffyFlower
    Discord - fluffy_flower
Date       : 13/03/2025
Version    : 0.9.2
Description: Application list panel with a table for displaying app details, allowing users to add applications,
             edit names, and display parsed app info.
"""

# ------------------------------------------------------ #
#                                                        #
# ██████                                                 #
#   ██    ██  ██  ████    ██████    ████    ██      ████ #
#   ██    ██████  ██  ██  ██  ██  ██      ██████    ██   #
#   ██    ██████  ██████  ██  ██  ██        ██      ██   #
# ██████  ██  ██  ██      ██████  ██        ████  ████   #
#                                                        #
# ------------------------------------------------------ #
import os
import re
import pefile
from PyQt6.QtWidgets import QLabel, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QFileDialog, QMessageBox, QRadioButton
from PyQt6.QtCore import Qt
from Window.json_handler import AppJSONHandler


# ------------------------------------------------------------------------------------------------------------ #
#                                                                                                              #
# ██████                          ██      ██                            ██████                                 #
# ██  ██  ████    ████            ██              ████    ██            ██  ██    ████  ██████    ████  ██     #
# ██████  ██  ██  ██  ██          ██      ██      ██    ██████          ██████  ██  ██  ██  ██  ██  ██  ██     #
# ██  ██  ██████  ██████          ██      ██      ██      ██            ██      ██  ██  ██  ██  ████    ██     #
# ██  ██  ██      ██              ██████  ████  ████      ████          ██      ██████  ██  ██    ████  ██████ #
#                                                                                                              #
# ------------------------------------------------------------------------------------------------------------ #


class AppListPanel(QWidget):

    # Global constants creation
    _RADIO_BUTTON_COL: int = 0
    _APP_EXE_COL: int = 1
    _APP_NAME_COL: int = 2
    _APP_GAPI_COL: int = 3
    _APP_PATH_COL: int = 4

    # Create class variable for linking to the JSON handling class.
    _json_handler = AppJSONHandler()

    # ------------------------------------------------------------------------------ #
    # Panel initialisation & table creation.                                         #
    # ------------------------------------------------------------------------------ #
    def __init__(self) -> None:
        """
        Initializes the AppListPanel widget.

        Args:
            None.

        Returns:
            None.

        Examples:
            Default Usage:
                .. code-block:: python
                >>> variable = AppListPanel()
        """
        super().__init__()

        # Create QVBoxLayout.
        self.setLayout(QVBoxLayout())

        # Create a panel label and add it to the layout (HTML used for rich text formatting).
        label_text: str = "Applications"
        self.label = QLabel(f"<html><body><h3><b><u>{label_text}</u></b></h3></body></html>")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout().addWidget(self.label)

        # Add application list table.
        self.app_table = QTableWidget()
        self.app_table.setColumnCount(5)
        self.app_table.setHorizontalHeaderLabels(["Selected", "File", "App Name", "Graphics API", "Path"])
        self.app_table.setColumnWidth(self._RADIO_BUTTON_COL, 75)   # Radio buttons column for selecting entries
        self.app_table.setColumnWidth(self._APP_EXE_COL, 150)  # File name column
        self.app_table.setColumnWidth(self._APP_NAME_COL, 200)  # Editable application name column
        self.app_table.setColumnWidth(self._APP_GAPI_COL, 150)  # GAPI Version column
        self.app_table.setColumnWidth(self._APP_PATH_COL, 300)  # Full path column
        self.layout().addWidget(self.app_table)

        # Create button layout.
        button_layout = QHBoxLayout()

        # Add buttons to add & delete applications.
        self.add_app_button = QPushButton("Add Application")
        self.del_app_button = QPushButton("Delete Application")

        # Add buttons to button layout.
        button_layout.addWidget(self.add_app_button)
        button_layout.addWidget(self.del_app_button)

        # Add button layout to main layout.
        self.layout().addLayout(button_layout)

        # Connect button click signal to handler.
        self.add_app_button.clicked.connect(self.add_application)
        self.del_app_button.clicked.connect(self.delete_application)

        # Check for changes to 'App Name' field.
        self.app_table.cellChanged.connect(self.update_application_name)

        # Load applications from file on startup.
        self.load_applications()

    # ------------------------------------------------------------------------------ #
    # Application selection & duplicate selection check.                             #
    # ------------------------------------------------------------------------------ #
    def add_application(self) -> None:
        """
        Opens file dialog and prepares for adding selected applications details to the table.

        Args:
            None.

        Returns:
            None.

        Examples:
            Default Usage:
                .. code-block:: python
                >>> .add_application()
        """
        # Create file dialog.
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)

        # File filters.
        filters = "Windows Executables (*.exe);;Shell Scripts (*.sh);;Batch Files (*.bat);;All Files (*)"
        file_path, selected_filter = file_dialog.getOpenFileName(self, "Select Application", "", filters)

        # Check selected file is not already added (file path check), if not then add to table.
        if file_path:
            if not self.is_app_already_added(file_path):
                self.add_application_to_table(file_path)
                self.save_application(file_path)
            else:
                QMessageBox.warning(self, "Duplicate Entry", "This application is already in the list.")

    # ------------------------------------------------------------------------------ #
    # Add applications to table.                                                     #
    # ------------------------------------------------------------------------------ #
    def add_application_to_table(self, 
                                 file_path_input: str, 
                                 app_name_input: str = None, 
                                 gapi_input: str = None) -> None:
        """
        Adds application details to the table, using saved values when available.

        Args:
            file_path(str): Application path of application to be added to table.
            app_name(str): Application name of application to be added to table.
            gapi(str): Applications reported DX version to be added to table.

        Returns:
            None.

        Examples:
            Default Usage:
                .. code-block:: python
                >>> .add_application_to_table("/path/to/application", "application name", "Graphics API")
        """
        # Get method input arguments and store in method for use.
        file_path: str = file_path_input
        file_name: str = os.path.basename(file_path)
        app_name: str = app_name_input
        gapi: str = gapi_input

        new_add: bool = False

        # Check if app_name contains any values.
        if not app_name:  # Only extract if not loaded from JSON.
            QMessageBox.information(self, "Slow Operation", '<p>Application name and graphics API detection may take a few moments..</p>\n\n<p style="color: FireBrick; font-weight: bold;">DO NOT CLOSE THE APPLICATION!!</p>\n\n<p>Press OK to proceed with the operation.</p>')
            new_add = True
            app_name = self.extract_app_name(file_path) or file_name.split(".")[0]

        # Check if gapi contains any values
        if not gapi:
            gapi = self.detect_gapi_version(file_path)

        # Get physical row count to insert new row at end of table.
        row_position: int = self.app_table.rowCount()
        self.app_table.insertRow(row_position)

        # Populate row cells with provided data.
        entry_selection = QRadioButton()
        self.app_table.setCellWidget(row_position, self._RADIO_BUTTON_COL, entry_selection)

        file_item = QTableWidgetItem(file_name)
        file_item.setFlags(Qt.ItemFlag.ItemIsEnabled)
        self.app_table.setItem(row_position, self._APP_EXE_COL, file_item)

        name_item = QTableWidgetItem(app_name)
        name_item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEditable | Qt.ItemFlag.ItemIsEnabled)
        self.app_table.setItem(row_position, self._APP_NAME_COL, name_item)

        gapi_item = QTableWidgetItem(gapi)
        gapi_item.setFlags(Qt.ItemFlag.ItemIsEnabled)
        self.app_table.setItem(row_position, self._APP_GAPI_COL, gapi_item)

        path_item = QTableWidgetItem(file_path)
        path_item.setFlags(Qt.ItemFlag.ItemIsEnabled)
        self.app_table.setItem(row_position, self._APP_PATH_COL, path_item)

        if new_add == True:
            QMessageBox.information(self, "Operation Complete", '<p>Application name and graphics API detection complete!</p>')

    # ------------------------------------------------------------------------------ #
    # Extract application real name using pefile.                                    #
    # ------------------------------------------------------------------------------ #
    def extract_app_name(self, 
                         file_path_input: str) -> str | None:
        """
        Extracts the actual application name from EXE metadata using pefile.

        Args:
            file_path(str): String containing application path of application to extract real name from.

        Returns:
            app_name(str): String containing applications extracted real name.
            None: If no name extracted.

        Raises:
            Exception: Extraction failure, returns 'None'.

        Examples:
            Default Usage:
                .. code-block:: python
                >>> .extract_app_name("/path/to/application")
                "Application Name"  # Application name extraction success
                >>> .extract_app_name("/path/to/application")
                None  # Application name extraction failure
        """
        # Get method input arguments and store in method for use.
        file_path: str = file_path_input

        # Check if selected file has the .exe extension.
        if not file_path.endswith(".exe"):
            return None  # Return None if not a .exe.

        # Try to pull application real name from applications .exe using pefile.
        try:
            pe: pefile.PE = pefile.PE(file_path)
            if hasattr(pe, 'FileInfo'):
                for file_info in pe.FileInfo:
                    if (hasattr(file_info, 'StringTable')):
                        for entry in file_info:
                            if (hasattr(entry, 'entries')):
                                if "FileDescription" in entry.entries:
                                    app_name: str = entry.entries["FileDescription"].decode(errors="ignore")
                                    return app_name
                                else:
                                    return None
                            else:
                                return None
                    else:
                        return None
            else:
                return None

        except (Exception, pefile.PEFormatError) as e:
            if not isinstance(e, pefile.PEFormatError):
                # Program should never reach this point.
                print("How did you get here? What have you done? >0_o<???\nAn unexpected error has occurred during application name extraction! Please report this issue, with terminal output where possible!")
            return None

    # ------------------------------------------------------------------------------ #
    # Detect Graphics API (GAPI) type / version using pefile to scan for linked DLLs #
    # ------------------------------------------------------------------------------ #
    def detect_gapi_version(self, 
                            file_path_input: str) -> str:
        """
        Detects the GAPI type / version by scanning linked DLLs.

        Args:
            file_path(String): Application path of application to extract GAPI type / version from.

        Returns:
            gapi_ver(String): Detected applications GAPI type / version, 'N/A' if file is not a .exe or not detected, 'Unknown' if exception raised.

        Raises:
            Exception: Returns GAPI_ver with value 'Unknown'.

        Examples:
            Default Usage:
                .. code-block:: python
                >>> .detect_gapi_version("/path/to/application")
                "N/A"  # Default value, and value assigned when application is not .exe
                >>> .detect_gapi_version("/path/to/application")
                "OpenGL"  # Value assigned if opengl32.dll links detected
                >>> .detect_gapi_version("/path/to/application")
                "Vulkan"  # Value assigned if vulkan-1.dll links detected
                >>> .detect_gapi_version("/path/to/application")
                "DirectX 12"  # Value assigned if d3d12.dll links detected
                >>> .detect_gapi_version("/path/to/application")
                "DirectX 11"  # Value assigned if d3d11.dll links detected
                >>> .detect_gapi_version("/path/to/application")
                "DirectX 10"  # Value assigned if d3d10.dll links detected
                >>> .detect_gapi_version("/path/to/application")
                "DirectX 9"  # Value assigned if d3d9.dll links detected
                >>> .detect_gapi_version("/path/to/application")
                "Unknown"  # Value assigned if dll link detection fails
        """
        # Get method input arguments and store in method for use.
        file_path: str = file_path_input

        # Create gapi_ver string variable and set to 'None'.
        gapi_ver: str = None

        # Check selected application has the .exe extension.
        if not file_path.endswith(".exe"):
            gapi_ver = "N/A"  # Set to N/A if file is not a .exe.
            return gapi_ver

        # Try to pull GAPI type / version from applications .exe using pefile.
        try:
            pe: pefile.PE = pefile.PE(file_path)
            if (hasattr(pe, 'DIRECTORY_ENTRY_IMPORT')):
                imported_dlls = [entry.dll.decode().lower() for entry in pe.DIRECTORY_ENTRY_IMPORT]

                # Check in case OpenGL
                if "opengl32.dll" in imported_dlls:
                    gapi_ver = "OpenGL"
                    return gapi_ver
                
                # Check in case Vulkan
                if "vulkan-1.dll" in imported_dlls:
                    gapi_ver = "Vulkan"
                    return gapi_ver
                
                # Create dictionary of possible DirectX versions
                dx_dll_patterns: dict = {
                    r"d3d12(_\d+)?\.dll": "DirectX 12",
                    r"d3d11(_\d+)?\.dll": "DirectX 11",
                    r"d3d10(_\d+)?\.dll": "DirectX 10",
                    r"d3d9(_\d+)?\.dll": "DirectX 9",
                }

                # Compare output to get right DirectX version, set to DX_ver string, and return.
                for dll_pattern, version in dx_dll_patterns.items():
                    for dll in imported_dlls:
                        if re.match(dll_pattern, dll):
                            gapi_ver = version
                            return gapi_ver

                gapi_ver = "N/A"
                return gapi_ver
            
            else:
                gapi_ver = "N/A"
                return gapi_ver

        except (Exception, pefile.PEFormatError) as e:
            gapi_ver = "Unknown"
            if not isinstance(e, pefile.PEFormatError):
                # Program should never reach this point!!
                print("How did you get here? What have you done? >0_o<???\nAn unexpected error has occurred during application name extraction! Please report this issue, with terminal output where possible!")
            return gapi_ver

    # ------------------------------------------------------------------------------ #
    # Save application list to JSON file for recall on fresh load                    #
    # ------------------------------------------------------------------------------ #
    def save_application(self, 
                         file_path_input: str) -> None:
        """
        Save the application details to user_apps.json, using json_handler.py.

        Args:
            file_path(String): Application path of application to be saved to user_apps.json using json_handler.py.

        Returns:
            None.

        Examples:
            Default Usage:
                .. code-block:: python
                >>> .save_application("/path/to/application")
        """
        # Get method input arguments and store in method for use.
        file_path: str = file_path_input

        # Set app_name from .exe using extract_app_name() or setting it to 'apps_name.exe'.
        app_name: str = self.extract_app_name(file_path) or os.path.basename(file_path).split(".")[0]

        # Set gapi from .exe using detect_gapi_version().
        gapi: str = self.detect_gapi_version(file_path)

        # Create a dictionary variable called data and load JSON data into it.
        data: dict = self._json_handler.load_app_details()

        # Check for duplicates before saving, if duplicate found, break.
        if any(entry["app_path"] == file_path for entry in data["applications"]):
            return  # Skip saving duplicates

        # Append new entry and save.
        self._json_handler.add_new_app(app_name, file_path, gapi)

    # ------------------------------------------------------------------------------ #
    # Retrieve application details from JSON file on load                            #
    # ------------------------------------------------------------------------------ #
    def load_applications(self) -> None:
        """
        Load applications from user_apps.json, using json_handler.py.

        Args:
            None.

        Returns:
            None.

        Examples:
            Default Usage:
                .. code-block:: python
                >>> .load_applications()
        """
        # Create a dictionary variable alled data and load JSON data into it.
        data: dict = self._json_handler.load_app_details()

        # Iterate through app entries in dictionary and add each in turn to table.
        for app in data.get("applications", []):
            self.add_application_to_table(app["app_path"], app["app_name"], app["app_gapi"])

    # ------------------------------------------------------------------------------ #
    # Check if application is already in the table                                   #
    # ------------------------------------------------------------------------------ #
    def is_app_already_added(self, 
                             file_path_input: str) -> bool:
        """
        Check if application is already in the table.

        Args:
            file_path(String): Application path of application to run check against.

        Returns:
            (bool): Either 'True' if application is already in table, or 'False' if not in table.

        Examples:
            Default Usage:
                .. code-block:: python
                >>> .is_app_already_added("/path/to/application")
                True  # Application duplicate has been found
                >>> .is_app_already_added("/path/to/application")
                False  # Application duplicate has not been found
        """
        # Get method input arguments and store in method.
        file_path: str = file_path_input

        # Check each rows fifth (path) column to check for potential duplicate entry insertion
        for row in range(self.app_table.rowCount()):
            if self.app_table.item(row, 4).text() == file_path:
                return True

        return False  # If no duplicate found return 'False'

    # ------------------------------------------------------------------------------ #
    # Allow user inputted application name & save to JSON file                       #
    # ------------------------------------------------------------------------------ #
    def update_application_name(self, 
                                row_input: int, 
                                column_input: int) -> None:
        """
        Update JSON when an app name is edited in the table.

        Args:
            row(int): Row number of selected application to update application name.
            column(int): Column number to make sure only 'App Name' is being updated.

        Returns:
            None.

        Examples:
            Default Usage:
                .. code-block:: python
                >>> .update_application_name(n, 0)  # row input 'n' can be any int in range, 0 is an impossible column selection
                >>> .update_application_name(n, 1)  # row input 'n' can be any int in range, 1 is an impossible column selection
                >>> .update_application_name(n, 2)  # row input 'n' can be any int in range, 2 means execution continues as normal
                >>> .update_application_name(n, 3)  # row input 'n' can be any int in range, 3 is an impossible column selection
                >>> .update_application_name(n, 4)  # row input 'n' can be any int in range, 4 is an impossible column selection
        """
        # Get method input arguments and store in method
        row: int = row_input
        column: int = column_input

        # Check selected column is second (App Name) column; it should always be the second column.
        if column != self._APP_NAME_COL:  # We only care about the 'App Name' column.
            return

        # Assign path to widget.
        app_path_item = self.app_table.item(row, self._APP_PATH_COL)

        # If path empty / None, return.
        if app_path_item is None:
            return

        # Set new variables name to new_name string, and path to app_path from tables current values.
        new_name: str = self.app_table.item(row, column).text()
        app_path: str = app_path_item.text()  # Get the app's path.

        # If either name or path variables are empty, return.
        if not new_name or not app_path:
            return  # Avoid empty names or missing data.

        # Load current JSON data.
        data: dict = self._json_handler.load_app_details()

        # Find and update the correct app entry.
        for app in data["applications"]:
            if app["app_path"] == app_path:
                app["app_name"] = new_name
                break

        # Save back to JSON.
        self._json_handler.save_app_details(data)

    # ------------------------------------------------------------------------------ #
    # Delete selected application from the list and JSON                             #
    # ------------------------------------------------------------------------------ #
    def delete_application(self) -> None:
        """
        Deletes the selected application from the table and user_apps.json using json_handler.py.

        Args:
            None.

        Returns:
            None.

        Examples:
            Default Usage:
                .. code-block:: python
                >>> .delete_application()
        """
        # Set selected_row to impossible arbitrary value.
        selected_row = -1

        # Find the selected radio button.
        for row in range(self.app_table.rowCount()):
            radio_button = self.app_table.cellWidget(row, self._RADIO_BUTTON_COL)
            if radio_button is not None and radio_button.isChecked():
                selected_row = row
                break

        # If selected row equals default value, no value has obviously been selected.
        if selected_row == -1:
            QMessageBox.warning(self, "No Selection", "Please select an application to delete!")
            return

        # Get file path of the selected application.
        file_path: str = self.app_table.item(selected_row, self._APP_PATH_COL).text()
        app_name: str = self.app_table.item(selected_row, self._APP_NAME_COL).text()

        # Create a warning dialog to confirm user wishes to delete entry.
        del_confirm = QMessageBox()
        del_confirm.setIcon(QMessageBox.Icon.Warning)
        del_confirm.setWindowTitle("Removal Confirmation")
        del_confirm.setText(f'Are you sure you want to delete application:\n\n{app_name}?')
        del_confirm.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        del_confirm.setDefaultButton(QMessageBox.StandardButton.No)
        confirmation = del_confirm.exec()

        # If user selected 'Yes' to confirm deletion then remove entry from table and user_apps.json, else return.
        if confirmation == QMessageBox.StandardButton.Yes:
            # Remove row from table
            self.app_table.removeRow(selected_row)
            # Remove from JSON
            self._json_handler.remove_app(file_path)
        else:
            return

    # ------------------------------------------------------------------------------ #
    # Get selected application details for settings panel                            #
    # ------------------------------------------------------------------------------ #
    def get_selected_application(self) -> list:
        """
        Retrieves the selected application's details from the table.

        Args:
            None.
        
        Returns:
            list: A list containing:
                bool: Selection status (True if an application is selected, False otherwise).
                str: File path of the selected application.
                str: Application name of the selected application.
                str: Graphics API of the selected application.
        
        Examples:
            Default Usage:
                .. code-block:: python
                >>> selection_details = .get_selected_application()
        """

        # Set selected_row to impossible arbitrary value.
        selected_row = -1

        # Find the selected radio button.
        for row in range(self.app_table.rowCount()):
            radio_button = self.app_table.cellWidget(row, self._RADIO_BUTTON_COL)
            if radio_button is not None and radio_button.isChecked():
                selected_row = row
                break

        # If selected row equals default value, no value has obviously been selected.
        if selected_row == -1:
            QMessageBox.warning(self, "No Selection", "Please select an application to proceed.")
            selection: bool = False
            return [selection]
        else:
            selection: bool = True
        
        # Get path & name of the selected application.
        file_path: str = self.app_table.item(selected_row, self._APP_PATH_COL).text()
        app_name: str = self.app_table.item(selected_row, self._APP_NAME_COL).text()
        gapi: str = self.app_table.item(selected_row, self._APP_GAPI_COL).text()

        return [
            selection,
            file_path, 
            app_name, 
            gapi,
        ]
