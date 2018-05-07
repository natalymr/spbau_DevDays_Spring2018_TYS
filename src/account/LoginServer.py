import os
import pickle
import hashlib

from src.account.User import User
from src.task import ChatTask

class LoginServer:
    def __init__(self, file_name):
        self.file_name = file_name
        if not os.path.exists(file_name):
            with open(file_name, 'wb') as file:
                self.users = dict()
                pickle.dump(self.users, file)
        else:
            with open(file_name, 'rb') as file:
                self.users = pickle.load(file)

    def dump(self):
        with open(self.file_name, 'wb') as file:
            pickle.dump(self.users, file)

    def clean(self):
        os.remove(self.file_name)

    def register(self, login, passwd, name):
        passwd_hash = hashlib.sha256(passwd.encode()).hexdigest()
        user = User(login, passwd_hash, name)
        if user.login in self.users:
            return False
        self.users.update({user.login: user})
        return True

    def login(self, login, passwd):
        if login not in self.users:
            return None
        user = self.users[login]
        passwd_hash = hashlib.sha256(passwd.encode()).hexdigest()
        if passwd_hash != user.passwd_hash:
            return None
        user.login_callback()
        return user

    @staticmethod
    def test():
        login_server = LoginServer("test.pickle")
        login_server.register('u1', 'p1', 'n1')
        assert login_server.login('u1', 'p1') is not None, 'user must be registered'
        assert login_server.login('u1', 'p2') is None, 'must be invalid passwd'
        assert login_server.login('u2', 'p1') is None, 'user must not be registered'
        login_server.register('u2', 'p2', 'n2')
        assert login_server.login('u2', 'p2') is not None, 'user must be registered'

        login_server.dump()
        login_server = LoginServer("test.pickle")
        assert login_server.login('u1', 'p1') is not None, 'user must be registered'
        assert login_server.login('u2', 'p2') is not None, 'user must be registered'

        login_server.clean()
        login_server = LoginServer("test.pickle")
        assert login_server.login('u1', 'p1') is None, 'user must not be registered'
        assert login_server.login('u2', 'p1') is None, 'user must not be registered'
        login_server.clean()

    @staticmethod
    def fill_test_statistic():
        from random import randint
        from datetime import datetime, timedelta
        import matplotlib.pyplot as plt
        from matplotlib import dates
        import numpy as np

        login_server = LoginServer('LoginServer.pickle')
        login_server.register('old_boy', 'old_boy', 'name of old_boy')
        user = login_server.login('old_boy', 'old_boy')
        beginning_of_time = datetime.strptime("21/11/17 16:30", "%d/%m/%y %H:%M").date()
        now = datetime.now().date() - timedelta(days=20)
        count = 0
        while beginning_of_time < now:
            count += 1
            beginning_of_time += timedelta(days=randint(1, 27))
            user.login_date = beginning_of_time
            task_array = list()

            difficulty_class = randint(0, 2)
            difficulty = 5
            if difficulty_class == 0:
                difficulty = 1
            elif difficulty_class == 1:
                difficulty = 3
            result = randint(0, 1)
            task = ChatTask(None, difficulty, id=count)
            task_array.append((task, result))

            for i in range(randint(1, 5)):
                count += 1
                task = ChatTask(None, 1, id=count)
                result = randint(0, 1)
                task_array.append((task, result))
            user.end_interview_callback(task_array)
            user.logout_callback(login_server)
        date, data = user.get_statistic()
        t = date
        t = np.append(t, t[-1])
        s = np.append(data, 0)

        plt.gca().xaxis.set_major_formatter(dates.DateFormatter('%m/%Y'))
        plt.gca().xaxis.set_major_locator(dates.MonthLocator())
        plt.fill_between(t, np.zeros_like(s), s, color='g', alpha=.7)
        plt.plot(t, s, t, np.zeros_like(s), color='g', alpha=.74)
        plt.autoscale(enable=True, axis='x', tight=True)
        plt.show()


