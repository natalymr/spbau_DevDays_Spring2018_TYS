from PyQt5.QtWidgets import QFrame, QSplitter, QTextEdit, QPushButton, QWidget
from PyQt5.QtCore import Qt


class WindowCode(QSplitter):

    def __init__(self, window):
        self.window = window
        super().__init__(Qt.Vertical)

        fst_frame = QTextEdit()
        fst_frame.setFontPointSize(8)
        fst_frame.setTabStopWidth(24)

        snd_frame = QFrame(self)
        snd_frame.setFrameShape(QFrame.StyledPanel)
        self.addWidget(fst_frame)
        self.addWidget(snd_frame)
        self.setSizes([self.width(),
                       0])

        btn = QPushButton('Check', self)
        btn.move(0, 0)
        btn.clicked.connect(self.check)

    def check(self):
        self.SW = SecondWindow()
        self.SW.show()


class SecondWindow(QWidget):
    def __init__(self):
        super(SecondWindow, self).__init__()
        self.setWindowTitle('Result')