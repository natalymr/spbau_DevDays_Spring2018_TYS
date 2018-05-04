import sys

from PyQt5.QtGui import QIcon

from src.account.LoginServer import LoginServer
from src.account.LoginWidget import LoginWidget
from src.account.RegisterWidget import Register
from PyQt5.QtWidgets import *


class MainWidget(QWidget):
    def __init__(self, owner):
        super(MainWidget, self).__init__()
        self.owner = owner

        self.button_register = QPushButton('Register', self)
        self.button_register.clicked.connect(self.handle_register)
        self.button_register.setMaximumSize(100, 80)
        self.button_login = QPushButton('Login', self)
        self.button_login.clicked.connect(self.handle_login)
        self.button_login.setMaximumSize(100, 80)
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.button_register)
        button_layout.addWidget(self.button_login)

        self.setLayout(button_layout)
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QMainWidget')
        self.setWindowIcon(QIcon('web.jpg'))
        self.show()

    def handle_register(self):
        self.hide()
        self.owner.current_widget = Register(self.owner.login_server, self.owner, self)

    def handle_login(self):
        self.hide()
        self.owner.current_widget = LoginWidget(self.owner.login_server, self.owner, self)

