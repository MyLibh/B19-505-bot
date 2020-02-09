import os
import json
from enum import Enum
from vk_api.utils import get_random_id
from src.Core import Core

class Subject(Enum):
    Angem = 'ангем'
    Matan = 'матан'
    Inf = 'инфа'
    History = 'история' 
    Phys = 'физика'
    Disc = 'комба'
    NumTheory = 'тч'

def is_subject(text):
    for subj in Subject:
        if subj.value == text:
            return True
    return False

class Hometask(object):
    subj = 'undefined'

class Diary(object):
    def _filename(subj):
        return 'data/Hometask/' + subj + '.json'

    def send_last_ht(api, msg_id, user_id, subj):
        filename = Diary._filename(subj)
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as file:
                data = json.loads(file.read())
                
                api.messages.send(user_id=user_id, message=data['text'], attachment=data['attachment'], reply_to=msg_id, random_id=get_random_id())
        else:                
            api.messages.send(user_id=user_id, message='По данному предмету дз не найдено', reply_to=msg_id, random_id=get_random_id())

    def set_ht(text, attach, subj):
        filename = Diary._filename(subj)
        if os.path.exists(filename) == False:
            open(filename, 'x')

        data = {'text': text, 'attachment': attach}
        with open(filename, 'w', encoding='utf-8') as file:
           try:
               file.write(unicode(json.dumps(data, ensure_ascii=False, indent=4)))
           except NameError:
               file.write(str(json.dumps(data, ensure_ascii=False, indent=4)))

class Info(object):
    PATH = 'data/Hometask/info.json'

    def send_last_info(api, msg_id, user_id):
        if os.path.exists(Info.PATH):
            with open(Info.PATH, 'r', encoding='utf-8') as file:
                data = json.loads(file.read())
                
                api.messages.send(user_id=user_id, message=data['text'], attachment=data['attachment'], reply_to=msg_id, random_id=get_random_id())
        else:
            api.messages.send(user_id=user_id, message='Актуальная инфа отсутствует', reply_to=msg_id, random_id=get_random_id())

    def set_info(text, attach):
        if os.path.exists(Info.PATH) == False:
            open(Info.PATH, 'x')

        data = {'text': text, 'attachment': attach}
        with open(Info.PATH, 'w', encoding='utf-8') as file:
           try:
               file.write(unicode(json.dumps(data, ensure_ascii=False, indent=4)))
           except NameError:
               file.write(str(json.dumps(data, ensure_ascii=False, indent=4)))