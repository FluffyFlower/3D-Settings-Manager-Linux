"""
File:
    __init__.py
Author:
    Fluffy Flower (Martin Wylde)
Date:
    03/05/2024
Description:
    Initialization file for the 3D Settings Manager package.
    This package provides a collection of classes representing various
    graphics settings to be manged for either VKBasalt or DXVK including:
    Anistropic Filtering (AF),
    Context Adaptive Shading (CAS),
    DirectX 3D Feature Level (D3DLEVEL),
    Denoised Luma Sharpening (DLS),
    Fast Approximate Anti-Aliasing (FXAA),
    High Dynamic Range (HDR),
    Subpixel Morphological Anti-Aliasing (SMAA), and
    Vertical Synchronization (VSYNC).

    Each setting class is contained in its respective module and is imported
    here to provide a convenient interface for users of the package.
"""

from Window.Settings.AF import (
    Anistropic_Filtering_Enable,
    Anistropic_Filtering_Level,
    Anistropic_Filtering_Level_D3D9,
    LOD_Enable, LOD_Bias, LOD_Bias_D3D9,
    Clamp_Negative_LOD,
    Clamp_Negative_LOD_D3D9)
from Window.Settings.CAS import (
    CAS_Enable,
    CAS_Sharpness)
from Window.Settings.D3DLEVEL import (
    D3D_Level)
from Window.Settings.DLS import (
    DLS_Enable,
    DLS_Sharpness,
    DLS_Denoise)
from Window.Settings.FXAA import (
    FXAA_Enable,
    FXAA_Quality_Subpixel,
    FXAA_Quality_Edge_Threshold,
    FXAA_Edge_Threshold_Bias)
from Window.Settings.HDR import (
    HighDynamicRange)
from Window.Settings.SMAA import (
    SMAA_Enable,
    SMAA_Edge_Detection,
    SMAA_Threshold,
    SMAA_Search_Steps,
    SMAA_Search_Steps_Diagonal,
    SMAA_Corner_Rounding)
from Window.Settings.VSYNC import (
    VSync_Enable,
    VSync_Level,
    VSync_Level_D3D9,
    Frame_Limit_Enable,
    Frame_Limit, Frame_Limit_D3D9)
