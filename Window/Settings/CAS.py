"""
File:
    CAS.py
Author:
    Fluffy Flower (Martin Wylde)
Date:
    23/01/2025
Version:
    0.1.1
Description:
    Contains classes representing various settings related to CAS (Contrast
    Adaptive Sharpening), along with a base class for all graphics settings.

    Each setting class includes attributes for title, options, tooltip header,
    and tooltip body, along with methods for retrieving these attributes.

    Additionally, global style variables are defined for consistent styling
    of HTML elements within the settings.

    These settings specifically pertain to the VKBasalt post-processing
    tool's CAS (Contrast Adaptive Sharpening) settings.
"""

# Global style variables
header = 'style="font-weight: bold; text-decoration: underline;"'
bodyTop = 'style="font-weight: bold;"'
bodyBot = 'style="font-style: italic;"'


class BaseSetting:
    """
    Base class for all graphics settings.

    Attributes:
        title (str): Title of the setting.
        options (list): List of options for the setting.
        tooltip_header (str): Header text for the tooltip.
        tooltip_body (str): Body text for the tooltip.
        rule (bool): Horizontal rule (optional).
    """

    def __init__(self, title, options, tooltip_header, tooltip_body, rule):
        """
        Initializes a graphics setting.

        Args:
            title (str): Title of the setting.
            options (list): List of options for the setting.
            tooltip_header (str): Header text for the tooltip.
            tooltip_body (str): Body text for the tooltip.
            rule (bool): Horizontal rule (optional).
        """
        self.title = title
        self.options = options
        self.tooltip_header = tooltip_header
        self.tooltip_body = tooltip_body
        self.rule = rule

    def get_title(self):
        """
        Gets the title of the setting.

        Returns:
            str: Title of the setting.
        """
        return self.title

    def get_options(self):
        """
        Gets the options of the setting.

        Returns:
            list: List of options for the setting.
        """
        return self.options

    def get_tooltip_header(self):
        """
        Gets the header text for the tooltip.

        Returns:
            str: Header text for the tooltip.
        """
        return self.tooltip_header

    def get_tooltip_body(self):
        """
        Gets the body text for the tooltip.

        Returns:
            str: Body text for the tooltip.
        """
        return self.tooltip_body

    def get_rule(self):
        """
        Gets the boolean value for whether to draw a horizontal rule.

        Returns:
            bool: True / False
        """
        return self.rule


class CAS_Enable(BaseSetting):
    # Class representing the enabling of CAS (Contrast Adaptive Sharpening).

    def __init__(self):
        """
        Initializes the CAS_Enable setting.

        Returns:

            str: Title of the setting (CAS_Enable) encoded in HTML
            tuple: Set of immutable options for the current setting (CAS_Enable)
            str: Tooltip header of the setting (CAS_Enable) encoded in HTML
            str: Tooltip body of the setting (CAS_Enable) encoded in HTML

        Examples:

        Instantiate the CAS_Enable setting:
            >>> cas_enable_setting = CAS()

        Retrieve the settings title:
            >>> cas_enable_setting.get_title()

        Retrieve the settings options:
            >>> cas_enable_setting.get_options()

        Retrieve the settings tooltip header:
            >>> cas_enable_setting.get_tooltip_header()

        Retrieve the settings tooltip body:
            >>> cas_enable_setting.get_tooltip_body()
        """
        title = f'<p>Enable CAS&nbsp;&nbsp;&nbsp;&nbsp;{u"\u2753"}</p>'
        options = ("Select Option...", "Enable", "Disable")
        tooltip_header = f'<h3 {header}>Select whether to enable CAS - Contrast Adaptive Sharpening</h3>'
        tooltip_body = f'<p {bodyTop}>Contrast Adaptive Sharpening</p><p {bodyBot}>Enabled - Turns on CAS<br>Disabled - Turns off CAS</p>'
        rule = False
        super().__init__(title, options, tooltip_header, tooltip_body, rule)


class CAS_Sharpness(BaseSetting):
    # Class representing the CAS_Sharpness (Contrast Adaptive Sharpening) setting.

    def __init__(self):
        """
        Initializes the CAS_Sharpness setting.

        Returns:

            str: Title of the setting (CAS_Sharpness) encoded in HTML
            tuple: Set of immutable options for the current setting (CAS_Sharpness)
            str: Tooltip header of the setting (CAS_Sharpness) encoded in HTML
            str: Tooltip body of the setting (CAS_Sharpness) encoded in HTML

        Examples:

        Instantiate the CAS_Sharpness setting:
            >>> cas_sharpness_setting = CAS_Sharpness()

        Retrieve the settings title:
            >>> cas_sharpness_setting.get_title()

        Retrieve the settings options:
            >>> cas_sharpness_setting.get_options()

        Retrieve the settings tooltip header:
            >>> cas_sharpness_setting.get_tooltip_header()

        Retrieve the settings tooltip body:
            >>> cas_sharpness_setting.get_tooltip_body()
        """
        title = f'<p>&nbsp;&nbsp;&nbsp;&nbsp;-CAS Level&nbsp;&nbsp;&nbsp;&nbsp;{u"\u2753"}</p>'
        options = ("Select Option...", "1.00", "0.75", "0.50", "0.25", "0.00", "Off")
        tooltip_header = f'<h3 {header}>Select the level of Adaptive Sharpening</h3>'
        tooltip_body = f'<p {bodyTop}>Contrast Adaptive Sharpening</p><p {bodyBot}>1.00 - Sharpest<br>0.75 - Sharp<br>0.50 - Medium<br>0.25 - Soft<br>0.00 - Softest</p>'
        rule = True
        super().__init__(title, options, tooltip_header, tooltip_body, rule)
