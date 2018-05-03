from PyQt5.QtWidgets import QApplication, QWidget, QFrame, QSplitter, QHBoxLayout, QDesktopWidget
from PyQt5.QtCore import Qt


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('TryYourSkills')
        self.setGeometry(0, 0,
                         QDesktopWidget().availableGeometry().width(),
                         QDesktopWidget().availableGeometry().height())
        self.set_windows()

    def set_windows(self):
        hbox = QHBoxLayout(self)

        task_window = QFrame(self)
        task_window.setFrameShape(QFrame.StyledPanel)
        # task_window.setGeometry(1, 1, 20, 20)

        chat_window = QFrame(self)
        chat_window.setFrameShape(QFrame.StyledPanel)
        # chat_window.setGeometry(1, 1, 20, 20)

        code_window = QFrame(self)
        code_window.setFrameShape(QFrame.StyledPanel)
        code_window.setFrameShadow(QFrame.Raised)
        # code_window.setGeometry(1, 1, 20, 20)

        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(task_window)
        splitter2.addWidget(code_window)

        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(task_window)
        splitter1.addWidget(code_window)
        splitter1.addWidget(chat_window)

        hbox.addWidget(splitter1)
        hbox.addWidget(splitter2)

        self.setLayout(hbox)