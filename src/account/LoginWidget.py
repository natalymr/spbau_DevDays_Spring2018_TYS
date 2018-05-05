#!/usr/bin/python3
# -*- coding: utf-8 -*-

from src.account.ProfileWidget import ProfileWidget
from PyQt5.QtWidgets import *


class LoginWidget(QVBoxLayout):
    def __init__(self, login_server, owner, parent):
        super(LoginWidget, self).__init__()
        self.owner = owner
        self.parent = parent
        self.login_server = login_server
        self.widget = None

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

        self.buttonBack = QPushButton('Back')
        self.buttonBack.clicked.connect(self.handle_back)
        self.buttonLogin = QPushButton('Log in')
        self.buttonLogin.clicked.connect(self.handle_login)
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.buttonBack)
        button_layout.addWidget(self.buttonLogin)

        layout = QVBoxLayout()
        layout.addLayout(form_layout)
        layout.addLayout(button_layout)

        self.addLayout(layout)
        self.windowTitle = 'TryYourSkills: Log in'

    def hide(self):
        self.widget.hide()
    def show(self):
        self.widget.show()

    def handle_back(self):
        self.owner.current_widget = self.parent
        self.parent.show()
        self.widget.close()

    def handle_login(self):
        user = self.login_server.login(self.textLogin.text(), self.textPasswd.text())
        if user is not None:
            self.owner.current_widget = ProfileWidget.create(self.login_server, user, self.owner)
        else:
            self.textPasswd.setText('')
            QMessageBox.warning(self.widget, 'Error', 'Bad user or password')

    # def closeEvent(self, event):
    #     reply = QMessageBox.question(self, 'Quit', 'Are you sure to quit?',
    #                                  QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
    #     if reply == QMessageBox.Yes:
    #         event.accept()
    #     else:
    #         event.ignore()

    @staticmethod
    def create(login_server, owner, parent):
        login_layout = LoginWidget(login_server, owner, parent)
        w = QWidget()
        w.setLayout(login_layout)
        login_layout.widget = w
        w.setGeometry(300, 300, 280, 150)
        w.setWindowTitle(login_layout.windowTitle)
        w.show()
        return w
