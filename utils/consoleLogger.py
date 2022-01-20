from colorama import Fore
import utils.timeUtils as sysTime

def error(message:str):
    print(Fore.LIGHTYELLOW_EX + f"[{sysTime.get_current_time()}]" + Fore.RED + "[E]: " + message + Fore.WHITE)

def alert(message:str):
    print(Fore.LIGHTYELLOW_EX + f"[{sysTime.get_current_time()}]" + Fore.YELLOW + "[A]: " + message + Fore.WHITE)

def info(message:str):
    print(Fore.LIGHTYELLOW_EX + f"[{sysTime.get_current_time()}]" + Fore.CYAN + "[I]: " + message + Fore.WHITE)

def success(message:str):
    print(Fore.LIGHTYELLOW_EX + f"[{sysTime.get_current_time()}]" + Fore.LIGHTGREEN_EX + "[S]: " + message + Fore.WHITE)