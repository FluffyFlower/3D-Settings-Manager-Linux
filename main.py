"""
File       : main.py
Author     : Fluffy Flower (Martin Wylde)
Contact    :
    Email   - martincw1989@gmail.com
    Telegram- @FluffyFlower
    Discord - fluffy_flower
Date       : 13/03/2025
Version    : 1.0.3
Description: Main file for starting the main window via main_window.py.
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
import sys, base64
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtWidgets import QApplication
from Window.main_window import MainWindow


# ---------------------------- #
#                              #
# ██  ██          ██           #
# ██████    ████        ██████ #
# ██  ██  ██  ██  ██    ██  ██ #
# ██  ██  ██  ██  ██    ██  ██ #
# ██  ██  ██████  ████  ██  ██ #
#                              #
# ---------------------------- #


def main() -> None:
    """
    Main entry point for the program.

    Args:
        None.

    Returns:
        None.
    """
    # Constant 
    _ICON_BASE64_STRING = "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"
    
    def icon_from_base64(app: QApplication) -> QIcon:
        """
        Converts a base64 string to a QIcon.

        Args:
            base64_string (str): Base64 encoded string of the icon image.

        Returns:
            QIcon: QIcon object created from the base64 string.

        Raises:
            Exception: If there is an error during conversion.

        Examples:
            Default Usage:
            .. code-block:: python
            >>> icon_from_base64(QApplication)
        """
        try:
            icon = base64.b64decode(_ICON_BASE64_STRING)
            pixmap = QPixmap()
            pixmap.loadFromData(icon)
        
            app.setWindowIcon(QIcon(pixmap))

        except Exception as e:
            print(f"Error converting base64 string to QIcon: {e}")
    
    # Create the application
    app = QApplication(sys.argv)

    # Set the application icon from base64 string
    icon_from_base64(app)

    # Create the main window
    window = MainWindow()

    # Show the main window
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
