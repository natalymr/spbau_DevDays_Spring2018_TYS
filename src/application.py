import sys
from src.account.MainWidget import MainWidget
from src.account.LoginServer import LoginServer
from src.window import Window
from PyQt5.QtWidgets import QApplication
from enum import Enum


class Difficulties(Enum):
    EASY = 1
    MEDIUM = 2
    HARD = 3


class App:
    def __init__(self):
        self.login_server = LoginServer('LoginServer.pickle')
        self.current_widget = None
        self.__app = QApplication(sys.argv)

    def run(self):
        self.current_widget = MainWidget(self)
        sys.exit(self.__app.exec_())
