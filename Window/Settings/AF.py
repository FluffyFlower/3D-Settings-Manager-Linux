"""
File       :AF.py
Author     :Fluffy Flower (Martin Wylde)
Contact    :
    Email   - martincw1989@gmail.com
    Telegram- @FluffyFlower
    Discord - fluffy_flower
Date       :23/01/2025
Version    :1.0.0
Description: Contains classes representing various settings related to AF (Anisotropic Filtering), and LOD Bias, along with a base class for all graphics settings.
Each setting class includes attributes for title, options, tooltip header, and tooltip body, along with methods for retrieving these attributes.
Additionally, global style variables are defined for consistent styling of HTML elements within the settings.
These settings specifically pertain to the DXVK tool's AF settings.
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


class Anisotropic_Filtering_Enable(BaseSetting):
    # Class representing the Anisotropic_Filtering setting.

    def __init__(self):
        """
        Initializes the Enable Anisotropic_Filtering setting.

        Returns:

            str: Title of the setting (Anisotropic_Filtering_Enable) encoded in HTML
            tuple: Set of immutable options for the current setting (Anisotropic_Filtering_Enable)
            str: Tooltip header of the setting (Anisotropic_Filtering_Enable) encoded in HTML
            str: Tooltip body of the setting (Anisotropic_Filtering_Enable) encoded in HTML

        Examples:

        Instantiate the Enable Anisotropic Filtering setting:
            >>> af__enable_setting = Anisotropic_Filtering_Enable()

        Retrieve the settings title:
            >>> af__enable_setting.get_title()

        Retrieve the settings options:
            >>> af__enable_setting.get_options()

        Retrieve the settings tooltip header:
            >>> af__enable_setting.get_tooltip_header()

        Retrieve the settings tooltip body:
            >>> af__enable_setting.get_tooltip_body()
        """
        title = f'<p>Enable Anisotropic Filtering&nbsp;&nbsp;&nbsp;&nbsp;{u"\u2753"}</p>'
        options = ("Select Option...", "Enable", "Enable (D3D9)", "Disable")
        tooltip_header = f'<h3 {header}>Enabling Anisotropic Filtering:</h3>'
        tooltip_body = f'<p {body_top}>Anisotropic filtering is a texture filtering technique that enhances the clarity of distant textures in 3D rendering by improving the sharpness of textures viewed at oblique angles</p><p {body_bot}>Enable - Turn on Anisotropic Filtering<br>Disable - Turn off Anisotropic Filtering</p>'
        rule = False
        super().__init__(title, options, tooltip_header, tooltip_body, rule)


class Anisotropic_Filtering_Level(BaseSetting):
    # Class representing the Anisotropic_Filtering_Level setting.

    def __init__(self):
        """
        Initializes the Anisotropic_Filtering_Level setting.

        Returns:

            str: Title of the setting (Anisotropic_Filtering_Level) encoded in HTML
            tuple: Set of immutable options for the current setting (Anisotropic_Filtering_Level)
            str: Tooltip header of the setting (Anisotropic_Filtering_Level) encoded in HTML
            str: Tooltip body of the setting (Anisotropic_Filtering_Level) encoded in HTML

        Examples:

        Instantiate the Anisotropic_Filtering_Level setting:
            >>> af_level_setting = Anisotropic_Filtering_Level()

        Retrieve the settings title:
            >>> af_level_setting.get_title()

        Retrieve the settings options:
            >>> af_level_setting.get_options()

        Retrieve the settings tooltip header:
            >>> af_level_setting.get_tooltip_header()

        Retrieve the settings tooltip body:
            >>> af_level_setting.get_tooltip_body()
        """
        title = f'<p>&nbsp;&nbsp;&nbsp;&nbsp;-Anisotropic Filtering Level&nbsp;&nbsp;&nbsp;&nbsp;{u"\u2753"}</p>'
        options = ("Select Option...", "x16", "x8", "x4", "x2", "x1")
        tooltip_header = f'<h3 {header}>Select the level of Anisotropic Filtering:</h3>'
        tooltip_body = f'<p {body_top}>Higher values provide sharper textures but require more resources.<br>Lower values provide less clear textures but requires less resources.</p><p {body_bot}>x16 Samples - High Quality<br>x8 Samples - Quality<br>x4 Samples - Balanced<br>x2 Samples - Performance<br>x1 Sample - High Performance<br>x0 Samples - Off</p>'
        rule = False
        super().__init__(title, options, tooltip_header, tooltip_body, rule)


class Anisotropic_Filtering_Level_D3D9(BaseSetting):
    # Class representing the Anisotropic_Filtering_Level_D3D9 setting.

    def __init__(self):
        """
        Initializes the Anisotropic_Filtering_Level_D3D9 setting.

        Returns:

            str: Title of the setting (Anisotropic_Filtering_Level_D3D9) encoded in HTML
            tuple: Set of immutable options for the current setting (Anisotropic_Filtering_Level_D3D9)
            str: Tooltip header of the setting (Anisotropic_Filtering_Level_D3D9) encoded in HTML
            str: Tooltip body of the setting (Anisotropic_Filtering_Level_D3D9) encoded in HTML

        Examples:

        Instantiate the Anisotropic_Filtering_Level_D3D9 setting:
            >>> af_level_d3d9_setting = Anisotropic_Filtering_Level_D3D9()

        Retrieve the settings title:
            >>> af_level_d3d9_setting.get_title()

        Retrieve the settings options:
            >>> af_level_d3d9_setting.get_options()

        Retrieve the settings tooltip header:
            >>> af_level_d3d9_setting.get_tooltip_header()

        Retrieve the settings tooltip body:
            >>> af_level_d3d9_setting.get_tooltip_body()
        """
        title = f'<p>&nbsp;&nbsp;&nbsp;&nbsp;-Anisotropic Filtering Level (D3D9 Applications)&nbsp;&nbsp;&nbsp;&nbsp;{u"\u2753"}</p>'
        options = ("Select Option...", "x16", "x8", "x4", "x2", "x1")
        tooltip_header = f'<h3 {header}>(D3D9 applications only) Select the level of Anisotropic Filtering:</h3>'
        tooltip_body = f'<p {body_top}>Higher values provide sharper textures but require more resources.<br>Lower values provide less clear textures but requires less resources.</p><p {body_bot}>x16 Samples - High Quality<br>x8 Samples - Quality<br>x4 Samples - Balanced<br>x2 Samples - Performance<br>x1 Sample - High Performance<br>x0 Samples - Off</p>'
        rule = True
        super().__init__(title, options, tooltip_header, tooltip_body, rule)


class LOD_Enable(BaseSetting):
    # Class representing the LOD_Bias setting.

    def __init__(self):
        """
        Initializes the LOD_Bias setting.

        Returns:

            str: Title of the setting (LOD_Bias) encoded in HTML
            tuple: Set of immutable options for the current setting (LOD_Bias)
            str: Tooltip header of the setting (LOD_Bias) encoded in HTML
            str: Tooltip body of the setting (LOD_Bias) encoded in HTML

        Examples:

        Instantiate the LOD Bias setting:
            >>> lod_bias_setting = LOD_Bias()

        Retrieve the settings title:
            >>> lod_bias_setting.get_title()

        Retrieve the settings options:
            >>> lod_bias_setting.get_options()

        Retrieve the settings tooltip header:
            >>> lod_bias_setting.get_tooltip_header()

        Retrieve the settings tooltip body:
            >>> lod_bias_setting.get_tooltip_body()
        """
        title = f'<p>LOD Settings&nbsp;&nbsp;&nbsp;&nbsp;{u"\u2753"}</p>'
        options = ("Select Option...", "Enable", "Enable (D3D9)", "Disable")
        tooltip_header = f'<h3 {header}>Select the level of LOD Bias:</h3>'
        tooltip_body = f'<p {body_top}>LOD bias, or Level of Detail bias, is a rendering technique used to control the level of detail of textures based on their distance from the viewer. Lower or negative values of LOD bias result in higher texture detail for distant objects, while higher or positive values reduce texture detail to improve performance.</p><p {body_bot}>-2 - Highest Quality<br>-1 - High Quality<br>0 - Balanced<br>0.5 - Low Quality<br>1 - Lowest Quality</p>'
        rule = False
        super().__init__(title, options, tooltip_header, tooltip_body, rule)


class LOD_Bias(BaseSetting):
    # Class representing the LOD_Bias setting.

    def __init__(self):
        """
        Initializes the LOD_Bias setting.

        Returns:

            str: Title of the setting (LOD_Bias) encoded in HTML
            tuple: Set of immutable options for the current setting (LOD_Bias)
            str: Tooltip header of the setting (LOD_Bias) encoded in HTML
            str: Tooltip body of the setting (LOD_Bias) encoded in HTML

        Examples:

        Instantiate the LOD Bias setting:
            >>> lod_bias_setting = LOD_Bias()

        Retrieve the settings title:
            >>> lod_bias_setting.get_title()

        Retrieve the settings options:
            >>> lod_bias_setting.get_options()

        Retrieve the settings tooltip header:
            >>> lod_bias_setting.get_tooltip_header()

        Retrieve the settings tooltip body:
            >>> lod_bias_setting.get_tooltip_body()
        """
        title = f'<p>&nbsp;&nbsp;&nbsp;&nbsp;-LOD Bias&nbsp;&nbsp;&nbsp;&nbsp;{u"\u2753"}</p>'
        options = ("Select Option...", "-2.0", "-1.0", "0.0", "0.5", "1.0")
        tooltip_header = f'<h3 {header}>Select the level of LOD Bias:</h3>'
        tooltip_body = f'<p {body_top}>LOD bias, or Level of Detail bias, is a rendering technique used to control the level of detail of textures based on their distance from the viewer. Lower or negative values of LOD bias result in higher texture detail for distant objects, while higher or positive values reduce texture detail to improve performance.</p><p {body_bot}>-2.0 - Highest Quality<br>-1.0 - High Quality<br>0.0 - Balanced<br>0.5 - Low Quality<br>1.0 - Lowest Quality</p>'
        rule = False
        super().__init__(title, options, tooltip_header, tooltip_body, rule)


class LOD_Bias_D3D9(BaseSetting):
    # Class representing the LOD_Bias_D3D9 setting.

    def __init__(self):
        """
        Initializes the LOD_Bias_D3D9 setting.

        Returns:

            str: Title of the setting (LOD_Bias_D3D9) encoded in HTML
            tuple: Set of immutable options for the current setting (LOD_Bias_D3D9)
            str: Tooltip header of the setting (LOD_Bias_D3D9) encoded in HTML
            str: Tooltip body of the setting (LOD_Bias_D3D9) encoded in HTML

        Examples:

        Instantiate the LOD Bias setting:
            >>> lod_bias_d3d9_setting = LOD_Bias_D3D9()

        Retrieve the settings title:
            >>> lod_bias_d3d9_setting.get_title()

        Retrieve the settings options:
            >>> lod_bias_d3d9_setting.get_options()

        Retrieve the settings tooltip header:
            >>> lod_bias_d3d9_setting.get_tooltip_header()

        Retrieve the settings tooltip body:
            >>> lod_bias_d3d9_setting.get_tooltip_body()
        """
        title = f'<p>&nbsp;&nbsp;&nbsp;&nbsp;-LOD Bias (D3D9 Applications)&nbsp;&nbsp;&nbsp;&nbsp;{u"\u2753"}</p>'
        options = ("Select Option...", "-2", "-1", "0", "0.5", "1")
        tooltip_header = f'<h3 {header}>(D3D9 applications only) Select the level of LOD Bias:</h3>'
        tooltip_body = f'<p {body_top}>LOD bias, or Level of Detail bias, is a rendering technique used to control the level of detail of textures based on their distance from the viewer. Lower or negative values of LOD bias result in higher texture detail for distant objects, while higher or positive values reduce texture detail to improve performance.</p><p {body_bot}>-2 - Highest Quality<br>-1 - High Quality<br>0 - Balanced<br>0.5 - Low Quality<br>1 - Lowest Quality</p>'
        rule = False
        super().__init__(title, options, tooltip_header, tooltip_body, rule)


class Clamp_Negative_LOD(BaseSetting):
    # Class representing the Clamp_Negative_LOD setting.

    def __init__(self):
        """
        Initializes the Clamp_Negative_LOD setting.

        Returns:

            str: Title of the setting (Clamp_Negative_LOD) encoded in HTML
            tuple: Set of immutable options for the current setting (Clamp_Negative_LOD)
            str: Tooltip header of the setting (Clamp_Negative_LOD) encoded in HTML
            str: Tooltip body of the setting (Clamp_Negative_LOD) encoded in HTML

        Examples:

        Instantiate the Clamp Negative LOD setting:
            >>> clamp_lod_setting = Clamp_Negative_LOD()

        Retrieve the settings title:
            >>> clamp_lod_setting.get_title()

        Retrieve the settings options:
            >>> clamp_lod_setting.get_options()

        Retrieve the settings tooltip header:
            >>> clamp_lod_setting.get_tooltip_header()

        Retrieve the settings tooltip body:
            >>> clamp_lod_setting.get_tooltip_body()
        """
        title = f'<p>&nbsp;&nbsp;&nbsp;&nbsp;-Clamp Negative LOD Bias&nbsp;&nbsp;&nbsp;&nbsp;{u"\u2753"}</p>'
        options = ("Select Option...", "Enabled", "Disabled")
        tooltip_header = f'<h3 {header}>Select whether to enable negative LOD bias clamping</h3>'
        tooltip_body = f'<p {body_top}>Clamps the negative values of LOD bias to 0, helps in games that use a high negative LOD bias by default.</p><p {body_bot}></p>'
        rule = False
        super().__init__(title, options, tooltip_header, tooltip_body, rule)


class Clamp_Negative_LOD_D3D9(BaseSetting):
    # Class representing the Clamp_Negative_LOD_D3D9 setting.

    def __init__(self):
        """
        Initializes the Clamp_Negative_LOD_D3D9 setting.

        Returns:

            str: Title of the setting (Clamp_Negative_LOD_D3D9) encoded in HTML
            tuple: Set of immutable options for the current setting (Clamp_Negative_LOD_D3D9)
            str: Tooltip header of the setting (Clamp_Negative_LOD_D3D9) encoded in HTML
            str: Tooltip body of the setting (Clamp_Negative_LOD_D3D9) encoded in HTML

        Examples:

        Instantiate the Clamp Negative LOD setting:
            >>> clamp_lod_d3d9_setting = Clamp_Negative_LOD_D3D9()

        Retrieve the settings title:
            >>> clamp_lod_d3d9_setting.get_title()

        Retrieve the settings options:
            >>> clamp_lod_d3d9_setting.get_options()

        Retrieve the settings tooltip header:
            >>> clamp_lod_d3d9_setting.get_tooltip_header()

        Retrieve the settings tooltip body:
            >>> clamp_lod_d3d9_setting.get_tooltip_body()
        """
        title = f'<p>&nbsp;&nbsp;&nbsp;&nbsp;-Clamp Negative LOD Bias (D3D9 Applications)&nbsp;&nbsp;&nbsp;&nbsp;{u"\u2753"}</p>'
        options = ("Select Option...", "Enabled", "Disabled")
        tooltip_header = f'<h3 {header}>(D3D9 applications only) Select whether to enable negative LOD bias clamping</h3>'
        tooltip_body = f'<p {body_top}>Clamps the negative values of LOD bias to 0, helps in games that use a high negative LOD bias by default.</p><p {body_bot}></p>'
        rule = False
        super().__init__(title, options, tooltip_header, tooltip_body, rule)
