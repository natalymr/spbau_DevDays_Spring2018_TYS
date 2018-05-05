from PyQt5.QtWidgets import *

from src.account_window import AccountLayout
from src.window import InterviewWindow
from src.account.LoginServer import LoginServer
from src.account.StatisticWindow import StatisticWindow


class MainWindow(QWidget):

    @staticmethod
    def clear_layout(layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    MainWindow.clear_layout(item.layout())

    def __init__(self):
        super(MainWindow, self).__init__()
        self.current_user = None
        self.current_layout = None
        self.login_server = LoginServer('LoginServer.pickle')

        self.setWindowTitle('TryYourSkills')
        self.interview_results = list()
        # self.account_layout = AccountLayout(self)
        # self.interview_window =

        self.setGeometry(0, 0,
                         QDesktopWidget().availableGeometry().width(),
                         QDesktopWidget().availableGeometry().height())

        self.set_account_window()
        self.show()

    def accept_result(self, result):
        self.interview_results.append((self.current_task, result))

    def get_results(self):
        return self.interview_results

    def set_interview_window(self):
        self.__pre_set()
        self.current_layout = InterviewWindow(self, self, 1)
        self.__post_set()

    def set_statistics_window(self):
        self.__pre_set()
        self.current_layout = StatisticWindow(self.current_user)
        self.__post_set()

    def set_account_window(self):
        self.__pre_set()
        self.current_layout = AccountLayout(self)
        self.__post_set()

    def __pre_set(self):
        if self.current_layout is not None:
            self.clear_layout(self.current_layout)
            self.current_layout.setParent(None)

    def __post_set(self):
        self.setLayout(self.current_layout)
