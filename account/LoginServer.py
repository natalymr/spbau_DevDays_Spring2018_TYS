import os
import pickle
import hashlib


class User:
    def __init__(self, login, passwd_hash, name):
        self.login = login
        self.name = name
        self.passwd_hash = passwd_hash


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

# LoginServer.test()
