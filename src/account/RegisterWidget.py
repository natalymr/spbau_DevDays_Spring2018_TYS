from PyQt5.QtWidgets import *


class Register(QVBoxLayout):
    def __init__(self, login_server, main_window, account_layout):
        super(Register, self).__init__()
        self.main_window = main_window
        self.account_layout = account_layout

        login_label = QLabel('login:')
        passwd_label = QLabel('password:')
        name_label = QLabel('name:')
        self.login_server = login_server
        self.textLogin = QLineEdit()
        self.textPasswd = QLineEdit()
        self.textPasswd.setEchoMode(QLineEdit.Password)
        self.textName = QLineEdit()

        label_layout = QVBoxLayout()
        input_layout = QVBoxLayout()
        label_layout.addWidget(login_label)
        input_layout.addWidget(self.textLogin)
        label_layout.addWidget(passwd_label)
        input_layout.addWidget(self.textPasswd)
        label_layout.addWidget(name_label)
        input_layout.addWidget(self.textName)

        form_layout = QHBoxLayout()
        form_layout.addLayout(label_layout)
        form_layout.addLayout(input_layout)

        self.buttonBack = QPushButton('Back')
        self.buttonBack.clicked.connect(self.handle_back)
        self.buttonLogin = QPushButton('Sign up')
        self.buttonLogin.clicked.connect(self.handle_register)
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.buttonBack)
        button_layout.addWidget(self.buttonLogin)

        layout = QVBoxLayout()
        layout.addLayout(form_layout)
        layout.addLayout(button_layout)

        self.addLayout(layout)
        self.windowTitle = 'TryYourSkills: Sign up'

    def handle_back(self):
        self.account_layout.set_start_page()

    def handle_register(self):
        login = self.textLogin.text()
        passwd = self.textPasswd.text()
        name = self.textName.text()
        if 0 == len(login) or 0 == len(passwd) or 0 == len(name):
            QMessageBox.warning(self.main_window, 'Error', 'All fields must be completed')
        elif self.login_server.register(login, passwd, name):
            self.login_server.dump()
            user = self.login_server.login(login, passwd)
            self.account_layout.set_profile(user)
        else:
            QMessageBox.warning(self.main_window, 'Error', 'Login are already exist')

