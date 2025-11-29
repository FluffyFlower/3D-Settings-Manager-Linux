# <img src="icon.png" alt="App Icon" width="64" height="64" style="vertical-align: middle;"> 3D Settings Manager for Linux
A crossplatform GUI helping to streamline configuration of DXVK (`dxvk.conf`), and vkBasalt (`vkBasalt.conf`) settings for individual games when playing via proton / wine.<br/>
It offers a seamless and persistent way to manage per game 3D settings profiles, ensuring your proton / wine games run and look their best without manually editing the configuration files.<br/><br/>
Visit the following to find more information about the two projects:
- [DXVK](https://github.com/doitsujin/dxvk)
- [vkBasalt](https://github.com/DadSchoorse/vkBasalt)

<p align="center">
    <a href="https://ko-fi.com/S6S8XSPQX" target="_blank">
        <img 
            src="https://storage.ko-fi.com/cdn/kofi4.png?v=6" 
            alt="Buy Me a Coffee at ko-fi.com" 
            height="36" 
        />
    </a>
</p>

# Key Features
- ### GUI Wrapper for DXVK & vkBasalt:
  - Easily control and configure critical settings for DXVK and vkBasalt.
- ### Per Game Settings Management / JSON Persistence:
  - Add and manage entries for your favourite wine / proton games. These entries and their associated settings are saved uniquely for each application in a JSON file.
    - This application automatically attempts to detect the games name and graphics API (e.g. D3D12 / Vulkan etc) of the executable using the `pefile` library; for user reference.
- ### Automatic Deployment:
  - Upon saving, the manager automatically generates and places the necessary DXVK and vkBasalt configuration (`dxvk.conf` and `vkBasalt.conf`) directly into the selected applications working directory (where the executable is located).
- ### Load / Save Functionality:
  - Quickly load settings to populate the GUI dropdowns with the saved configuration for the selected game, or save settings to apply your changes; enabling quick tweaking of settings.
- ### Linux Native, Distro Agnostic Release:
  - Built specifically for the Linux ecosystem and distributed as a convenient, ready to run Appimage.
 
# Supported Settings & Values
| Setting | Possible Values | DXVK or vkBasalt |
| ------- | --------------- | ---------------- |
| <ins>**FXAA**</ins><br/><sub>Fast Approximate Anti-Aliasing</sub> | | |
| Subpixel Quality | *1.00 (Smoothest)<br/>0.75<br/>0.50<br/>0.25<br/>0.00 (Sharpest)* | vkBasalt |
| Edge Quality | *Highest Quality (0.063)<br/>High Quality<br/>Default (0.166)<br/>Low Quality<br/>Lowest Quality (0.333)* | vkBasalt |
| Edge Threshold Bias | *Upper Limit (0.0833)<br/>High Quality (0.0625)<br/>Visible Limit (0.0312)<br/>Zero* | vkBasalt |
| <ins>**SMAA**</ins><br/><sub>Subpixel Morphological Anti-Aliasing</sub> | | |
| Edge Detection Method | *Luma (Default)<br/>Color (Catches more edges)* | vkBasalt |
| Threshold | *Highest Quality<br/>Quality<br/>Balanced<br/>Low Quality<br/>Lowest Quality* | vkBasalt |
| Max Search Steps | *x32 (Highest Quality)<br/>x16<br/>x8<br/>x4<br/>x2 (Lowest Quality)* | vkBasalt |
| Max Diagonal Search Steps | *x16 (Highest Quality)<br/>x8<br/>x4<br/>x2<br/>x0 (Lowest Quality)* | vkBasalt |
| Corner Rounding | *1.00 (Highest Rounding)<br/>0.75<br/>0.50<br/>0.25<br/>0.00 (Lowest Rounding) | vkBasalt |
| <ins>**AF**</ins><br/><sub>Anisotropic Filtering</sub> | | |
| Level | *x16 (Highest Quality)<br/>x8<br/>x4<br/>x2<br/>x1 (Lowest Quality)* | DXVK |
| <ins>**LOD**</ins><br/><sub>Level of Detail</sub> | | |
| Bias | *-2.00 (Highest Quality)<br/>-1.00<br/>0.00 (Balanced)<br/>0.5<br/>1.00 (Lowest Quality) | DXVK |
| Clamp Negative LOD Bias | *Enabled<br/>Disabled*| DXVK |
| <ins>**CAS**</ins><br/><sub>Contrast Adaptive Sharpening</sub> | | |
| Level | *1.00 (Sharpest)<br/>0.75<br/>0.50<br/>0.25<br/>0.00 (Softest)* | vkBasalt |
| <ins>**DLS**</ins><br/><sub>Denoised Luma Sharpening</sub> | | |
| Sharpness Level | *1.00 (Sharpest)<br/>0.75<br/>0.50<br/>0.25<br/>0.00 (Softest)* | vkBasalt |
| Denoise Level | *1.00 (Full)<br/>0.75<br/>0.50<br/>0.25<br/>0.00 (Off)* | vkBasalt |
| <ins>**VSync**</ins><br/><sub>Vertical Synchronization</sub> | | |
| Level | *1 Frame (Match Refresh Rate)<br/>2 Frames (Double Refresh Rate)* | DXVK |
| Frame Limit | *30 Hz<br/>60 Hz<br/>75 Hz<br/>120 Hz<br/>144 Hz<br/>240 Hz* | DXVK |
| <ins>**HDR**</ins><br/><sub>High Dynamic Range | | |
| Toggle Enable | *Enabled<br/>Disabled* | DXVK |
| <ins>**Direct X Feature Level**</ins> | | |
| Toggle Level | *Direct X 9.1<br/>Direct X 9.2<br/>Direct X 9.3<br/>Direct X 10.0<br/>Direct X 10.1<br/>Direct X 11.0<br/>Direct X 11.1<br/>Direct X 12.0<br/>Direct X 12.1* | DXVK |

# How it Works / How to Use
1. Add Application
   - Push 'Add Application', Navigate to the games executable, then select it to let the manager scan and add it to the list.
2. Select the application to configure by pushing the corresponding radio button, then adjust the settings in the right panel.
3. Save Application
   - When you push 'Save Settings' two key actions are performed;
     1. Saves the selected applications settings to a JSON file for recall.
     2. Generates and places both `dxvk.conf` and `vkBasalt.conf` in the games working directory and gives you launch arguments to add to the applications steam listing.
4. Launch game
   - Test your settings...
  
Want to tweak settings?
1. Select the applications listing, then push 'Load Settings'
2. The settings should auto populate with the last saved settings ready to tweak.

Want to delete an applications listing?
1. Select the applications listing, then push 'Delete Application'
   - This removes the Application from the JSON file (manual removal of configuration files is required)
  
## Support This Project
If you find this tool helpful, please consider supporting its development:<br/>
<p align="center">
    <a href="https://ko-fi.com/S6S8XSPQX" target="_blank">
        <img 
            src="https://storage.ko-fi.com/cdn/kofi4.png?v=6" 
            alt="Buy Me a Coffee at ko-fi.com" 
            height="72" 
        />
    </a>
</p>
