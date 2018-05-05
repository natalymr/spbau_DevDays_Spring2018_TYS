import sys
from src.account.LoginServer import LoginServer
from PyQt5.QtWidgets import QApplication

from src.main_window import MainWindow


class App:

    def __init__(self):
        self.__app = QApplication(sys.argv)
        self.asked_tasks = dict()
        self.chat_tasks = dict()

    def run(self):
        self.current_widget = MainWindow()
        sys.exit(self.__app.exec_())
