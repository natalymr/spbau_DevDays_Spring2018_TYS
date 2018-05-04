from copy import deepcopy
from datetime import datetime, timedelta


class Task:
    def __init__(self, name, score, date):
        self.name = name
        self.score = score
        self.date = date


class User:
    def __init__(self, login, passwd_hash, name):
        self.login = deepcopy(login)
        self.passwd_hash = deepcopy(passwd_hash)
        self.name = name
        self.born_date = datetime.now().date()
        self.login_date = datetime.now().date()
        self.per_week_task_solved = dict()   # week -> list of tasks
        self.best_task_solved = dict()       # names -> score
        self.flatten_task_proposed = set()   # set of names
        self.curr_week_task_solved = list()  # list of tasks

    def login_callback(self):
        last_login = self.login_date
        self.login_date = datetime.now().date()
        if User.start_week_date(last_login) != User.start_week_date(self.login_date):
            best_task_on_week = dict()      # name -> task
            for task in self.curr_week_task_solved:
                best_task = best_task_on_week.get(task.name)
                if best_task is None or best_task.score < task.score:
                    best_task_on_week[task.name] = task
            best_task_list = best_task_on_week.values()
            if 0 < len(best_task_list):
                self.per_week_task_solved[last_login] = best_task_list
            self.curr_week_task_solved = list()

    def logout_callback(self):
        self.login_date = datetime.now().date()

    def start_task_callback(self, task):
        self.flatten_task_proposed.add(task.name)

    def end_task_callback(self, task):
        best_score = self.best_task_solved.get(task.name)
        if best_score is None or best_score < task.score:
            self.best_task_solved[task.name] = task.score
            if User.start_week_date(self.login_date) < User.start_week_date(task.date):
                self.login_date = datetime.now().date()
                self.curr_week_task_solved = list()
            if User.start_week_date(self.login_date) == User.start_week_date(task.date):
                self.curr_week_task_solved.append(task)

    def get_current_statistic(self):z
        pass

    @staticmethod
    def start_week_date(date):
        return date - timedelta(days=date.weekday())
