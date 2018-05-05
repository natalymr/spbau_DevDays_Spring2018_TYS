from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
from src.window import Window


class SelectDifficultyWidget(QVBoxLayout):
    def __init__(self, owner, parent):
        super(SelectDifficultyWidget, self).__init__()
        self.parent = parent
        self.owner = owner
        self.widget = None

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
        self.windowTitle = 'TryYourSkills'

    def hide(self):
        self.widget.hide()
    def show(self):
        self.widget.show()

    def handle_easy(self):
        self.hide()
        self.owner.current_widget = Window(self.owner, self.parent, difficulty=1)

    def handle_mid(self):
        self.hide()
        self.owner.current_widget = Window(self.owner, self.parent, difficulty=2)

    def handle_hard(self):
        self.hide()
        self.owner.current_widget = Window(self.owner, self.parent, difficulty=3)

    @staticmethod
    def create(owner, parent):
        selectLayout = SelectDifficultyWidget(owner, parent)
        w = QWidget()
        w.setLayout(selectLayout)
        selectLayout.widget = w
        w.setGeometry(300, 300, 300, 100)
        w.setWindowTitle(selectLayout.windowTitle)
        w.show()
        return w
