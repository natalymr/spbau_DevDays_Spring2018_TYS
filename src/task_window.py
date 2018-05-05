from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QTextDocument
from PyQt5.QtWidgets import QFrame, QSplitter, QProgressBar, QToolBox, QLabel, QTableWidgetItem
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QLabel
import subprocess
import threading
import time
import sys
import matplotlib as mpl
from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtWidgets import *
import json

from src.application import *
from src.task import TaskType


class WindowTask(QSplitter):

    def __init__(self, window):
        self.window = window
        super(WindowTask, self).__init__(Qt.Vertical)

        self.setHandleWidth(0)

        self.fst_frame = QSplitter(Qt.Vertical)
        self.fst_frame.setHandleWidth(0)

        self.up_frame = QFrame(self)
        self.up_text = QLabel(self.up_frame)


        f = open("src/tasks/coding_problems.json", "r")

        st = f.readline()
        st = f.readline()
        st = f.readline()
        st = f.readline()
        st = st.replace("'", "\"")
        ste = json.loads(st)
        self.prob_name = ste["name"]
        self.description_tex = ste["legend"]
        # self.texToHtml(self.description_tex, "description")

        self.inTex = ste["input"]
        self.outTex = ste["output"]
        text = "Input:\n\n" + self.inTex + "\n\nOutput:\n\n" + self.outTex
        # self.texToHtml(text, "io")

        self.examplesTex = ""
        for ioTex in ste["sampleTests"]:
            examplesIn_tex = ioTex["input"].replace("\n", "\\newline")
            examplesOut_tex = ioTex["output"].replace("\n", "\\newline")
            self.examplesTex += "\n\ninput:\n\n" + examplesIn_tex + "\n\noutput:\n\n" + examplesOut_tex
        # self.texToHtml(self.examplesTex, "examples")


        self.up_text.setText(self.prob_name)
        self.bot_frame = QToolBox()

        self.desc = QTextEdit()
        fht = open("tmp/description.html")
        txt = fht.read()
        fht.close()
        self.desc.setHtml(txt)
        self.desc.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)

        self.io = QTextEdit()
        fht = open("tmp/io.html")
        txt = fht.read()
        fht.close()
        self.io.setHtml(txt)
        self.io.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)

        self.examp = QTextEdit()
        fht = open("tmp/examples.html")
        txt = fht.read()
        fht.close()
        self.examp.setHtml(txt)
        self.examp.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)

        self.bot_frame.insertItem(0, self.desc, "Desctiption")
        self.bot_frame.insertItem(1, self.io, "I/O Format")
        self.bot_frame.insertItem(2, self.examp, "Examples")

        self.fst_frame.addWidget(self.up_frame)
        self.fst_frame.addWidget(self.bot_frame)
        self.fst_frame.setSizes([100,900])

        self.snd_frame = QProgressBar(self)
        self.snd_frame.setValue(0)
        palette = QtGui.QPalette(self.palette())
        palette.setColor(QtGui.QPalette.Highlight,
                         QtGui.QColor(QtCore.Qt.green))
        self.snd_frame.setPalette(palette)
        self.val = 0.00
        self.snd_frame.setFormat('0.00')
        self.totalMin = 3

        self.addWidget(self.fst_frame)
        self.addWidget(self.snd_frame)
        self.setSizes([self.width() * 11 // 12,
                       self.width() // 12])

        self.count = 1
        self.scale = 1000
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.tick_status)
        self.timer.start(1000)


    def update_task(self, task):
        if task.type == TaskType.CODING:
            pass

    def tick_status(self):
        if self.window is None:
            self.clear_back()
            return
        min = int(self.count/60)
        sec = int(self.count % 60)
        self.val = min + sec/100
        self.snd_frame.setValue(self.count*100/(self.totalMin*60))
        self.snd_frame.setFormat('%.02f' % self.val)
        self.count += 1
        if self.count % 10 == 0:
            self.window.run_chat_task(difficulty=1)
        if self.count > 300:
            self.timer.stop()

    def close(self):
        self.timer.stop()
        self.timer = None
        super(WindowTask, self).close()

    def textToTex(self, text):
        prefTex = "\\documentclass{article}\n\
\\usepackage[english,russian]{babel}\n\
\\usepackage[T1]{fontenc}\n\
\\usepackage{amsmath}\n\
\\usepackage{amssymb}\n\
\\usepackage[utf8]{inputenc}\n\
\\begin{document}\n"
        suffTex = "\n\\end{document}"
        outTex = prefTex + text + suffTex
        oTex = open("tempTex.tex", "w")
        oTex.write(outTex)
        oTex.flush()
        oTex.close()
        # time.sleep(2)

    def texToHtml(self, text, name):
        self.textToTex(text)
        p = subprocess.Popen("htlatex tempTex.tex", shell=True)
        p.wait()
        p = subprocess.Popen("mv tempTex.html " + str(name) + ".html", shell=True)
        p.wait()
        p = subprocess.Popen("mv " + str(name) + ".html tmp", shell=True)
        p.wait()
        p = subprocess.Popen("rm tempTex.*", shell=True)
        p.wait()
