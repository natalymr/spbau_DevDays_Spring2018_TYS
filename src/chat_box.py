from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from src.utils import Design


class ChatBox(QSplitter):

    def __init__(self, parent):
        self.parent_window = parent
        super().__init__(Qt.Vertical)

        self.question_box = QTextEdit()
        self.question_box.setFontPointSize(12)
        self.question_box.setTabStopWidth(24)
        self.question_box.setReadOnly(True)
        self.parent_window.set_style(self.question_box)

        self.create_answer_box()

        self.addWidget(self.question_box)
        self.addWidget(self.answer_box)
        self.setSizes([self.width() // 2,
                       self.width() // 2])

    def yes_no_question(self, task):
        test_text = 'cvbhnjkmvlweon jnfwie ' \
                    'fiwjfowiejofwijfoei jwdqj 2ejfpo2' \
                    'fp2o3jojmv   oefjp2jf2?'
        self.question_box.setPlainText(test_text)
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
        self.parent_window.answer_flush(True, self.answer_box.yes_button)
        print('YES button click')

    @pyqtSlot()
    def no_click(self):
        self.parent_window.answer_flush(False, self.answer_box.no_button)
        print('NO button click')

    def check_box(self, task):
        tests = ['aaaaaaa', 'aaaaaaaaaaaaa',
                 'aaaaaaaaaaaaaa', 'aaaaaaaa',
                 'aaaaaaaaaaaaaaaaaaaaaaaa']
        self.answers = [2]
        self.answer_box.v_test_box = QVBoxLayout()
        self.make_checkbox(tests)
        self.answer_box.v_test_box.addStretch(1)
        go_button = QPushButton('Go', self.answer_box)
        go_button.clicked.connect(self.check_ckeckbox)
        self.answer_box.v_test_box.addWidget(go_button, 3)
        self.answer_box.setLayout(self.answer_box.v_test_box)
        # self.show()

    def make_checkbox(self, tests):
        self.checkbox_list = []
        for i in range(len(tests)):
            self.checkbox_list.append(QCheckBox(tests[i], self.answer_box))
            self.answer_box.v_test_box.addWidget(self.checkbox_list[i], i)

    def check_ckeckbox(self):
        selected = []
        for i, check_item in enumerate(self.checkbox_list):
            if check_item.isChecked():
                selected.append(i)
        correct = len(selected) == len(self.answers) and sorted(selected) == sorted(self.answers)
        self.parent_window.answer_flush(correct, self.answer_box)

    def default_view(self):
        self.question_box.setPlainText('')
        self.create_answer_box()

    def create_answer_box(self):
        self.answer_box = QFrame(self)
        self.answer_box.setFrameShape(QFrame.StyledPanel)
        self.parent_window.set_style(self.answer_box)
        self.answer_box.setStyleSheet(Design.DEFAULT_STYLE)