from PyQt5.QtWidgets import QFrame


class WindowTask(QFrame):

    def __init__(self, window):
        super().__init__(window)
        self.setFrameShape(QFrame.StyledPanel)
