import os
from vk_api.utils import get_random_id
from enum import Enum

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
    comment = 'Hometask'
    attach = ''

class Diary(object):
    def send_last_ht(api, msg_id, user_id, subj):
        filename = 'data/Hometask/' + subj + '.txt'
        if os.path.exists(filename):
            with open(filename, 'r') as task:
                if sum(1 for c in task) > 0:
                    dic = {}
                    for line in task:
                        tmp = line.split('=')
                        dic[tmp[0]] = tmp[1].replace('\n', '')

                    msg = 'До: ' + dic['until'] + '\n' + 'Комментарий: ' + dic['comment'] + '\n'
                    # parse attach
                    api.messages.send(user_id=user_id, message=msg, reply_to=msg_id, random_id=get_random_id())
                    return
        else:
            open(filename, 'x')

        api.messages.send(user_id=user_id, message='По данному предмету дз не найдено', reply_to=msg_id, random_id=get_random_id())

    def set_ht(text, attach):
        return

class Info(object):
    path = 'data/Hometask/info.txt'

    def send_last_info(api, msg_id, user_id):
        if os.path.exists(Info.path):
            with open(Info.path, 'r') as task:
                content = task.read()
                
                # parse attach
                if len(content) != 0:
                    api.messages.send(user_id=user_id, message=content, reply_to=msg_id, random_id=get_random_id())
                    return
        else:
            open(Info.path, 'x')

        api.messages.send(user_id=user_id, message='Актуальная инфа отсутствует', reply_to=msg_id, random_id=get_random_id())

    def set_info(text, attach):
        if os.path.exists(Info.path) == False:
            open(Info.path, 'x')

        with open(Info.path, 'w') as info:
            info.write(text)
            info.write('\nattach=')
            for x in attach:
                info.write(str(x) + ',')
