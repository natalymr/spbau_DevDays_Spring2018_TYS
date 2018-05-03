import sys
from src.window import Window
from PyQt5.QtWidgets import QApplication


class App:

    def __init__(self):
        self.__app = QApplication(sys.argv)

    def run(self):
        w = Window()
        w.show()
        sys.exit(self.__app.exec_())
