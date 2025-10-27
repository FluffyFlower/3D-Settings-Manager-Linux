"""
File:
    settings_panel.py
Author:
    Fluffy Flower (Martin Wylde)
Date:
    23/01/2025
Version:
    0.1.1
Description:
    Settings panel file for building settings panel and importing settings
    objects to be displayed as titles, comboboxes, tooltips.
"""

from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QComboBox,
    QScrollArea,
    QPushButton,
    QTabWidget)
from Window.Settings import *
from PyQt6.QtCore import Qt


class SettingsPanel(QWidget):
    def __init__(self):
        """
        Initializes the SettingsPanel widget.

        Args:
            None

        Returns:
            None
        """
        super().__init__()

        # Create QVBoxLayout
        self.setLayout(QVBoxLayout())

        # Create a panel label and add it to the layout
        label_text = "Settings"
        self.label = QLabel(f'<html><body><h3><b><u>{label_text}</u></b></h3></body></html>')
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout().addWidget(self.label)

        # Create a tab widget and add it to the layout
        self.tab_widget = QTabWidget()
        self.layout().addWidget(self.tab_widget)

        # Dynamically make and add the tabs to the layout
        self.create_settings_tab(
            "Anti-Aliasing",
            "aa_settings_layout")
        self.create_settings_tab(
            "Anisotropic Filtering",
            "af_settings_layout")
        self.create_settings_tab(
            "Sharpening",
            "sharpness_settings_layout")
        self.create_settings_tab(
            "VSync && Frame Limits",
            "vsync_settings_layout")
        self.create_settings_tab(
            "Misc Settings",
            "misc_settings_layout")

        # Dictionary to store comboboxes and their IDs
        self.comboboxes = {}

        # List of the setting classes
        setting_classes = [
            # Anti-Aliasing Classes:
            FXAA_Enable(),                      # ID - 00
            FXAA_Quality_Subpixel(),            # ID - 01
            FXAA_Quality_Edge_Threshold(),      # ID - 02
            FXAA_Edge_Threshold_Bias(),         # ID - 03
            SMAA_Enable(),                      # ID - 04
            SMAA_Edge_Detection(),              # ID - 05
            SMAA_Threshold(),                   # ID - 06
            SMAA_Search_Steps(),                # ID - 07
            SMAA_Search_Steps_Diagonal(),       # ID - 08
            SMAA_Corner_Rounding(),             # ID - 09

            # Anistropic Filtering / LOD Classes:
            Anistropic_Filtering_Enable(),      # ID - 10
            Anistropic_Filtering_Level(),       # ID - 11
            Anistropic_Filtering_Level_D3D9(),  # ID - 12
            LOD_Enable(),                       # ID - 13
            LOD_Bias(),                         # ID - 14
            LOD_Bias_D3D9(),                    # ID - 15
            Clamp_Negative_LOD(),               # ID - 16
            Clamp_Negative_LOD_D3D9(),          # ID - 17

            # Sharpening Classes
            CAS_Enable(),                       # ID - 18
            CAS_Sharpness(),                    # ID - 19
            DLS_Enable(),                       # ID - 20
            DLS_Sharpness(),                    # ID - 21
            DLS_Denoise(),                      # ID - 22

            # VSync / Frame Limiting Classes
            VSync_Enable(),                     # ID - 23
            VSync_Level(),                      # ID - 24
            VSync_Level_D3D9(),                 # ID - 25
            Frame_Limit_Enable(),               # ID - 26
            Frame_Limit(),                      # ID - 27
            Frame_Limit_D3D9(),                 # ID - 28

            # Misc Classes
            HighDynamicRange(),                 # ID - 29
            D3D_Level()                         # ID - 30
            ]

        # Populate the settings
        self.populate_settings(setting_classes)

        # Create and add a 'Save Settings' button to the layout
        self.add_app_button = QPushButton("Save Settings")
        self.layout().addWidget(self.add_app_button)

    def create_settings_tab(self, tab_name, layout_name):
        """
        Creates a settings tab with a scroll area and layout.

        Args:
            tab_name (str): Name of the tab.
            layout_name (str): Name of the layout variable.

        Returns:
            None
        """
        # Create a tab
        tab = QWidget()
        tab_layout = QVBoxLayout(tab)

        # Create a scroll area and add it to the tab
        tab_scroll_area = QScrollArea()
        tab_scroll_area.setWidgetResizable(True)
        tab_layout.addWidget(tab_scroll_area)

        # Create a widget to hold settings for the tab
        tab_settings_widget = QWidget()

        # Set the scroll area's widget to the tab settings widget
        tab_scroll_area.setWidget(tab_settings_widget)

        # Set the layout for the tab settings widget
        setattr(self, layout_name, QVBoxLayout(tab_settings_widget))
        tab_settings_widget.setLayout(getattr(self, layout_name))

        self.tab_widget.addTab(tab, tab_name)

    def populate_settings(self, setting_classes):
        """
        Populates the settings panel with the provided setting classes.

        Args:
            setting_classes (list): List of setting classes to populate the
            panel with.

        Returns:
            None
        """
        for setting_class in setting_classes:
            title = setting_class.get_title()
            options = setting_class.get_options()
            tooltip_header = setting_class.get_tooltip_header()
            tooltip_body = setting_class.get_tooltip_body()
            rule = setting_class.get_rule()
            self.add_setting(
                title,
                options,
                tooltip_header,
                tooltip_body,
                rule)

    def add_setting(self, title, options, tooltip_header, tooltip_body, rule):
        """
    Adds a setting to the appropriate settings layout based on combobox ID
    range.

    Args:
        title (str): Title of the setting.
        options (list): List of options for the setting.
        tooltip_header (str): Header text for the tooltip.
        tooltip_body (str): Body text for the tooltip.

    Returns:
        None
    """
        # Create a container widget for the setting
        container = QWidget()
        container_layout = QVBoxLayout(container)

        # Create a horizontal rule
        horizontal_rule = QLabel(
            '<html><body><hr /></body></html>')

        # Create a QLabel to display the setting title
        label = QLabel(
            f'<html><body>{title}</body></html>')

        # Create a QComboBox to select options
        combobox = QComboBox()
        combobox.addItems(options)

        # Set tooltip for the label
        label.setToolTip(
            f'<html><body>{tooltip_header}{tooltip_body}</body></html>')

        # Add the label and combobox to the container layout
        container_layout.addWidget(label)
        container_layout.addWidget(combobox)
        if rule == (True):
            container_layout.addWidget(horizontal_rule)

        # Determine the appropriate settings layout based on combobox ID range
        combobox_id = len(self.comboboxes)
        if combobox_id in range(10):
            settings_layout = self.aa_settings_layout
            disabled_comboboxes = (1, 2, 3, 5, 6, 7, 8, 9)
        elif combobox_id in range(10, 18):
            settings_layout = self.af_settings_layout
            disabled_comboboxes = (11, 12, 14, 15, 16, 17)
        elif combobox_id in range(18, 23):
            settings_layout = self.sharpness_settings_layout
            disabled_comboboxes = (19, 21, 22)
        elif combobox_id in range(23, 29):
            settings_layout = self.vsync_settings_layout
            disabled_comboboxes = (24, 25, 27, 28)
        else:
            settings_layout = self.misc_settings_layout
            disabled_comboboxes = []

        # Add the container to the appropriate settings layout
        settings_layout.addWidget(container)

        # Set property ID for the combobox and store it in the dictionary
        combobox.setProperty("id", combobox_id)
        self.comboboxes[combobox_id] = combobox

        # Connect combobox signal to function for enabling or disabling
        # other comboboxes
        combobox.currentIndexChanged.connect(self.toggle_comboboxes)

        # Disable specific comboboxes initially
        if combobox_id in disabled_comboboxes:
            combobox.setEnabled(False)

    def toggle_comboboxes(self, index):
        """
        Toggles the state of comboboxes based on the index of the selected
        item.

        Args:
            index (int): Index of the selected item in the combobox.

        Returns:
            None
        """
        # Get the combobox that emitted the signal
        sender_combobox = self.sender()
        # Get the combobox ID
        combobox_id = sender_combobox.property("id")

        # Determine which comboboxes to activate based on the sender_combobox

        # FXAA Enable:
        if combobox_id == 0 and index == 1:
            for id in range(1, 4):
                self.comboboxes[id].setEnabled(True)
        elif combobox_id == 0 and index in [0, 2]:
            for id in range(1, 4):
                self.comboboxes[id].setEnabled(False)

        # SMAA Enable:
        elif combobox_id == 4 and index == 1:
            for id in range(5, 10):
                self.comboboxes[id].setEnabled(True)
        elif combobox_id == 4 and index in [0, 2]:
            for id in range(5, 10):
                self.comboboxes[id].setEnabled(False)

        # AF Enable:
        elif combobox_id == 10 and index == 1:
            self.comboboxes[11].setEnabled(True)
            self.comboboxes[12].setEnabled(False)
        elif combobox_id == 10 and index == 2:
            self.comboboxes[11].setEnabled(False)
            self.comboboxes[12].setEnabled(True)
        elif combobox_id == 10 and index in [0, 3]:
            self.comboboxes[11].setEnabled(False)
            self.comboboxes[12].setEnabled(False)

        # LOD Enable:
        elif combobox_id == 13 and index == 1:
            self.comboboxes[14].setEnabled(True)
            self.comboboxes[15].setEnabled(False)
            self.comboboxes[16].setEnabled(True)
            self.comboboxes[17].setEnabled(False)
        elif combobox_id == 13 and index == 2:
            self.comboboxes[14].setEnabled(False)
            self.comboboxes[15].setEnabled(True)
            self.comboboxes[16].setEnabled(False)
            self.comboboxes[17].setEnabled(True)
        elif combobox_id == 13 and index in [0, 3]:
            self.comboboxes[14].setEnabled(False)
            self.comboboxes[15].setEnabled(False)
            self.comboboxes[16].setEnabled(False)
            self.comboboxes[17].setEnabled(False)

        # CAS Enable:
        elif combobox_id == 18 and index == 1:
            self.comboboxes[19].setEnabled(True)
        elif combobox_id == 18 and index in [0, 2]:
            self.comboboxes[19].setEnabled(False)

        # DLS Enable:
        elif combobox_id == 20 and index == 1:
            self.comboboxes[21].setEnabled(True)
            self.comboboxes[22].setEnabled(True)
        elif combobox_id == 20 and index in [0, 2]:
            self.comboboxes[21].setEnabled(False)
            self.comboboxes[22].setEnabled(False)

        # VSync Enable:
        elif combobox_id == 23 and index == 1:
            self.comboboxes[24].setEnabled(True)
            self.comboboxes[25].setEnabled(False)
        elif combobox_id == 23 and index == 2:
            self.comboboxes[24].setEnabled(False)
            self.comboboxes[25].setEnabled(True)
        elif combobox_id == 23 and index in [0, 3]:
            self.comboboxes[24].setEnabled(False)
            self.comboboxes[25].setEnabled(False)

        # Frame Limit Enable
        elif combobox_id == 26 and index == 1:
            self.comboboxes[27].setEnabled(True)
            self.comboboxes[28].setEnabled(False)
        elif combobox_id == 26 and index == 2:
            self.comboboxes[27].setEnabled(False)
            self.comboboxes[28].setEnabled(True)
        elif combobox_id == 26 and index in [0, 3]:
            self.comboboxes[27].setEnabled(False)
            self.comboboxes[28].setEnabled(False)

    def set_panel_inactive(self, inactive: bool) -> None:
        pass

    def pass_to_settings_panel(self, app_settings_input: dict) -> None:
        app_settings: dict = app_settings_input

    def pass_to_app_list_panel():
        pass

    def save_settings(self, index):
        pass
