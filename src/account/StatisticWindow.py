
import matplotlib

# Make sure that we are using QT5
from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel, QGridLayout, QVBoxLayout
matplotlib.use('Qt5Agg')

import numpy as np
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
    def __init__(self, user):
        super(StatisticWindow, self).__init__()
        self.windowTitle = "TYS: statistic"

        grid = QGridLayout()
        grid.setSpacing(10)

        sc = ByWeekStatisticCanvas(width=5, height=4, dpi=100, user=user)

        progress_week_label = QLabel('Progress during week:')
        progress_week_label.setFont(QFont("Times", 14, QFont.Bold))

        week_stat = user.get_current_week_summary_statistic()
        week_stat_easy_label = QLabel('Easy:')
        week_stat_easy_v_label = QLabel('%s' % (week_stat.easy_amount))
        week_stat_mid_label = QLabel('Median:')
        week_stat_mid_v_label = QLabel('%s' % (week_stat.mid_amount))
        week_stat_hard_label = QLabel('Hard:')
        week_stat_hard_v_label = QLabel('%s' % (week_stat.hard_amount))

        progress_label = QLabel('Progress during all time:')
        progress_label.setFont(QFont("Times", 14, QFont.Bold))

        stat = user.get_summary_statistic()
        stat_easy_label = QLabel('Easy:')
        stat_easy_v_label = QLabel('%s' % (stat.easy_amount))
        stat_mid_label = QLabel('Median:')
        stat_mid_v_label = QLabel('%s' % (stat.mid_amount))
        stat_hard_label = QLabel('Hard:')
        stat_hard_v_label = QLabel('%s' % (stat.hard_amount))

        grid.addWidget(sc, 1, 0, 5, 2)
        grid.addWidget(progress_week_label, 6, 0, 1, 2)
        grid.addWidget(week_stat_easy_label, 7, 0, 1, 1)
        grid.addWidget(week_stat_easy_v_label, 7, 1)
        grid.addWidget(week_stat_mid_label, 8, 0)
        grid.addWidget(week_stat_mid_v_label, 8, 1)
        grid.addWidget(week_stat_hard_label, 9, 0)
        grid.addWidget(week_stat_hard_v_label, 9, 1)

        grid.addWidget(progress_label, 6 + 9, 0, 1, 2)
        grid.addWidget(stat_easy_label, 7 + 9, 0, 1, 1)
        grid.addWidget(stat_easy_v_label, 7 + 9, 1)
        grid.addWidget(stat_mid_label, 8 + 9, 0)
        grid.addWidget(stat_mid_v_label, 8 + 9, 1)
        grid.addWidget(stat_hard_label, 9 + 9, 0)
        grid.addWidget(stat_hard_v_label, 9 + 9, 1)

        self.addLayout(grid)
