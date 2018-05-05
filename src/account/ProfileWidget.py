from PyQt5.QtWidgets import *
from src.window import Window
from src.account.StatisticWindow import StatisticWindow
from src.account.SelectDifficultyWidget import SelectDifficultyWidget


class ProfileWidget(QWidget):
    def __init__(self, login_server, user, owner, parent):
        super(ProfileWidget, self).__init__()
        self.parent = parent
        self.owner = owner
        self.user = user
        self.login_server = login_server
        self.stat = None

        ql_login = QLabel('<center>login:  %s<\center>' % user.login, self)
        ql_name = QLabel('<center>name:   %s<\center>' % user.name, self)
        self.start_button = QPushButton('Start', self)
        self.start_button.clicked.connect(self.handle_start)

        self.statistic_button = QPushButton('Statistic', self)
        self.statistic_button.clicked.connect(self.handle_statistic)

        layout = QVBoxLayout()
        layout.addWidget(ql_login)
        layout.addWidget(ql_name)
        layout.addWidget(self.start_button)
        layout.addWidget(self.statistic_button)

        self.setLayout(layout)
        self.setGeometry(0, 0,
                         QDesktopWidget().availableGeometry().width(),
                         QDesktopWidget().availableGeometry().height())
        self.setWindowTitle('TryYourSkills: Profile')
        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Quit', 'Are you sure to quit?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            self.user.logout_callback(self.login_server)
            if self.parent is not None:
                self.parent.show()
                self.owner.current_widget = self.parent
            event.accept()
        else:
            event.ignore()

    def handle_start(self):
        # self.hide()
        self.close()
        self.owner.current_widget = SelectDifficultyWidget(self.owner, self)

    def handle_statistic(self):
        self.stat = StatisticWindow(self.user)
        self.stat.show()
