from PyQt5.QtWidgets import *
from src.window import Window
from src.account.StatisticWindow import StatisticWindow
from src.account.SelectDifficultyWidget import SelectDifficultyWidget
from copy import deepcopy


class ProfileWidget(QVBoxLayout):
    def __init__(self, login_server, user, owner):
        super(ProfileWidget, self).__init__()
        self.widget = None  # parent
        self.owner = owner
        self.user = user
        self.login_server = login_server
        self.stat = None

        ql_login = QLabel('<center>login:  %s<\center>' % user.login)
        ql_name = QLabel('<center>name:   %s<\center>' % user.name)
        self.start_button = QPushButton('Start')
        self.start_button.clicked.connect(self.handle_start)

        self.statistic_button = QPushButton('Statistic')
        self.statistic_button.clicked.connect(self.handle_statistic)

        layout = QVBoxLayout()
        layout.addWidget(ql_login)
        layout.addWidget(ql_name)
        layout.addWidget(self.start_button)
        layout.addWidget(self.statistic_button)

        self.addLayout(layout)
        self.windowTitle = 'TryYourSkills: Profile'

    # def closeEvent(self, event):
    #     reply = QMessageBox.question(self, 'Quit', 'Are you sure to quit?',
    #                                  QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
    #     if reply == QMessageBox.Yes:
    #         self.user.logout_callback(self.login_server)
    #         # if self.parent is not None:
    #         #     self.parent.show()
    #         #     self.owner.current_widget = self.parent
    #         event.accept()
    #     else:
    #         event.ignore()

    def hide(self):
        self.widget.hide()

    def show(self):
        self.widget.show()

    def handle_start(self):
        self.hide()
        self.owner.current_widget = SelectDifficultyWidget.create(self.owner, self)

    def handle_statistic(self):
        stat = StatisticWindow(self.user)
        self.stat = QWidget()
        self.stat.setLayout(stat)
        self.stat.setWindowTitle(stat.windowTitle)
        self.stat.show()

    def handle_finish(self):
        task_list = deepcopy(self.owner.current_widget.current_answers)
        self.user.end_interview_callback(task_list)

    @staticmethod
    def create(login_server, user, owner):
        profile = ProfileWidget(login_server, user, owner)
        w = QWidget()
        w.setLayout(profile)
        profile.widget = w
        w.setGeometry(300, 300, 300, 100)
        w.setWindowTitle(profile.windowTitle)
        w.show()
        return w
