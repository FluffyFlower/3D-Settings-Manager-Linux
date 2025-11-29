"""
File       : VSYNC.py
Author     : Fluffy Flower (Martin Wylde)
Contact    :
    Email   - martincw1989@gmail.com
    Telegram- @FluffyFlower
    Discord - fluffy_flower
Date       : 23/01/2025
Version    : 1.0.0
Description: Contains classes representing various settings related to Vsync, and frame limiting, along with a base class for all graphics settings.
Each setting class includes attributes for title, options, tooltip header, and tooltip body, along with methods for retrieving these attributes.
Additionally, global style variables are defined for consistent styling of HTML elements within the settings.
These settings specifically pertain to the DXVK tool's Vsync settings.
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


class VSync_Enable(BaseSetting):
    # Class representing the VSync setting.

    def __init__(self):
        """
        Initializes the VSYNC setting.

        Returns:

            str: Title of the setting (VSYNC) encoded in HTML
            tuple: Set of immutable options for the current setting (VSYNC)
            str: Tooltip header of the setting (VSYNC) encoded in HTML
            str: Tooltip body of the setting (VSYNC) encoded in HTML

        Examples:

        Instantiate the VSYNC setting:
            >>> vsync_setting = VSYNC()

        Retrieve the settings title:
            >>> vsync_setting.get_title()

        Retrieve the settings options:
            >>> vsync_setting.get_options()

        Retrieve the settings tooltip header:
            >>> vsync_setting.get_tooltip_header()

        Retrieve the settings tooltip body:
            >>> vsync_setting.get_tooltip_body()
        """
        title = f'<p>Enable VSync&nbsp;&nbsp;&nbsp;&nbsp;{u"\u2753"}</p>'
        options = ["Select Option...", "Enable", "Enable (D3D9)", "Disable"]
        tooltip_header = f'<h3 {header}>Select to enable VSync and how many frames</h3>'
        tooltip_body = f'<p {bodyTop}>VSync (Vertical Synchronisation) Vertical Sync (VSync) synchronizes the frame rate of a game with the refresh rate of your monitor to prevent screen tearing. It ensures smoother visuals but may introduce input lag. If frames drop below the VSync level, it can result in performance issues such as stuttering or lower frame rates.</p><p {bodyBot}>1 Frame - Synchronizes the rendering of frames with the display refresh rate, ensuring one frame is displayed per refresh cycle.<br>2 Frames - Synchronizes rendering with the display refresh rate, buffering two frames for reduced tearing and slightly higher latency.</p>'
        rule = False
        super().__init__(title, options, tooltip_header, tooltip_body, rule)


class VSync_Level(BaseSetting):
    # Class representing the VSync setting.

    def __init__(self):
        """
        Initializes the VSYNC setting.

        Returns:

            str: Title of the setting (VSYNC) encoded in HTML
            tuple: Set of immutable options for the current setting (VSYNC)
            str: Tooltip header of the setting (VSYNC) encoded in HTML
            str: Tooltip body of the setting (VSYNC) encoded in HTML

        Examples:

        Instantiate the VSYNC setting:
            >>> vsync_setting = VSYNC()

        Retrieve the settings title:
            >>> vsync_setting.get_title()

        Retrieve the settings options:
            >>> vsync_setting.get_options()

        Retrieve the settings tooltip header:
            >>> vsync_setting.get_tooltip_header()

        Retrieve the settings tooltip body:
            >>> vsync_setting.get_tooltip_body()
        """
        title = f'<p>&nbsp;&nbsp;&nbsp;&nbsp;-VSync Level&nbsp;&nbsp;&nbsp;&nbsp;{u"\u2753"}</p>'
        options = ["Select Option...", "1 Frame", "2 Frames", "Off"]
        tooltip_header = f'<h3 {header}>Select to enable VSync and how many frames</h3>'
        tooltip_body = f'<p {bodyTop}>VSync (Vertical Synchronisation) Vertical Sync (VSync) synchronizes the frame rate of a game with the refresh rate of your monitor to prevent screen tearing. It ensures smoother visuals but may introduce input lag. If frames drop below the VSync level, it can result in performance issues such as stuttering or lower frame rates.</p><p {bodyBot}>1 Frame - Synchronizes the rendering of frames with the display refresh rate, ensuring one frame is displayed per refresh cycle.<br>2 Frames - Synchronizes rendering with the display refresh rate, buffering two frames for reduced tearing and slightly higher latency.</p>'
        rule = False
        super().__init__(title, options, tooltip_header, tooltip_body, rule)


class VSync_Level_D3D9(BaseSetting):
    # Class representing the VSync_D3D9 setting.

    def __init__(self):
        """
        Initializes the VSYNC_D3D9 setting.

        Returns:

            str: Title of the setting (VSYNC_D3D9) encoded in HTML
            tuple: Set of immutable options for the current setting (VSYNC_D3D9)
            str: Tooltip header of the setting (VSYNC_D3D9) encoded in HTML
            str: Tooltip body of the setting (VSYNC_D3D9) encoded in HTML

        Examples:

        Instantiate the VSYNC_D3D9 setting:
            >>> vsync_d3d9_setting = VSYNC_D3D9()

        Retrieve the settings title:
            >>> vsync_d3d9_setting.get_title()

        Retrieve the settings options:
            >>> vsync_d3d9_setting.get_options()

        Retrieve the settings tooltip header:
            >>> vsync_d3d9_setting.get_tooltip_header()

        Retrieve the settings tooltip body:
            >>> vsync_d3d9_setting.get_tooltip_body()
        """
        title = f'<p>&nbsp;&nbsp;&nbsp;&nbsp;-VSync Level (D3D9 Applications)&nbsp;&nbsp;&nbsp;&nbsp;{u"\u2753"}</p>'
        options = ["Select Option...", "1 Frame", "2 Frames", "Off"]
        tooltip_header = f'<h3 {header}>Select to enable VSync and how many frames (D3D9 applications only)</h3>'
        tooltip_body = f'<p {bodyTop}>VSync (Vertical Synchronisation) Vertical Sync (VSync) synchronizes the frame rate of a game with the refresh rate of your monitor to prevent screen tearing. It ensures smoother visuals but may introduce input lag. If frames drop below the VSync level, it can result in performance issues such as stuttering or lower frame rates.</p><p {bodyBot}>1 Frame - Synchronizes the rendering of frames with the display refresh rate, ensuring one frame is displayed per refresh cycle.<br>2 Frames - Synchronizes rendering with the display refresh rate, buffering two frames for reduced tearing and slightly higher latency.</p>'
        rule = True
        super().__init__(title, options, tooltip_header, tooltip_body, rule)


class Frame_Limit_Enable(BaseSetting):
    # Class representing the Frame_Limit setting.

    def __init__(self):
        """
        Initializes the Frame_Limit setting.

        Returns:

            str: Title of the setting (Frame_Limit) encoded in HTML
            tuple: Set of immutable options for the current setting (Frame_Limit)
            str: Tooltip header of the setting (Frame_Limit) encoded in HTML
            str: Tooltip body of the setting (Frame_Limit) encoded in HTML

        Examples:

        Instantiate the Frame_Limit setting:
            >>> frame_limit_setting = Frame_Limit()

        Retrieve the settings title:
            >>> frame_limit_setting.get_title()

        Retrieve the settings options:
            >>> frame_limit_setting.get_options()

        Retrieve the settings tooltip header:
            >>> frame_limit_setting.get_tooltip_header()

        Retrieve the settings tooltip body:
            >>> frame_limit_setting.get_tooltip_body()
        """
        title = f'<p>Enable Frame Limit&nbsp;&nbsp;&nbsp;&nbsp;{u"\u2753"}</p>'
        options = ["Select Option...", "Enable", "Enable (D3D9)", "Disable"]
        tooltip_header = f'<h3 {header}>Select the frame limit</h3>'
        tooltip_body = f'<p {bodyTop}>Frame limiting is a technique used to cap the maximum number of frames rendered per second, controlling the rate at which the GPU generates frames for smoother performance.</p><p {bodyBot}>The most common values are:<br>30Hz (30FPS)<br>60Hz (60FPS)<br>75Hz (75FPS)<br>120Hz (120FPS)<br>144Hz (144FPS)<br>240Hz (240FPS)</p>'
        rule = False
        super().__init__(title, options, tooltip_header, tooltip_body, rule)


class Frame_Limit(BaseSetting):
    # Class representing the Frame_Limit setting.

    def __init__(self):
        """
        Initializes the Frame_Limit setting.

        Returns:

            str: Title of the setting (Frame_Limit) encoded in HTML
            tuple: Set of immutable options for the current setting (Frame_Limit)
            str: Tooltip header of the setting (Frame_Limit) encoded in HTML
            str: Tooltip body of the setting (Frame_Limit) encoded in HTML

        Examples:

        Instantiate the Frame_Limit setting:
            >>> frame_limit_setting = Frame_Limit()

        Retrieve the settings title:
            >>> frame_limit_setting.get_title()

        Retrieve the settings options:
            >>> frame_limit_setting.get_options()

        Retrieve the settings tooltip header:
            >>> frame_limit_setting.get_tooltip_header()

        Retrieve the settings tooltip body:
            >>> frame_limit_setting.get_tooltip_body()
        """
        title = f'<p>&nbsp;&nbsp;&nbsp;&nbsp;-Frame Limit&nbsp;&nbsp;&nbsp;&nbsp;{u"\u2753"}</p>'
        options = ["Select Option...", "30", "60", "75", "120", "144", "240"]
        tooltip_header = f'<h3 {header}>Select the frame limit</h3>'
        tooltip_body = f'<p {bodyTop}>Frame limiting is a technique used to cap the maximum number of frames rendered per second, controlling the rate at which the GPU generates frames for smoother performance.</p><p {bodyBot}>The most common values are:<br>30Hz (30FPS)<br>60Hz (60FPS)<br>75Hz (75FPS)<br>120Hz (120FPS)<br>144Hz (144FPS)<br>240Hz (240FPS)</p>'
        rule = False
        super().__init__(title, options, tooltip_header, tooltip_body, rule)


class Frame_Limit_D3D9(BaseSetting):
    # Class representing the Frame_Limit_D3D9 setting.

    def __init__(self):
        """
        Initializes the Frame_Limit_D3D9 setting.

        Returns:

            str: Title of the setting (Frame_Limit_D3D9) encoded in HTML
            tuple: Set of immutable options for the current setting (Frame_Limit_D3D9)
            str: Tooltip header of the setting (Frame_Limit_D3D9) encoded in HTML
            str: Tooltip body of the setting (Frame_Limit_D3D9) encoded in HTML

        Examples:

        Instantiate the Frame_Limit_D3D9 setting:
            >>> frame_limit_d3d9_setting = Frame_Limit_D3D9()

        Retrieve the settings title:
            >>> frame_limit_d3d9_setting.get_title()

        Retrieve the settings options:
            >>> frame_limit_d3d9_setting.get_options()

        Retrieve the settings tooltip header:
            >>> frame_limit_d3d9_setting.get_tooltip_header()

        Retrieve the settings tooltip body:
            >>> frame_limit_d3d9_setting.get_tooltip_body()
        """
        title = f'<p>&nbsp;&nbsp;&nbsp;&nbsp;-Frame Limit (D3D9 Applications)&nbsp;&nbsp;&nbsp;&nbsp;{u"\u2753"}</p>'
        options = ["Select Option...", "30", "60", "75", "120", "144", "240"]
        tooltip_header = f'<h3 {header}>Select the frame limit (D3D9 applications only)</h3>'
        tooltip_body = f'<p {bodyTop}>Frame limiting is a technique used to cap the maximum number of frames rendered per second, controlling the rate at which the GPU generates frames for smoother performance.</p><p {bodyBot}>The most common values are:<br>30Hz (30FPS)<br>60Hz (60FPS)<br>75Hz (75FPS)<br>120Hz (120FPS)<br>144Hz (144FPS)<br>240Hz (240FPS)</p>'
        rule = False
        super().__init__(title, options, tooltip_header, tooltip_body, rule)
