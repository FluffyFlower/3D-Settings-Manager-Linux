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

    def log_col_names(self) -> None:
        # Output
        print(f"{self._BLD}{'TIME':^8}{self._RES}║ {self._BLD}{'FILE':^17}{self._RES}║ {self._BLD}NO#{self._RES}║ {self._BLD}{'LINES':^15}{self._RES}║ {self._BLD}SEVERITY{self._RES}║ {self._BLD}MESSAGE{self._RES}")
        print("════════╬══════════════════╬════╬════════════════╬═════════╬════════")

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
        print(f"{self._time}{self._RES}║ {self._BLU}{file_string}{self._RES}║ {instruction_string}{self._RES}║ line {line_from} to {line_to}{self._RES}║{self._GRE}{self._BLD} ROUTINE {self._RES}║{self._GRE} {message}{self._RES}")

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
        print(f"{self._time}{self._RES}║ {self._BLU}{file_string}{self._RES}║ {instruction_string}{self._RES}║ line {line_from} to {line_to}{self._RES}║{self._YEL}{self._BLD} WARNING {self._RES}║{self._YEL} {message}{self._RES}")

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
        print(f"{self._time}{self._RES}║ {self._BLU}{file_string}{self._RES}║ {instruction_string}{self._RES}║ line {line_from} to {line_to}{self._RES}║{self._RED}{self._BLD} FATAL   {self._RES}║{self._RED} {message}{self._RES}")
