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
from PyQt6.QtWidgets import (
    QLabel,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QFileDialog,
    QMessageBox,
    QRadioButton
)
from Window.app_logging import OutputLog
from PyQt6.QtCore import Qt
from Window.json_handler import AppJSONHandler
from Window.settings_panel import SettingsPanel


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
    # Logging variables
    _log = OutputLog()
    _file_name: str = "app_list_panel.py"

    # Global constants creation
    _RADIO_BUTTON_COL: int = 0
    _APP_EXE_COL: int = 1
    _APP_NAME_COL: int = 2
    _APP_DX_COL: int = 3
    _APP_PATH_COL: int = 4

    # Create class variable for linking to the JSON handling class.
    _json_handler = AppJSONHandler()

    # --------------------------------------------------------------------------- #
    # Panel initialisation & table creation.                                      #
    # --------------------------------------------------------------------------- #
    def __init__(self) -> None:
        """
        Initializes the AppListPanel widget.

        Args:
            None.

        Returns:
            None.

        Examples:
            Default Usage:
                >>> variable = AppListPanel()
        """
        super().__init__()

        # Create QVBoxLayout.
        self.setLayout(QVBoxLayout())
        self._log.log_routine(self._file_name, 1, 89, 89, "Set panel layout to QVBoxLayout..")

        # Create a panel label and add it to the layout (HTML used for rich text formatting).
        label_text = "Applications"
        self.label = QLabel(f'<html><body><h3><b><u>{label_text}</u></b></h3></body></html>')
        self._log.log_routine(self._file_name, 2, 93, 94, "Create and set panel QLabel (label)..")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._log.log_routine(self._file_name, 3, 96, 96, "Center align label..")
        self.layout().addWidget(self.label)
        self._log.log_routine(self._file_name, 4, 98, 98, "Add label to layout..")

        # Add application list table.
        self.app_table = QTableWidget()
        self._log.log_routine(self._file_name, 5, 102, 102, "Create QTableWidget (app_table)..")
        self.app_table.setColumnCount(5)
        self._log.log_routine(self._file_name, 6, 104, 104, "Set app_table columns to 5..")
        self.app_table.setHorizontalHeaderLabels(["Selected", "File", "App Name", "Graphics API", "Path"])
        self._log.log_routine(self._file_name, 7, 106, 106, "Set app_table header labels..")
        self.app_table.setColumnWidth(self._RADIO_BUTTON_COL, 75)   # Radio buttons column for selecting entries
        self.app_table.setColumnWidth(self._APP_EXE_COL, 150)  # File name column
        self.app_table.setColumnWidth(self._APP_NAME_COL, 200)  # Editable application name column
        self.app_table.setColumnWidth(self._APP_DX_COL, 150)  # DirectX Version column
        self.app_table.setColumnWidth(self._APP_PATH_COL, 300)  # Full path column
        self._log.log_routine(self._file_name, 8, 108, 112, "Set app_table column widths..")
        self.layout().addWidget(self.app_table)
        self._log.log_routine(self._file_name, 9, 114, 114, "Add app_table to layout..")

        # Create button layout.
        button_layout = QHBoxLayout()
        self._log.log_routine(self._file_name, 10, 118, 118, "Create QHBoxLayout (button_layout)..")

        # Add buttons to add & delete applications.
        self.add_app_button = QPushButton("Add Application")
        self._log.log_routine(self._file_name, 11, 122, 122, "Create and label QPushButton (add_app_button)..")
        self.del_app_button = QPushButton("Delete Application")
        self._log.log_routine(self._file_name, 12, 124, 124, "Create and label QPushButton (del_app_button)..")
        self.load_settings_button = QPushButton("Load Settings")
        self._log.log_routine(self._file_name, 13, 126, 126, "Create and label QPushButton (load_settings_button)..")

        # Add buttons to button layout.
        button_layout.addWidget(self.add_app_button)
        button_layout.addWidget(self.del_app_button)
        button_layout.addWidget(self.load_settings_button)
        self._log.log_routine(self._file_name, 14, 130, 132, "Add buttons to button_layout..")

        # Add button layout to main layout.
        self.layout().addLayout(button_layout)
        self._log.log_routine(self._file_name, 15, 136, 136, "Add button_layout to layout..")

        # Connect button click signal to handler.
        self.add_app_button.clicked.connect(self.add_application)
        self.del_app_button.clicked.connect(self.delete_application)
        self.load_settings_button.clicked.connect(self.load_application_settings)
        self._log.log_routine(self._file_name, 16, 140, 142, "Connect button click signal to respective handling methods..")

        # Check for changes to 'App Name' field.
        self.app_table.cellChanged.connect(self.update_application_name)
        self._log.log_routine(self._file_name, 17, 146, 146, "Connect cell change signal to handling method..")

        # Load applications from file on startup.
        self.load_applications()
        self._log.log_routine(self._file_name, 18, 150, 150, "Populate settings to app_table..")

    # --------------------------------------------------------------------------- #
    # Application selection & duplicate selection check.                          #
    # --------------------------------------------------------------------------- #
    def add_application(self) -> None:
        """
        Opens file dialog and prepares for adding selected applications details to the table.

        Args:
            None.

        Returns:
            None.

        Examples:
            Default Usage:
                >>> .add_application()
        """
        # Create file dialog.
        file_dialog = QFileDialog(self)
        self._log.log_routine(self._file_name, 19, 171, 171, "Create QFileDialog (file_dialog)..")
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)

        # File filters.
        filters = "Windows Executables (*.exe);;Shell Scripts (*.sh);;Batch Files (*.bat);;All Files (*)"
        file_path, selected_filter = file_dialog.getOpenFileName(self, "Select Application", "", filters)

        # Check selected file is not already added (file path check), if not then add to table.
        if file_path:
            self._log.log_routine(self._file_name, 20, 180, 180, f"File selected at {str(file_path)}")
            self._log.log_routine(self._file_name, 21, 183, 183, "Performing duplicate check..")
            if not self.is_app_already_added(file_path):
                self._log.log_routine(self._file_name, 22, 183, 183, "Duplicate check passed..")
                self.add_application_to_table(file_path)
                self._log.log_routine(self._file_name, 23, 185, 185, "Adding new application to app_table..")
                self.save_application(file_path)
                self._log.log_routine(self._file_name, 24, 187, 187, "Adding new application to JSON file (user_apps.json)..")
            else:
                self._log.log_routine(self._file_name, 25, 189, 189, "Duplicate check failed..")
                QMessageBox.warning(self, "Duplicate Entry", "This application is already in the list.")
                self._log.log_warning(self._file_name, 26, 191, 191, "Adding new application failed! Duplicate entry detected!")

    # --------------------------------------------------------------------------- #
    # Add applications to table.                                                  #
    # --------------------------------------------------------------------------- #
    def add_application_to_table(self, file_path_input: str, app_name_input: str = None, dx_version_input: str = None) -> None:
        """
        Adds application details to the table, using saved values when available.

        Args:
            file_path(str): Application path of application to be added to table.
            app_name(str): Application name of application to be added to table.
            dx_version(str): Applications reported DX version to be added to table.

        Returns:
            None.

        Examples:
            Default Usage:
                >>> .add_application_to_table("/path/to/application", "application name", "DirectX version")
        """
        # Get method input arguments and store in method for use.
        file_path: str = file_path_input
        file_name: str = os.path.basename(file_path)
        app_name: str = app_name_input
        dx_version: str = dx_version_input

        # Check if app_name contains any values.
        self._log.log_routine(self._file_name, 27, 221, 221, "Performing app_name check..")
        if not app_name:  # Only extract if not loaded from JSON.
            self._log.log_warning(self._file_name, 28, 221, 221, "Check failed! app_name is empty! extracting application name..")
            app_name = self.extract_app_name(file_path) or file_name.split(".")[0]
            self._log.log_routine(self._file_name, 29, 223, 223, "Application name extracted, and stored to app_name..")

        # Check if dx_ver contains any values
        self._log.log_routine(self._file_name, 30, 228, 228, "Performing dx_version check..")
        if not dx_version:
            self._log.log_warning(self._file_name, 31, 228, 228, "Check failed! dx_version is empty! extracting DirectX Version..")
            dx_version = self.detect_dx_version(file_path)
            self._log.log_routine(self._file_name, 32, 230, 230, "DirectX version extracted, and stored in dx_version..")

        # Get physical row count to insert new row at end of table.
        row_position: int = self.app_table.rowCount()
        self.app_table.insertRow(row_position)
        self._log.log_routine(self._file_name, 33, 235, 235, "Add new row to end of app_table..")

        # Populate row cells with provided data.
        entry_selection = QRadioButton()
        self.app_table.setCellWidget(row_position, self._RADIO_BUTTON_COL, entry_selection)
        self._log.log_routine(self._file_name, 34, 239, 240, f"Create QRadioButton (entry_selection), and store in app_table in column {str(self._RADIO_BUTTON_COL)}..")

        file_item = QTableWidgetItem(file_name)
        file_item.setFlags(Qt.ItemFlag.ItemIsEnabled)
        self.app_table.setItem(row_position, self._APP_EXE_COL, file_item)
        self._log.log_routine(self._file_name, 35, 243, 245, f"Create QTableWidgetItem (file_item), set item flag to be enabled, then store in app_table in column {str(self._APP_EXE_COL)}..")

        name_item = QTableWidgetItem(app_name)
        name_item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEditable | Qt.ItemFlag.ItemIsEnabled)
        self.app_table.setItem(row_position, self._APP_NAME_COL, name_item)
        self._log.log_routine(self._file_name, 36, 248, 250, f"Create QTableWidgetItem (name_item), set item flags to be selectable, editable & enabled, then store in app_table in column {str(self._APP_NAME_COL)}..")

        dx_item = QTableWidgetItem(dx_version)
        dx_item.setFlags(Qt.ItemFlag.ItemIsEnabled)
        self.app_table.setItem(row_position, self._APP_DX_COL, dx_item)
        self._log.log_routine(self._file_name, 37, 253, 255, f"Create QTableWidgetItem (dx_item), set item flag to be enabled, then store in app_table in column {str(self._APP_DX_COL)}..")

        path_item = QTableWidgetItem(file_path)
        path_item.setFlags(Qt.ItemFlag.ItemIsEnabled)
        self.app_table.setItem(row_position, self._APP_PATH_COL, path_item)
        self._log.log_routine(self._file_name, 38, 258, 260, f"Create QTableWidgetItem (path_item), set item flag enabled, then store in app_table in column {str(self._APP_PATH_COL)}..")

    # --------------------------------------------------------------------------- #
    # Extract application real name using pefile.                                 #
    # --------------------------------------------------------------------------- #
    def extract_app_name(self, file_path_input: str) -> str | None:
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
                >>> .extract_app_name("/path/to/application")
                "Application Name"  # Application name extraction success

                >>> .extract_app_name("/path/to/application")
                None  # Application name extraction failure
        """
        # Get method input arguments and store in method for use.
        file_path: str = file_path_input

        # Check if selected file has the .exe extension.
        self._log.log_routine(self._file_name, 39, 293, 293, "Performing file type check..")
        if not file_path.endswith(".exe"):
            self._log.log_warning(self._file_name, 40, 293, 293, "File type check failed! File type is not .exe, returning None!")
            return None  # Return None if not a .exe.

        # Try to pull application real name from applications .exe using pefile.
        self._log.log_routine(self._file_name, 41, 299, 299, f"File type check Successful. Attempting to extract file name from {str(file_path)}..")
        try:
            pe = pefile.PE(file_path)
            if hasattr(pe, 'FileInfo'):
                for file_info in pe.FileInfo:
                    if (hasattr(file_info, 'StringTable')):
                        for entry in file_info:
                            if (hasattr(entry, 'entries')):
                                if "FileDescription" in entry.entries:
                                    self._log.log_routine(self._file_name, 42, 305, 305, "File name extraction complete..")
                                    app_name: str = entry.entries["FileDescription"].decode(errors="ignore")
                                    self._log.log_routine(self._file_name, 43, 307, 307, f"File name for application at '{str(file_path)}' is set to '{app_name}'..")
                                    self._log.log_routine(self._file_name, 44, 310, 310, "Returning app_name..")
                                    return app_name
                                else:
                                    self._log.log_warning(self._file_name, 45, 312, 312, "FileDescription not found in StringTable! Returning None!")
                                    return None
                            else:
                                self._log.log_warning(self._file_name, 46, 315, 315, "StringTable entry has no entries attribute! Returning None!")
                                return None
                    else:
                        self._log.log_warning(self._file_name, 47, 318, 318, "FileInfo has no StringTable attribute! Returning None!")
                        return None
            else:
                self._log.log_warning(self._file_name, 48, 321, 321, "File has no FileInfo attribute! Returning None!")
                return None

        except (Exception, pefile.PEFormatError) as e:
            if not isinstance(e, pefile.PEFormatError):
                # Program should never reach this point.
                self._log.log_fatal(self._file_name, 49, 327, 327, "How did you get here? What have you done? >0_o<??? \n An unexpected error has occurred during application name extraction! Please report this issue, with terminal output where possible!")
            self._log.log_warning(self._file_name, 50, 331, 331, f"File name extraction failed! File might be corrupted! Returning None! \n{e}")
            return None

    # --------------------------------------------------------------------------- #
    # Detect DirectX version using pefile to scan for linked DLLs                 #
    # --------------------------------------------------------------------------- #
    def detect_dx_version(self, file_path_input: str) -> str:
        """
        Detects the DirectX version by scanning linked DLLs.

        Args:
            file_path(String): Application path of application to extract DX version from.

        Returns:
            DX_ver(String): Detected applications DirectX version, 'N/A' if file is not a .exe or not detected, 'Unknown' if exception raised.

        Raises:
            Exception: Returns DX_ver with value 'Unknown'.

        Examples:
            Default Usage:
                >>> .detect_dx_version("/path/to/application")
                "N/A"  # Default value, and value assigned when application is not .exe

                >>> .detect_dx_version("/path/to/application")
                "DirectX 12"  # Value assigned if d3d12.dll links detected

                >>> .detect_dx_version("/path/to/application")
                "DirectX 11"  # Value assigned if d3d11.dll links detected

                >>> .detect_dx_version("/path/to/application")
                "DirectX 10"  # Value assigned if d3d10.dll links detected

                >>> .detect_dx_version("/path/to/application")
                "DirectX 9"  # Value assigned if d3d9.dll links detected

                >>> .detect_dx_version("/path/to/application")
                "Unknown"  # Value assigned if dll link detection fails
        """
        # Get method input arguments and store in method for use.
        file_path: str = file_path_input

        # Create DX_ver string variable and set to 'None'.
        DX_ver: str = None

        # Check selected application has the .exe extension.
        self._log.log_routine(self._file_name, 51, 377, 377, "Performing file type check..")
        if not file_path.endswith(".exe"):
            self._log.log_warning(self._file_name, 52, 377, 380, "File type check failed! File type is not .exe! Returning 'N/A'!")
            DX_ver = "N/A"  # Set to N/A if file is not a .exe.
            return DX_ver

        # Try to pull DirectX version from applications .exe using pefile.
        self._log.log_routine(self._file_name, 53, 384, 384, f"File type check successful. Attempting to extract DirectX version from {str(file_path)}..")
        try:
            pe = pefile.PE(file_path)
            if (hasattr(pe, 'DIRECTORY_ENTRY_IMPORT')):
                imported_dlls = [entry.dll.decode().lower() for entry in pe.DIRECTORY_ENTRY_IMPORT]

                # Check incase OpenGL
                if "opengl32.dll" in imported_dlls:
                    self._log.log_warning(self._file_name, 54, 390, 393, "OpenGL detected! Returning 'OpenGL'!")
                    DX_ver = "OpenGL"
                    return DX_ver

                # Create dictionary of possible DirectX versions
                dx_dll_patterns: dict = {
                    "d3d12(_\d+)?\.dll": "DirectX 12",
                    "d3d11(_\d+)?\.dll": "DirectX 11",
                    "d3d10(_\d+)?\.dll": "DirectX 10",
                    "d3d9(_\d+)?\.dll": "DirectX 9",
                }

                # Compare output to get right DirectX version, set to DX_ver string, and return.
                for dll_pattern, version in dx_dll_patterns.items():
                    for dll in imported_dlls:
                        if re.match(dll_pattern, dll):
                            self._log.log_routine(self._file_name, 55, 406, 406, "DirectX version extraction complete..")
                            DX_ver = version
                            self._log.log_routine(self._file_name, 56, 408, 408, f"DirectX version for application at '{file_path}' is set to '{DX_ver}'..")
                            self._log.log_routine(self._file_name, 57, 411, 411, "Returning DX_ver..")
                            return DX_ver

                self._log.log_warning(self._file_name, 58, 414, 415, f"No matching dlls in import list! \n{imported_dlls}\n Returning 'N/A'!")
                DX_ver = "N/A"
                return DX_ver
            else:
                self._log.log_warning(self._file_name, 59, 416, 419, "File has no import table! Returning 'N/A'!")
                DX_ver = "N/A"
                return DX_ver

        except (Exception, pefile.PEFormatError) as e:
            self._log.log_warning(self._file_name, 60, 421, 421, f"DirectX version for application at '{file_path}' is Unknown! File might be corrupted!\n {e} ")
            DX_ver = "Unknown"
            self._log.log_routine(self._file_name, 61, 423, 423, "Setting DX_ver to 'Unknown'..")
            if not isinstance(e, pefile.PEFormatError):
                # Program should never reach this point.
                self._log.log_fatal(self._file_name, 62, 425, 425, "How did you get here? What have you done? >0_o<??? \n An unexpected error has occurred during application name extraction! Please report this issue, with terminal output where possible!")
            self._log.log_routine(self._file_name, 63, 429, 429, "Returning DX_ver..")
            return DX_ver

    # --------------------------------------------------------------------------- #
    # Save application list to JSON file for recall on fresh load                 #
    # --------------------------------------------------------------------------- #
    def save_application(self, file_path_input: str) -> None:
        """
        Save the application details to user_apps.json, using json_handler.py.

        Args:
            file_path(String): Application path of application to be saved to user_apps.json using json_handler.py.

        Returns:
            None.

        Examples:
            Default Usage:
                >>> .save_application("/path/to/application")
        """
        # Get method input arguments and store in method for use.
        file_path: str = file_path_input

        # Set app_name from .exe using extract_app_name() or setting it to 'apps_name.exe'.
        app_name: str = self.extract_app_name(file_path) or os.path.basename(file_path).split(".")[0]

        # Set dx_version from .exe using detect_dx_version().
        dx_version: str = self.detect_dx_version(file_path)

        # Create a dictionary variable called data and load JSON data into it.
        data: dict = self._json_handler.load_app_details()

        # Check for duplicates before saving, if duplicate found, break.
        if any(entry["app_path"] == file_path for entry in data["applications"]):
            self._log.log_warning(self._file_name, 64, 463, 463, "Duplicate entry! Skipping..")
            return  # Skip saving duplicates

        # Append new entry and save.
        self._json_handler.add_app_details(app_name, file_path, dx_version)
        self._log.log_routine(self._file_name, 65, 466, 466, f"Entry saved to user_apps.json with values; App name: {app_name}, File path: {file_path}, DirectX: {dx_version}..")

    # --------------------------------------------------------------------------- #
    # Retrieve application details from JSON file on load                         #
    # --------------------------------------------------------------------------- #
    def load_applications(self) -> None:
        """
        Load applications from user_apps.json, using json_handler.py.

        Args:
            None.

        Returns:
            None.

        Examples:
            Default Usage:
                >>> .load_applications()
        """
        # Create a dictionary variable alled data and load JSON data into it.
        data: dict = self._json_handler.load_app_details()
        self._log.log_routine(self._file_name, 66, 487, 487, "user_apps.json loaded and stored in data..")

        # Iterate through app entries in dictionary and add each in turn to table.
        self._log.log_routine(self._file_name, 67, 492, 492, "Iterating through data..")
        for app in data.get("applications", []):
            self.add_application_to_table(app["app_path"], app["app_name"], app["app_dx"])
            self._log.log_routine(self._file_name, 68, 493, 493, f"Adding application to app_table with values; App name: {app["app_name"]}, DirectX: {app["app_dx"]}, File path: {app["app_path"]}..")

    # --------------------------------------------------------------------------- #
    # Check if application is already in the table                                #
    # --------------------------------------------------------------------------- #
    def is_app_already_added(self, file_path_input: str) -> bool:
        """
        Check if application is already in the table.

        Args:
            file_path(String): Application path of application to run check against.

        Returns:
            (bool): Either 'True' if application is already in table, or 'False' if not in table.

        Examples:
            Default Usage:
                >>> .is_app_already_added("/path/to/application")
                True  # Application duplicate has been found

                >>> .is_app_already_added("/path/to/application")
                False  # Application duplicate has not been found
        """
        # Get method input arguments and store in method.
        file_path: str = file_path_input

        # Check each rows fifth (path) column to check for potential duplicate entry insertion
        self._log.log_routine(self._file_name, 69, 522, 522, "ÚwÙ Performing duplicate check.. ÚwÙ")
        for row in range(self.app_table.rowCount()):
            if self.app_table.item(row, 4).text() == file_path:
                self._log.log_warning(self._file_name, 70, 523, 523, "Duplicate check failed! Duplicate Found!")
                self._log.log_routine(self._file_name, 71, 526, 526, "Returning True..")
                return True

        self._log.log_routine(self._file_name, 72, 529, 529, "Duplicate check passed, returning False..")
        return False  # If no duplicate found return 'False'

    # --------------------------------------------------------------------------- #
    # Allow user inputted application name & save to JSON file                    #
    # --------------------------------------------------------------------------- #
    def update_application_name(self, row_input: int, column_input: int) -> None:
        """
        Update JSON when an app name is edited in the table.

        Args:
            row(int): Row number of selected application to update application name.
            column(int): Column number to make sure only 'App Name' is being updated.

        Returns:
            None.

        Examples:
            Default Usage:
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
        self._log.log_routine(self._file_name, 73, 563, 563, "Performing column check..")
        if column != self._APP_NAME_COL:  # We only care about the 'App Name' column.
            self._log.log_warning(self._file_name, 74, 563, 563, "Selected column is not 'App Name'.. Can be safely ignored if seeing this on application boot..")
            return

        # Assign path to widget.
        app_path_item = self.app_table.item(row, self._APP_PATH_COL)

        # If path empty / None, return.
        self._log.log_routine(self._file_name, 75, 572, 572, "Performing path check..")
        if app_path_item is None:
            self._log.log_warning(self._file_name, 76, 572, 572, "'App Path' column is empty.. Can be safely ignored if seeing this on application boot..")
            return

        # Set new variables name to new_name string, and path to app_path from tables current values.
        new_name: str = self.app_table.item(row, column).text()
        app_path: str = app_path_item.text()  # Get the app's path.
        self._log.log_routine(self._file_name, 77, 577, 578, "Setting variables with correct values..")

        # If either name or path variables are empty, return.
        if not new_name or not app_path:
            self._log.log_fatal(self._file_name, 78, 582, 582, "How did you get here? What have you done? >0_o<???")
            return  # Avoid empty names or missing data.

        # Load current JSON data.
        data: dict = self._json_handler.load_app_details()
        self._log.log_routine(self._file_name, 79, 587, 587, "user_apps.json loaded and stored in data..")

        # Find and update the correct app entry.
        self._log.log_routine(self._file_name, 80, 592, 592, "Iterating through data..")
        for app in data["applications"]:
            if app["app_path"] == app_path:
                self._log.log_routine(self._file_name, 81, 593, 593, "App found..")
                app["app_name"] = new_name
                self._log.log_routine(self._file_name, 82, 595, 595, "Setting app[\"app_name\"] to new_name..")
                break

        # Save back to JSON.
        self._json_handler.save_app_details(data)
        self._log.log_routine(self._file_name, 83, 600, 600, "data saved to user_apps.json..")

    # --------------------------------------------------------------------------- #
    # Delete selected application from the list and JSON                          #
    # --------------------------------------------------------------------------- #
    def delete_application(self) -> None:
        """
        Deletes the selected application from the table and user_apps.json using json_handler.py.

        Args:
            None.

        Returns:
            None.

        Examples:
            Default Usage:
                >>> .delete_application()
        """
        # Set selected_row to impossible arbitrary value.
        selected_row = -1

        # Find the selected radio button.
        self._log.log_routine(self._file_name, 84, 625, 625, "Finding selection..")
        for row in range(self.app_table.rowCount()):
            radio_button = self.app_table.cellWidget(row, self._RADIO_BUTTON_COL)
            if radio_button is not None and radio_button.isChecked():
                self._log.log_routine(self._file_name, 85, 627, 627, "Selection found..")
                selected_row = row
                break

        # If selected row equals default value, no value has obviously been selected.
        if selected_row == -1:
            self._log.log_warning(self._file_name, 86, 633, 633, "No selection made!")
            QMessageBox.warning(self, "No Selection", "Please select an application to delete!")
            return

        # Get file path of the selected application.
        file_path: str = self.app_table.item(selected_row, self._APP_PATH_COL).text()
        app_name: str = self.app_table.item(selected_row, self._APP_NAME_COL).text()
        self._log.log_routine(self._file_name, 87, 639, 640, "Collecting selection details..")

        # Create a warning dialog to confirm user wishes to delete entry.
        del_confirm = QMessageBox()
        del_confirm.setIcon(QMessageBox.Icon.Warning)
        del_confirm.setWindowTitle("Removal Confirmation")
        del_confirm.setText(f'Are you sure you want to delete application:\n\n{app_name}?')
        del_confirm.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        del_confirm.setDefaultButton(QMessageBox.StandardButton.No)
        self._log.log_routine(self._file_name, 88, 644, 649, "Create confirmation dialog box..")
        confirmation = del_confirm.exec()

        # If user selected 'Yes' to confirm deletion then remove entry from table and user_apps.json, else return.
        self._log.log_routine(self._file_name, 89, 655, 655, "Performing user confirmation check..")
        if confirmation == QMessageBox.StandardButton.Yes:
            self._log.log_routine(self._file_name, 90, 655, 655, "User confirmed..")
            # Remove row from table
            self.app_table.removeRow(selected_row)
            self._log.log_routine(self._file_name, 91, 658, 658, "Removing entry from app_table..")
            # Remove from JSON
            self._json_handler.remove_app(file_path)
            self._log.log_routine(self._file_name, 92, 661, 661, "Removing entry from user_apps.json..")
        else:
            self._log.log_routine(self._file_name, 93, 663, 663, "User declined.. Returning..")
            return

    # --------------------------------------------------------------------------- #
    # Loads selected application from the list and its settings from the JSON     #
    # --------------------------------------------------------------------------- #
    def load_application_settings(self) -> None:
        """
        Loads the selected applications settings from user_apps.json using json_handler.py, and sends them to settings panel.

        Args:
            None.

        Returns:
            None.

        Examples:
            Default Usage:
                >>> .load_application_settings()
        """
        # Set selected_row to impossible arbitrary value.
        selected_row = -1

        # Find the selected radio button.
        self._log.log_routine(self._file_name, 94, 689, 689, "Finding selection..")
        for row in range(self.app_table.rowCount()):
            radio_button = self.app_table.cellWidget(row, self._RADIO_BUTTON_COL)
            if radio_button is not None and radio_button.isChecked():
                self._log.log_routine(self._file_name, 95, 691, 691, "Selection found..")
                selected_row = row
                break

        # If selected row equals default value, no value has obviously been selected.
        if selected_row == -1:
            self._log.log_warning(self._file_name, 96, 697, 697, "No selection made!")
            QMessageBox.warning(self, "No Selection", "Please select an application to load settings for.")
            return

        # Get file path of the selected application.
        file_path: str = self.app_table.item(selected_row, self._APP_PATH_COL).text()
        app_name: str = self.app_table.item(selected_row, self._APP_NAME_COL).text()
        self._log.log_routine(self._file_name, 97, 703, 704, "Colecting selection details..")

        # Get settings from JSON.
        data: dict = self._json_handler.load_app_details()
        self._log.log_routine(self._file_name, 98, 708, 708, "user_apps.json loaded and stored in data..")

        # Set up connection to Settings Panel.
        settings_panel_connection = SettingsPanel()
        self._log.log_routine(self._file_name, 99, 712, 712, "Connecting to settings panel..")

        self._log.log_routine(self._file_name, 100, 716, 716, "Iterating through data..")
        for app in data["applications"]:
            if os.path.basename(app["app_path"]) == os.path.basename(file_path):
                self._log.log_routine(self._file_name, 101, 717, 717, "App found in user_apps.json..")
                app_found: dict = app
                self._log.log_routine(self._file_name, 102, 721, 722, "Check if app_found[\"settings\"] is populated..")
                for setting in app_found["settings"]:
                    if setting["settings_set"] is True:
                        self._log.log_routine(self._file_name, 103, 722, 722, "App settings found..")
                        # If populated send across to settings panel.
                        self._log.log_routine(self._file_name, 104, 726, 726, "Sending data to settings panel..")
                        settings_panel_connection.pass_to_settings_panel(data)
                    else:
                        self._log.log_warning(self._file_name, 105, 727, 727, "app_found[\"settings\"] is not populated!")
                        QMessageBox.warning(self, "No Settings Found", f"There are no saved settings for:\n\n{app_name}\n\nPlease select an application with saved settings, or save some settings for the application first.")
