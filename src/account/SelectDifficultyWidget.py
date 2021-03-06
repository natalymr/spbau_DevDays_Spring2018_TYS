from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *


class SelectDifficultyWidget(QVBoxLayout):
    def __init__(self, main_window, account_layout):
        super(SelectDifficultyWidget, self).__init__()
        self.main_window = main_window
        self.account_layout = account_layout

        label = QLabel('<center> Select your difficulty: <\center>')
        label.setFont(QFont("Times", 14, QFont.Bold))

        label_fake = QLabel('<center> ----------------- <\center>')
        label_fake.setFont(QFont("Times", 12))
        label_fake.setFixedSize(225, 10)
        easy_button = QPushButton('Easy')
        easy_button.setFixedSize(225, 25)
        easy_button.clicked.connect(self.handle_easy)
        mid_button = QPushButton('Median')
        mid_button.clicked.connect(self.handle_mid)
        mid_button.setFixedSize(225, 25)
        hard_button = QPushButton('Hard')
        hard_button.clicked.connect(self.handle_hard)
        hard_button.setFixedSize(225, 25)
        back_button = QPushButton('Back')
        back_button.setShortcut('Esc')
        back_button.setFixedSize(back_button.sizeHint())
        back_button.setFixedSize(225, 25)
        back_button.clicked.connect(self.handle_back)

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(easy_button)
        layout.addWidget(mid_button)
        layout.addWidget(hard_button)
        layout.addWidget(label_fake)
        layout.addWidget(back_button)

        self.addLayout(layout)
        self.windowTitle = 'TryYourSkills: Select your difficulty'

    def handle_easy(self):
        self.main_window.set_interview_window(difficulty=1)

    def handle_mid(self):
        self.main_window.set_interview_window(difficulty=2)

    def handle_hard(self):
        self.main_window.set_interview_window(difficulty=3)

    def handle_back(self):
        self.account_layout.set_profile(self.main_window.current_user)

