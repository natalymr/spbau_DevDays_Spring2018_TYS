from PyQt5.QtWidgets import QFrame


class WindowChat(QFrame):

    def __init__(self, window):
        super().__init__(window)
        self.setFrameShape(QFrame.StyledPanel)
