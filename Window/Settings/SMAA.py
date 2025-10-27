"""
File:
    SMAA.py
Author:
    Fluffy Flower (Martin Wylde)
Date:
    23/01/2025
Version:
    0.1.1
Description:
    Contains classes representing various settings related to SMAA (Subpixel
    Morphological Anti-Aliasing), along with a base class for all graphics
    settings.

    Each setting class includes attributes for title, options, tooltip header,
    and tooltip body, along with methods for retrieving these attributes.

    Additionally, global style variables are defined for consistent styling of
    HTML elements within the settings.

    These settings specifically pertain to the VKBasalt post-processing tool's
    SMAA (Subpixel Morphological Anti-Aliasing) settings.
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


class SMAA_Enable(BaseSetting):
    # Class representing the SMAA (Subpixel Morphological Anti-Aliasing)
    # setting.

    def __init__(self):
        """
        Initializes the SMAA setting.

        Returns:

            str: Title of the setting (SMAA) encoded in HTML
            tuple: Set of immutable options for the current setting (SMAA)
            str: Tooltip header of the setting (SMAA) encoded in HTML
            str: Tooltip body of the setting (SMAA) encoded in HTML

        Examples:

        Instantiate the SMAA setting:
            >>> smaa_setting = SMAA()

        Retrieve the settings title:
            >>> smaa_setting.get_title()

        Retrieve the settings options:
            >>> smaa_setting.get_options()

        Retrieve the settings tooltip header:
            >>> smaa_setting.get_tooltip_header()

        Retrieve the settings tooltip body:
            >>> smaa_setting.get_tooltip_body()
        """
        title = f'<p>Enable SMAA&nbsp;&nbsp;&nbsp;&nbsp;{u"\u2753"}</p>'
        options = ("Select Option...", "Enabled", "Disabled")
        tooltip_header = f'<h3 {header}>Select whether to enable SMAA:</h3>'
        tooltip_body = f'<p {body_top}>Subpixel Morphological Anti-Aliasing.<br>Use when image quality is paramount and the hardware can handle the additional processing overhead.</p><p {body_bot}>Enabled - Turns on SMAA.<br>Disabled - Turns off SMAA.</p>'
        rule = False
        super().__init__(title, options, tooltip_header, tooltip_body, rule)


class SMAA_Edge_Detection(BaseSetting):
    # Class representing the SMAA Edge Detection setting.

    def __init__(self):
        """
        Initializes the SMAA_Edge_Detection setting.

        Returns:

            str: Title of the setting (SMAA_Edge_Detection) encoded in HTML
            tuple: Set of immutable options for the current setting (SMAA_Edge_Detection)
            str: Tooltip header of the setting (SMAA_Edge_Detection) encoded in HTML
            str: Tooltip body of the setting (SMAA_Edge_Detection) encoded in HTML

        Examples:

        Instantiate the SMAA_Edge_Detection setting:
            >>> smaa_edge_setting = SMAA_Edge_Detection()

        Retrieve the settings title:
            >>> smaa_edge_setting.get_title()

        Retrieve the settings options:
            >>> smaa_edge_setting.get_options()

        Retrieve the settings tooltip header:
            >>> smaa_edge_setting.get_tooltip_header()

        Retrieve the settings tooltip body:
            >>> smaa_edge_setting.get_tooltip_body()
        """
        title = f'<p>&nbsp;&nbsp;&nbsp;&nbsp;-SMAA Edge Detection&nbsp;&nbsp;&nbsp;&nbsp;{u"\u2753"}</p>'
        options = ("Select Option...", "Luma", "Color")
        tooltip_header = f'<h3 {header}>Changes the edge detection shader.</h3>'
        tooltip_body = f'<p {body_bot}>Luma - Default<br>Color - Catches more edges (performance heavy)</p>'
        rule = False
        super().__init__(title, options, tooltip_header, tooltip_body, rule)


class SMAA_Threshold(BaseSetting):
    # Class representing the SMAA Threshold setting.

    def __init__(self):
        """
        Initializes the SMAA_Threshold setting.

        Returns:

            str: Title of the setting (SMAA_Threshold) encoded in HTML
            tuple: Set of immutable options for the current setting (SMAA_Threshold)
            str: Tooltip header of the setting (SMAA_Threshold) encoded in HTML
            str: Tooltip body of the setting (SMAA_Threshold) encoded in HTML

        Examples:

        Instantiate the SMAA_Threshold setting:
            >>> smaa_threshold_setting = SMAA_Threshold()

        Retrieve the settings title:
            >>> smaa_threshold_setting.get_title()

        Retrieve the settings options:
            >>> smaa_threshold_setting.get_options()

        Retrieve the settings tooltip header:
            >>> smaa_threshold_setting.get_tooltip_header()

        Retrieve the settings tooltip body:
            >>> smaa_threshold_setting.get_tooltip_body()
        """
        title = f'<p>&nbsp;&nbsp;&nbsp;&nbsp;-SMAA Threshold&nbsp;&nbsp;&nbsp;&nbsp;{u"\u2753"}</p>'
        options = ("Select Options...", "Highest Quality", "Quality", "Balanced", "Low Quality", "Lowest Quality")
        tooltip_header = f'<h3 {header}>Specifies the threshold or sensitivity to edges</h3>'
        tooltip_body = f'<p {body_top}>Lower values will detect more edges at the expense of performance.<br>Higher values increase performance, at the expense of image quality.</p><p {body_bot}>Highest Quality - (0.05) Overkill<br>Quality - (0.10)<br>Balanced - (0.25)<br>Low Quality - (0.40)<br>Lowest Quality - (0.50)</p>'
        rule = False
        super().__init__(title, options, tooltip_header, tooltip_body, rule)


class SMAA_Search_Steps(BaseSetting):
    # Class representing the SMAA Max Search Steps setting.

    def __init__(self):
        """
        Initializes the class SMAA_Search_Steps setting.

        Returns:

            str: Title of the setting (SMAA_Search_Steps) encoded in HTML
            tuple: Set of immutable options for the current setting (SMAA_Search_Steps)
            str: Tooltip header of the setting (SMAA_Search_Steps) encoded in HTML
            str: Tooltip body of the setting (SMAA_Search_Steps) encoded in HTML

        Examples:

        Instantiate the SMAA_Search_Steps setting:
            >>> smaa_search_steps_setting = SMAA_Search_Steps()

        Retrieve the settings title:
            >>> smaa_search_steps_setting.get_title()

        Retrieve the settings options:
            >>> smaa_search_steps_setting.get_options()

        Retrieve the settings tooltip header:
            >>> smaa_search_steps_setting.get_tooltip_header()

        Retrieve the settings tooltip body:
            >>> smaa_search_steps_setting.get_tooltip_body()
        """
        title = f'<p>&nbsp;&nbsp;&nbsp;&nbsp;-SMAA Max Search Steps&nbsp;&nbsp;&nbsp;&nbsp;{u"\u2753"}</p>'
        options = ("Select Options...", "x32", "x16", "x8", "x4", "x2")
        tooltip_header = f'<h3 {header}>Specifies the maximum steps performed in the horizontal/vertical pattern searches</h3>'
        tooltip_body = f'<p {body_top}>Higher values give higher image quality, at the expense of performance.<br>Lower values give higher performance, at the expense of image quality</p><p {body_bot}>x32 - Highest Quality<br>x16 - High Quality<br>x8 - Balanced<br>x4 - Low Quality<br>x2 - Lowest Quality</p>'
        rule = False
        super().__init__(title, options, tooltip_header, tooltip_body, rule)


class SMAA_Search_Steps_Diagonal(BaseSetting):
    # Class representing the SMAA Max Diagonal Search Steps setting.

    def __init__(self):
        """
        Initializes the SMAA_Search_Steps_Diagonal setting.

        Returns:

            str: Title of the setting (SMAA_Search_Steps_Diagonal) encoded in HTML
            tuple: Set of immutable options for the current setting (SMAA_Search_Steps_Diagonal)
            str: Tooltip header of the setting (SMAA_Search_Steps_Diagonal) encoded in HTML
            str: Tooltip body of the setting (SMAA_Search_Steps_Diagonal) encoded in HTML

        Examples:

        Instantiate the SMAA_Search_Steps_Diagonal setting:
            >>> smaa_search_steps_diag_setting = SMAA_Search_Steps_Diagonal()

        Retrieve the settings title:
            >>> smaa_search_steps_diag_setting.get_title()

        Retrieve the settings options:
            >>> smaa_search_steps_diag_setting.get_options()

        Retrieve the settings tooltip header:
            >>> smaa_search_steps_diag_setting.get_tooltip_header()

        Retrieve the settings tooltip body:
            >>> smaa_search_steps_diag_setting.get_tooltip_body()
        """
        title = f'<p>&nbsp;&nbsp;&nbsp;&nbsp;-SMAA Max Diagonal Search Steps&nbsp;&nbsp;&nbsp;&nbsp;{u"\u2753"}</p>'
        options = ("Select Options...", "x16", "x8", "x4", "x2", "x0")
        tooltip_header = f'<h3 {header}>Specifies the maximum steps performed in the diagonal pattern searches</h3>'
        tooltip_body = f'<p {body_top}>Higher values give higher image quality, at the expense of performance.<br>Lower values give higher performance, at the expense of image quality</p><p {body_bot}>x16 - Highest Quality<br>x8 - High Quality<br>x4 - Balanced<br>x2 - Low Quality<br>x0 - Lowest Quality</p>'
        rule = False
        super().__init__(title, options, tooltip_header, tooltip_body, rule)


class SMAA_Corner_Rounding(BaseSetting):
    # Class representing the SMAA Corner Rounding setting.

    def __init__(self):
        """
        Initializes the SMAA_Corner_Rounding setting.

        Returns:

            str: Title of the setting (SMAA_Corner_Rounding) encoded in HTML
            tuple: Set of immutable options for the current setting (SMAA_Corner_Rounding)
            str: Tooltip header of the setting (SMAA_Corner_Rounding) encoded in HTML
            str: Tooltip body of the setting (SMAA_Corner_Rounding) encoded in HTML

        Examples:

        Instantiate the SMAA_Corner_Rounding setting:
            >>> smaa_corner_setting = SMAA_Corner_Rounding()

        Retrieve the settings title:
            >>> smaa_corner_setting.get_title()

        Retrieve the settings options:
            >>> smaa_corner_setting.get_options()

        Retrieve the settings tooltip header:
            >>> smaa_corner_setting.get_tooltip_header()

        Retrieve the settings tooltip body:
            >>> smaa_corner_setting.get_tooltip_body()
        """
        title = f'<p>&nbsp;&nbsp;&nbsp;&nbsp;-SMAA Corner Rounding&nbsp;&nbsp;&nbsp;&nbsp;{u"\u2753"}</p>'
        options = ("Select Options...", "100", "75", "50", "25", "0")
        tooltip_header = f'<h3 {header}>Specifies how much sharp corners will be rounded</h3>'
        tooltip_body = f'<p {body_top}>Higher values round corners more.<br>Lower values round corners less (Adjust to your preference)</p><p {body_bot}>100 - Highest Quality<br>75 - High Quality<br>50 - Balanced<br>25 - Low Quality<br>0 - Lowest Quality</p>'
        rule = False
        super().__init__(title, options, tooltip_header, tooltip_body, rule)
