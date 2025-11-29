"""
File       : FXAA.py
Author     : Fluffy Flower (Martin Wylde)
Contact    :
    Email   - martincw1989@gmail.com
    Telegram- @FluffyFlower
    Discord - fluffy_flower
Date       : 23/01/2025
Version    : 1.0.0
Description: Contains classes representing various settings related to FXAA (Fast Approximate Anti-Aliasing), along with a base class for all graphics settings.
Each setting class includes attributes for title, options, tooltip header, and tooltip body, along with methods for retrieving these attributes.
Additionally, global style variables are defined for consistent styling of HTML elements within the settings.
These settings specifically pertain to the VKBasalt post-processing tool's FXAA settings.
"""

# Global style variables
header = 'style="font-weight: bold; text-decoration: underline;"'
body_top = 'style="font-weight: bold;"'
body_bot = 'style="font-style: italic;"'


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


class FXAA_Enable(BaseSetting):
    # Class representing the FXAA (Fast Approximate Anti-Aliasing) setting.

    def __init__(self):
        """
        Initializes the FXAA setting.

        Returns:

            str: Title of the setting (FXAA) encoded in HTML
            tuple: Set of immutable options for the current setting (FXAA)
            str: Tooltip header of the setting (FXAA) encoded in HTML
            str: Tooltip body of the setting (FXAA) encoded in HTML

        Examples:

        Instantiate the FXAA setting:
            >>> fxaa_setting = FXAA()

        Retrieve the settings title:
            >>> fxaa_setting.get_title()

        Retrieve the settings options:
            >>> fxaa_setting.get_options()

        Retrieve the settings tooltip header:
            >>> fxaa_setting.get_tooltip_header()

        Retrieve the settings tooltip body:
            >>> fxaa_setting.get_tooltip_body()
        """
        title = f'<p>Enable FXAA&nbsp;&nbsp;&nbsp;&nbsp;{u"\u2753"}</p>'
        options = ("Select Option...", "Enabled", "Disabled")
        tooltip_header = f'<h3 {header}>Select whether to enable FXAA:</h3>'
        tooltip_body = f'<p {body_top}>FXAA / Fast Approximate Anti-Aliasing.<br>Use if performance is a priority, or when targeting lower-end hardware.</p><p {body_bot}>Enabled - Turns on FXAA.<br>Disabled - Turns off FXAA.</p>'
        rule = False
        super().__init__(title, options, tooltip_header, tooltip_body, rule)


class FXAA_Quality_Subpixel(BaseSetting):
    # Class representing the FXAA Subpixel Quality setting.

    def __init__(self):
        """
        Initializes the FXAA Subpixel Quality setting.

        Returns:
            str: Title of the setting (FXAA Subpixel Quality) encoded in HTML
            tuple: Set of immutable options for the current setting (FXAA Subpixel Quality)
            str: Tooltip header of the setting (FXAA Subpixel Quality) encoded in HTML
            str: Tooltip body of the setting (FXAA Subpixel Quality) encoded in HTML

        Examples:

        Instantiate the FXAA_Quality_Subpixel setting:
            >>> fxaa_subpixel_setting = FXAA_Quality_Subpixel()

        Retrieve the settings title:
            >>> fxaa_subpixel_setting.get_title()

        Retrieve the settings options:
            >>> fxaa_subpixel_setting.get_options()

        Retrieve the settings tooltip header:
            >>> fxaa_subpixel_setting.get_tooltip_header()

        Retrieve the settings tooltip body:
            >>> fxaa_subpixel_setting.get_tooltip_body()
        """
        title = f'<p>&nbsp;&nbsp;&nbsp;&nbsp;-FXAA Subpixel Quality&nbsp;&nbsp;&nbsp;&nbsp;{u"\u2753"}</p>'
        options = ("Select Option...", "1.00", "0.75", "0.50", "0.25", "0.00")
        tooltip_header = f'<h3 {header}>Controls sharpness.</h3>'
        tooltip_body = f'<p {body_top}>Higher values make edges smoother.<br>Lower values make edges sharper.</p><p {body_bot}>1.00 - Smoothest<br>0.75 - Smooth (Default)<br>0.50 - Sharp<br>0.25 - Sharper<br>0.00 - Off / Sharpest</p>'
        rule = False
        super().__init__(title, options, tooltip_header, tooltip_body, rule)


