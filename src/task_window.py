from PyQt5.QtWidgets import QFrame, QSplitter, QProgressBar, QToolBox, QLabel
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QLabel
import json

from src.application import *

class WindowTask(QSplitter):

    def __init__(self, window):
        self.window = window
        super().__init__(Qt.Vertical)

        self.setHandleWidth(0)

        self.fst_frame = QSplitter(Qt.Vertical)
        self.fst_frame.setHandleWidth(0)

        self.up_frame = QFrame(self)
        # self.up_frame.setFrameShape(QFrame.StyledPanel)
        self.up_text = QLabel(self.up_frame)
        self.up_text.setText("task_name")

        # f = open("coding_problems.json", "r")
        #
        # st = f.read()
        # st = f.read()
        # st = f.read()
        # st = f.read()
        #
        # name = st["problems_name"]

        self.bot_frame = QToolBox()
        self.bot_frame.insertItem(0, QLabel("Содержимое вкладки 1"), "Desctiption")#"Вкладка &1")
        self.bot_frame.insertItem(1, QLabel("Coдepжимoe вкладки 2"), "Examples")#"Вкладка &2")
        self.bot_frame.insertItem(2, QLabel("Coдepжимoe вкладки 3"), "Note")

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
        self.totalMin = 1

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
        min = int(self.count/60)
        sec = int(self.count % 60)
        self.val = min + sec/100
        self.snd_frame.setValue(self.count*100/(self.totalMin*60))
        self.snd_frame.setFormat('%.02f' % self.val)
        self.count += 1







