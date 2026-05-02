from colorama import init, Fore, Style
import os
import subprocess

init(autoreset=True)

class UI:
    # Defining our color palette using Colorama constants
    ERROR = Fore.RED + Style.BRIGHT
    SUCCESS = Fore.GREEN
    GOLD = Fore.YELLOW
    INFO = Fore.CYAN
    RESET = Style.RESET_ALL  # For manual resets if needed

    @staticmethod
    def announce(msg, color_style):
        # The f-string will apply the color, print the message,
        # and then reset automatically due to init(autoreset=True)
        print(f"{color_style}>> {msg}")

    @staticmethod
    def clear_console():
        subprocess.run(["cls" if os.name == "nt" else "clear"], shell=True)