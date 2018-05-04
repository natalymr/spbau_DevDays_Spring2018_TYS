import os
from PyQt5.QtWidgets import QFrame, QSplitter, QTextEdit, QPushButton, QWidget
from PyQt5.QtCore import Qt
import subprocess
import json

from PyQt5.QtWidgets import QLabel


class WindowCode(QSplitter):

    def __init__(self, window):
        self.window = window
        super().__init__(Qt.Vertical)

        self.setHandleWidth(0)

        self.fst_frame = QTextEdit()
        self.fst_frame.setFontPointSize(8)
        self.fst_frame.setTabStopWidth(24)

        snd_frame = QFrame(self)
        snd_frame.setFrameShape(QFrame.StyledPanel)
        self.addWidget(self.fst_frame)
        self.addWidget(snd_frame)
        self.setSizes([self.width(),
                       0])

        btn = QPushButton('Check', self)
        btn.move(0, 0)
        btn.clicked.connect(self.check)

    def check(self):
        textInWindow = self.fst_frame.toPlainText()
        self.SW = SecondWindow(textInWindow)
        self.SW.show()


class SecondWindow(QWidget):
    def __init__(self, textIn):
        super(SecondWindow, self).__init__()
        self.setWindowTitle('Result')
        self.resize(200, 200)
        file = 'test.py'
        f = open(file, 'w')
        f.write(textIn)
        f.close()
        input = 3
        pref = '(echo ' + str(input) + ' | python3 '
        suff = ')>temp.txt'
        expectedRes = '3'
        expectedRes += '\n'
        p = subprocess.Popen(pref+file+suff, shell=True)
        p.wait()
        resFile = open("temp.txt", "r")
        resLst = resFile.readlines()
        res = ''
        for st in resLst:
            res += st
        resFile.close()
        result = ''
        os.remove(file)
        os.remove("temp.txt")
        if res == expectedRes:
            result += 'OK'
        else:
            result += 'False'
        self.text = QLabel(self)
        self.text.setText(result)
        self.text.move(80, 80)