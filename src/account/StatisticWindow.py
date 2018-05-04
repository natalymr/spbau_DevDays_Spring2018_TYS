# embedding_in_qt5.py --- Simple Qt5 application embedding matplotlib canvases
#
# Copyright (C) 2005 Florent Rougon
#               2006 Darren Dale
#               2015 Jens H Nielsen
#
# This file is an example program for matplotlib. It may be used and
# modified with no restriction; raw copies as well as modified versions
# may be distributed without limitation.


import sys
import os
import random
import matplotlib

# Make sure that we are using QT5
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel, QGridLayout

matplotlib.use('Qt5Agg')
from PyQt5 import QtCore, QtWidgets

import numpy as np
from numpy import arange, sin, pi, linspace, zeros_like
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib import dates


class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100, user=None):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        self.user = user

        self.compute_initial_figure()

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self):
        pass


class ByWeekStatisticCanvas(MplCanvas):
    def compute_initial_figure(self):
        assert self.user is not None, 'user must be not None'
        data = self.user.get_statistic()
        if len(data):
            date, data = self.user.get_statistic()
            t = date
            t = np.append(t, t[-1])
            s = np.append(data, 0)
            self.axes.xaxis.set_major_formatter(dates.DateFormatter('%m/%Y'))
            self.axes.xaxis.set_major_locator(dates.MonthLocator())
            self.axes.fill_between(t, zeros_like(s), s, color='g', alpha=.7)
            self.axes.plot(t, s, t, zeros_like(s), color='g', alpha=.74)
            self.axes.autoscale(enable=True, axis='x', tight=True)
            self.axes.set_ylabel('Score')


class StatisticWindow(QtWidgets.QMainWindow):
    def __init__(self, user):
        QtWidgets.QMainWindow.__init__(self)
        self.setWindowTitle("application main window")

        self.main_widget = QtWidgets.QWidget(self)

        grid = QGridLayout()
        grid.setSpacing(10)

        sc = ByWeekStatisticCanvas(self.main_widget, width=5, height=4, dpi=100, user=user)

        progress_week_label = QLabel('Progress during week:', self.main_widget)
        progress_week_label.setFont(QFont("Times", 14, QFont.Bold))

        week_stat = user.get_current_week_summary_statistic()
        week_stat_easy_label = QLabel('Easy:', self.main_widget)
        week_stat_easy_v_label = QLabel('%s' % (145 + week_stat.easy_amount), self.main_widget)
        week_stat_mid_label = QLabel('Median:', self.main_widget)
        week_stat_mid_v_label = QLabel('%s' % (146 + week_stat.mid_amount), self.main_widget)
        week_stat_hard_label = QLabel('Hard:', self.main_widget)
        week_stat_hard_v_label = QLabel('%s' % (147 + week_stat.hard_amount), self.main_widget)

        progress_label = QLabel('Progress during all time:', self.main_widget)
        progress_label.setFont(QFont("Times", 14, QFont.Bold))

        stat = user.get_summary_statistic()
        stat_easy_label = QLabel('Easy:', self.main_widget)
        stat_easy_v_label = QLabel('%s' % (145 + stat.easy_amount), self.main_widget)
        stat_mid_label = QLabel('Median:', self.main_widget)
        stat_mid_v_label = QLabel('%s' % (146 + stat.mid_amount), self.main_widget)
        stat_hard_label = QLabel('Hard:', self.main_widget)
        stat_hard_v_label = QLabel('%s' % (147 + stat.hard_amount), self.main_widget)

        grid.addWidget(sc, 1, 0, 5, 2)
        grid.addWidget(progress_week_label, 6, 0, 1, 2)
        grid.addWidget(week_stat_easy_label, 7, 0, 1, 1)
        grid.addWidget(week_stat_easy_v_label, 7, 1)
        grid.addWidget(week_stat_mid_label, 8, 0)
        grid.addWidget(week_stat_mid_v_label, 8, 1)
        grid.addWidget(week_stat_hard_label, 9, 0)
        grid.addWidget(week_stat_hard_v_label, 9, 1)

        grid.addWidget(progress_label, 6+9, 0, 1, 2)
        grid.addWidget(stat_easy_label, 7+9, 0, 1, 1)
        grid.addWidget(stat_easy_v_label, 7+9, 1)
        grid.addWidget(stat_mid_label, 8+9, 0)
        grid.addWidget(stat_mid_v_label, 8+9, 1)
        grid.addWidget(stat_hard_label, 9+9, 0)
        grid.addWidget(stat_hard_v_label, 9+9, 1)


        self.main_widget.setLayout(grid)
        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)
        self.statusBar().showMessage("All hail matplotlib!", 2000)
