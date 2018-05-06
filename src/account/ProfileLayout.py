from PyQt5.QtWidgets import *
from src.account.StatisticWindow import StatisticWindow
from src.account.SelectDifficultyWidget import SelectDifficultyWidget


class ProfileLayout(QVBoxLayout):
    def __init__(self, login_server, user, main_window, account_layout):
        super(ProfileLayout, self).__init__()
        self.login_server = login_server
        self.user = user
        self.main_window = main_window
        self.account_layout = account_layout

        ql_login = QLabel('<center>login:  %s<\center>' % user.login)
        ql_name = QLabel('<center>name:   %s<\center>' % user.name)
        start_button = QPushButton('Start')
        start_button.clicked.connect(self.handle_start)

        statistic_button = QPushButton('Statistic')
        statistic_button.clicked.connect(self.handle_statistic)

        layout = QVBoxLayout()
        layout.addWidget(ql_login)
        layout.addWidget(ql_name)
        layout.addWidget(start_button)
        layout.addWidget(statistic_button)

        self.addLayout(layout)
        self.windowTitle = 'TryYourSkills: Profile'

    def handle_start(self):
        self.account_layout.set_difficulty()

    def handle_statistic(self):
        self.main_window.set_statistics_window()

