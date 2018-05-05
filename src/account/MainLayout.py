from PyQt5.QtWidgets import *


class MainLayout(QVBoxLayout):

    def __init__(self, main_window, account_layout):
        super(MainLayout, self).__init__()
        self.main_window = main_window
        self.account_layout = account_layout

        button_register = QPushButton('Sign up')
        button_register.clicked.connect(self.handle_register)
        button_login = QPushButton('Log in')
        button_login.clicked.connect(self.handle_login)

        button_layout = QVBoxLayout()
        button_layout.addWidget(button_register)
        button_layout.addWidget(button_login)

        self.addLayout(button_layout)
        self.windowTitle = 'TryYourSkills: Start'

    def handle_register(self):
        self.account_layout.set_signup()

    def handle_login(self):
        self.account_layout.set_login()
