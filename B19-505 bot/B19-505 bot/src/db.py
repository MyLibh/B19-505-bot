class db(object):
    def __init__(self):
        self.users = set()
        with open('data/users.txt') as db_users:
            lines = db_users.readlines()

            for user in lines:
                self.users.add(int(user))

    def __del__(self):
        with open('data/users.txt', 'w') as db_users:
            for user in self.users:
                db_users.write(str(user) + '\n')

    def add_user(self, id):
        if id not in self.users:
            self.users.add(int(id))

            return True
        else:
            return False

    def remove_user(self, id):
        self.users.discard(id)