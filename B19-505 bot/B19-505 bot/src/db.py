class db(object):
    users = set()
    editors = set()
    admins = set()
    def load():
        with open('data/users.txt') as db_users:
            for user in db_users.readlines():
                db.users.add(int(user))

        with open('data/editors.txt') as db_editors:
            for user in db_editors.readlines():
                db.editors.add(int(user))

        with open('data/admins.txt') as db_admins:
            for user in db_admins.readlines():
                db.admins.add(int(user))

    @staticmethod
    def add_user(id):
        if id not in db.users:
            db.users.add(int(id))
            with open('data/users.txt', 'w') as db_users:
                for user in db.users:
                    db_users.write(str(user) + '\n')

            return True
        else:
            return False

    @staticmethod
    def remove_user(self, id):
        db.users.discard(id)

        with open('data/users.txt', 'w') as db_users:
            for user in db.users:
                db_users.write(str(user) + '\n')