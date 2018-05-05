import sys
from src.account.LoginServer import LoginServer
from PyQt5.QtWidgets import QApplication
from src.main_window import MainWindow


class App:

    def __init__(self):
        self.login_server = LoginServer('LoginServer.pickle')
        self.__app = QApplication(sys.argv)
        self.asked_tasks = dict()
        self.chat_tasks = dict()

    def run(self):
        self.main_window = MainWindow()
        sys.exit(self.__app.exec_())