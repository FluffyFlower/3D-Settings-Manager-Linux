"""
File       : main.py
Author     : Fluffy Flower (Martin Wylde)
Contact    :
    Email   - martincw1989@gmail.com
    Telegram- @FluffyFlower
    Discord - fluffy_flower
Date       : 13/03/2025
Version    : 1.0.2
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
import sys
from Window.app_logging import OutputLog
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
    # Logging variables
    _log = OutputLog()
    _file_name: str = "main.py          "

    app = QApplication(sys.argv)
    _log.log_routine(_file_name, 1, 53, 53, "QApplication (app) created..")
    window = MainWindow()
    _log.log_routine(_file_name, 2, 55, 55, "MainWindow (window) created..")
    window.show()
    _log.log_routine(_file_name, 3, 57, 57, "Showing window..")
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
