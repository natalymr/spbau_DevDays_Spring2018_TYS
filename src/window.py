from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from src.task_window import WindowTask
from src.code_window import WindowCode
from src.chat_window import WindowChat
from src.task import ChatTask
import json
import random
from src.utils import *
from copy import deepcopy


class InterviewWindow(QVBoxLayout):

    def __init__(self, main_window, user, difficulty=1):
        super(InterviewWindow, self).__init__()
        self.main_window = main_window
        self.user = user
        self.alive = True
        self.difficulty = difficulty
        self.windowTitle = 'TryYourSkills: Interview'
        self.set_windows()
        self.load_chat_tasks()

    def set_windows(self):
        hbox = QHBoxLayout()
        self.task_window = WindowTask(self)
        self.chat_window = WindowChat(self, self.main_window,
                                      difficulty=self.difficulty)
        self.code_window = WindowCode(self)

        splitter1 = QSplitter(Qt.Vertical)
        splitter1.addWidget(self.task_window)
        splitter1.addWidget(self.code_window)
        splitter1.setSizes([self.main_window.width() * 2 // 5,
                            self.main_window.width() * 3 // 5])
        splitter2 = QSplitter(Qt.Horizontal)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(self.chat_window)
        splitter2.setSizes([self.main_window.height() * 3 // 4,
                            self.main_window.height() // 4])
        hbox.addWidget(splitter2)
        self.insertWidget(0, splitter2)

    def handle_back(self):
        self.task_window.close()
        self.chat_window.close()
        self.code_window.close()
        self.main_window.set_account_window()

    def load_chat_tasks(self):
        with open(CHAT_TASKS) as json_file:
            self.chat_tasks = dict()
            self.current_answers = list()
            jsons = json.load(json_file)
            for j in jsons:
                i = j['id']
                difficulty = j['difficulty']
                self.chat_tasks.update({i: ChatTask(j, difficulty)})

    def run_chat_task(self, count=3, start=False, cont=False):
        if len(self.chat_tasks):
            tasks = list()
            for i in range(count):
                id, task = random.choice(list(self.chat_tasks.items()))
                del self.chat_tasks[id]
                tasks.append(task)
            self.chat_window.run_tasks(tasks, start, cont)

    def handle_finish(self):
        task_list = self.main_window.answers()
        print('RESULTS: ', task_list)
        self.user.end_interview_callback(task_list)
        self.handle_back()
        self.main_window.set_account_window()

    def run_code_window(self):
        self.task_window.run_code_task()

    def continue_code_window(self):
        self.task_window.continue_code_task()