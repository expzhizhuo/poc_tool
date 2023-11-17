"""
@Project ：pocsuite3测试文件 
@File    ：logger.py
@IDE     ：PyCharm 
@Author  ：zhizhuo
@Date    ：2023/11/14 09:45 
"""
import logging
import sys
from colorama import init as wininit

wininit(autoreset=True)


# logging.basicConfig(level=logging.INFO,
#                     format='[%(asctime)s] %(levelname)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
class Colored:
    def __init__(self):
        self.Red = '\033[1;31m'  # 红色
        self.Green = '\033[1;32m'  # 绿色
        self.Yellow = '\033[1;33m'  # 黄色
        self.Blue = '\033[1;34m'  # 蓝色
        self.Fuchsia = '\033[1;35m'  # 紫红色
        self.Cyan = '\033[1;36m'  # 青蓝色
        self.White = '\033[1;37m'  # 白色
        self.Reset = '\033[0m'  # 终端默认颜色

    def red(self, s):
        return "{0}{1}{2}".format(self.Red, s, self.Reset)

    def green(self, s):
        return "{0}{1}{2}".format(self.Green, s, self.Reset)

    def yellow(self, s):
        return "{0}{1}{2}".format(self.Yellow, s, self.Reset)

    def blue(self, s):
        return "{0}{1}{2}".format(self.Blue, s, self.Reset)

    def fuchsia(self, s):
        return "{0}{1}{2}".format(self.Fuchsia, s, self.Reset)

    def cyan(self, s):
        return "{0}{1}{2}".format(self.Cyan, s, self.Reset)

    def white(self, s):
        return "{0}{1}{2}".format(self.White, s, self.Reset)


color = Colored()


class LoggingLevel:
    SUCCESS = 50
    INFO = 49
    ERROR = 48
    WARNING = 47
    DEBUG = 46


logging.addLevelName(LoggingLevel.SUCCESS, color.cyan("SUCCESS"))
logging.addLevelName(LoggingLevel.INFO, "INFO")
logging.addLevelName(LoggingLevel.ERROR, color.red("ERROR"))
logging.addLevelName(LoggingLevel.WARNING, color.yellow("WARNING"))
logging.addLevelName(LoggingLevel.DEBUG, color.blue("DEBUG"))

# 初始化日志
LOGGER = logging.getLogger()
# 设置输出格式
formatter = logging.Formatter(
    "%(asctime)s %(levelname)s %(message)s",
    datefmt="[%Y-%m-%d %H:%M:%S]"
)
LOGGER_HANDLER = logging.StreamHandler(sys.stdout)
LOGGER_HANDLER.setFormatter(formatter)
LOGGER.addHandler(LOGGER_HANDLER)
LOGGER.setLevel(LoggingLevel.INFO)


class MY_LOGGER:
    @staticmethod
    def info(msg: str):
        return LOGGER.log(LoggingLevel.INFO, msg)

    @staticmethod
    def error(msg: str):
        return LOGGER.log(LoggingLevel.ERROR, msg)

    @staticmethod
    def warning(msg: str):
        return LOGGER.log(LoggingLevel.WARNING, msg)

    @staticmethod
    def debug(msg: str):
        return LOGGER.log(LoggingLevel.DEBUG, msg)

    @staticmethod
    def success(msg: str):
        return LOGGER.log(LoggingLevel.SUCCESS, msg)


log = MY_LOGGER()
