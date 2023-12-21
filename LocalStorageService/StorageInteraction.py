import random
import string

from Core.Exceptions import AuthException
from LocalStorageService.Connection import get_db

from LocalStorageService.Models import Users, Pools, Connections
from logger import err


class StorageInteraction:
    conn = get_db()

    def existed_users(self):
        users = self.conn.query(Users).all()
        if len(users) == 0:
            return None
        return True

    def check_user(self, password):
        user = self.conn.query(Users.username).filter(Users.password == password).first()
        if user is None:
            raise AuthException("User not Found")
        return user[0]

    def create_user(self, username, password, privilege):
        auth_key = "".join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)
                           for _ in range(128))
        new_user = Users(
            username=username,
            password=password,
            auth_key=auth_key,
            privilege=privilege
        )
        self.conn.add(new_user)
        self.conn.commit()
        return auth_key

    def root_user(self):
        user = self.conn.query(Users.username).filter(Users.privilege).all()
        try:
            return user[0][0]
        except IndexError:
            err("Root users not found")



