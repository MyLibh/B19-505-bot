import datetime
from vk_api.utils import get_random_id

class Shedule(object):
    PATH = 'data/shedule.json'

    def _get_cur_week():
        if int(datetime.date(2019, 9, 1).isocalendar()[1] - datetime.datetime.today().isocalendar()[1] + 1) % 2 == 0:
            return 'even'
        else:
            return 'odd'

    def _get_weekday():
        return datetime.datetime.today().weekday()

    def get_shedule_today(api, user_id, msg_id):
        with open(Shedule.PATH, 'r', encoding='utf-8') as file:
                data = json.loads(file.read())
                
                api.messages.send(user_id=user_id, message=data[Shedule._get_cur_week()][Shedule._get_weekday()], reply_to=msg_id, random_id=get_random_id())
        return

    def get_shedule_tomorrow():
        return