class FXAA_Quality_Edge_Threshold(BaseSetting):
    # Class representing the FXAA Edge Quality setting.

    def __init__(self):
        """
        Initializes the FXAA Edge Quality setting.

        Returns:
            str: Title of the setting (FXAA Edge Quality setting) encoded in HTML
            tuple: Set of immutable options for the current setting (FXAA Edge Quality setting)
            str: Tooltip header of the setting (FXAA Edge Quality setting) encoded in HTML
            str: Tooltip body of the setting (FXAA Edge Quality setting) encoded in HTML

        Examples:

        Instantiate the FXAA_Quality_Edge_Threshold setting:
            >>> fxaa_edge_quality_setting = FXAA_Quality_Edge_Threshold()

        Retrieve the settings title:
            >>> fxaa_edge_quality_setting.get_title()

        Retrieve the settings options:
            >>> fxaa_edge_quality_setting.get_options()

        Retrieve the settings tooltip header:
            >>> fxaa_edge_quality_setting.get_tooltip_header()

        Retrieve the settings tooltip body:
            >>> fxaa_edge_quality_setting.get_tooltip_body()
        """
        title = f'<p>&nbsp;&nbsp;&nbsp;&nbsp;-FXAA Edge Quality&nbsp;&nbsp;&nbsp;&nbsp;{u"\u2753"}</p>'
        options = ("Select Option...", "Highest Quality", "High Quality", "Default", "Low Quality", "Lowest Quality")
        tooltip_header = f'<h3 {header}>Minimum local contrast required to apply algorithm.</h3>'
        tooltip_body = f'<p {body_top}>Lower values result in more edges being smoothed.<br>Higher values preserve more detail but may leave some aliasing.</p><p {body_bot}>Highest Quality (0.063) - Overkill / Slowest<br>Default (0.166) - Balanced<br>Lowest Quality (0.333) - Fastest</p>'
        rule = False
        super().__init__(title, options, tooltip_header, tooltip_body, rule)


class FXAA_Edge_Threshold_Bias(BaseSetting):
    # Class representing the FXAA Edge Threshold Bias setting.

    def __init__(self):
        """
        Initializes the FXAA Edge Threshold Bias setting.

        Returns:
            str: Title of the setting (FXAA Edge Threshold Bias) encoded in HTML
            tuple: Set of immutable options for the current setting (FXAA Edge Threshold Bias)
            str: Tooltip header of the setting (FXAA Edge Threshold Bias) encoded in HTML
            str: Tooltip body of the setting (FXAA Edge Threshold Bias) encoded in HTML

        Examples:

        Instantiate the FXAA_Edge_Threshold_Bias setting:
            >>> fxaa_edge_bias_setting = FXAA_Edge_Threshold_Bias()

        Retrieve the settings title:
            >>> fxaa_edge_bias_setting.get_title()

        Retrieve the settings options:
            >>> fxaa_edge_bias_setting.get_options()

        Retrieve the settings tooltip header:
            >>> fxaa_edge_bias_setting.get_tooltip_header()

        Retrieve the settings tooltip body:
            >>> fxaa_edge_bias_setting.get_tooltip_body()
        """
        title = f'<p>&nbsp;&nbsp;&nbsp;&nbsp;-FXAA Edge Threshold Bias&nbsp;&nbsp;&nbsp;&nbsp;{u"\u2753"}</p>'
        options = ("Select Option...", "Upper Limit", "High Quality", "Visible Limit", "Zero")
        tooltip_header = f'<h3 {header}>Trims the algorithm from processing darks.</h3>'
        tooltip_body = f'<p {body_top}>Adjusts processing of dark areas.<br>Lower values may cause loss of detail in shadows.<br>Higher values preserve shadow detail but may increase aliasing.</p><p {body_bot}>Upper limit - (0.0833) Default<br>High quality - (0.0625) Faster<br>Visible limit - (0.0312) Slower<br>Zero - For non green content'
        rule = True
        super().__init__(title, options, tooltip_header, tooltip_body, rule)
