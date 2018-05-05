from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from src.task import *
from src.chat_box import ChatBox
import time
from src.utils import *


class WindowChat(QSplitter):

    def __init__(self, window, difficulty):
        self.difficulty = difficulty
        self.parent = window
        super(WindowChat, self).__init__(Qt.Vertical)
        self.__create_interviewer_box()
        self.chat_box = ChatBox(self)
        self.addWidget(self.info_window)
        self.addWidget(self.chat_box)
        self.setSizes([self.width() * 3 // 10,
                       self.width() * 7 // 10])
        self.setFixedWidth(self.parent.width() * 1 // 4)

    @staticmethod
    def set_style(window):
        window.setFrameShape(QFrame.StyledPanel)
        window.setLineWidth(2)
        window.setFrameShape(QFrame.Box)
        window.setFrameShadow(QFrame.Plain)

    @pyqtSlot()
    def change_difficulty(self):
        pass

    def getInteger(self):
        i, okPressed = QInputDialog.getInt\
            (self, 'Difficulty', 'level', 28, 0, 100, 1)
        if okPressed:
            print(i)

    def run_task(self, task):
        if task.type == TaskType.TEST:
            self.chat_box.test_question(task)
        if task.type == TaskType.YES_NO:
            self.chat_box.yes_no_question(task)
        if task.type == TaskType.SINGLE_ANSWER:
            self.chat_box.single_question(task)

    def set_answer(self, task, answer):
        self.parent.current_answers.add((task, answer))

    def __create_interviewer_box(self):
        self.info_window = QFrame(self)
        self.info_window.setFrameShape(QFrame.StyledPanel)
        self.set_style(self.info_window)
        self.info_window.setFixedWidth(self.width() * 3 // 5)
        # self.info_window.setFixedWidth(self.)
        splitter1 = QSplitter(Qt.Vertical)

        hbox = QHBoxLayout(self.info_window)
        button = QPushButton('Back', splitter1)
        button.clicked.connect(self.parent.handle_back)
        button.setFixedSize(100, 40)

        label_difficulty = QLabel(splitter1)
        label_difficulty.setText('Difficulty: {}'.format(self.difficulty))
        label_difficulty.setFont(QFont("Times", 12, QFont.Bold))
        splitter1.addWidget(button)
        splitter1.addWidget(label_difficulty)
        lab = QLabel()
        pixmap = QPixmap(INTERVIEWER.format(self.difficulty))
        lab.setPixmap(pixmap)
        hbox.addWidget(splitter1)
        hbox.addWidget(lab)
        self.info_window.setLayout(hbox)

    def update_info_window(self):
        self.set_style(self.info_window)