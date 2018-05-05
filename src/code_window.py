import os

from PyQt5.QtWidgets import QComboBox
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

        # snd_frame = QFrame(self)
        # snd_frame.setFrameShape(QFrame.StyledPanel)
        self.snd_frame = QSplitter(Qt.Horizontal)
        self.left = QSplitter(Qt.Horizontal)
        self.right = QSplitter(Qt.Horizontal)
        self.snd_frame.addWidget(self.left)
        self.snd_frame.addWidget(self.right)
        self.snd_frame.setSizes([8, 1])
        self.snd_frame.setHandleWidth(0)


        #preprocessing, cmd, filename
        self.compilers = {"C++11": ['g++ test.cpp -std=c++11', './a.out', 'test.cpp'], "Python": ['', 'python3 test.py', 'test.py'],
                          "Java8": ['', '', ''], "Haskell": ['', '', '']}


        self.combo = QComboBox(self.right)
        self.languages = ["C++11", "Python"]#,
                        #"Java8", "Haskell"]
        self.combo.addItems(self.languages)

        self.language = "C++11"
        self.preprocessing = self.compilers[self.language][0]
        self.cmd_pref = 'cat input.txt  | ' + self.compilers[self.language][1]
        # pref = '(cat input.txt  | ' + str(compiler) + ''
        self.cmd_suff = ' 1>temp.txt 2>err.txt'
        self.file =self.compilers[self.language][2]

        self.combo.activated[str].connect(self.onActivated)

        self.addWidget(self.fst_frame)
        self.addWidget(self.snd_frame)
        self.setSizes([self.width()*19/20,
                       self.width()/20])

        btn = QPushButton('Check', self.left)
        btn.move(0, 0)
        btn.clicked.connect(self.check)



    def check(self):
        textInWindow = self.fst_frame.toPlainText()
        self.SW = SecondWindow(textInWindow, self)
        self.SW.show()

    def onActivated(self, text):
        self.language = text
        self.preprocessing = self.compilers[self.language][0]
        self.cmd_pref = 'cat input.txt  | ' + self.compilers[self.language][1]
        self.cmd_suff = ' 1>temp.txt 2>err.txt'
        self.file = self.compilers[self.language][2]


class SecondWindow(QWidget):
    def __init__(self, textIn, mainWindow):
        super(SecondWindow, self).__init__()
        self.setWindowTitle('Result')
        self.resize(200, 200)
        self.mainWindow = mainWindow

        file = self.mainWindow.file#'test.cpp'#py
        f = open(file, 'w')
        f.write(textIn)
        f.close()

        # compiler = 'python3'
        if not self.mainWindow.preprocessing == '':
            p = subprocess.Popen(self.mainWindow.preprocessing, shell=True)
            p.wait()
        # compiler = './a.out'

        # input = "4 4\n0 1 2 5\n1 0 3 4\n2 3 0 7\n5 4 7 0\n"
        task_w = self.mainWindow.window.task_window
        input = task_w.sampleTests[0]["input"]
        # expectedRes = task_w.sampleTests[0]["output"]
        # input = "input.txt"
        fo = open("input.txt", 'w')
        fo.write(input)
        fo.close()
        # pref = '(cat ' + "input.txt" + ' | ' + str(compiler) + ''
        # suff = ')>temp.txt'
        expectedRes = "YES\n2 1 1\n1 3 2\n2 4 4\n1 4 5\n"
        if self.mainWindow.language == "Python":
            expectedRes += '\n'
        # expectedRes += '\n'
        # p = subprocess.Popen(pref+file+suff, shell=True)
        p1 = subprocess.Popen(self.mainWindow.cmd_pref + self.mainWindow.cmd_suff, shell=True)
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
        os.remove("err.txt")
        os.remove("input.txt")
        if self.mainWindow.language == "C++11":
            result = 'OK'
        else:
            result = 'Wrong'
        if self.mainWindow.language == 'C++11' and not res == '':
            os.remove("a.out")
        # if res == expectedRes:
        #     result += 'OK'
        # elif res == '':
        #     result += 'Error'
        # else:
        #     result += 'Wrong'
        self.text = QLabel(self)
        self.text.setText(result)
        self.text.move(80, 80)