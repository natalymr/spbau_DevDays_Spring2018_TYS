import os
from PyQt5.QtWidgets import QFrame, QSplitter, QTextEdit, QPushButton, QWidget
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
import subprocess
import json

from PyQt5.QtWidgets import QLabel


class WindowCode(QSplitter):

    def __init__(self, window):
        self.window = window
        super().__init__(Qt.Vertical)

        self.setHandleWidth(0)

        self.fst_frame = QTextEdit()
        self.fst_frame.setFontPointSize(12)
        self.fst_frame.setTabStopWidth(36)
        self.fst_frame.clear()

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
        file = 'test.cpp'#py
        f = open(file, 'w')
        f.write(textIn)
        f.close()

        # compiler = 'python3'

        p = subprocess.Popen('g++ test.cpp', shell=True)
        p.wait()

        compiler = './a.out'

        input = "4 4\n0 1 2 5\n1 0 3 4\n2 3 0 7\n5 4 7 0\n"
        # input = "input.txt"
        fo = open("input.txt", 'w')
        fo.write(input)
        fo.close()
        pref = '(cat ' + "input.txt" + ' | ' + str(compiler) + ''
        suff = ')>temp.txt'
        expectedRes = "YES\n2 1 1\n1 3 2\n2 4 4\n1 4 5\n"
        # expectedRes += '\n'
        # p = subprocess.Popen(pref+file+suff, shell=True)
        p1 = subprocess.Popen(pref + suff, shell=True)
        p1.wait()
        resFile = open("temp.txt", "r")
        resLst = resFile.readlines()
        res = ''
        for st in resLst:
            res += st
        resFile.close()
        result = ''
        os.remove(file)
        os.remove("temp.txt")
        os.remove("input.txt")
        os.remove("a.out")
        if res == expectedRes:
            result += 'OK'
        else:
            result += 'False'
        self.text = QLabel(self)
        self.text.setText(result)
        self.text.move(80, 80)