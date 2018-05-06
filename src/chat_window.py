from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from src.task import *
from src.chat_box import ChatBox
from src.utils import *


class WindowChat(QSplitter):

    def __init__(self, window, main_window, difficulty):
        self.main_window = main_window
        self.difficulty = difficulty
        self.parent_window = window
        super(WindowChat, self).__init__(Qt.Vertical)
        self.__create_interviewer_box()
        self.chat_box = ChatBox(self)
        self.addWidget(self.info_window)
        self.addWidget(self.chat_box)
        self.setSizes([self.width() * 3 // 10,
                       self.width() * 7 // 10])
        self.setFixedWidth(self.main_window.width() * 1 // 4)

    def run_tasks(self, tasks, start, cont):
        self.chat_box.run_tasks(tasks, start, cont)

    def accept_result(self, task, answer):
        self.main_window.accept_result((task, answer))

    def __create_interviewer_box(self):
        self.info_window = QFrame(self)
        self.info_window.setFrameShape(QFrame.StyledPanel)
        set_style(self.info_window)
        splitter1 = QSplitter(Qt.Horizontal)

        hbox = QHBoxLayout(self.info_window)
        self.__holder = QSplitter(Qt.Vertical)
        self.__logo_temp = QFrame(self)
        self.__button_holder = QSplitter(Qt.Vertical)
        button = QPushButton('Back', self.__button_holder)
        button.clicked.connect(self.parent_window.handle_finish)
        self.__holder.addWidget(self.__logo_temp)
        self.__holder.addWidget(self.__button_holder)
        self.__holder.setHandleWidth(0)
        self.__holder.setSizes([300, 10])

        label_difficulty = QLabel(splitter1)
        label_difficulty.setText('Difficulty: {}'.format(self.difficulty))
        label_difficulty.setFont(QFont('Times', 14, QFont.Bold))

        lab = QLabel()
        pixmap = QPixmap(INTERVIEWER.format(self.difficulty))
        lab.setPixmap(pixmap)

        splitter1.addWidget(label_difficulty)
        splitter1.addWidget(lab)

        hbox.addWidget(splitter1)
        hbox.addWidget(self.__holder)
        self.info_window.setLayout(hbox)
