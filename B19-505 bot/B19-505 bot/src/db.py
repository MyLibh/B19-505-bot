import io
import json
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
    PATH = 'data/users.json'

    users = {}
    last_action = {}

    def _read():
        with io.open(db.PATH, 'r', encoding='utf-8-sig') as file:  
            db.users = json.load(file)
                
    def _write():
        with io.open(db.PATH, 'w', encoding='utf-8-sig') as file:
            try:
               file.write(unicode(json.dumps(db.users, ensure_ascii=False, indent=4)))
            except NameError:
               file.write(str(json.dumps(db.users, ensure_ascii=False, indent=4)))

    def _add_to_db(id, role='user'):
        if id not in db.users:
            db.users[id] = role
            db.last_action[id] = Act.Empty
            db._write()

            return True
        else:
            return False

    def _rem_from_db(id, role=''):
        if len(role) == 0:
            db.users.pop(id)
        else:
            db.users[id] = role
        db._write()

    def load():
        db._read()

        for user_id in db.users:
            db.last_action[int(user_id)] = Act.Empty

    def add_user(id):
        return db._add_to_db(str(id))

    def remove_user(id):
        db._rem_from_db(str(id))

    def add_editor(id):
        return db._add_to_db(str(id), 'editor')

    def remove_editor(id):
        db._rem_from_db(str(id), 'user')