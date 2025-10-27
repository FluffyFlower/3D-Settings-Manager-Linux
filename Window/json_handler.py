"""
File       : json_handler.py
Author     : Fluffy Flower (Martin Wylde)
Contact    :
    Email   - martincw1989@gmail.com
    Telegram- @FluffyFlower
    Discord - fluffy_flower
Date       : 10/03/2025
Version    : 0.1.1
Description: Management class for all JSON CRUD operations pertinent to the application.
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
import json


# ------------------------------------------------------------------------------------------------ #
#                                                                                                  #
#     ██  ██████  ██████      ██            ██  ██                      ██                         #
#     ██  ██      ██  ██  ██  ██            ██  ██    ████  ██████      ██  ██        ████    ████ #
#     ██  ██████  ██  ██  ██████            ██████  ██  ██  ██  ██    ████  ██      ██  ██  ██     #
# ██  ██      ██  ██  ██  ██  ██            ██  ██  ██  ██  ██  ██  ██  ██  ██      ████    ██     #
# ██████  ██████  ██████  ██                ██  ██  ██████  ██  ██  ██████  ██████    ████  ██     #
#                                                                                                  #
# ------------------------------------------------------------------------------------------------ #


class AppJSONHandler:
    # --------------------------------------------------------------------------- #
    # Class initialisation and private variable creation                          #
    # --------------------------------------------------------------------------- #
    def __init__(self, app_json="user_apps.json"):
        self._app_json: str = app_json

    # --------------------------------------------------------------------------- #
    # Load JSON data                                                              #
    # --------------------------------------------------------------------------- #
    def load_app_details(self) -> dict:
        """
        Load JSON data from user_apps.json.

        Args:
            None.

        Returns:
            data(dict): user_apps.json as a dict.

        Raises:
            None.

        Examples:
            Default usage:
            >>> AppJSONHandler.load_json()
        """
        data: dict = None

        # If user_apps.json is missing set data to defaults.
        if not os.path.exists(self._app_json):
            data = {"applications": []}
            return data

        # Set data to loaded JSON from user_apps.json.
        with open(self._app_json, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data

    # --------------------------------------------------------------------------- #
    # Save JSON data                                                              #
    # --------------------------------------------------------------------------- #
    def save_app_details(self, data_input: dict) -> None:
        """
        Save JSON data to user_apps.json

        Args:
            data(dict): Dictionary containing JSON data to be saved to user_apps.json.

        Returns:
            None.

        Raises:
            None.
        """
        data: dict = data_input

        with open(self._app_json, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    # --------------------------------------------------------------------------- #
    # Add application                                                             #
    # --------------------------------------------------------------------------- #
    def add_app_details(self, app_name_input: str, app_path_input: str, app_dx_input: str) -> None:
        """
        Add new app entry to user_apps.json

        Args:
            app_name(str): String containing applications name.
            app_path(str): String containing applications path.
            app_dx(str): String containing applications DirectX version.

        Returns:
            None.

        Raises:
            None.
        """
        app_name: str = app_name_input
        app_path: str = app_path_input
        app_dx: str = app_dx_input

        data: dict = self.load_app_details()

        data["applications"].append({
            "app_name": app_name,
            "app_path": app_path,
            "app_dx": app_dx,
            "settings": [{
                "settings_set": False,
                "fxaa_enable": None,
                "fxaa_quality_subpixel": None,
                "fxaa_quality_edge": None,
                "fxaa_edge_threshold": None,
                "smaa_enable": None,
                "smaa_edge_detection": None,
                "smaa_threshold": None,
                "smaa_search_steps": None,
                "smaa_search_steps_diagonal": None,
                "smaa_corner_rounding": None,
                "af_enable": None,
                "af_level": None,
                "af_level_d3d9": None,
                "lod_bias": None,
                "lod_bias_d3d9": None,
                "clamp_negative_lod": None,
                "clamp_negative_lod_d3d9": None,
                "cas_enable": None,
                "cas_level": None,
                "dls_enable": None,
                "dls_sharpness": None,
                "dls_denoise": None,
                "vsync_enable": None,
                "vsync_level": None,
                "vsync_level_d3d9": None,
                "frame_limit_enable": None,
                "frame_limit_level": None,
                "frame_limit_level_d3d9": None,
                "hdr_enable": None,
                "d3d_level": None
            }]
        })

        self.save_app_details(data)

    # --------------------------------------------------------------------------- #
    # Remove application                                                          #
    # --------------------------------------------------------------------------- #
    def remove_app(self, file_path_input: str) -> None:
        """
        Remove app entry from user_apps.json

        Args:
            file_path(str): String containing applications path.

        Returns:
            None.

        Raises:
            None.
        """
        file_path: str = file_path_input

        data: dict = self.load_app_details()

        app_list: list = [app for app in data["applications"] if os.path.basename(app["app_path"]) != os.path.basename(file_path)]

        data["applications"] = app_list

        self.save_app_details(data)

    # --------------------------------------------------------------------------- #
    # New settings                                                                #
    # --------------------------------------------------------------------------- #
    # def new_settings(data) -> None:
