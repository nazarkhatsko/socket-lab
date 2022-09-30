from enum import Enum
from datetime import datetime
from colorama import Fore, Back, Style


class LogType(Enum):
    INFO = "[INFO]"
    WARN = "[WARN]"
    ERROR = "[ERROR]"


def __time_now() -> str:
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")


def __logging(log_type: LogType, message: str):
    if log_type == LogType.INFO:
        print(Fore.GREEN, end="")
    elif log_type == LogType.WARN:
        print(Fore.YELLOW, end="")
    elif log_type == LogType.ERROR:
        print(Fore.RED, end="")
    print(f"{log_type.value} {message} - {__time_now()}", Style.RESET_ALL)


def log_info(message: str):
    __logging(LogType.INFO, message)


def log_warn(message: str):
    __logging(LogType.WARN, message)


def log_error(message: str):
    __logging(LogType.ERROR, message)
