from PyQt5.QtWidgets import *
from src.window import Window


class ProfileWidget(QWidget):
    def __init__(self, user, owner, parent):
        super(ProfileWidget, self).__init__()
        self.parent = parent
        self.owner = owner
        self.user = user

        ql_login = QLabel('<center>login:  %s<\center>' % user.login, self)
        ql_name = QLabel('<center>name:   %s<\center>' % user.name, self)
        self.start_button = QPushButton('Start', self)
        self.start_button.clicked.connect(self.handle_start)

        layout = QVBoxLayout()
        layout.addWidget(ql_login)
        layout.addWidget(ql_name)
        layout.addWidget(self.start_button)

        self.setLayout(layout)
        self.setGeometry(300, 300, 300, 100)
        self.setWindowTitle('TryYourSkills: Profile')
        self.show()

    def closeEvent(self, event):
        self.user.logout_callback()
        self.parent.show()
        self.owner.current_widget = self.parent
        event.accept()

    def handle_start(self):
        self.hide()
        self.owner.current_widget = Window(self.owner, self)
