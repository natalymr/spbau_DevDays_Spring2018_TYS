from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui
import subprocess
import random
from PyQt5.QtWidgets import *
import json


class WindowTask(QSplitter):

    def __init__(self, window):
        self.window = window
        super(WindowTask, self).__init__(Qt.Vertical)

        self.setHandleWidth(0)

        self.fst_frame = QSplitter(Qt.Vertical)
        self.fst_frame.setHandleWidth(0)

        self.up_frame = QFrame(self)
        self.up_text = QLabel(self.up_frame)


        with open("src/tasks/json/coding_problems/problems/coding_problems.json", "r") as f:
            self.st = json.load(f)

        self.task_dif = self.window.difficulty + 1
        if self.task_dif == 4:
            self.task_dif += 1

        self.dif_dict = {}
        self.dif_dict[2] = []
        self.dif_dict[3] = []
        self.dif_dict[5] = []

        for task in self.st:
            self.dif_dict[task["difficulty"]].append(task)

        num = random.randint(0, len(self.dif_dict[self.task_dif])-1)
        self.ste = self.dif_dict[self.task_dif][num]
        while self.ste["id"] >= 9 and not self.ste["id"] == 14:
            num = random.randint(0, len(self.dif_dict[self.task_dif]) - 1)
            self.ste = self.dif_dict[num]

        self.prob_name = self.ste["name"]
        self.id = self.ste["id"]
        self.up_text.setText(self.prob_name)
        self.prob_name_t = self.ste["problem_name_t"]
        self.inTex = self.ste["input"]
        self.outTex = self.ste["output"]
        self.sampleTests = self.ste["sampleTests"]
        self.bot_frame = QToolBox()

        self.desc = QTextEdit()
        self.desc.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)

        self.io = QTextEdit()
        self.io.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)

        self.examp = QTextEdit()
        self.examp.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)

        self.bot_frame.insertItem(0, self.desc, "Desctiption")
        self.bot_frame.insertItem(1, self.io, "I/O Format")
        self.bot_frame.insertItem(2, self.examp, "Examples")

        self.fst_frame.addWidget(self.up_frame)
        self.fst_frame.addWidget(self.bot_frame)
        self.fst_frame.setSizes([100,900])

        self.snd_frame = QProgressBar(self)
        self.snd_frame.setValue(0)
        self.palette_green = QtGui.QPalette(self.palette())
        self.palette_green.setColor(QtGui.QPalette.Highlight,
                         QtGui.QColor(QtCore.Qt.green))

        self.palette_gray = QtGui.QPalette(self.palette())
        self.palette_gray.setColor(QtGui.QPalette.Highlight,
                                    QtGui.QColor(QtCore.Qt.darkGray))

        self.snd_frame.setPalette(self.palette_green)
        self.val = 0.00
        self.snd_frame.setFormat('0.00')
        self.totalMin = 45

        self.addWidget(self.fst_frame)
        self.addWidget(self.snd_frame)
        self.setSizes([self.width() * 11 // 12,
                       self.width() // 12])

        self.count = 0
        self.scale = 1000
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.tick_status)

    def run_code_task(self):
        txt = ""
        desc = ("src/tasks/html/code/"+self.prob_name_t+"/description.html").replace('"', '')
        io = ("src/tasks/html/code/"+self.prob_name_t+"/io.html").replace('"','')
        examples = ("src/tasks/html/code/"+self.prob_name_t+"/examples.html").replace('"','')
        try:
            with open(desc) as fht:
                txt = fht.read()
            self.desc.setHtml(txt)

            with open(io) as fht:
                txt = fht.read()
            self.io.setHtml(txt)

            with open(examples) as fht:
                txt = fht.read()
            self.examp.setHtml(txt)
        except IOError:
            self.description_tex = self.ste["legend"]


            self.io_text = "Input:\n\n" + self.inTex + "\n\nOutput:\n\n" + self.outTex



            self.examplesTex = ""
            for ioTex in self.ste["sampleTests"]:
                examplesIn_tex = ioTex["input"].replace("\n", " \\newline ")
                examplesOut_tex = ioTex["output"].replace("\n", " \\newline ")
                self.examplesTex += "\n\ninput:\n\n" + examplesIn_tex + "\n\noutput:\n\n" + examplesOut_tex

            p = subprocess.Popen("mkdir src/tasks/html/code/" + self.prob_name_t, shell=True)
            p.wait()
            self.texToHtml(self.description_tex, "description", self.prob_name_t)
            self.texToHtml(self.io_text, "io", self.prob_name_t)
            self.texToHtml(self.examplesTex, "examples", self.prob_name_t)

            with open(desc) as fht:
                txt = fht.read()
            self.desc.setHtml(txt)

            with open(io) as fht:
                txt = fht.read()
            self.io.setHtml(txt)

            with open(examples) as fht:
                txt = fht.read()
            self.examp.setHtml(txt)


        self.timer.start(1000)



    def tick_status(self):
        min = int(self.count/60)
        sec = int(self.count % 60)
        self.val = min + sec/100
        self.snd_frame.setValue(self.count*100/(self.totalMin*60))
        self.snd_frame.setFormat('%.02f' % self.val)
        self.count += 1
        if self.count == 900 or self.count == 1800 or self.count == 2700:
            self.timer.stop()
            self.snd_frame.setPalette(self.palette_gray)
            co = 1
            if not self.count == 2700 and self.window.difficulty>1:
                co += 1
            if self.count == 2700:
                co += self.window.difficulty
            self.window.run_chat_task(count=co, cont=not self.count == 2700)
            if self.count == 2700:
                self.window.handle_finish()

        if self.count > 60*self.totalMin:
            self.timer.stop()

    def continue_code_task(self):
        self.snd_frame.setPalette(self.palette_green)
        self.timer.start(1000)

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
\\usepackage{graphicx}\n\
\\usepackage[utf8]{inputenc}\n\
\\begin{document}\n"
        suffTex = "\n\\end{document}"
        outTex = prefTex + text + suffTex
        with open("tempTex.tex", "w") as oTex:
            oTex.write(outTex)
            oTex.flush()

    def texToHtml(self, text, name, task_name):
        self.textToTex(text)
        p = subprocess.Popen("htlatex tempTex.tex", shell=True)
        p.wait()
        p = subprocess.Popen("mv tempTex.html " + str(name) + ".html", shell=True)
        p.wait()
        p = subprocess.Popen("mv " + str(name) + ".html src/tasks/html/code/"+str(task_name), shell=True)
        p.wait()
        p = subprocess.Popen("rm tempTex.*", shell=True)
        p.wait()