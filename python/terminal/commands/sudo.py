from main import PREFIX, PREFIX_COLOR
from termcolor import colored as col
import platform

class commands():
    def su():
        global PREFIX, PREFIX_COLOR
        PREFIX = col(f'root@{str()}')

