#!/usr/bin/python3
# -*- coding: utf-8 -*-

from src.account.ProfileLayout import ProfileLayout
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QKeySequence, QKeyEvent

class LoginWidget(QVBoxLayout):
    def __init__(self, main_window, account_layout):
        super(LoginWidget, self).__init__()
        self.main_window = main_window
        self.account_layout = account_layout
        self.login_server = main_window.login_server

        login_label = QLabel('login:')
        passwd_label = QLabel('password:')

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

        self.buttonBack = QPushButton('Back')
        self.buttonBack.setFixedSize(225, 25)
        self.buttonBack.clicked.connect(self.handle_back)
        self.buttonLogin = QPushButton('Log in')
        self.buttonLogin.setShortcut(QKeySequence.InsertLineSeparator)
        self.buttonLogin.setFixedSize(225, 25)
        self.buttonLogin.clicked.connect(self.handle_login)
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.buttonBack)
        button_layout.addWidget(self.buttonLogin)

        layout = QVBoxLayout()
        layout.addLayout(form_layout)
        layout.addLayout(button_layout)

        self.addLayout(layout)
        self.windowTitle = 'TryYourSkills: Log in'

    def handle_back(self):
        self.account_layout.set_start_page()

    def handle_login(self):
        user = self.login_server.login(self.textLogin.text(), self.textPasswd.text())
        if user is not None:
            self.account_layout.set_profile(user)
        else:
            self.textPasswd.setText('')
            QMessageBox.warning(self.main_window, 'Error', 'Bad user or password')