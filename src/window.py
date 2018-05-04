from PyQt5.QtWidgets import QWidget, QSplitter, QHBoxLayout, QDesktopWidget
from PyQt5.QtCore import *
from src.task_window import WindowTask
from src.code_window import WindowCode
from src.chat_window import WindowChat


class Window(QWidget):

    def __init__(self, owner, parent):
        super().__init__()
        self.owner = owner
        self.parent = parent
        self.initUI()
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
        self.chat_window = WindowChat(self)
        self.code_window = WindowCode(self)

        splitter1 = QSplitter(Qt.Vertical)
        splitter1.setHandleWidth(0)
        splitter1.addWidget(self.task_window)
        splitter1.addWidget(self.code_window)
        splitter1.setSizes([self.width() // 3,
                            self.width() * 2 // 3])

        splitter2 = QSplitter(Qt.Horizontal)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(self.chat_window)
        splitter2.setSizes([self.height() * 2 // 3,
                            self.height() // 3])
        hbox.addWidget(splitter2)
        self.setLayout(hbox)

    def closeEvent(self, event):
        self.owner.current_widget = self.parent
        self.parent.show()
        event.accept()

    # def event(self, e):
    #     if e.type() == QEvent.Timer:
    #         print('TIMER ends')
    #         return True
    #
    #     if e.type() == QEvent.Hide:
    #         print('hide')
    #         return True
    #
    #     if e.type() == QEvent.Close:
    #         print('close')
    #         return True