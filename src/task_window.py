from PyQt5.QtWidgets import QFrame, QSplitter, QProgressBar
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui
from src.application import *

class WindowTask(QSplitter):

    def __init__(self, window):
        self.window = window
        super().__init__(Qt.Vertical)



        fst_frame = QFrame(self)
        fst_frame.setFrameShape(QFrame.StyledPanel)


        self.snd_frame = QProgressBar(self)
        self.snd_frame.setValue(0)
        palette = QtGui.QPalette(self.palette())
        palette.setColor(QtGui.QPalette.Highlight,
                         QtGui.QColor(QtCore.Qt.green))
        self.snd_frame.setPalette(palette)
        self.val = 0.00
        self.snd_frame.setFormat('0.00')
        self.totalMin = 1


        self.addWidget(fst_frame)
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







