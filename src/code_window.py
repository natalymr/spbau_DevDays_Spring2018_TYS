import os

from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QFrame, QSplitter, QTextEdit, QPushButton, QWidget
from PyQt5.QtCore import Qt
import random
import subprocess
import json

from PyQt5.QtWidgets import QLabel

from spbau_DevDays_Spring2018_TYS.src.code_task import CodeTask


class WindowCode(QSplitter):

    def __init__(self, window):
        self.window = window
        super().__init__(Qt.Vertical)

        self.setHandleWidth(0)

        self.fst_frame = QTextEdit()
        self.fst_frame.setFontPointSize(12)
        self.fst_frame.setTabStopWidth(36)
        self.fst_frame.clear()

        self.snd_frame = QSplitter(Qt.Horizontal)
        self.left = QSplitter(Qt.Horizontal)
        self.right = QSplitter(Qt.Horizontal)
        self.snd_frame.addWidget(self.left)
        self.snd_frame.addWidget(self.right)
        self.snd_frame.setSizes([8, 1])
        self.snd_frame.setHandleWidth(0)


        self.compilers = {"C++11": ['g++ test.cpp -std=c++11', './a.out', 'test.cpp'], "Python": ['', 'python3 test.py', 'test.py']}


        self.combo = QComboBox(self.right)
        self.languages = ["C++11", "Python"]
        self.combo.addItems(self.languages)

        self.language = "C++11"
        self.preprocessing = self.compilers[self.language][0]
        self.cmd_pref = 'cat input.txt  | ' + self.compilers[self.language][1]
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

        file = self.mainWindow.file
        f = open(file, 'w')
        f.write(textIn)
        f.close()

        if not self.mainWindow.preprocessing == '':
            p = subprocess.Popen(self.mainWindow.preprocessing, shell=True)
            p.wait()
        task_w = self.mainWindow.window.task_window
        with open("src/tasks/json/coding_problems/tests/tests_for_all_problems.json", "r") as f:
            self.st = json.load(f)
        tests = []
        for test in self.st:
            if test["problem_name_t"] == task_w.prob_name_t:
                tests = test["tests"]
        input = ""
        expectedRes = ""
        num_test = random.randint(0,len(tests))
        for im in tests[num_test]["input"]:
            input += im
        for om in tests[num_test]["output"]:
            expectedRes += om
        with open("input.txt", 'w') as fo:
            fo.write(input)
        if self.mainWindow.language == "Python":
            expectedRes += '\n'
        p1 = subprocess.Popen(self.mainWindow.cmd_pref + self.mainWindow.cmd_suff, shell=True)
        p1.wait()
        with open("temp.txt", "r") as resFile:
            resLst = resFile.readlines()
        res = ''
        for st in resLst:
            res += st
        result = ''
        os.remove(file)
        os.remove("temp.txt")
        os.remove("err.txt")
        os.remove("input.txt")
        if self.mainWindow.language == 'C++11' and not res == '':
            os.remove("a.out")
        if res == expectedRes:
            result += 'OK'
        elif res == '':
            result += 'Error'
        else:
            result += 'Wrong'
        self.text = QLabel(self)
        self.text.setText(result)
        if result=="OK":
            self.mainWindow.window.run_chat_task(count=5, cont=False)
            task = CodeTask(task_w.id, task_w.task_dif)
            self.mainWindow.window.main_window.accept_result(task, True)
            self.mainWindow.window.handle_finish()
        self.text.move(80, 80)