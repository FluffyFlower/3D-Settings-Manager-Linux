"""
File:      : main_window.py
Author     : Fluffy Flower (Martin Wylde)
Contact    :
    Email   - martincw1989@gmail.com
    Telegram- @FluffyFlower
    Discord - fluffy_flower
Date       : 28/02/2025
Version    : 1.0.2
Description: Main window file for building the main window incorporating panels defined in app_list_panel.py and settings_panel.py.
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

    def __init__(self):
        """
        Class constructor for main window initialisation

        Args:
            None.

        Returns:
            None.

        Raises:
            None.

        Examples:
            Default Usage:
            .. code-block:: python
            >>> main_window = MainWindow()
        """
        super().__init__()
        self.setWindowTitle("Graphics Settings Manager")
        self.resize(1024, 768)

        # Create main layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout(main_widget)

        # Create splitter
        splitter = QSplitter()
        layout.addWidget(splitter)

        # Create app list panel and settings panel
        self.app_list_panel = AppListPanel()
        self.settings_panel = SettingsPanel(app_list_panel_ref=self.app_list_panel) # Pass reference to app_list_panel

        # Add panels to splitter
        splitter.addWidget(self.app_list_panel)
        splitter.addWidget(self.settings_panel)

        # Set sizes for the splitter
        splitter.setSizes([10, 20])
