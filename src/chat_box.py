from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from src.utils import *
from src.task import *
import time


class ChatBox(QSplitter):

    def __init__(self, parent):
        self.parent_window = parent
        super().__init__(Qt.Vertical)
        self.answer_box = None
        self.dialog_box = self.__create_text_editor(True)
        self.dialog_box.setFixedHeight(100)
        self.question_box = self.__create_text_editor(True)
        self.__answer_box_clear()
        self.say_to_user()
        self.insertWidget(0, self.dialog_box)
        self.insertWidget(1, self.question_box)
        self.insertWidget(2, self.answer_box)
        self.setSizes([self.width() // 3,
                       self.width() * 2 // 4,
                       self.width() // 4])

        self.answer_botton = QPushButton('Answer', self)
        self.answer_botton.clicked.connect(self.answer_click)
        self.answer_botton.resize(self.answer_botton.sizeHint())
        self.answer_botton.move(self.width() // 10,
                                self.height() // 10)

    def yes_no_question(self, task):
        self.__set_task(task)
        self.__answer_box_yes_no()

    def test_question(self, task):
        self.__set_task(task)
        self.__answer_box_test()

    def __make_checkbox(self, proposed_answers):
        self.checkbox_list = []
        for i in range(len(proposed_answers)):
            self.checkbox_list.append(QCheckBox(proposed_answers[i], self.answer_box))
            self.answer_box.v_test_box.addWidget(self.checkbox_list[i], i)

    def __check_ckeckbox(self):
        selected = []
        for i, check_item in enumerate(self.checkbox_list):
            if check_item.isChecked():
                selected.append(i)
        answer = len(selected) == len(self.answers) \
                 and sorted(selected) == sorted(self.answers)
        self.answer_flush(answer, self.answer_box)
        self.accept_result(answer)

    def single_question(self, task):
        self.__set_task(task)
        self.__answer_box_single()

    def __create_text_editor(self, read_only):
        window = QTextEdit()
        window.setFontPointSize(12)
        window.setTabStopWidth(24)
        set_style(window)
        window.setReadOnly(read_only)
        return window

    def say_to_user(self, text=None):
        if not text:
            text = DEFAULT_TEXT
        self.dialog_box.setPlainText(text)

    def __answer_box_clear(self):
        if self.answer_box:
            self.answer_box.setParent(None)
        self.answer_box = QFrame(self)
        self.answer_box.setFrameShape(QFrame.StyledPanel)
        set_style(self.answer_box)
        self.answer_box.setStyleSheet(Design.DEFAULT_STYLE)
        self.insertWidget(2, self.answer_box)

    def __answer_box_yes_no(self):
        if self.answer_box:
            self.answer_box.setParent(None)
        self.__answer_box_clear()
        self.answer_box.yes_button = QPushButton('YES', self)
        self.answer_box.yes_button.clicked.connect(self.yes_click)
        self.answer_box.no_button = QPushButton('NO', self)
        self.answer_box.no_button.clicked.connect(self.no_click)

        hbox = QHBoxLayout()
        vbox = QVBoxLayout()
        hbox.addWidget(self.answer_box.yes_button)
        hbox.addWidget(self.answer_box.no_button)
        vbox.addLayout(hbox)
        self.answer_box.setLayout(vbox)
        self.insertWidget(2, self.answer_box)

    def __answer_box_single(self):
        if self.answer_box:
            self.answer_box.setParent(None)
        self.answer_box = self.__create_text_editor(False)
        self.insertWidget(2, self.answer_box)

    def __answer_box_test(self):
        self.__answer_box_clear()
        self.answer_box.v_test_box = QVBoxLayout()
        self.__make_checkbox(self.current_task.proposed_answers)
        self.answer_box.v_test_box.addStretch(1)
        self.answer_box.setLayout(self.answer_box.v_test_box)
        self.insertWidget(2, self.answer_box)

    @pyqtSlot()
    def yes_click(self):
        self.__check_bool_answer(1, self.answer_box.yes_button)

    @pyqtSlot()
    def no_click(self):
        self.__check_bool_answer(0, self.answer_box.no_button)

    @pyqtSlot()
    def answer_click(self):
        if self.current_task.type == TaskType.TEST:
            self.__check_ckeckbox()
            return
        elif self.current_task.type == TaskType.SINGLE_ANSWER:
            answer_box = self.answer_box
            answer = answer_box.toPlainText()
            right_answers = self.current_task.right_answers
            self.answer_box.setPlainText(answer)
            if answer:
                correct = False
                if answer.lower().replace(' ', '') in right_answers:
                    correct = True
                self.answer_flush(correct, answer_box)
                QApplication.processEvents()
                time.sleep(0.2)
            answer_box.setPlainText('')

    @staticmethod
    def answer_flush(correct, obj):
        time.sleep(0.5)
        flush = Design.WRONG_STYLE
        if correct:
            flush = Design.RIGHT_STYLE
        obj.setStyleSheet(flush)
        QApplication.processEvents()
        time.sleep(0.4)
        obj.setStyleSheet(Design.DEFAULT_STYLE)
        time.sleep(0.2)

    def __set_task(self, task):
        self.current_task = task
        self.attempts = 0
        self.question_box.setPlainText(self.current_task.legend)
        self.answers = task.right_answers

    def __check_bool_answer(self, answer, button):
        answer = len(self.answers) == 1 and self.answers[0] == answer
        self.answer_flush(answer, button)
        self.accept_result(answer)

    def accept_result(self, answer):
        print(answer, self.attempts, self.current_task)
        if not answer or (answer and self.attempts != 0):
            self.parent_window.main_window.accept_result(self.current_task, answer)
        self.attempts += 1
        if self.attempts == 3:
            self.parent_window.parent_window.run_chat_task()
