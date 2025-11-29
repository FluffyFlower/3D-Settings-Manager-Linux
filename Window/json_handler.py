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
    def __init__(self, 
                 app_json="user_apps.json"):
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
            .. code-block:: python
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
    def save_app_details(self, 
                         data_input: dict) -> None:
        """
        Save JSON data to user_apps.json

        Args:
            data(dict): Dictionary containing JSON data to be saved to user_apps.json.

        Returns:
            None.

        Raises:
            None.

        Examples:
            Default usage:
            .. code-block:: python
            >>> AppJSONHandler.save_json(data)
        """
        # Unpack inputs
        data: dict = data_input

        # Save data to user_apps.json
        with open(self._app_json, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    # --------------------------------------------------------------------------- #
    # Add application                                                             #
    # --------------------------------------------------------------------------- #
    def add_new_app(self, 
                        app_name_input: str, 
                        app_path_input: str, 
                        app_gapi_input: str) -> None:
        """
        Add new app entry to user_apps.json

        Args:
            app_name(str): String containing applications name.
            app_path(str): String containing applications path.
            app_gapi(str): String containing applications DirectX version.

        Returns:
            None.

        Raises:
            None.

        Examples:
            Default usage:
            .. code-block:: python
            >>> AppJSONHandler.add_new_app("Application Name", "Application Path", "Application Graphics API")
        """
        # Unpack inputs
        app_name: str = app_name_input
        app_path: str = app_path_input
        app_gapi: str = app_gapi_input

        # Load existing data from user_apps.json
        data: dict = self.load_app_details()

        # Append new app entry to data
        data["applications"].append({
            "app_name": app_name,
            "app_path": app_path,
            "app_gapi": app_gapi,
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
                "lod_enable": None,
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

        # Save updated data to user_apps.json
        self.save_app_details(data)

    def add_app_settings(self, 
                         app_path_input: str, 
                         app_name_input: str, 
                         app_gapi_input: str,
                         settings_list_input: list) -> None:
        """
        Save / update app settings to user_apps.json

        Args:
            app_name(str): String containing applications name.
            app_path(str): String containing applications path.
            settings_list(list): List containing all settings values from GUI.

        Returns:
            None.
        
        Raises:
            None.

        Examples:
            Default usage:
            .. code-block:: python
            >>> AppJSONHandler.add_app_settings("Application Path", "Application Name", "Application Graphics API", settings_list)
        """
        # Unpack inputs
        app_path: str = app_path_input
        app_name: str = app_name_input
        app_gapi: str = app_gapi_input

        # Load existing data from user_apps.json
        data: dict = self.load_app_details()

        # Unpack settings list
        settings_list: list = settings_list_input

        # Assign settings values from list
        fxaa_enable: bool = settings_list[0]
        fxaa_quality_subpixel: str = settings_list[1]
        fxaa_quality_edge: str = settings_list[2]
        fxaa_edge_threshold: str = settings_list[3]
        smaa_enable: bool = settings_list[4]
        smaa_edge_detection: str = settings_list[5]
        smaa_threshold: str = settings_list[6]
        smaa_search_steps: str = settings_list[7]
        smaa_search_steps_diagonal: str = settings_list[8]
        smaa_corner_rounding: str = settings_list[9]
        anisotropic_enable: bool = settings_list[10]
        anisotropic_level: str = settings_list[11]
        anisotropic_level_d3d9: str = settings_list[12]
        lod_enable: bool = settings_list[13]
        lod_bias: str = settings_list[14]
        lod_bias_d3d9: str = settings_list[15]
        clamp_negative_lod: str = settings_list[16]
        clamp_negative_lod_d3d9: str = settings_list[17]
        cas_enable: bool = settings_list[18]
        cas_sharpness: str = settings_list[19]
        dls_enable: bool = settings_list[20]
        dls_sharpness: str = settings_list[21]
        dls_denoise: str = settings_list[22]
        vsync_enable: bool = settings_list[23]
        vsync_level: str = settings_list[24]
        vsync_level_d3d9: str = settings_list[25]
        frame_limit_enable: bool = settings_list[26]
        frame_limit_level: str = settings_list[27]
        frame_limit_level_d3d9: str = settings_list[28]
        hdr_enable: bool = settings_list[29]
        d3d_level: str = settings_list[30]

        # Iterate through apps in data
        for app in data["applications"]:
            # Match app entry
            if app["app_name"] == app_name and app["app_path"] == app_path and app["app_gapi"] == app_gapi:
                # Get settings dict for app
                settings: dict = app["settings"][0]
                # Update only changed settings values. On initial save all values will be changed from None.
                if settings["settings_set"] != True:
                    settings["settings_set"] = True
                if settings["fxaa_enable"] != fxaa_enable:
                    settings["fxaa_enable"] = fxaa_enable
                if settings["fxaa_quality_subpixel"] != fxaa_quality_subpixel:
                    settings["fxaa_quality_subpixel"] = fxaa_quality_subpixel
                if settings["fxaa_quality_edge"] != fxaa_quality_edge:
                    settings["fxaa_quality_edge"] = fxaa_quality_edge
                if settings["fxaa_edge_threshold"] != fxaa_edge_threshold:
                    settings["fxaa_edge_threshold"] = fxaa_edge_threshold
                if settings["smaa_enable"] != smaa_enable:
                    settings["smaa_enable"] = smaa_enable
                if settings["smaa_edge_detection"] != smaa_edge_detection:
                    settings["smaa_edge_detection"] = smaa_edge_detection
                if settings["smaa_threshold"] != smaa_threshold:
                    settings["smaa_threshold"] = smaa_threshold
                if settings["smaa_search_steps"] != smaa_search_steps:
                    settings["smaa_search_steps"] = smaa_search_steps
                if settings["smaa_search_steps_diagonal"] != smaa_search_steps_diagonal:
                    settings["smaa_search_steps_diagonal"] = smaa_search_steps_diagonal
                if settings["smaa_corner_rounding"] != smaa_corner_rounding:
                    settings["smaa_corner_rounding"] = smaa_corner_rounding
                if settings["af_enable"] != anisotropic_enable:
                    settings["af_enable"] = anisotropic_enable
                if settings["af_level"] != anisotropic_level:
                    settings["af_level"] = anisotropic_level
                if settings["af_level_d3d9"] != anisotropic_level_d3d9:
                    settings["af_level_d3d9"] = anisotropic_level_d3d9
                if settings["lod_enable"] != lod_enable:
                    settings["lod_enable"] = lod_enable
                if settings["lod_bias"] != lod_bias:
                    settings["lod_bias"] = lod_bias
                if settings["lod_bias_d3d9"] != lod_bias_d3d9:
                    settings["lod_bias_d3d9"] = lod_bias_d3d9
                if settings["clamp_negative_lod"] != clamp_negative_lod:
                    settings["clamp_negative_lod"] = clamp_negative_lod
                if settings["clamp_negative_lod_d3d9"] != clamp_negative_lod_d3d9:
                    settings["clamp_negative_lod_d3d9"] = clamp_negative_lod_d3d9
                if settings["cas_enable"] != cas_enable:
                    settings["cas_enable"] = cas_enable
                if settings["cas_level"] != cas_sharpness:
                    settings["cas_level"] = cas_sharpness
                if settings["dls_enable"] != dls_enable:
                    settings["dls_enable"] = dls_enable
                if settings["dls_sharpness"] != dls_sharpness:                    
                    settings["dls_sharpness"] = dls_sharpness
                if settings["dls_denoise"] != dls_denoise:
                    settings["dls_denoise"] = dls_denoise
                if settings["vsync_enable"] != vsync_enable:
                    settings["vsync_enable"] = vsync_enable
                if settings["vsync_level"] != vsync_level:
                    settings["vsync_level"] = vsync_level
                if settings["vsync_level_d3d9"] != vsync_level_d3d9:
                    settings["vsync_level_d3d9"] = vsync_level_d3d9
                if settings["frame_limit_enable"] != frame_limit_enable:
                    settings["frame_limit_enable"] = frame_limit_enable
                if settings["frame_limit_level"] != frame_limit_level:
                    settings["frame_limit_level"] = frame_limit_level
                if settings["frame_limit_level_d3d9"] != frame_limit_level_d3d9:
                    settings["frame_limit_level_d3d9"] = frame_limit_level_d3d9
                if settings["hdr_enable"] != hdr_enable:
                    settings["hdr_enable"] = hdr_enable
                if settings["d3d_level"] != d3d_level:
                    settings["d3d_level"] = d3d_level
        
        # Save updated data to user_apps.json
        self.save_app_details(data)

    # --------------------------------------------------------------------------- #
    # Remove application                                                          #
    # --------------------------------------------------------------------------- #
    def remove_app(self, 
                   file_path_input: str) -> None:
        """
        Remove app entry from user_apps.json

        Args:
            file_path(str): String containing applications path.

        Returns:
            None.

        Raises:
            None.

        Examples:
            Default usage:
            .. code-block:: python
            >>> AppJSONHandler.add_new_app("Application Path")
        """
        # Unpack inputs
        file_path: str = file_path_input

        # Load existing data from user_apps.json
        data: dict = self.load_app_details()

        # Create new app list excluding app to be removed
        app_list: list = [app for app in data["applications"] if os.path.basename(app["app_path"]) != os.path.basename(file_path)]

        # Update data dict with new app list
        data["applications"] = app_list

        # Save updated data to user_apps.json
        self.save_app_details(data)

    # --------------------------------------------------------------------------- #
    # Get application details                                                     #
    # --------------------------------------------------------------------------- #
    def get_app_settings(self, 
                        app_path_input: str,
                        app_name_input: str,
                        app_gapi_input: str) -> dict:
        """
        Get app entry from user_apps.json

        Args:
            file_path(str): String containing applications path.

        Returns:
            app(dict): Dictionary containing app entry details.

        Raises:
            None.

        Examples:
            Default usage:
            .. code-block:: python
            >>> AppJSONHandler.get_app_settings("Application Path", "Application Name", "Application Graphics API")
        """
        # Unpack inputs
        app_path: str = app_path_input
        app_name: str = app_name_input
        app_gapi: str = app_gapi_input

        # Load existing data from user_apps.json
        data: dict = self.load_app_details()

        # Initialize empty setting list
        setting_list: list

        # Iterate through apps in data
        for app in data["applications"]:
            # Match app entry
            if app["app_name"] == app_name and app["app_path"] == app_path and app["app_gapi"] == app_gapi:
                # Get settings dict for app
                settings: dict = app["settings"][0]
                # Assign settings values to list
                setting_list = [None] * 31
                setting_list[0] = settings["fxaa_enable"]
                setting_list[1] = settings["fxaa_quality_subpixel"]
                setting_list[2] = settings["fxaa_quality_edge"]
                setting_list[3] = settings["fxaa_edge_threshold"]
                setting_list[4] = settings["smaa_enable"]
                setting_list[5] = settings["smaa_edge_detection"]
                setting_list[6] = settings["smaa_threshold"]
                setting_list[7] = settings["smaa_search_steps"]
                setting_list[8] = settings["smaa_search_steps_diagonal"]
                setting_list[9] = settings["smaa_corner_rounding"]
                setting_list[10] = settings["af_enable"]
                setting_list[11] = settings["af_level"]
                setting_list[12] = settings["af_level_d3d9"]
                setting_list[13] = settings["lod_enable"]
                setting_list[14] = settings["lod_bias"]
                setting_list[15] = settings["lod_bias_d3d9"]
                setting_list[16] = settings["clamp_negative_lod"]
                setting_list[17] = settings["clamp_negative_lod_d3d9"]
                setting_list[18] = settings["cas_enable"]
                setting_list[19] = settings["cas_level"]
                setting_list[20] = settings["dls_enable"]
                setting_list[21] = settings["dls_sharpness"]
                setting_list[22] = settings["dls_denoise"]
                setting_list[23] = settings["vsync_enable"]
                setting_list[24] = settings["vsync_level"]
                setting_list[25] = settings["vsync_level_d3d9"]
                setting_list[26] = settings["frame_limit_enable"]
                setting_list[27] = settings["frame_limit_level"]
                setting_list[28] = settings["frame_limit_level_d3d9"]
                setting_list[29] = settings["hdr_enable"]
                setting_list[30] = settings["d3d_level"]
        
        return setting_list