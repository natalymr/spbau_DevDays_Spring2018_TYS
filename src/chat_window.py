from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate, QTime, Qt
from src.application import *


class WindowChat(QSplitter):

    def __init__(self, window):
        self.window = window
        super().__init__(Qt.Vertical)

        self.grid = QGridLayout()
        self.text_window = QTextEdit()
        self.text_window.setFontPointSize(12)
        self.text_window.setTabStopWidth(24)
        self.text_window.setLineWidth(2)
        self.text_window.setFrameShape(QFrame.Box)
        self.text_window.setFrameShadow(QFrame.Plain)

        self.info_window = QFrame(self)
        self.info_window.setFrameShape(QFrame.StyledPanel)
        self.info_window.setLineWidth(2)
        self.info_window.setFrameShape(QFrame.Box)
        self.info_window.setFrameShadow(QFrame.Plain)

        self.chat_window = QFrame(self)
        self.chat_window.setFrameShape(QFrame.StyledPanel)
        self.chat_window.setLineWidth(2)
        self.chat_window.setFrameShape(QFrame.Box)
        self.chat_window.setFrameShadow(QFrame.Plain)
        # self.chat_area.setStyleSheet("background-color: rgb(0, 255, 0)")

        self.addWidget(self.info_window)
        self.addWidget(self.chat_window)
        self.addWidget(self.text_window)
        self.setSizes([self.width() * 2 // 10,
                       self.width() * 7 // 10,
                       self.width() * 1 // 10])

        answer_botton = QPushButton('Answer', self)
        answer_botton.resize(answer_botton.sizeHint())
        answer_botton.setShortcut(Qt.Key_Enter)
        answer_botton.move(self.width() // 10, self.width() // 10)
        self.make_test(10)

    def update_task(self, task):
        if task.type != TaskType.TEST:
            test = self.make_test(task)


    def make_test(self, task):
        tests = ['aaaaaaa', 'aaaaaaaaaaaaa',
                 'aaaaaaaaaaaaaa', 'aaaaaaaa']
        go_button = QPushButton('Go!')
        go_button.setShortcut(Qt.Key_Enter)
        go_button.setFixedSize(50, 30)
        go_button.setGeometry(self.chat_window.width() // 2,
                              self.chat_window.height() * 4 // 5, 50, 30)

        go_button.move(self.width() // 10, self.width() // 10)

        # hbox = QHBoxLayout()
        hbox = QVBoxLayout()
        test_group = QGroupBox('Test')
        test_group.move(0, 0)
        test_group.setFixedSize(len(max(tests, key=lambda x: len(x))) * 10 + 50,
                       len(tests) * 30)
        hbox.addWidget(go_button)
        form = QFormLayout()
        form.addRow(hbox)
        form.addRow(test_group)
        for i in range(len(tests)):
            cb = QCheckBox(tests[i], self.chat_window)
            cb.move(self.width() // 20, self.height() * i // 15)
        self.chat_window.setLayout(form)


