"""
File:      : app_logging.py
Author     : Fluffy Flower (Martin Wylde)
Contact    :
    Email   - martincw1989@gmail.com
    Telegram- @FluffyFlower
    Discord - fluffy_flower
Date       : 13/03/2025
Version    : 0.0.3
Description: Logging output system for entire app.
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
import time


# ---------------------------------------------------- #
#                                                      #
# ██                              ██                   #
# ██      ██████    ████    ████        ██████    ████ #
# ██      ██  ██  ██  ██  ██  ██  ██    ██  ██  ██  ██ #
# ██      ██  ██  ██████  ██████  ██    ██  ██  ██████ #
# ██████  ██████      ██      ██  ████  ██  ██      ██ #
#                 ████    ████                  ████   #
# ---------------------------------------------------- #

class OutputLog():
    # Terminal logging formatting
    _RED = '\033[91m'
    _YEL = '\033[93m'
    _GRE = '\033[92m'
    _BLU = '\033[94m'
    _BLD = '\033[1m'
    _RES = '\033[0m'

    _time: time

    def log_routine(self, file_string_input: str, instruction_input: int, line_from_input: int, line_to_input: int, message_input: str) -> None:
        # Pull input and convert to strings
        file_string: str = file_string_input

        if instruction_input < 10:
            instruction_string: str = str(f"00{instruction_input}")
        elif instruction_input >= 10 and instruction_input < 100:
            instruction_string: str = str(f"0{instruction_input}")
        else:
            instruction_string: str = str(instruction_input)

        if line_from_input < 100:
            line_from: str = str(f"0{line_from_input}")
        else:
            line_from: str = str(line_from_input)

        if line_to_input < 100:
            line_to: str = str(f"0{line_to_input}")
        else:
            line_to: str = str(line_to_input)

        message: str = message_input

        self._time = time.strftime("%H:%M:%S", time.localtime())

        # Output
        print(f"{self._time}: {self._BLU}{file_string}: {instruction_string}: line {line_from} to {line_to}:{self._GRE}{self._BLD} ROUTINE:{self._RES} {message}")

    def log_warning(self, file_string_input: str, instruction_input: int, line_from_input: int, line_to_input: int, message_input: str) -> None:
        # Pull input and convert to strings
        file_string: str = file_string_input

        if instruction_input < 10:
            instruction_string: str = str(f"00{instruction_input}")
        elif instruction_input >= 10 and instruction_input < 100:
            instruction_string: str = str(f"0{instruction_input}")
        else:
            instruction_string: str = str(instruction_input)

        if line_from_input < 100:
            line_from: str = str(f"0{line_from_input}")
        else:
            line_from: str = str(line_from_input)

        if line_to_input < 100:
            line_to: str = str(f"0{line_to_input}")
        else:
            line_to: str = str(line_to_input)

        message: str = message_input

        self._time = time.strftime("%H:%M:%S", time.localtime())

        # Output
        print(f"{self._time}: {self._BLU}{file_string}: {instruction_string}: line {line_from} to {line_to}:{self._YEL}{self._BLD} WARNING:{self._RES} {message}")

    def log_fatal(self, file_string_input: str, instruction_input: int, line_from_input: int, line_to_input: int, message_input: str) -> None:
        # Pull input and convert to strings
        file_string: str = file_string_input

        if instruction_input < 10:
            instruction_string: str = str(f"00{instruction_input}")
        elif instruction_input >= 10 and instruction_input < 100:
            instruction_string: str = str(f"0{instruction_input}")
        else:
            instruction_string: str = str(instruction_input)

        if line_from_input < 100:
            line_from: str = str(f"0{line_from_input}")
        else:
            line_from: str = str(line_from_input)

        if line_to_input < 100:
            line_to: str = str(f"0{line_to_input}")
        else:
            line_to: str = str(line_to_input)

        message: str = message_input

        self._time = time.strftime("%H:%M:%S", time.localtime())

        # Output
        print(f"{self._time}: {self._BLU}{file_string}: {instruction_string}: line {line_from} to {line_to}:{self._RED}{self._BLD} FATAL  :{self._RES} {message}")
