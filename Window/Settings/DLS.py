"""
File       : DLS.py
Author     : Fluffy Flower (Martin Wylde)
Contact    :
    Email   - martincw1989@gmail.com
    Telegram- @FluffyFlower
    Discord - fluffy_flower
Date       : 23/01/2025
Version    : 1.0.0
Description: Contains classes representing various settings related to DLS (Denoised Luma Sharpening), along with a base class for all graphics settings.
Each setting class includes attributes for title, options, tooltip header, and tooltip body, along with methods for retrieving these attributes.
Additionally, global style variables are defined for consistent styling of HTML elements within the settings.
These settings specifically pertain to the VKBasalt post-processing tool's DLS (Denoised Luma Sharpening) settings.
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


class DLS_Enable(BaseSetting):
    # Class representing the DLS Sharpness setting.

    def __init__(self):
        """
        Initializes the DLS_Sharpness setting.

        Returns:

            str: Title of the setting (DLS_Sharpness) encoded in HTML
            tuple: Set of immutable options for the current setting (DLS_Sharpness)
            str: Tooltip header of the setting (DLS_Sharpness) encoded in HTML
            str: Tooltip body of the setting (DLS_Sharpness) encoded in HTML

        Examples:

        Instantiate the DLS Sharpness setting:
            >>> dls_sharpness_setting = DLS_Sharpness()

        Retrieve the settings title:
            >>> dls_sharpness_setting.get_title()

        Retrieve the settings options:
            >>> dls_sharpness_setting.get_options()

        Retrieve the settings tooltip header:
            >>> dls_sharpness_setting.get_tooltip_header()

        Retrieve the settings tooltip body:
            >>> dls_sharpness_setting.get_tooltip_body()
        """
        title = f'<p>Enable DLS&nbsp;&nbsp;&nbsp;&nbsp;{u"\u2753"}</p>'
        options = ["Select Option...", "Enable", "Disable"]
        tooltip_header = f'<h3 {header}>Select whether to enable DLS - Denoised Luma Sharpening</h3>'
        tooltip_body = f'<p {bodyTop}>DLS / Denoised Luma Sharpening is a technique used in graphics processing to enhance image sharpness while minimizing the introduction of noise, resulting in clearer and more defined visual output.</p><p {bodyBot}>1.00 - Sharpest (More artifacts)<br>0.75 - Sharp<br>0.50 - Medium<br>0.25 - Soft<br>0.00 - Softest (Less artifacts)</p>'
        rule = False
        super().__init__(title, options, tooltip_header, tooltip_body, rule)


class DLS_Sharpness(BaseSetting):
    # Class representing the DLS Sharpness setting.

    def __init__(self):
        """
        Initializes the DLS_Sharpness setting.

        Returns:

            str: Title of the setting (DLS_Sharpness) encoded in HTML
            tuple: Set of immutable options for the current setting (DLS_Sharpness)
            str: Tooltip header of the setting (DLS_Sharpness) encoded in HTML
            str: Tooltip body of the setting (DLS_Sharpness) encoded in HTML

        Examples:

        Instantiate the DLS Sharpness setting:
            >>> dls_sharpness_setting = DLS_Sharpness()

        Retrieve the settings title:
            >>> dls_sharpness_setting.get_title()

        Retrieve the settings options:
            >>> dls_sharpness_setting.get_options()

        Retrieve the settings tooltip header:
            >>> dls_sharpness_setting.get_tooltip_header()

        Retrieve the settings tooltip body:
            >>> dls_sharpness_setting.get_tooltip_body()
        """
        title = f'<p>&nbsp;&nbsp;&nbsp;&nbsp;-DLS - Sharpness Level&nbsp;&nbsp;&nbsp;&nbsp;{u"\u2753"}</p>'
        options = ["Select Option...", "1.00", "0.75", "0.50", "0.25", "0.00"]
        tooltip_header = f'<h3 {header}>Select the level of DLS (Denoised Luma Sharpening)</h3>'
        tooltip_body = f'<p {bodyTop}>Used to set the amount of sharpening in the Denoised Luma Sharpening shader. Higher levels are more sharp.</p><p {bodyBot}>1.00 - Sharpest (More artifacts)<br>0.75 - Sharp<br>0.50 - Medium<br>0.25 - Soft<br>0.00 - Softest (Less artifacts)</p>'
        rule = False
        super().__init__(title, options, tooltip_header, tooltip_body, rule)


class DLS_Denoise(BaseSetting):
    # Class representing the DLS Denoise setting.

    def __init__(self):
        """
        Initializes the DLS_Denoise setting.

        Returns:

            str: Title of the setting (DLS_Denoise) encoded in HTML
            tuple: Set of immutable options for the current setting (DLS_Denoise)
            str: Tooltip header of the setting (DLS_Denoise) encoded in HTML
            str: Tooltip body of the setting (DLS_Denoise) encoded in HTML

        Examples:

        Instantiate the DLS Denoising Level setting:
            >>> dls_denoise_setting = DLS_Denoise()

        Retrieve the settings title:
            >>> dls_denoise_setting.get_title()

        Retrieve the settings options:
            >>> dls_denoise_setting.get_options()

        Retrieve the settings tooltip header:
            >>> dls_denoise_setting.get_tooltip_header()

        Retrieve the settings tooltip body:
            >>> dls_denoise_setting.get_tooltip_body()
        """
        title = f'<p>&nbsp;&nbsp;&nbsp;&nbsp;-DLS - Denoise Level&nbsp;&nbsp;&nbsp;&nbsp;{u"\u2753"}</p>'
        options = ["Select Option...", "1.00", "0.75", "0.50", "0.25"]
        tooltip_header = f'<h3 {header}>Select the level of DLS Denoise</h3>'
        tooltip_body = f'<p {bodyTop}>Used to set the amount of denoising in the Denoised Luma Sharpening shader. Higher levels increase the amount of film grain within the image gets sharpened.</p><p {bodyBot}>1.00 - Full<br>0.75 - Most<br>0.50 - Fair<br>0.25 - Default<br>0.00 - Off</p>'
        rule = False
        super().__init__(title, options, tooltip_header, tooltip_body, rule)
