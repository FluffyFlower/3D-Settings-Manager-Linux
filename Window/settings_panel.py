"""
File       : settings_panel.py
Author     : Fluffy Flower (Martin Wylde)
Contact    :
    Email   - martincw1989@gmail.com
    Telegram- @FluffyFlower
    Discord - fluffy_flower
Date       : 23/01/2025
Version    : 1.0.1
Description: Settings panel file for building settings panel and importing settings objects to be displayed as titles, comboboxes, tooltips.
Also contains methods for loading and saving settings.
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
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QComboBox, QScrollArea, QPushButton, QTabWidget, QMessageBox
from Window.Settings import *
from PyQt6.QtCore import Qt
from Window.json_handler import AppJSONHandler
from Window.conf_handler import AppConfHandler


# ------------------------------------------------------------------------------------------------------------ #
#                                                                                                              #
# ██████                          ██                                    ██████                                 #
# ██        ████    ██      ██          ██████    ████    ████          ██  ██    ████  ██████    ████  ██     #
# ██████  ██  ██  ██████  ██████  ██    ██  ██  ██  ██    ██            ██████  ██  ██  ██  ██  ██  ██  ██     #
#     ██  ████      ██      ██    ██    ██  ██  ██████    ██            ██      ██  ██  ██  ██  ████    ██     #
# ██████    ████    ████    ████  ████  ██  ██      ██  ████            ██      ██████  ██  ██    ████  ██████ #
#                                               ████                                                           #
# ------------------------------------------------------------------------------------------------------------ #


class SettingsPanel(QWidget):
    """
    SettingsPanel class for creating the settings panel widget, and associated operations (load and save).
    """

    _json_handler = AppJSONHandler()
    _conf_handler = AppConfHandler()

    # ------------------------------------------------------------------------------ #
    # Panel initialisation & layout creation.                                        #
    # ------------------------------------------------------------------------------ #
    def __init__(self, app_list_panel_ref, parent=None) -> None:
        """
        Initializes the SettingsPanel widget.

        Args:
            None

        Returns:
            None

        Examples:
            Default usage:
                .. code-block:: python
                >>> variable = SettingsPanel()
        """
        super().__init__(parent)

        # Store reference to app_list_panel
        self.app_list_panel_ref = app_list_panel_ref

        # Create QVBoxLayout
        self.setLayout(QVBoxLayout())

        # Create a panel label and add it to the layout
        label_text: str = "Settings"
        self.label = QLabel(f'<html><body><h3><b><u>{label_text}</u></b></h3></body></html>')
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout().addWidget(self.label)

        # Create a tab widget and add it to the layout
        self.tab_widget = QTabWidget()
        self.layout().addWidget(self.tab_widget)

        # Dynamically make and add the tabs to the layout
        self.create_settings_tab("Anti-Aliasing", "aa_settings_layout")
        self.create_settings_tab("Anisotropic Filtering", "af_settings_layout")
        self.create_settings_tab("Sharpening", "sharpness_settings_layout")
        self.create_settings_tab("VSync && Frame Limits", "vsync_settings_layout")
        self.create_settings_tab("Misc Settings", "misc_settings_layout")
        
        # Dictionary to store comboboxes and their IDs
        self.comboboxes: dict = {}

        # List of the setting classes
        setting_classes: list = [
            # Anti-Aliasing Classes:              ComboBox IDs 0 - 9
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

            # Anistropic Filtering / LOD Classes: ComboBox IDs 10 - 17
            Anisotropic_Filtering_Enable(),     # ID - 10
            Anisotropic_Filtering_Level(),      # ID - 11
            Anisotropic_Filtering_Level_D3D9(), # ID - 12
            LOD_Enable(),                       # ID - 13
            LOD_Bias(),                         # ID - 14
            LOD_Bias_D3D9(),                    # ID - 15
            Clamp_Negative_LOD(),               # ID - 16
            Clamp_Negative_LOD_D3D9(),          # ID - 17

            # Sharpening Classes:                 ComboBox IDs 18 - 22
            CAS_Enable(),                       # ID - 18
            CAS_Sharpness(),                    # ID - 19
            DLS_Enable(),                       # ID - 20
            DLS_Sharpness(),                    # ID - 21
            DLS_Denoise(),                      # ID - 22

            # VSync / Frame Limiting Classes:     ComboBox IDs 23 - 28
            VSync_Enable(),                     # ID - 23
            VSync_Level(),                      # ID - 24
            VSync_Level_D3D9(),                 # ID - 25
            Frame_Limit_Enable(),               # ID - 26
            Frame_Limit(),                      # ID - 27
            Frame_Limit_D3D9(),                 # ID - 28

            # Misc Classes:                       ComboBox IDs 29 - 30
            HighDynamicRange(),                 # ID - 29
            D3D_Level()                         # ID - 30
            ]

        # Populate the settings
        self.populate_settings(setting_classes)

        # Create and add a 'Load Settings' button to the layout
        self.load_settings_button = QPushButton("Load Settings")
        self.layout().addWidget(self.load_settings_button)

        # Connect the load button click signal to handler
        self.load_settings_button.clicked.connect(self.load_settings)

        # Create and add a 'Save Settings' button to the layout
        self.save_settings_button = QPushButton("Save Settings")
        self.layout().addWidget(self.save_settings_button)

        # Connect the save button click signal to handler
        self.save_settings_button.clicked.connect(self.save_settings)

    # ------------------------------------------------------------------------------ #
    # Create settings tab.                                                           #
    # ------------------------------------------------------------------------------ #
    def create_settings_tab(self, 
                            tab_name: str, 
                            layout_name: str) -> None:
        """
        Creates a settings tab with a scroll area and layout.

        Args:
            tab_name (str): Name of the tab.
            layout_name (str): Name of the layout variable.

        Returns:
            None
        
        Raises:
            None

        Examples:
            Create a settings tab:
                .. code-block:: python
                >>> create_settings_tab("Tab Name", "layout_name")
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

    # ------------------------------------------------------------------------------ #
    # Populate settings tab.                                                         #
    # ------------------------------------------------------------------------------ #
    def populate_settings(self, 
                          setting_classes: list) -> None:
        """
        Populates the settings panel with the provided setting classes.

        Args:
            setting_classes (list): List of setting classes to populate the
            panel with.

        Returns:
            None

        Raises:
            None

        Examples:
            Default usage:
                .. code-block:: python
                >>> populate_settings(setting_classes)
        """
        for setting_class in setting_classes:
            title = setting_class.get_title()
            options = setting_class.get_options()
            tooltip_header = setting_class.get_tooltip_header()
            tooltip_body = setting_class.get_tooltip_body()
            rule = setting_class.get_rule()
            self.add_setting(title, options, tooltip_header, tooltip_body,rule)

        # Keep settings pushed to top of tab
        self.aa_settings_layout.addStretch()
        self.af_settings_layout.addStretch()
        self.sharpness_settings_layout.addStretch()
        self.vsync_settings_layout.addStretch()
        self.misc_settings_layout.addStretch()

    # ------------------------------------------------------------------------------ #
    # Add setting to settings tab.                                                   #
    # ------------------------------------------------------------------------------ #
    def add_setting(self, 
                    title: str, 
                    options: list, 
                    tooltip_header: str, 
                    tooltip_body: str, 
                    rule: bool) -> None:
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

        Raises:
            None

        Examples:
            Default usage:
                .. code-block:: python
                >>> add_setting(title, options, tooltip_header, tooltip_body, rule)
        """
        # Create a container widget for the setting
        container = QWidget()
        container_layout = QVBoxLayout(container)

        # Create a horizontal rule
        horizontal_rule = QLabel('<html><body><hr /></body></html>')

        # Create a QLabel to display the setting title
        label = QLabel(f'<html><body>{title}</body></html>')

        # Create a QComboBox to select options
        combobox = QComboBox()
        combobox.addItems(options)

        # Set tooltip for the label
        label.setToolTip(f'<html><body>{tooltip_header}{tooltip_body}</body></html>')
        
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

    # ------------------------------------------------------------------------------ #
    # Toggle comboboxes in settings tabs.                                            #
    # ------------------------------------------------------------------------------ #
    def toggle_comboboxes(self, 
                          index: int) -> None:
        """
        Toggles the state of comboboxes based on the index of the selected
        item and for initial display.

        Args:
            index (int): Index of the selected item in the combobox.

        Returns:
            None

        Raises:
            None

        Examples:
            Default usage:
                .. code-block:: python
                >>> toggle_comboboxes(index)
        """
        # Get the combobox that emitted the signal
        sender_combobox = self.sender()
        # Get the combobox ID
        combobox_id = sender_combobox.property("id")

        # Determine which comboboxes to activate based on the sender_combobox

        # FXAA Enable:
        if combobox_id == 0 and index == 1: # Set to 'Enabled'
            for id in range(1, 4):
                self.comboboxes[id].setEnabled(True) # Activate FXAA options
        elif combobox_id == 0 and index in [0, 2]: # Not set to 'Enabled' or not selected
            for id in range(1, 4):
                self.comboboxes[id].setEnabled(False) # Deactivate FXAA options

        # SMAA Enable:
        elif combobox_id == 4 and index == 1: # Set to 'Enabled'
            for id in range(5, 10):
                self.comboboxes[id].setEnabled(True) # Activate SMAA options
        elif combobox_id == 4 and index in [0, 2]: # Not set to 'Enabled' or not selected
            for id in range(5, 10):
                self.comboboxes[id].setEnabled(False) # Deactivate SMAA options

        # AF Enable:
        elif combobox_id == 10 and index == 1: # Set to 'Enabled'
            self.comboboxes[11].setEnabled(True) # Activate AF Level
            self.comboboxes[12].setEnabled(False) # Deactivate AF Level D3D9
        elif combobox_id == 10 and index == 2: # Set to 'Enabled D3D9'
            self.comboboxes[11].setEnabled(False) # Deactivate AF Level
            self.comboboxes[12].setEnabled(True) # Activate AF Level D3D9
        elif combobox_id == 10 and index in [0, 3]: # Not set to 'Enabled' or not selected
            self.comboboxes[11].setEnabled(False) # Deactivate AF Level
            self.comboboxes[12].setEnabled(False) # Deactivate AF Level D3D9

        # LOD Enable:
        elif combobox_id == 13 and index == 1: # Set to 'Enabled'
            self.comboboxes[14].setEnabled(True) # Activate LOD Bias
            self.comboboxes[15].setEnabled(False) # Deactivate LOD Bias D3D9
            self.comboboxes[16].setEnabled(True) # Activate Clamp Negative LOD
            self.comboboxes[17].setEnabled(False) # Deactivate Clamp Negative LOD D3D9
        elif combobox_id == 13 and index == 2: # Set to 'Enabled D3D9'
            self.comboboxes[14].setEnabled(False) # Deactivate LOD Bias
            self.comboboxes[15].setEnabled(True) # Activate LOD Bias D3D9
            self.comboboxes[16].setEnabled(False) # Deactivate Clamp Negative LOD
            self.comboboxes[17].setEnabled(True) # Activate Clamp Negative LOD D3D9
        elif combobox_id == 13 and index in [0, 3]: # Not set to 'Enabled' or not selected
            self.comboboxes[14].setEnabled(False) # Deactivate LOD Bias
            self.comboboxes[15].setEnabled(False) # Deactivate LOD Bias D3D9
            self.comboboxes[16].setEnabled(False) # Deactivate Clamp Negative LOD
            self.comboboxes[17].setEnabled(False) # Deactivate Clamp Negative LOD D3D9

        # CAS Enable:
        elif combobox_id == 18 and index == 1: # Set to 'Enabled'
            self.comboboxes[19].setEnabled(True) # Activate CAS Sharpness
        elif combobox_id == 18 and index in [0, 2]: # Not set to 'Enabled' or not selected
            self.comboboxes[19].setEnabled(False) # Deactivate CAS Sharpness

        # DLS Enable:
        elif combobox_id == 20 and index == 1: # Set to 'Enabled'
            self.comboboxes[21].setEnabled(True) # Activate DLS Sharpness
            self.comboboxes[22].setEnabled(True) # Activate DLS Denoise
        elif combobox_id == 20 and index in [0, 2]: # Not set to 'Enabled' or not selected
            self.comboboxes[21].setEnabled(False) # Deactivate DLS Sharpness
            self.comboboxes[22].setEnabled(False) # Deactivate DLS Denoise

        # VSync Enable:
        elif combobox_id == 23 and index == 1: # Set to 'Enabled'
            self.comboboxes[24].setEnabled(True) # Activate VSync Level
            self.comboboxes[25].setEnabled(False) # Deactivate VSync Level D3D9
        elif combobox_id == 23 and index == 2: # Set to 'Enabled D3D9'
            self.comboboxes[24].setEnabled(False) # Deactivate VSync Level
            self.comboboxes[25].setEnabled(True) # Activate VSync Level D3D9
        elif combobox_id == 23 and index in [0, 3]: # Not set to 'Enabled' or not selected
            self.comboboxes[24].setEnabled(False) # Deactivate VSync Level
            self.comboboxes[25].setEnabled(False) # Deactivate VSync Level D3D9

        # Frame Limit Enable
        elif combobox_id == 26 and index == 1: # Set to 'Enabled'
            self.comboboxes[27].setEnabled(True) # Activate Frame Limit
            self.comboboxes[28].setEnabled(False) # Deactivate Frame Limit D3D9
        elif combobox_id == 26 and index == 2: # Set to 'Enabled D3D9'
            self.comboboxes[27].setEnabled(False) # Deactivate Frame Limit
            self.comboboxes[28].setEnabled(True) # Activate Frame Limit D3D9
        elif combobox_id == 26 and index in [0, 3]: # Not set to 'Enabled' or not selected
            self.comboboxes[27].setEnabled(False) # Deactivate Frame Limit
            self.comboboxes[28].setEnabled(False) # Deactivate Frame Limit D3D9

    # ------------------------------------------------------------------------------ #
    # Get combobox current values                                                    #
    # ------------------------------------------------------------------------------ #
    def get_combobox_values(self) -> list:
        """
        Gets the current values of all comboboxes in the settings panel.

        Args:
            None.

        Returns:
            list: List of current combobox values.

        Raises:
            None.

        Examples:
            Default usage:
                .. code-block:: python
                >>> combobox_values: list = get_combobox_values()
        """
        # Check each sectional combobox and get its value based on its index
        # FXAA Settings
        if self.comboboxes[0].currentIndex() == 1: # If FXAA is enabled
            fxaa_enable: bool = True
            fxaa_quality_subpixel: str = self.comboboxes[1].currentText()
            fxaa_quality_edge: str = self.comboboxes[2].currentText()
            fxaa_edge_threshold: str = self.comboboxes[3].currentText()
        elif self.comboboxes[0].currentIndex() == 2: # If FXAA is disabled
            fxaa_enable: bool = False
            fxaa_quality_subpixel: str = None
            fxaa_quality_edge: str = None
            fxaa_edge_threshold: str = None
        else: # If FXAA is not selected
            fxaa_enable: bool = None
            fxaa_quality_subpixel: str = None
            fxaa_quality_edge: str = None
            fxaa_edge_threshold: str = None

        # SMAA Settings
        if self.comboboxes[4].currentIndex() == 1: # If SMAA is enabled
            smaa_enable: bool = True
            smaa_edge_detection: str = self.comboboxes[5].currentText()
            smaa_threshold: str = self.comboboxes[6].currentText()
            smaa_search_steps: str = self.comboboxes[7].currentText()
            smaa_search_steps_diagonal: str = self.comboboxes[8].currentText()
            smaa_corner_rounding: str = self.comboboxes[9].currentText()
        elif self.comboboxes[4].currentIndex() == 2: # If SMAA is disabled
            smaa_enable: bool = False
            smaa_edge_detection: str = None
            smaa_threshold: str = None
            smaa_search_steps: str = None
            smaa_search_steps_diagonal: str = None
            smaa_corner_rounding: str = None
        else: # If SMAA is not selected
            smaa_enable: bool = None
            smaa_edge_detection: str = None
            smaa_threshold: str = None
            smaa_search_steps: str = None
            smaa_search_steps_diagonal: str = None
            smaa_corner_rounding: str = None

        # Anistropic Filtering Settings
        if self.comboboxes[10].currentText() == "Enable": # If AF is enabled
            anistropic_enable: str = self.comboboxes[10].currentText()
            anistropic_level: str = self.comboboxes[11].currentText()
            anistropic_level_d3d9: str = None
        elif self.comboboxes[10].currentText() == "Enable (D3D9)": # If AF is enabled D3D9
            anistropic_enable: str = self.comboboxes[10].currentText()
            anistropic_level: str = None
            anistropic_level_d3d9: str = self.comboboxes[12].currentText()
        elif self.comboboxes[10].currentText() == "Disable": # If AF is disabled
            anistropic_enable: str = self.comboboxes[10].currentText()
            anistropic_level: str = None
            anistropic_level_d3d9: str = None
        else: # If AF is not selected
            anistropic_enable: str = None
            anistropic_level: str = None
            anistropic_level_d3d9: str = None

        # LOD Settings
        if self.comboboxes[13].currentText() == "Enable": # If LOD is enabled
            lod_enable: str = self.comboboxes[13].currentText()
            lod_bias: str = self.comboboxes[14].currentText()
            lod_bias_d3d9: str = None
            clamp_negative_lod: str = self.comboboxes[16].currentText()
            clamp_negative_lod_d3d9: str = None
        elif self.comboboxes[13].currentText() == "Enable (D3D9)": # If LOD is enabled D3D9
            lod_enable: str = self.comboboxes[13].currentText()
            lod_bias: str = None
            lod_bias_d3d9: str = self.comboboxes[15].currentText()
            clamp_negative_lod: str = None
            clamp_negative_lod_d3d9: str = self.comboboxes[17].currentText()
        elif self.comboboxes[13].currentText() == "Disable": # If LOD is disabled
            lod_enable: str = self.comboboxes[13].currentText()
            lod_bias: str = None
            lod_bias_d3d9: str = None
            clamp_negative_lod: str = None
            clamp_negative_lod_d3d9: str = None
        else: # If LOD is not selected
            lod_enable: bool = None
            lod_bias: str = None
            lod_bias_d3d9: str = None
            clamp_negative_lod: str = None
            clamp_negative_lod_d3d9: str = None

        # Contrast Adaptive Sharpening (CAS) Settings
        if self.comboboxes[18].currentIndex() == 1: # If CAS is enabled
            cas_enable: bool = True
            cas_sharpness: str = self.comboboxes[19].currentText()
        elif self.comboboxes[18].currentIndex() == 2: # If CAS is disabled
            cas_enable: bool = False
            cas_sharpness: str = None
        else: # If CAS is not selected
            cas_enable: bool = None
            cas_sharpness: str = None

        # Denoised Luma Sharpening (DLS) Settings
        if self.comboboxes[20].currentIndex() == 1: # If DLS is enabled
            dls_enable: bool = True
            dls_sharpness: str = self.comboboxes[21].currentText()
            dls_denoise: str = self.comboboxes[22].currentText()
        elif self.comboboxes[20].currentIndex() == 2: # If DLS is disabled
            dls_enable: bool = False
            dls_sharpness: str = None
            dls_denoise: str = None
        else: # If DLS is not selected
            dls_enable: bool = None
            dls_sharpness: str = None
            dls_denoise: str = None

        # VSync Settings
        if self.comboboxes[23].currentText() == "Enable": # If VSync is enabled
            vsync_enable: str = self.comboboxes[23].currentText()
            vsync_level: str = self.comboboxes[24].currentText()
            vsync_level_d3d9: str = None
        elif self.comboboxes[23].currentText() == "Enable (D3D9)": # If VSync is enabled D3D9
            vsync_enable: str = self.comboboxes[23].currentText()
            vsync_level: str = None
            vsync_level_d3d9: str = self.comboboxes[25].currentText()
        elif self.comboboxes[23].currentText() == "Disable": # If VSync is disabled
            vsync_enable: bool = self.comboboxes[23].currentText()
            vsync_level: str = None
            vsync_level_d3d9: str = None
        else: # If VSync is not selected
            vsync_enable: bool = None
            vsync_level: str = None
            vsync_level_d3d9: str = None

        # Frame Limit Settings
        if self.comboboxes[26].currentText() == "Enable": # If Frame Limit is enabled
            frame_limit_enable: str = self.comboboxes[23].currentText()
            frame_limit_level: str = self.comboboxes[27].currentText()
            frame_limit_level_d3d9: str = None
        elif self.comboboxes[26].currentText() == "Enable (D3D9)": # If Frame Limit is enabled D3D9
            frame_limit_enable: str = self.comboboxes[23].currentText()
            frame_limit_level: str = None
            frame_limit_level_d3d9: str = self.comboboxes[28].currentText()
        elif self.comboboxes[26].currentText() == "Disable": # If Frame Limit is disabled
            frame_limit_enable: str = self.comboboxes[23].currentText()
            frame_limit_level: str = None
            frame_limit_level_d3d9: str = None
        else: # If Frame Limit is not selected
            frame_limit_enable: bool = None
            frame_limit_level: str = None
            frame_limit_level_d3d9: str = None

        # Misc Settings
        if self.comboboxes[29].currentIndex() == 1: # If HDR is enabled
            hdr_enable: bool = True
        elif self.comboboxes[29].currentIndex() == 2: # If HDR is disabled
            hdr_enable: bool = False
        else: # If HDR is not selected
            hdr_enable: bool = None

        if self.comboboxes[30].currentIndex() != 0: # If D3D Level is selected
            d3d_level: str = self.comboboxes[30].currentText()
        else: # If D3D Level is not selected
            d3d_level: str = None


        return [
            fxaa_enable,
            fxaa_quality_subpixel,
            fxaa_quality_edge,
            fxaa_edge_threshold,
            smaa_enable,
            smaa_edge_detection,
            smaa_threshold,
            smaa_search_steps,
            smaa_search_steps_diagonal,
            smaa_corner_rounding,
            anistropic_enable,
            anistropic_level,
            anistropic_level_d3d9,
            lod_enable,
            lod_bias,
            lod_bias_d3d9,
            clamp_negative_lod,
            clamp_negative_lod_d3d9,
            cas_enable,
            cas_sharpness,
            dls_enable,
            dls_sharpness,
            dls_denoise,
            vsync_enable,
            vsync_level,
            vsync_level_d3d9,
            frame_limit_enable,
            frame_limit_level,
            frame_limit_level_d3d9,
            hdr_enable,
            d3d_level
        ]
    # ------------------------------------------------------------------------------ #
    # Save settings values                                                           #
    # ------------------------------------------------------------------------------ #
    def save_settings(self):
        """
        Saves the current settings to the JSON database and configuration files (dxvk.conf | vkBasalt.conf).
        
        Args: 
            None

        Returns:
            None

        Raises:
            None

        Examples:
            Default usage:
                .. code-block:: python
                >>> save_settings()
        """
        settings_list: list = self.app_list_panel_ref.get_selected_application()

        selection_check: bool = settings_list[0]
        if selection_check == False:
            return

        app_path: str = settings_list[1]
        app_name: str = settings_list[2]
        app_gapi: str = settings_list[3]

        gui_data: list = self.get_combobox_values()

        self._json_handler.add_app_settings(app_path, app_name, app_gapi, gui_data)
        
        self._conf_handler.save_conf_vkbasalt(app_path, gui_data)
        self._conf_handler.save_conf_dxvk(app_path, gui_data)

        converted_path = os.path.dirname(app_path) + "/"
        QMessageBox.information(self, "Application Settings Saved!", f'<p>Application settings have been saved successfully, to both the internal database and configuration files;</p>\n\n<p style="font-style: italic; color: green;">{converted_path}dxvk.conf<br>{converted_path}vkBasalt.conf</p>\n\n<p>Add the following line to your steam launch arguments (<span style="font-style: italic;">if not already present</span>):</p>\n\n<p style="font-weight: bold; color: CornflowerBlue;">ENABLE_VKBASALT=1 &lt;<span style="font-style: italic;">your existing launch arguments</span>&gt; %command%')

    # ------------------------------------------------------------------------------ #
    # Load settings values                                                           #
    # ------------------------------------------------------------------------------ #
    def load_settings(self):
        """
        Loads the settings from the JSON database and updates the GUI comboboxes accordingly.

        Args:
            None
        
        Returns:
            None

        Raises:
            None

        Examples:
            Default usage:
                .. code-block:: python
                >>> load_settings()
        """
        settings_list: list = self.app_list_panel_ref.get_selected_application()

        selection_check: bool = settings_list[0]
        if selection_check == False:
            return
        
        app_path: str = settings_list[1]
        app_name: str = settings_list[2]
        app_gapi: str = settings_list[3]

        gui_data: list = self._json_handler.get_app_settings(app_path, app_name, app_gapi)
        
        fxaa_enable: bool = gui_data[0]
        fxaa_quality_subpixel: str = gui_data[1]
        fxaa_quality_edge: str = gui_data[2]
        fxaa_edge_threshold: str = gui_data[3]
        smaa_enable: bool = gui_data[4]
        smaa_edge_detection: str = gui_data[5]
        smaa_threshold: str = gui_data[6]
        smaa_search_steps: str = gui_data[7]
        smaa_search_steps_diagonal: str = gui_data[8]
        smaa_corner_rounding: str = gui_data[9]
        anisotropic_enable: str = gui_data[10]
        anisotropic_level: str = gui_data[11]
        anisotropic_level_d3d9: str = gui_data[12]
        lod_enable: str = gui_data[13]
        lod_bias: str = gui_data[14]
        lod_bias_d3d9: str = gui_data[15]
        clamp_negative_lod: str = gui_data[16]
        clamp_negative_lod_d3d9: str = gui_data[17]
        cas_enable: bool = gui_data[18]
        cas_sharpness: str = gui_data[19]
        dls_enable: bool = gui_data[20]
        dls_sharpness: str = gui_data[21]
        dls_denoise: str = gui_data[22]
        vsync_enable: str = gui_data[23]
        vsync_level: str = gui_data[24]
        vsync_level_d3d9: str = gui_data[25]
        frame_limit_enable: str = gui_data[26]
        frame_limit_level: str = gui_data[27]
        frame_limit_level_d3d9: str = gui_data[28]
        hdr_enable: bool = gui_data[29]
        d3d_level: str = gui_data[30]

        # Set each sectional combobox based on the retrieved values
        # FXAA Settings
        if fxaa_enable == True:
            self.comboboxes[0].setCurrentIndex(1) # Enable
            # Set FXAA Quality Subpixel
            if fxaa_quality_subpixel == None:
                self.comboboxes[1].setCurrentIndex(0)
            elif fxaa_quality_subpixel == "1.00":
                self.comboboxes[1].setCurrentIndex(1)
            elif fxaa_quality_subpixel == "0.75":
                self.comboboxes[1].setCurrentIndex(2)
            elif fxaa_quality_subpixel == "0.50":
                self.comboboxes[1].setCurrentIndex(3)
            elif fxaa_quality_subpixel == "0.25":
                self.comboboxes[1].setCurrentIndex(4)
            elif fxaa_quality_subpixel == "0.00":
                self.comboboxes[1].setCurrentIndex(5)
            # Set FXAA Quality Edge
            if fxaa_quality_edge == None:
                self.comboboxes[2].setCurrentIndex(0)
            elif fxaa_quality_edge == "Highest Quality":
                self.comboboxes[2].setCurrentIndex(1)
            elif fxaa_quality_edge == "High Quality":
                self.comboboxes[2].setCurrentIndex(2)
            elif fxaa_quality_edge == "Default":
                self.comboboxes[2].setCurrentIndex(3)
            elif fxaa_quality_edge == "Low Quality  ":
                self.comboboxes[2].setCurrentIndex(4)
            elif fxaa_quality_edge == "Lowest Quality":
                self.comboboxes[2].setCurrentIndex(5)
            # Set FXAA Edge Threshold
            if fxaa_edge_threshold == None:
                self.comboboxes[3].setCurrentIndex(0)
            elif fxaa_edge_threshold == "Upper Limit":
                self.comboboxes[3].setCurrentIndex(1)
            elif fxaa_edge_threshold == "High Quality":
                self.comboboxes[3].setCurrentIndex(2)
            elif fxaa_edge_threshold == "Visible Limit":
                self.comboboxes[3].setCurrentIndex(3)
            elif fxaa_edge_threshold == "Zero":
                self.comboboxes[3].setCurrentIndex(4)
        elif fxaa_enable == False:
            self.comboboxes[0].setCurrentIndex(2) # Disable
            self.comboboxes[1].setCurrentIndex(0)
            self.comboboxes[2].setCurrentIndex(0)
            self.comboboxes[3].setCurrentIndex(0)
        else:
            self.comboboxes[0].setCurrentIndex(0) # Not Selected
            self.comboboxes[1].setCurrentIndex(0)
            self.comboboxes[2].setCurrentIndex(0)
            self.comboboxes[3].setCurrentIndex(0)

        # SMAA Settings
        if smaa_enable == True:
            self.comboboxes[4].setCurrentIndex(1) # Enable
            # Set SMAA Edge Detection
            if smaa_edge_detection == None:
                self.comboboxes[5].setCurrentIndex(0)
            elif smaa_edge_detection == "Luma":
                self.comboboxes[5].setCurrentIndex(1)
            elif smaa_edge_detection == "Color":
                self.comboboxes[5].setCurrentIndex(2)
            # Set SMAA Threshold
            if smaa_threshold == None:
                self.comboboxes[6].setCurrentIndex(0)
            elif smaa_threshold == "Highest Quality":
                self.comboboxes[6].setCurrentIndex(1)
            elif smaa_threshold == "Quality":
                self.comboboxes[6].setCurrentIndex(2)
            elif smaa_threshold == "Balanced":
                self.comboboxes[6].setCurrentIndex(3)
            elif smaa_threshold == "Low Quality":
                self.comboboxes[6].setCurrentIndex(4)
            elif smaa_threshold == "Lowest Quality":
                self.comboboxes[6].setCurrentIndex(5)
            # Set SMAA Search Steps
            if smaa_search_steps == None:
                self.comboboxes[7].setCurrentIndex(0)
            elif smaa_search_steps == "x32":
                self.comboboxes[7].setCurrentIndex(1)
            elif smaa_search_steps == "x16":
                self.comboboxes[7].setCurrentIndex(2)
            elif smaa_search_steps == "x8":
                self.comboboxes[7].setCurrentIndex(3)
            elif smaa_search_steps == "x4":
                self.comboboxes[7].setCurrentIndex(4)
            elif smaa_search_steps == "x2":
                self.comboboxes[7].setCurrentIndex(5)
            # Set SMAA Search Steps Diagonal
            if smaa_search_steps_diagonal == None:
                self.comboboxes[8].setCurrentIndex(0)
            elif smaa_search_steps_diagonal == "x16":
                self.comboboxes[8].setCurrentIndex(1)
            elif smaa_search_steps_diagonal == "x8":
                self.comboboxes[8].setCurrentIndex(2)
            elif smaa_search_steps_diagonal == "x4":
                self.comboboxes[8].setCurrentIndex(3)
            elif smaa_search_steps_diagonal == "x2":
                self.comboboxes[8].setCurrentIndex(4)
            elif smaa_search_steps_diagonal == "x0":
                self.comboboxes[8].setCurrentIndex(5)
            # Set SMAA Corner Rounding
            if smaa_corner_rounding == None:
                self.comboboxes[9].setCurrentIndex(0)
            elif smaa_corner_rounding == "100":
                self.comboboxes[9].setCurrentIndex(1)
            elif smaa_corner_rounding == "75":
                self.comboboxes[9].setCurrentIndex(2)
            elif smaa_corner_rounding == "50":
                self.comboboxes[9].setCurrentIndex(3)
            elif smaa_corner_rounding == "25":
                self.comboboxes[9].setCurrentIndex(4)
            elif smaa_corner_rounding == "0":
                self.comboboxes[9].setCurrentIndex(5)
        elif smaa_enable == False:
            self.comboboxes[4].setCurrentIndex(2) # Disable
            self.comboboxes[5].setCurrentIndex(0)
            self.comboboxes[6].setCurrentIndex(0)
            self.comboboxes[7].setCurrentIndex(0)
            self.comboboxes[8].setCurrentIndex(0)
            self.comboboxes[9].setCurrentIndex(0)
        else:
            self.comboboxes[4].setCurrentIndex(0) # Not Selected
            self.comboboxes[5].setCurrentIndex(0)
            self.comboboxes[6].setCurrentIndex(0)
            self.comboboxes[7].setCurrentIndex(0)
            self.comboboxes[8].setCurrentIndex(0)
            self.comboboxes[9].setCurrentIndex(0)

        # Anisotropic Filtering Settings
        if anisotropic_enable == "Enable":
            self.comboboxes[10].setCurrentIndex(1) # Enable
            # Set Anisotropic Level
            if anisotropic_level == None:
                self.comboboxes[11].setCurrentIndex(0)
            elif anisotropic_level == "x16":
                self.comboboxes[11].setCurrentIndex(1)
            elif anisotropic_level == "x8":
                self.comboboxes[11].setCurrentIndex(2)
            elif anisotropic_level == "x4":
                self.comboboxes[11].setCurrentIndex(3)
            elif anisotropic_level == "x2":
                self.comboboxes[11].setCurrentIndex(4)
            elif anisotropic_level == "x1":
                self.comboboxes[11].setCurrentIndex(5)
        elif anisotropic_enable == "Enable (D3D9)":
            self.comboboxes[10].setCurrentIndex(2) # Enable (D3D9)
            # Set Anisotropic Level D3D9
            if anisotropic_level_d3d9 == None:
                self.comboboxes[12].setCurrentIndex(0)
            elif anisotropic_level_d3d9 == "x16":
                self.comboboxes[12].setCurrentIndex(1)
            elif anisotropic_level_d3d9 == "x8":
                self.comboboxes[12].setCurrentIndex(2)
            elif anisotropic_level_d3d9 == "x4":
                self.comboboxes[12].setCurrentIndex(3)
            elif anisotropic_level_d3d9 == "x2":
                self.comboboxes[12].setCurrentIndex(4)
            elif anisotropic_level_d3d9 == "x1":
                self.comboboxes[12].setCurrentIndex(5)
        elif anisotropic_enable == "Disable":
            self.comboboxes[10].setCurrentIndex(3) # Disable
            self.comboboxes[11].setCurrentIndex(0)
            self.comboboxes[12].setCurrentIndex(0)
        else:
            self.comboboxes[10].setCurrentIndex(0) # Not Selected
            self.comboboxes[11].setCurrentIndex(0)
            self.comboboxes[12].setCurrentIndex(0)

        # LOD Settings
        if lod_enable == "Enable":
            self.comboboxes[13].setCurrentIndex(1) # Enable
            # Set LOD Bias
            if lod_bias == None:
                self.comboboxes[14].setCurrentIndex(0)
            elif lod_bias == "-2.0":
                self.comboboxes[14].setCurrentIndex(1)
            elif lod_bias == "-1.0":
                self.comboboxes[14].setCurrentIndex(2)
            elif lod_bias == "0.0":
                self.comboboxes[14].setCurrentIndex(3)
            elif lod_bias == "0.5":
                self.comboboxes[14].setCurrentIndex(4)
            elif lod_bias == "1.0":
                self.comboboxes[14].setCurrentIndex(5)
            # Set Clamp Negative LOD
            if clamp_negative_lod == None:
                self.comboboxes[16].setCurrentIndex(0)
            elif clamp_negative_lod == "Enabled":
                self.comboboxes[16].setCurrentIndex(1)
            elif clamp_negative_lod == "Disabled":
                self.comboboxes[16].setCurrentIndex(2)
        elif lod_enable == "Enable (D3D9)":
            self.comboboxes[13].setCurrentIndex(2) # Enable (D3D9)
            # Set LOD Bias D3D9
            if lod_bias_d3d9 == None:
                self.comboboxes[15].setCurrentIndex(0)
            elif lod_bias_d3d9 == "-2.0":
                self.comboboxes[15].setCurrentIndex(1)
            elif lod_bias_d3d9 == "-1.0":
                self.comboboxes[15].setCurrentIndex(2)
            elif lod_bias_d3d9 == "0.0":
                self.comboboxes[15].setCurrentIndex(3)
            elif lod_bias_d3d9 == "0.5":
                self.comboboxes[15].setCurrentIndex(4)
            elif lod_bias_d3d9 == "1.0":
                self.comboboxes[15].setCurrentIndex(5)
            # Set Clamp Negative LOD D3D9
            if clamp_negative_lod_d3d9 == None:
                self.comboboxes[17].setCurrentIndex(0)
            elif clamp_negative_lod_d3d9 == "Enabled":
                self.comboboxes[17].setCurrentIndex(1)
            elif clamp_negative_lod_d3d9 == "Disabled":
                self.comboboxes[17].setCurrentIndex(2)
        elif lod_enable == "Disable":
            self.comboboxes[13].setCurrentIndex(3) # Disable
            self.comboboxes[14].setCurrentIndex(0)
            self.comboboxes[15].setCurrentIndex(0)
            self.comboboxes[16].setCurrentIndex(0)
            self.comboboxes[17].setCurrentIndex(0)
        else:
            self.comboboxes[13].setCurrentIndex(0) # Not Selected
            self.comboboxes[14].setCurrentIndex(0)
            self.comboboxes[15].setCurrentIndex(0)
            self.comboboxes[16].setCurrentIndex(0)
            self.comboboxes[17].setCurrentIndex(0)

        # CAS Settings
        if cas_enable == True:
            self.comboboxes[18].setCurrentIndex(1) # Enable
            # Set CAS Sharpness
            if cas_sharpness == None:
                self.comboboxes[19].setCurrentIndex(0)
            elif cas_sharpness == "1.00":
                self.comboboxes[19].setCurrentIndex(1)
            elif cas_sharpness == "0.75":
                self.comboboxes[19].setCurrentIndex(2)
            elif cas_sharpness == "0.50":
                self.comboboxes[19].setCurrentIndex(3)
            elif cas_sharpness == "0.25":
                self.comboboxes[19].setCurrentIndex(4)
            elif cas_sharpness == "0.00":
                self.comboboxes[19].setCurrentIndex(5)
            elif cas_sharpness == "Off":
                self.comboboxes[19].setCurrentIndex(6)
        elif cas_enable == False:
            self.comboboxes[18].setCurrentIndex(2) # Disable
            self.comboboxes[19].setCurrentIndex(0)
        else:
            self.comboboxes[18].setCurrentIndex(0) # Not Selected
            self.comboboxes[19].setCurrentIndex(0)

        # DLS Settings
        if dls_enable == True:
            self.comboboxes[20].setCurrentIndex(1) # Enable
            # Set DLS Sharpness
            if dls_sharpness == None:
                self.comboboxes[21].setCurrentIndex(0)
            elif dls_sharpness == "1.00":
                self.comboboxes[21].setCurrentIndex(1)
            elif dls_sharpness == "0.75":
                self.comboboxes[21].setCurrentIndex(2)
            elif dls_sharpness == "0.50":
                self.comboboxes[21].setCurrentIndex(3)
            elif dls_sharpness == "0.25":
                self.comboboxes[21].setCurrentIndex(4)
            elif dls_sharpness == "0.00":
                self.comboboxes[21].setCurrentIndex(5)
            # Set DLS Denoise
            if dls_denoise == None:
                self.comboboxes[22].setCurrentIndex(0)
            elif dls_denoise == "1.00":
                self.comboboxes[22].setCurrentIndex(1)
            elif dls_denoise == "0.75":
                self.comboboxes[22].setCurrentIndex(2)
            elif dls_denoise == "0.50":
                self.comboboxes[22].setCurrentIndex(3)
            elif dls_denoise == "0.25":
                self.comboboxes[22].setCurrentIndex(4)
        elif dls_enable == False:
            self.comboboxes[20].setCurrentIndex(2) # Disable
            self.comboboxes[21].setCurrentIndex(0)
            self.comboboxes[22].setCurrentIndex(0)
        else:
            self.comboboxes[20].setCurrentIndex(0) # Not Selected
            self.comboboxes[21].setCurrentIndex(0)
            self.comboboxes[22].setCurrentIndex(0)

        # VSync Settings
        if vsync_enable == "Enable":
            self.comboboxes[23].setCurrentIndex(1) # Enable
            # Set VSync Level
            if vsync_level == None:
                self.comboboxes[24].setCurrentIndex(0)
            elif vsync_level == "1 Frame":
                self.comboboxes[24].setCurrentIndex(1)
            elif vsync_level == "2 Frames":
                self.comboboxes[24].setCurrentIndex(2)
            elif vsync_level == "Off":
                self.comboboxes[24].setCurrentIndex(3)
        elif vsync_enable == "Enable (D3D9)":
            self.comboboxes[23].setCurrentIndex(2) # Enable (D3D9)
            # Set VSync Level D3D9
            if vsync_level_d3d9 == None:
                self.comboboxes[25].setCurrentIndex(0)
            elif vsync_level_d3d9 == "1 Frame":
                self.comboboxes[25].setCurrentIndex(1)
            elif vsync_level_d3d9 == "2 Frames":
                self.comboboxes[25].setCurrentIndex(2)
            elif vsync_level_d3d9 == "Off":
                self.comboboxes[25].setCurrentIndex(3)
        elif vsync_enable == "Disable":
            self.comboboxes[23].setCurrentIndex(3) # Disable
            self.comboboxes[24].setCurrentIndex(0)
            self.comboboxes[25].setCurrentIndex(0)
        else:            
            self.comboboxes[23].setCurrentIndex(0) # Not Selected
            self.comboboxes[24].setCurrentIndex(0)
            self.comboboxes[25].setCurrentIndex(0)

        # Frame Limit Settings
        if frame_limit_enable == "Enable":
            self.comboboxes[26].setCurrentIndex(1) # Enable
            # Set Frame Limit Level
            if frame_limit_level == None:
                self.comboboxes[27].setCurrentIndex(0)
            elif frame_limit_level == "30":
                self.comboboxes[27].setCurrentIndex(1)
            elif frame_limit_level == "60":
                self.comboboxes[27].setCurrentIndex(2)
            elif frame_limit_level == "75":
                self.comboboxes[27].setCurrentIndex(3)
            elif frame_limit_level == "120":
                self.comboboxes[27].setCurrentIndex(4)
            elif frame_limit_level == "144":
                self.comboboxes[27].setCurrentIndex(5)
            elif frame_limit_level == "240":
                self.comboboxes[27].setCurrentIndex(6)
        elif frame_limit_enable == "Enable (D3D9)":
            self.comboboxes[26].setCurrentIndex(2) # Enable (D3D9)
            # Set Frame Limit Level D3D9
            if frame_limit_level_d3d9 == None:
                self.comboboxes[28].setCurrentIndex(0)
            elif frame_limit_level_d3d9 == "30":
                self.comboboxes[28].setCurrentIndex(1)
            elif frame_limit_level_d3d9 == "60":
                self.comboboxes[28].setCurrentIndex(2)
            elif frame_limit_level_d3d9 == "75":
                self.comboboxes[28].setCurrentIndex(3)
            elif frame_limit_level_d3d9 == "120":
                self.comboboxes[28].setCurrentIndex(4)
            elif frame_limit_level_d3d9 == "144":
                self.comboboxes[28].setCurrentIndex(5)
            elif frame_limit_level_d3d9 == "240":
                self.comboboxes[28].setCurrentIndex(6)
        elif frame_limit_enable == "Disable":
            self.comboboxes[26].setCurrentIndex(3) # Disable
            self.comboboxes[27].setCurrentIndex(0)
            self.comboboxes[28].setCurrentIndex(0)
        else:         
            self.comboboxes[26].setCurrentIndex(0) # Not Selected
            self.comboboxes[27].setCurrentIndex(0)
            self.comboboxes[28].setCurrentIndex(0)

        # Misc Settings
        if hdr_enable == True:
            self.comboboxes[29].setCurrentIndex(1) # Enable
        elif hdr_enable == False:
            self.comboboxes[29].setCurrentIndex(2) # Disable
        else:
            self.comboboxes[29].setCurrentIndex(0) # Not Selected

        if d3d_level != None:
            # Set D3D Level
            if d3d_level == "Direct X 9.1":
                self.comboboxes[30].setCurrentIndex(1)
            elif d3d_level == "Direct X 9.2":
                self.comboboxes[30].setCurrentIndex(2)
            elif d3d_level == "Direct X 9.3":
                self.comboboxes[30].setCurrentIndex(3)
            elif d3d_level == "Direct X 10.0":
                self.comboboxes[30].setCurrentIndex(4)
            elif d3d_level == "Direct X 10.1":
                self.comboboxes[30].setCurrentIndex(5)
            elif d3d_level == "Direct X 11.0":
                self.comboboxes[30].setCurrentIndex(6)
            elif d3d_level == "Direct X 11.1":
                self.comboboxes[30].setCurrentIndex(7)
            elif d3d_level == "Direct X 12.0":
                self.comboboxes[30].setCurrentIndex(8)
            elif d3d_level == "Direct X 12.1":
                self.comboboxes[30].setCurrentIndex(9)
        else:
            self.comboboxes[30].setCurrentIndex(0) # Not Selected
            
        QMessageBox.information(self, "Application Settings Loaded!", f'Application settings have been loaded successfully from the internal database for <span style="font-weight: bold; color: CornflowerBlue;">{app_name}</span>.')