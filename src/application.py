import sys
from src.window import Window
from PyQt5.QtWidgets import QApplication
from enum import Enum


class TaskType(Enum):
    TEST = 1
    CODING = 2
    YES_NO = 3
    SINGLE_ANSWER = 4


class App:

    def __init__(self):
        self.__app = QApplication(sys.argv)

    def run(self):
        w = Window()
        w.show()
        sys.exit(self.__app.exec_())
