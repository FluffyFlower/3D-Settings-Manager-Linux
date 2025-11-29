"""
File       : HDR.py
Author     : Fluffy Flower (Martin Wylde)
Contact    :
    Email   - martincw1989@gmail.com
    Telegram- @FluffyFlower
    Discord - fluffy_flower
Date       : 23/01/2025
Version    : 1.0.0
Description: Contains classes representing various settings related to HDR (High Dynamic Range), along with a base class for all graphics settings.
Each setting class includes attributes for title, options, tooltip header, and tooltip body, along with methods for retrieving these attributes.
Additionally, global style variables are defined for consistent styling of HTML elements within the settings.
These settings specifically pertain to the DXVK's HDR (High Dynamic Range) settings.
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


class HighDynamicRange(BaseSetting):
    # Class representing the HDR (High Dynamic Range) setting.

    def __init__(self):
        """
        Initializes the HDR setting.

        Returns:

            str: Title of the setting (HDR) encoded in HTML
            tuple: Set of immutable options for the current setting (HDR)
            str: Tooltip header of the setting (HDR) encoded in HTML
            str: Tooltip body of the setting (HDR) encoded in HTML

        Examples:

        Instantiate the HDR setting:
            >>> hdr_setting = HDR()

        Retrieve the settings title:
            >>> hdr_setting.get_title()

        Retrieve the settings options:
            >>> hdr_setting.get_options()

        Retrieve the settings tooltip header:
            >>> hdr_setting.get_tooltip_header()

        Retrieve the settings tooltip body:
            >>> hdr_setting.get_tooltip_body()
        """
        title = f'<p>HDR - High Dynamic Range&nbsp;&nbsp;&nbsp;&nbsp;{u"\u2753"}</p>'
        options = ["Select Option...", "Enabled", "Disabled"]
        tooltip_header = f'<h3 {header}>Select whether to enable or disable HDR:</h3>'
        tooltip_body = f'<p {bodyTop}>High Dynamic Range (HDR) enhances visual quality by expanding the range of brightness and contrast levels, resulting in more vibrant and realistic images.</p><p {bodyBot}>This shows to the game that the global Windows "HDR Mode" is enabled. Many (broken) games will need this to be set to consider exposing HDR output as determine it based on the DXGIOutputs current ColorSpace instead of using CheckColorSpaceSupport.<br>This will not enable HDR for Games that dont support it!!</p>'
        rule = True
        super().__init__(title, options, tooltip_header, tooltip_body, rule)
