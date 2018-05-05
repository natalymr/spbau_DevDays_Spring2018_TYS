from PyQt5.QtWidgets import *
from src.window import InterviewWindow
from src.account.LoginServer import LoginServer
from src.task_window import WindowTask
from src.code_window import WindowCode
from src.chat_window import WindowChat
from PyQt5.QtCore import Qt
import subprocess
import json


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.init_content()
        self.show()

    def init_content(self):
        self.interview_results = list()
        self.current_window = None
        self.account_window = None
        self.interview_window = InterviewWindow(self, self, 1)
        self.statistic_window = None
        self.setWindowTitle('TryYourSkills')
        self.setGeometry(0, 0,
                         QDesktopWidget().availableGeometry().width(),
                         QDesktopWidget().availableGeometry().height())
        self.set_interview_window()

    def accept_result(self, result):
        self.interview_results.append((self.current_task, result))

    def get_results(self):
        return self.interview_results

    def set_interview_window(self):
        if self.current_window:
            self.current_window.setParent(None)
        self.current_window = self.interview_window
        self.current_window.setParent(self)
        self.setCentralWidget(self.current_window)

    def set_statistics_window(self):
        if self.current_window:
            self.current_window.setParent(None)
        self.current_window = self.interview_window
        self.current_window.setParent(self)
        self.setCentralWidget(self.current_window)