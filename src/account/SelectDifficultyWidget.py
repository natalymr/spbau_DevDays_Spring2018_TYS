from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *


class SelectDifficultyWidget(QVBoxLayout):
    def __init__(self, main_window):
        super(SelectDifficultyWidget, self).__init__()
        self.main_window = main_window

        label = QLabel('<center> Select your difficulty: <\center>')
        label.setFont(QFont("Times", 14, QFont.Bold))

        easy_button = QPushButton('Easy')
        easy_button.clicked.connect(self.handle_easy)
        mid_button = QPushButton('Median')
        mid_button.clicked.connect(self.handle_mid)
        hard_button = QPushButton('Hard')
        hard_button.clicked.connect(self.handle_hard)

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(easy_button)
        layout.addWidget(mid_button)
        layout.addWidget(hard_button)

        self.addLayout(layout)
        self.windowTitle = 'TryYourSkills: Select your difficulty'

    def handle_easy(self):
        self.main_window.set_interview_window(difficulty=1)

    def handle_mid(self):
        self.main_window.set_interview_window(difficulty=2)

    def handle_hard(self):
        self.main_window.set_interview_window(difficulty=3)

