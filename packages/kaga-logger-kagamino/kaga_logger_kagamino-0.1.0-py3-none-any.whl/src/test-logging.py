import datetime as dt
from dataclasses import dataclass

@dataclass
class LogLevel:
    name: str
    short_name: str
    priority: int
    color: str

DEBUG = LogLevel('DEBUG', 'DEBU', 0, "\033[35m")
INFO = LogLevel('INFO', 'INFO', 1, "\033[34m")
WARNING = LogLevel('WARNING', 'WARN', 2, "\033[33m")
ERROR = LogLevel('ERROR', 'ERRO', 3, "\033[31m")
CRITICAL = LogLevel('CRITICAL', 'CRIT', 4, "\033[31m")


LOG_FORMAT = "{color}[ {level} ] {datetime} - {message}\033[39m"

class Logger:
    level: LogLevel

    def __init__(self, level: LogLevel = INFO):
        self.level = level

    def log(self, msg: str, level: LogLevel):
        if level.priority >= self.level.priority:
            print(LOG_FORMAT.format(datetime=dt.datetime.now(), level=level.short_name, message=msg, color=level.color))
    
    def debug(self, msg: str):
        self.log(msg, DEBUG)

    def info(self, msg: str):
        self.log(msg, INFO)

    def warn(self, msg: str):
        self.log(msg, WARNING)

    def error(self, msg: str):
        self.log(msg, ERROR)

    def critical(self, msg: str):
        self.log(msg, CRITICAL)

if __name__ == "__main__":
    logger = Logger(DEBUG)
    logger.debug("debug")
    logger.info("information")
    logger.warn("warn")
    logger.error("error")
    logger.critical("critical")
