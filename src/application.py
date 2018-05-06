import sys
from PyQt5.QtGui import QIcon
from src.account.LoginServer import LoginServer
from PyQt5.QtWidgets import QApplication, QLabel

from src.main_window import MainWindow


class App:

    def __init__(self):
        self.__app = QApplication(sys.argv)
        self.asked_tasks = dict()
        self.chat_tasks = dict()
        self.__app.setWindowIcon(QIcon('src/images/main.jpg'))

    def run(self):
        self.current_widget = MainWindow()
        sys.exit(self.__app.exec_())
