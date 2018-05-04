import sys
from src.window import Window
from PyQt5.QtWidgets import QApplication
from enum import Enum


class Difficulties(Enum):
    EASY = 1
    MEDIUM = 2
    HARD = 3


class App:

    def __init__(self):
        self.__app = QApplication(sys.argv)

    def run(self):
        w = Window()
        w.show()
        sys.exit(self.__app.exec_())
