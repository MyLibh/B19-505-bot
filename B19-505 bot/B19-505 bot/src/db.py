from enum import Enum

class Act(Enum):
    Empty = 0
    Report = 1
    Send = 2
    Choose = 3
    AddInfo = 5
    AddHT_subj = 6
    AddHT_task = 7
    Demote = 8
    Promote = 9
    GetClassbook = 10

class db(object):
    users = set()
    last_action = {}
    editors = set()
    admins = set()

    def _get_filename_by_db(dbase):
        if dbase is db.users:
            return 'users'
        elif dbase is db.editors:
            return 'editors'
        else:
            return 'admins'

    def _read(dbase):
        with open('data/' + db._get_filename_by_db(dbase) + '.txt') as file:
            for user in file.readlines():
                dbase.add(int(user))

    def _write(dbase):
        with open('data/' + db._get_filename_by_db(dbase) + '.txt', 'w') as file:
            for user in dbase:
                file.write(str(user) + '\n')

    def _add_to_db(dbase, id):
        if id not in dbase:
            dbase.add(id)
            db.last_action[id] = Act.Empty
            db._write(dbase)

            return True
        else:
            return False

    def _rem_from_db(dbase, id):
        dbase.discard(id)

        db._write(dbase)

    def load():
        db._read(db.users)
        db._read(db.editors)
        db._read(db.admins)

        for user in db.users:
            db.last_action[user] = Act.Empty

    def add_user(id):
        return db._add_to_db(db.users, id)

    def remove_user(id):
        db._rem_from_db(db.users, id)

    def add_editor(id):
        return db._add_to_db(db.editors, id)

    def remove_editor(id):
        db._rem_from_db(db.editors, id)