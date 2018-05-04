from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from src.utils import Design


class ChatBox(QSplitter):

    def __init__(self, parent):
        self.parent_window = parent
        super().__init__(Qt.Vertical)

        self.dialog_box = QTextEdit()
        self.dialog_box.setFontPointSize(12)
        self.dialog_box.setTabStopWidth(24)
        self.dialog_box.setReadOnly(True)
        self.parent_window.set_style(self.dialog_box)
        self.dialog_box.setPlainText('Hello!')

        self.question_box = QTextEdit()
        self.question_box.setFontPointSize(12)
        self.question_box.setTabStopWidth(24)
        self.question_box.setReadOnly(True)
        self.parent_window.set_style(self.question_box)
        self.create_answer_box()

        self.addWidget(self.dialog_box)
        self.addWidget(self.question_box)
        self.addWidget(self.answer_box)
        self.setSizes([self.width() // 2,
                       self.width() // 2])

    def yes_no_question(self, task):
        self.current_task = task
        self.question_box.setPlainText(self.current_task.legend)
        self.answer_box.yes_button = QPushButton('YES', self)
        self.answer_box.yes_button.clicked.connect(self.yes_click)
        self.answer_box.no_button = QPushButton('NO', self)
        self.answer_box.no_button.clicked.connect(self.no_click)

        hbox = QHBoxLayout()
        self.answer_box.vbox = QVBoxLayout()
        hbox.addWidget(self.answer_box.yes_button)
        hbox.addWidget(self.answer_box.no_button)
        self.answer_box.vbox.addLayout(hbox)
        self.answer_box.setLayout(self.answer_box.vbox)

    @pyqtSlot()
    def yes_click(self):
        answer = self.current_task.right_answers[0] == 1
        self.parent_window.answer_flush(answer, self.answer_box.yes_button)
        self.parent_window.current_answers[self.current_task.id] = answer

    @pyqtSlot()
    def no_click(self):
        answer = self.current_task.right_answers[0] == 0
        self.parent_window.answer_flush(answer, self.answer_box.no_button)
        self.parent_window.current_answers[self.current_task.id] = answer

    def test_question(self, task):
        self.current_task = task
        self.question_box.setPlainText(self.current_task.legend)
        self.answers = task.right_answers
        self.answer_box.v_test_box = QVBoxLayout()
        self.__make_checkbox(task.proposed_answers)
        self.answer_box.v_test_box.addStretch(1)
        self.answer_box.setLayout(self.answer_box.v_test_box)

    def __make_checkbox(self, proposed_answers):
        self.checkbox_list = []
        for i in range(len(proposed_answers)):
            self.checkbox_list.append(QCheckBox(proposed_answers[i], self.answer_box))
            self.answer_box.v_test_box.addWidget(self.checkbox_list[i], i)

    def check_ckeckbox(self):
        selected = []
        for i, check_item in enumerate(self.checkbox_list):
            if check_item.isChecked():
                selected.append(i)
        answer = len(selected) == len(self.answers) and sorted(selected) == sorted(self.answers)
        self.parent_window.answer_flush(answer, self.answer_box)
        self.parent_window.current_answers[self.current_task.id] = answer

    def single_question(self, task):
        self.current_task = task
        self.question_box.setPlainText(self.current_task.legend)
        self.answers = task.right_answers

    def default_view(self):
        self.question_box.setPlainText('')
        self.create_answer_box()

    def create_answer_box(self):
        self.answer_box = QFrame(self)
        self.answer_box.setFrameShape(QFrame.StyledPanel)
        self.parent_window.set_style(self.answer_box)
        self.answer_box.setStyleSheet(Design.DEFAULT_STYLE)