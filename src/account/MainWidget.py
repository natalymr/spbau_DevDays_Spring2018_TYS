from src.account.LoginWidget import LoginWidget
from src.account.RegisterWidget import Register
from PyQt5.QtWidgets import *


class MainWidget(QWidget):

    def __init__(self, owner):
        super(MainWidget, self).__init__()
        self.owner = owner

        self.button_register = QPushButton('Sign up', self)
        self.button_register.clicked.connect(self.handle_register)
        self.button_login = QPushButton('Log in', self)
        self.button_login.clicked.connect(self.handle_login)

        button_layout = QVBoxLayout()
        button_layout.addWidget(self.button_register)
        button_layout.addWidget(self.button_login)

        self.setLayout(button_layout)
        self.setGeometry(300, 300, 300, 100)
        self.setWindowTitle('TryYourSkills: Start')
        self.show()

    def handle_register(self):
        self.hide()
        self.owner.current_widget = Register(self.owner.login_server, self.owner, None)

    def handle_login(self):
        self.hide()
        self.owner.current_widget = LoginWidget(self.owner.login_server, self.owner, None)

