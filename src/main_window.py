from PyQt5.QtWidgets import *

from src.window import InterviewWindow
from src.account_window import AccountLayout
from src.account.LoginServer import LoginServer
from src.account.StatisticWindow import StatisticWindow


class MainWindow(QWidget):

    @staticmethod
    def clear_layout(layout):
        i = 0
        if layout is not None:
            while i < layout.count():
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

        self.setGeometry(0, 0,
                         QDesktopWidget().availableGeometry().width() // 2,
                         QDesktopWidget().availableGeometry().height() // 2)

        self.set_account_window()
        self.show()

    def accept_result(self, result):
        self.interview_results.append((self.current_task, result))

    def get_results(self):
        return self.interview_results

    def set_interview_window(self, difficulty):
        self.__pre_set()
        self.current_layout = InterviewWindow(self, self.current_user, difficulty=difficulty)
        self.__post_set()

    def set_statistics_window(self):
        self.__pre_set()
        self.current_layout = StatisticWindow(self.current_user, self)
        self.__post_set()

    def set_account_window(self):
        self.__pre_set()
        self.current_layout = AccountLayout(self)
        self.__post_set()
        if self.current_user is not None:
            self.current_layout.set_profile(self.current_user)

    def __pre_set(self):
        if self.current_layout is not None:
            self.clear_layout(self.layout())

    def __post_set(self):
        if self.layout() is None:
            self.setLayout(self.current_layout)
        else:
            self.layout().addLayout(self.current_layout)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Quit', 'Are you sure to quit?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            if self.current_user is not None:
                self.current_user.logout_callback(self.login_server)
            event.accept()
        else:
            event.ignore()
