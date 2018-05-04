from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from src.task import *
from src.application import *
from src.chat_box import ChatBox
import time
from src.utils import Design


class WindowChat(QSplitter):

    def __init__(self, window):
        self.window = window
        super().__init__(Qt.Vertical)
        self.grid = QGridLayout()
        self.text_window = QTextEdit()
        self.text_window.setFontPointSize(12)
        self.text_window.setTabStopWidth(24)
        self.set_style(self.text_window)
        self.text_window.setStyleSheet(Design.DEFAULT_STYLE)

        self.info_window = QFrame(self)
        self.info_window.setFrameShape(QFrame.StyledPanel)
        self.set_style(self.info_window)

        l = QLabel(self.info_window)
        pixmap = QPixmap('boss.jpg')
        l.setPixmap(pixmap)
        vvbox = QVBoxLayout()
        vvbox.addWidget(l)
        self.info_window.setLayout(vvbox)

        self.chat_box = ChatBox(self)

        self.addWidget(self.info_window)
        self.addWidget(self.chat_box)
        self.addWidget(self.text_window)
        self.setSizes([self.width() * 3 // 10,
                       self.width() * 5 // 10,
                       self.width() * 2 // 10])

        self.answer_botton = QPushButton('Answer', self)
        self.answer_botton.clicked.connect(self.answer_click)
        self.answer_botton.resize(self.answer_botton.sizeHint())
        self.answer_botton.setShortcut(Qt.Key_Enter)
        self.answer_botton.move(self.width() // 10,
                                self.height() // 10)
        # self.chat_box.default_view()
        self.chat_box.check_box(10)
        self.chat_box.yes_no_question(10)

    @staticmethod
    def set_style(window):
        window.setFrameShape(QFrame.StyledPanel)
        window.setLineWidth(2)
        window.setFrameShape(QFrame.Box)
        window.setFrameShadow(QFrame.Plain)

    def update_task(self, task):
        if task.type != TaskType.TEST:
            test = self.make_test(task)

    @pyqtSlot()
    def answer_click(self):
        answer = self.text_window.toPlainText()
        self.text_window.setPlainText(answer)
        if answer:
            correct = False
            if answer.lower() == 'kek':
                correct = True
            self.answer_flush(correct, self.text_window)
            QApplication.processEvents()
            time.sleep(0.2)
            print(answer)
        self.text_window.setPlainText('')

    @pyqtSlot()
    def change_difficulty(self):
        pass

    def getInteger(self):
        i, okPressed = QInputDialog.getInt\
            (self, 'Difficulty', 'level', 28, 0, 100, 1)
        if okPressed:
            print(i)

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
