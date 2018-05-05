#!/usr/bin/python3
# -*- coding: utf-8 -*-

from src.account.ProfileWidget import ProfileWidget
from PyQt5.QtWidgets import *


class LoginWidget(QWidget):

    def __init__(self, login_server, owner, parent):
        super(LoginWidget, self).__init__()
        self.owner = owner
        self.parent = parent
        self.login_server = login_server

        login_label = QLabel('login:')
        passwd_label = QLabel('password:')

        self.login_server = login_server

        self.textLogin = QLineEdit()
        self.textPasswd = QLineEdit()
        self.textPasswd.setEchoMode(QLineEdit.Password)

        label_layout = QVBoxLayout()
        input_layout = QVBoxLayout()
        label_layout.addWidget(login_label)
        input_layout.addWidget(self.textLogin)
        label_layout.addWidget(passwd_label)
        input_layout.addWidget(self.textPasswd)

        form_layout = QHBoxLayout()
        form_layout.addLayout(label_layout)
        form_layout.addLayout(input_layout)

        self.buttonBack = QPushButton('Back', self)
        self.buttonBack.clicked.connect(self.handle_back)
        self.buttonLogin = QPushButton('Log in', self)
        self.buttonLogin.clicked.connect(self.handle_login)
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.buttonBack)
        button_layout.addWidget(self.buttonLogin)

        layout = QVBoxLayout()
        layout.addLayout(form_layout)
        layout.addLayout(button_layout)

        self.setLayout(layout)
        self.setGeometry(0, 0,
                         QDesktopWidget().availableGeometry().width(),
                         QDesktopWidget().availableGeometry().height())
        self.setWindowTitle('TryYourSkills: Log in')
        self.show()

    def handle_back(self):
        self.owner.current_widget = self.parent
        self.parent.show()

    def handle_login(self):
        user = self.login_server.login(self.textLogin.text(), self.textPasswd.text())
        if user is not None:
            self.owner.current_widget = ProfileWidget(self.login_server, user, self.owner, self.parent)
        else:
            self.textPasswd.setText('')
            QMessageBox.warning(self, 'Error', 'Bad user or password')
