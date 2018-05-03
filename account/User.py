from copy import deepcopy
from datetime import datetime, timedelta


class Task:
    def __init__(self, name, score):
        self.name = name
        self.score = score


class User:
    def __init__(self, login, passwd_hash, name):
        self.login = deepcopy(login)
        self.passwd_hash = deepcopy(passwd_hash)
        self.name = name
        self.born_date = datetime.now().date()
        self.login_date = datetime.now().date()
        self.per_week_task_passed = dict()
        self.flatten_task_passed = list()

    def login_callback(self):
        last_login = self.login_date
        self.login_date = datetime.now().date()

    def logout_callback(self):
        self.login_date = datetime.now().date()

    @staticmethod
    def start_week_date(date):
        return date - timedelta(days=date.weekday())
