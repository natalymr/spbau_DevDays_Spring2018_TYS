from PyQt5.QtWidgets import QFrame, QSplitter
from PyQt5.QtCore import Qt


class WindowCode(QSplitter):

    def __init__(self, window):
        self.window = window
        super().__init__(Qt.Vertical)
        fst_frame = QFrame(self)
        fst_frame.setFrameShape(QFrame.StyledPanel)
        snd_frame = QFrame(self)
        snd_frame.setFrameShape(QFrame.StyledPanel)
        self.addWidget(fst_frame)
        self.addWidget(snd_frame)
        self.setSizes([self.width(), 0])
