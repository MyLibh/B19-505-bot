import os
from enum import Enum
from vk_api.utils import get_random_id
from src.Core import Core

class Subject(Enum):
    Angem = 'ангем'
    Matan = 'матан'
    Evm = 'эвм'
    Inf = 'инфа'
    Ogz = 'огз' 
    Phys = 'физика'
    Disc = 'дискретка'

class Hometask(object):
    #until = ''
    subj = 'undefined'

class Diary(object):
    def send_last_ht(api, msg_id, user_id, subj):
        filename = 'data/Hometask/' + subj + '.txt'
        if os.path.exists(filename):
            with open(filename, 'r') as task:
                    text = ''
                    attach = []
                    for line in task.readlines():
                        if line.startswith('text'):
                            text = line[5:].replace('\n', '')
                        else:
                            attach = line[7:].replace(',', ' ').split()
                
                    api.messages.send(user_id=user_id, message=text, attachment=attach, reply_to=msg_id, random_id=get_random_id())
                    return

        api.messages.send(user_id=user_id, message='По данному предмету дз не найдено', reply_to=msg_id, random_id=get_random_id())

    def set_ht(text, attach, subj):
        filename = 'data/Hometask/' + subj + '.txt'
        if os.path.exists(filename) == False:
            open(filename, 'x')

        with open(filename, 'w') as task:
            task.write('text=')
            task.write(text)
            task.write('\nattach=')
            task.write(','.join(attach))

class Info(object):
    path = 'data/Hometask/info.txt'

    def send_last_info(api, msg_id, user_id):
        if os.path.exists(Info.path):
            with open(Info.path, 'r') as info:
                text = ''
                attach = []
                for line in info.readlines():
                    if line.startswith('text'):
                        text = line[5:].replace('\n', '')
                    else:
                        attach = line[7:].replace(',', ' ').split()
                
                api.messages.send(user_id=user_id, message=text, attachment=attach, reply_to=msg_id, random_id=get_random_id())
                return

        api.messages.send(user_id=user_id, message='Актуальная инфа отсутствует', reply_to=msg_id, random_id=get_random_id())

    def set_info(text, attach):
        if os.path.exists(Info.path) == False:
            open(Info.path, 'x')

        with open(Info.path, 'w') as info:
            info.write('text=')
            info.write(text)
            info.write('\nattach=')
            info.write(','.join(attach))

