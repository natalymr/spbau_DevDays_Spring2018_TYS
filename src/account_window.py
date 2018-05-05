from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

from src.account.MainLayout import MainLayout
from src.account.RegisterWidget import Register
from src.account.LoginWidget import LoginWidget
from src.account.ProfileLayout import ProfileLayout


class AccountLayout(QVBoxLayout):

    def __init__(self, main_window):
        super(AccountLayout, self).__init__()
        self.main_window = main_window
        main_box, wrapper_layout = self.create_main_layout()
        self.main_box = main_box
        self.addLayout(wrapper_layout)

        self.current_layout = None

        self.set_start_page()

    def create_main_layout(self):
        main_box = QVBoxLayout()
        vertical_layout = QVBoxLayout()
        vertical_layout.addStretch()
        vertical_layout.addLayout(main_box)
        vertical_layout.addStretch()
        wrapper_layout = QHBoxLayout()
        wrapper_layout.addStretch()
        wrapper_layout.addLayout(vertical_layout)
        wrapper_layout.addStretch()
        return (main_box, wrapper_layout)

    def __pre_set(self):
        if self.current_layout is not None:
            self.main_window.clear_layout(self.main_box)

    def __post_set(self):
        self.main_box.addLayout(self.current_layout)
        self.main_window.setWindowTitle(self.current_layout.windowTitle)

    def __pre_login(self, user):
        if self.main_window.current_user is not None:
            self.main_window.current_user.logout_callback(self.main_window.login_server)
        self.main_window.current_user = user

    def set_start_page(self):
        self.__pre_set()
        self.current_layout = MainLayout(self.main_window, self)
        self.__post_set()

    def set_signup(self):
        self.__pre_set()
        self.current_layout = Register(self.main_window.login_server, self.main_window, self)
        self.__post_set()

    def set_login(self):
        self.__pre_set()
        self.current_layout = LoginWidget(self.main_window.login_server, self.main_window, self)
        self.__post_set()

    def set_profile(self, user):
        self.__pre_set()
        self.__pre_login(user)
        self.current_layout = ProfileLayout(self.main_window.login_server, user, self.main_window, self)
        self.__post_set()

    def set_difficulty(self):
        self.__pre_set()
        self.current_layout = SelectDifficultyWidget(self.main_window, self)