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

                    api.messages.send(user_id=user_id, message=msg, reply_to=msg_id, random_id=get_random_id())
                    return
        else:
            open(filename, 'x')

        api.messages.send(user_id=user_id, message='По данному предмету дз не найдено', reply_to=msg_id, random_id=get_random_id())



