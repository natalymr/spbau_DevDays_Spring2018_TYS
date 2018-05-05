from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from src.task_window import WindowTask
from src.code_window import WindowCode
from src.chat_window import WindowChat
from src.task import ChatTask
import json
import random
from src.utils import CHAT_TASKS


class Window(QWidget):

    def __init__(self, owner, parent, difficulty=3):
        super(Window, self).__init__()
        self.owner = owner
        self.parent = parent
        self.difficulty = difficulty
        self.initUI()
        self.asked_tasks = dict()
        self.chat_tasks = dict()
        self.current_answers = dict()
        self.load_chat_tasks()
        self.show()

    def initUI(self):
        self.setWindowTitle('TryYourSkills')
        self.setGeometry(0, 0,
                         QDesktopWidget().availableGeometry().width(),
                         QDesktopWidget().availableGeometry().height())
        self.set_windows()

    def set_windows(self):
        hbox = QHBoxLayout(self)
        self.task_window = WindowTask(self)
        self.chat_window = WindowChat(self, difficulty=self.difficulty)
        self.code_window = WindowCode(self)

        splitter1 = QSplitter(Qt.Vertical)
        splitter1.addWidget(self.task_window)
        splitter1.addWidget(self.code_window)
        splitter1.setSizes([self.width() // 3,
                            self.width() * 2 // 3])
        splitter2 = QSplitter(Qt.Horizontal)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(self.chat_window)
        splitter2.setSizes([self.height() * 3 // 4,
                            self.height() // 4])
        hbox.addWidget(splitter2)
        self.setLayout(hbox)

    def closeEvent(self, event):
        self.handle_back(can_close=False)
        event.accept()

    def handle_back(self, can_close=True):
        self.task_window.close()
        self.chat_window.close()
        self.code_window.close()
        if self.owner != None:
            self.owner.current_widget = self.parent
            self.parent.show()
        if can_close:
            self.close()
        else:
            self.hide()

    def load_chat_tasks(self):
        for difficulty, file in CHAT_TASKS.items():
            with open(file) as json_file:
                self.asked_tasks[difficulty] = dict()
                self.chat_tasks[difficulty] = dict()
                jsons = json.load(json_file)
                for j in jsons:
                    i = j['id']
                    self.chat_tasks[difficulty].update({i: ChatTask(j, difficulty)})

    def run_chat_task(self, difficulty):
        current_task = random.choice(self.chat_tasks[difficulty].items())
        del self.chat_tasks[difficulty][current_task.id]
        result = self.chat_window.run_task(current_task)