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
        passwd_label = QLabel('passwd:')

        self.login_server = login_server

        self.textLogin = QLineEdit()
        self.textPasswd = QLineEdit()
        self.textPasswd.setEchoMode(QLineEdit.Password)

        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(login_label, 1, 0)
        grid.addWidget(self.textLogin, 1, 1)
        grid.addWidget(passwd_label, 2, 0)
        grid.addWidget(self.textPasswd, 2, 1)

        self.buttonBack = QPushButton('Back', self)
        self.buttonBack.clicked.connect(self.handle_back)
        self.buttonLogin = QPushButton('Login', self)
        self.buttonLogin.clicked.connect(self.handle_login)
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
        self.owner.current_widget = self.parent
        self.parent.show()

    def handle_login(self):
        user = self.login_server.login(self.textLogin.text(), self.textPasswd.text())
        if user is not None:
            self.owner.current_widget = ProfileWidget(user, self.owner, self.parent)
        else:
            self.textPasswd.setText("")
            QMessageBox.warning(self, 'Error', 'Bad user or password')

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', "Are you sure to quit?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
