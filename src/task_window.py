from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui

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


        # f = open("coding_problems.json", "r")
        #
        # st = f.readline()
        # st = f.readline()
        # st = f.readline()
        # st = f.readline()
        # st = st.replace("'", "\"")
        # ste = json.loads(st)
        # name = ste["problems_name"]
        #
        # examples_input = ste["sampleTests"]
        #
        # rows = len(examples_input)
        #
        # self.tableWidget = QTableWidget()
        # self.tableWidget.setRowCount(rows)
        # self.tableWidget.setColumnCount(2)

        # dt = ["input", "output"]
        # for i in range(rows):
        #     for j in range(2):
        #         self.tableWidget.setItem(i, j, QTableWidgetItem(examples_input[i][dt[j]]))


        # self.up_text.setText(name)
        self.up_text.setText("Потерянные улицы")
        self.bot_frame = QToolBox()
        # self.w = QWidget(self)
        # self.pic = QPixmap("src/task01.png")
        # self.label = QLabel(self.w)
        # self.label.setPixmap(self.pic)

        self.desc = "Компания РДЖ запланировала построить в стране новую железнодорожную сеть. В этой стране имеется n городов.\n\
РДЖ запланировала построить m новых двунаправленных дорог, которые будут соединять города этой страны.\n\
Разумеется, на строительство сети планируется потратить как можно меньше средств из бюджета, поэтому был \n\
составлен план строительства, где был произведен расчет кратчайших расстояний между каждой парой городов. \n\
План представляет собой матрицу, где на пересечении i-ой и j-ой строки записано число, равное кратчайшему \n\
расстоянию между городами i и j. Железнодорожная сеть представляет собой набор участков железной дороги, \n\
каждый участок соединяет два различных города. Между двумя любыми городами существует не более одного участка\n\
железной дороги. Помогите восстановить дорожную сеть между городами, если возможно построить её согласно плану."


        self.io = 'Input:\n\
В первой строке входных данных даны два целых числаnиm  количество городов\n\
и дорог в стране(1<=n<=500,0<= m <=2000). В последующихnстроках содержится\n\
таблица кратчайших расстояниймежду каждой парой городов, элементы таблицы - целые\n\
неотрицательные числа, не превышающие10^6\n\
Output:\nЕсли такая сеть существует, выведите в первой строке сообщение "YES" (без кавычек),\n\
в противном случае   сообщение "NO" (без кавычек). сеть существует, то, \n\
начиная со второй строки, выведитеmтроек целых чисел, описывающих участки\n\
железной дороги. Каждый участок железной дороги описы-вается номерами городов,\n\
которые им соединяются и его длину. Длина любого участка должна бытьположительнаи\n\
не должна превышать10^6'


        self.examp = 'input:\n\
4 4\n\
0 1 2 5\n\
1 0 3 4\n\
2 3 0 7\n\
5 4 7 0\n\
OUTPUT:\n\
YES\n\
2 1 1\n\
1 3 2\n\
2 4 4\n\
1 4 5\n\
INPUT:\n\
3 2\n\
0 1 1\n\
1 0 1\n\
1 1 0,\n\
OUTPUT:\n\
NO\n'

        self.bot_frame.insertItem(0, QLabel(self.desc), "Desctiption")#"Вкладка &1")
        # self.bot_frame.insertItem(0, self.w, "Desctiption")
        # self.label.show()
        # self.w.show()
        self.bot_frame.insertItem(1, QLabel(self.io), "I/O Format")#"Вкладка &2")
        self.bot_frame.insertItem(2, QLabel(self.examp), "Examples")
        # self.bot_frame.insertItem(2, self.tableWidget, "Examples")

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
        self.totalMin = 5

        self.addWidget(self.fst_frame)
        self.addWidget(self.snd_frame)
        self.setSizes([self.width() * 11 // 12,
                       self.width() // 12])

        self.count = 1
        self.scale = 1000
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.tick_status)
        self.timer.start(1000)


    # def update_task(self, task):
    #     if task.type == TaskType.CODING:
    #         pass

    def tick_status(self):
        min = int(self.count/60)
        sec = int(self.count % 60)
        self.val = min + sec/100
        self.snd_frame.setValue(self.count*100/(self.totalMin*60))
        self.snd_frame.setFormat('%.02f' % self.val)
        self.count += 1
        if self.count == 6:
            self.window.chat_window.run_task(self.window.chat_tasks[1][1]) # yes no
        if self.count == 12:
            self.window.chat_window.run_task(self.window.chat_tasks[1][3])  # test
        if self.count == 18:
            self.window.chat_window.run_task(self.window.chat_tasks[1][5]) # single
        if self.count > 300:
            self.timer.stop()

