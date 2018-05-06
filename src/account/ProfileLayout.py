from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont


class ProfileLayout(QVBoxLayout):
    def __init__(self, user, main_window, account_layout):
        super(ProfileLayout, self).__init__()
        self.main_window = main_window
        self.login_server = main_window.login_server
        self.user = user
        self.account_layout = account_layout

        ql_login = QLabel('<center>login:  %s<\center>' % user.login)
        ql_name = QLabel('<center>name:   %s<\center>' % user.name)
        start_button = QPushButton('Start')
        start_button.clicked.connect(self.handle_start)
        start_button.setFont(QFont('Times', 12, QFont.Bold))
        log_out_button = QPushButton('Log out')
        log_out_button.clicked.connect(self.handle_logout)

        statistic_button = QPushButton('Statistic')
        statistic_button.clicked.connect(self.handle_statistic)

        layout = QVBoxLayout()
        layout.addWidget(ql_login)
        layout.addWidget(ql_name)
        layout.addWidget(start_button)
        layout.addWidget(statistic_button)
        layout.addWidget(log_out_button)

        self.addLayout(layout)
        self.windowTitle = 'TryYourSkills: Profile'

    def handle_start(self):
        self.account_layout.set_difficulty()

    def handle_statistic(self):
        self.main_window.set_statistics_window()

    def handle_logout(self):
        self.main_window.current_user.logout_callback(self.main_window.login_server)
        self.main_window.current_user = None
        self.main_window.set_account_window()
