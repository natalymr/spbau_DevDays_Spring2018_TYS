from src.account.LoginWidget import LoginWidget
from src.account.RegisterWidget import Register
from PyQt5.QtWidgets import *


class MainWidget(QVBoxLayout):

    def __init__(self, owner):
        super(MainWidget, self).__init__()
        self.owner = owner
        self.widget = None

        button_register = QPushButton('Sign up')
        button_register.clicked.connect(self.handle_register)
        button_login = QPushButton('Log in')
        button_login.clicked.connect(self.handle_login)

        button_layout = QVBoxLayout()
        button_layout.addWidget(button_register)
        button_layout.addWidget(button_login)

        self.addLayout(button_layout)
        self.windowTitle = 'TryYourSkills: Start'

    def hide(self):
        self.widget.hide()
    def show(self):
        self.widget.show()

    def handle_register(self):
        self.hide()
        self.owner.current_widget = Register.create(self.owner.login_server, self.owner, self)

    def handle_login(self):
        self.hide()
        self.owner.current_widget = LoginWidget.create(self.owner.login_server, self.owner, self)

    @staticmethod
    def create(owner):
        main_layout = MainWidget(owner)
        w = QWidget()
        w.setLayout(main_layout)
        main_layout.widget = w
        w.setGeometry(300, 300, 300, 100)
        w.setWindowTitle(main_layout.windowTitle)
        w.show()
        return w
