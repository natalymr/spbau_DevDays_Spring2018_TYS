from copy import deepcopy
from datetime import datetime, timedelta


class Task:
    def __init__(self, id, difficulty):
        self.id = id
        self.difficulty = difficulty


class SummaryStatistic:
    def __init__(self, easy_amount, mid_amount, hard_amount):
        self.easy_amount = easy_amount
        self.mid_amount = mid_amount
        self.hard_amount = hard_amount


class User:
    def __init__(self, login, passwd_hash, name):
        self.login = deepcopy(login)
        self.passwd_hash = deepcopy(passwd_hash)
        self.name = name
        self.born_date = datetime.now().date()
        self.login_date = datetime.now().date()
        self.per_week_task_solved = dict()      # week -> list of pair (task, result)
        self.best_task_solved = dict()          # ids -> score
        self.flatten_task_proposed = set()      # set of ids
        self.curr_session_task_solved = list()  # list of tasks

    def login_callback(self):
        self.login_date = datetime.now().date()

    def logout_callback(self, login_server):
        self._dump_curr_session()
        self.curr_session_task_solved = list()
        login_server.users[self.login] = self
        login_server.dump()

    def end_interview_callback(self, task_array):
        for task, result in task_array:
            best_score = self.best_task_solved.get(task.id)
            if best_score is None or best_score < result * task.difficulty:
                self.best_task_solved[task.id] = result * task.difficulty
                self.curr_session_task_solved.append((task, result))
        self._dump_curr_session()

    def _dump_curr_session(self):
        week_date = self._get_week_date()
        best_task_on_week = dict()  # id -> (task, result)
        for task, result in self.curr_session_task_solved:
            self.flatten_task_proposed.add(task.id)
            best_pair = best_task_on_week.get(task.id)
            if best_pair is not None:
                best_task, best_result = best_pair
                if result * task.difficulty <= best_result * best_task.difficulty:
                    continue
            best_task_on_week[task.id] = (task, result)
        best_task_list = list(best_task_on_week.values())
        if 0 < len(best_task_list):
            self.per_week_task_solved[week_date] = best_task_list

    def get_current_week_summary_statistic(self):
        week_date = self._get_week_date()
        easy_counter = 0
        mid_counter = 0
        hard_counter = 0
        task_solved = self.per_week_task_solved[week_date]
        for task, result in task_solved:
            if result:
                if task.difficulty == 1:
                    easy_counter += 1
                elif task.difficulty == 3:
                    mid_counter += 1
                elif task.difficulty == 5:
                    hard_counter += 1
        return SummaryStatistic(easy_counter, mid_counter, hard_counter)

    def get_summary_statistic(self):
        easy_counter = 0
        mid_counter = 0
        hard_counter = 0
        for score in self.best_task_solved.values():
            if score == 1:
                easy_counter += 1
            elif score == 3:
                mid_counter += 1
            elif score == 5:
                hard_counter += 1
        return SummaryStatistic(easy_counter, mid_counter, hard_counter)

    def get_statistic(self):
        import numpy as np
        date_list = list()
        acc_score_list = list()
        acc_score = 0
        for date, task_list in sorted(self.per_week_task_solved.items(), key=lambda p: p[0]):
            for task, result in task_list:
                acc_score += task.difficulty * result
            acc_score_list.append(acc_score)
            date_list.append(date)
        full_score_list = list()
        full_date_list = list()
        acc_score = 0
        if len(date_list):
            last_date = date_list[0]
            for i in range(len(date_list)):
                date = date_list[i]
                while last_date < date:
                    full_score_list.append(acc_score)
                    full_date_list.append(last_date)
                    last_date += timedelta(days=7)
                acc_score = acc_score_list[i]
        return (full_date_list, np.array(full_score_list))

    def _get_week_date(self):
        week_date = User.start_week_date(self.login_date)
        if week_date not in self.per_week_task_solved:
            self.per_week_task_solved[week_date] = list()
        return week_date

    @staticmethod
    def start_week_date(date):
        return date - timedelta(days=date.weekday())
