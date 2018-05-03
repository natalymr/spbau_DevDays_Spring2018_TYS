
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout

class Profile(QWidget):
    def __init__(self, user, owner, parent):
        super(Profile, self).__init__()
        self.parent = parent
        self.owner = owner
        self.user = user
        ql_login = QLabel('login:  %s' % user.login, self)
        ql_name = QLabel('name:   %s' % user.name, self)
        layout = QVBoxLayout(self)
        layout.addWidget(ql_login)
        layout.addWidget(ql_name)
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Profile')
        self.show()

    def closeEvent(self, event):
        self.parent.show()
        event.accept()
