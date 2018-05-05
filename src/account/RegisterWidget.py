from src.account.ProfileWidget import ProfileWidget
from PyQt5.QtWidgets import *


class Register(QVBoxLayout):
    def __init__(self, login_server, owner, parent):
        super(Register, self).__init__()
        self.owner = owner
        self.parent = parent
        self.widget = None

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

    def hide(self):
        self.widget.hide()
    def show(self):
        self.widget.show()

    def handle_back(self):
        self.parent.show()
        self.owner.current_widget = self.parent
        self.widget.close()

    def handle_register(self):
        login = self.textLogin.text()
        passwd = self.textPasswd.text()
        name = self.textName.text()
        if 0 == len(login) or 0 == len(passwd) or 0 == len(name):
            QMessageBox.warning(self.widget, 'Error', 'All fields must be completed')
        elif self.login_server.register(login, passwd, name):
            self.login_server.dump()
            user = self.login_server.login(login, passwd)
            self.owner.current_widget = ProfileWidget.create(self.login_server, user, self.owner)
            self.hide()
        else:
            QMessageBox.warning(self.widget, 'Error', 'Login are already exist')

    # def closeEvent(self, event):
    #     reply = QMessageBox.question(self, 'Quit', 'Are you sure to quit?',
    #                                  QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
    #     if reply == QMessageBox.Yes:
    #         event.accept()
    #     else:
    #         event.ignore()

    @staticmethod
    def create(login_server, owner, parent):
        register_layout = Register(login_server, owner, parent)
        w = QWidget()
        w.setLayout(register_layout)
        register_layout.widget = w
        w.setGeometry(300, 300, 280, 170)
        w.setWindowTitle(register_layout.windowTitle)
        w.show()
        return w
