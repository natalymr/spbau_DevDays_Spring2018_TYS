import sys
from src.account.MainWidget import MainWidget
from src.account.LoginServer import LoginServer
from PyQt5.QtWidgets import QApplication
from src.window import Window

class App:
    def __init__(self):
        self.login_server = LoginServer('LoginServer.pickle')
        self.current_widget = None
        self.__app = QApplication(sys.argv)
        self.asked_tasks = dict()
        self.chat_tasks = dict()

    def run(self):
        self.current_widget = MainWidget(self)
        # self.current_widget = Window(None, self)
        sys.exit(self.__app.exec_())
