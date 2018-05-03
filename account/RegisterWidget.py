
import sys
from LoginServer import LoginServer, User
from ProfileWidget import Profile
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, \
    QHBoxLayout, QGridLayout


class Register(QWidget):
    def __init__(self, login_server, owner, parent):
        super(Register, self).__init__()
        self.owner = owner
        self.parent = parent

        login_label = QLabel('login:')
        passwd_label = QLabel('passwd:')
        name_label = QLabel('name:')

        self.login_server = login_server

        self.textLogin = QLineEdit()
        self.textPasswd = QLineEdit()
        self.textPasswd.setEchoMode(QLineEdit.Password)
        self.textName = QLineEdit()

        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(login_label, 1, 0)
        grid.addWidget(self.textLogin, 1, 1)
        grid.addWidget(passwd_label, 2, 0)
        grid.addWidget(self.textPasswd, 2, 1)
        grid.addWidget(name_label, 3, 0)
        grid.addWidget(self.textName, 3, 1)

        self.buttonBack = QPushButton('Back', self)
        self.buttonBack.clicked.connect(self.handle_back)
        self.buttonLogin = QPushButton('Login', self)
        self.buttonLogin.clicked.connect(self.handle_register)
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.buttonBack)
        button_layout.addWidget(self.buttonLogin)

        layout = QVBoxLayout()
        layout.addLayout(grid)
        layout.addLayout(button_layout)

        self.setLayout(layout)
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QLineEdit')
        self.show()

    def handle_back(self):
        self.parent.show()
        self.owner.current_widget = self.parent

    def handle_register(self):
        login = self.textLogin.text()
        passwd = self.textPasswd.text()
        name = self.textName.text()
        if 0 == len(login) or 0 == len(passwd) or 0 == len(name):
            QMessageBox.warning(self, 'Error', 'All fields must be completed')
        elif self.login_server.register(login, passwd, name):
            print(self.login_server.users)
            self.login_server.dump()
            print('after', self.login_server.users)
            self.owner.current_widget = Profile(self.login_server.login(login, passwd), self.owner, self.parent)
            self.hide()
        else:
            QMessageBox.warning(self, 'Error', 'login are already exist')


# class WindowDispathcher:
#     def __init__(self, login_server_file_name):
#         self.login_server = LoginServer(login_server_file_name)
#         self.current_widget = Register(self.login_server, self, None)
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     w = WindowDispathcher('LoginServer.pickle')
#     sys.exit(app.exec_())
#