"""
File:      : main_window.py
Author     : Fluffy Flower (Martin Wylde)
Contact    :
    Email   - martincw1989@gmail.com
    Telegram- @FluffyFlower
    Discord - fluffy_flower
Date       : 28/02/2025
Version    : 1.0.2
Description: Main window file for building the main window incorporating
             panels defined in app_list_panel.py and settings_panel.py.
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
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QSplitter
from Window.app_logging import OutputLog
from Window.settings_panel import SettingsPanel
from Window.app_list_panel import AppListPanel


# ---------------------------------------------------------------------------------- #
#                                                                                    #
# ██  ██          ██                    ██  ██  ██                ██                 #
# ██████    ████        ██████          ██  ██        ██████      ██  ██████  ██  ██ #
# ██  ██  ██  ██  ██    ██  ██          ██  ██  ██    ██  ██    ████  ██  ██  ██████ #
# ██  ██  ██  ██  ██    ██  ██          ██████  ██    ██  ██  ██  ██  ██  ██  ██████ #
# ██  ██  ██████  ████  ██  ██          ██  ██  ████  ██  ██  ██████  ██████    ██   #
#                                                                                    #
# ---------------------------------------------------------------------------------- #


class MainWindow(QMainWindow):
    # Logging variables
    _log = OutputLog()
    _file_name: str = "main_window.py   "

    def __init__(self):
        """
        __init__():
        Class constructor for main window initialisation

        Args:
            None.

        Returns:
            None.
        """
        super().__init__()
        self.setWindowTitle("Graphics Settings Manager")
        self._log.log_routine(self._file_name, 1, 57, 57, "Set window title..")
        self.resize(1024, 768)
        self._log.log_routine(self._file_name, 2, 59, 59, "Set window size..")

        # Create main layout
        main_widget = QWidget()
        self._log.log_routine(self._file_name, 3, 63, 63, "Create QWidget (main_widget)..")
        self.setCentralWidget(main_widget)
        self._log.log_routine(self._file_name, 4, 65, 65, "Set main_widget as cental widget..")
        layout = QVBoxLayout(main_widget)
        self._log.log_routine(self._file_name, 5, 67, 67, "Set main_widget layout to QVBoxLayout..")

        # Create splitter
        splitter = QSplitter()
        self._log.log_routine(self._file_name, 6, 71, 71, "Create QSplitter (splitter)..")
        layout.addWidget(splitter)
        self._log.log_routine(self._file_name, 7, 73, 73, "Add splitter to layout..")

        # Create app list panel and settings panel
        self.app_list_panel = AppListPanel()
        self._log.log_routine(self._file_name, 8, 77, 77, "Create AppListPanel (app_list_panel)..")
        self.settings_panel = SettingsPanel()
        self._log.log_routine(self._file_name, 9, 79, 79, "Create SettingsPanel (settings_panel)..")

        # Add panels to splitter
        splitter.addWidget(self.app_list_panel)
        self._log.log_routine(self._file_name, 10, 83, 83, "Add app_list_panel to splitter..")
        splitter.addWidget(self.settings_panel)
        self._log.log_routine(self._file_name, 11, 85, 85, "Add settings_panel to splitter..")

        # Set sizes for the splitter
        splitter.setSizes([10, 20])
        self._log.log_routine(self._file_name, 12, 89, 89, "Set splitter sizes..")
