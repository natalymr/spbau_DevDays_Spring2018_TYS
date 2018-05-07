import matplotlib

# Make sure that we are using QT5
from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QGridLayout, QVBoxLayout
matplotlib.use('Qt5Agg')

import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib import dates
from PyQt5.QtWidgets import *

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
        date, data = self.user.get_statistic()
        if len(data):
            t = date
            t = np.append(t, t[-1])
            s = np.append(data, 0)
            self.axes.xaxis.set_major_formatter(dates.DateFormatter('%m/%Y'))
            self.axes.xaxis.set_major_locator(dates.MonthLocator())
            self.axes.fill_between(t, np.zeros_like(s), s, color='g', alpha=.7)
            self.axes.plot(t, s, t, np.zeros_like(s), color='g', alpha=.74)
            self.axes.autoscale(enable=True, axis='x', tight=True)
            self.axes.set_ylabel('Score')


class StatisticWindow(QVBoxLayout):
    def __init__(self, user, main_window):
        super(StatisticWindow, self).__init__()
        self.windowTitle = "Try Your Skills: Statistic"

        grid = QGridLayout()
        grid.setSpacing(10)

        sc = ByWeekStatisticCanvas(width=5, height=4, dpi=100, user=user)

        progress_week_label = QLabel('<center> Progress during week: <\center>')
        progress_week_label.setFont(QFont("Times", 14, QFont.Bold))
        week_stat = user.get_current_week_summary_statistic()
        week_stat_easy_label = QLabel('<center> Easy:\t\t%s<\center>' % (week_stat.easy_amount))
        font = week_stat_easy_label.font()
        font.setPointSizeF(12)
        week_stat_easy_label.setFont(font)
        week_stat_mid_label = QLabel('<center> Median:\t\t%s<\center>' % (week_stat.mid_amount))
        week_stat_mid_label.setFont(font)
        week_stat_hard_label = QLabel('<center> Hard:\t\t%s<\center>' % (week_stat.hard_amount))
        week_stat_hard_label.setFont(font)

        progress_label = QLabel('<center> Progress during all time: <\center>')
        progress_label.setFont(QFont("Times", 14, QFont.Bold))
        stat = user.get_summary_statistic()
        stat_easy_label = QLabel('<center> Easy: %s<\center>' % (stat.easy_amount))
        stat_easy_label.setFont(font)
        stat_mid_label = QLabel('<center> Median: %s<\center>' % (stat.mid_amount))
        stat_mid_label.setFont(font)
        stat_hard_label = QLabel('<center> Hard: %s<\center>' % (stat.hard_amount))
        stat_hard_label.setFont(font)


        self.addWidget(sc)
        self.addWidget(progress_week_label)
        self.addWidget(week_stat_easy_label)
        self.addWidget(week_stat_mid_label)
        self.addWidget(week_stat_hard_label)
        self.addWidget(progress_label)
        self.addWidget(stat_easy_label)
        self.addWidget(stat_mid_label)
        self.addWidget(stat_hard_label)
        self.setAlignment(Qt.AlignCenter)

        back_button = QPushButton('Back')
        back_button.setShortcut('Esc')
        back_button.setFixedSize(225, 25)
        back_button.clicked.connect(main_window.set_account_window)
        back_button.move(100, 100)
        back_button.setShortcut('Esc')
        self.addWidget(back_button)