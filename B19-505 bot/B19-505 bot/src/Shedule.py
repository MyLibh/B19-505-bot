import json
import io
import calendar
import datetime
from datetime import date
from vk_api.utils import get_random_id

class Shedule(object):
    PATH = 'data/shedule.json'

    def _get_cur_week(cur_day=date.today()):
        if int(date(2019, 9, 1).isocalendar()[1] - cur_day.isocalendar()[1] + 1) % 2 == 0:
            return 'even'
        else:
            return 'odd'

    def _get_weekday(weekday=date.today().weekday()):
        return calendar.day_name[weekday]

# [time]
# type subj
# teacher
# spot
    def send_shedule_today(api, user_id, msg_id):
        with io.open(Shedule.PATH, 'r', encoding='utf-8-sig') as file:  
            data = json.load(file)
            text = ''
            for lesson in data['weeks'][Shedule._get_cur_week()][Shedule._get_weekday()]:
                text += '[' + lesson['time'] + ']\n' + lesson['type'] + ' ' + lesson['subj'] + '\n' + lesson['teacher'] + '\n' + lesson['spot'] + '\n\n'

            if len(text) == 0:
                text = 'Пар нет!'

            api.messages.send(user_id=user_id, message=text, reply_to=msg_id, random_id=get_random_id())

    def send_shedule_tomorrow(api, user_id, msg_id):
        with io.open(Shedule.PATH, 'r', encoding='utf-8-sig') as file:  
            data = json.load(file)
            text = ''
            week = Shedule._get_cur_week(date.today() + datetime.timedelta(days=1))
            weekday = Shedule._get_weekday((date.today() + datetime.timedelta(days=1)).weekday())
            for lesson in data['weeks'][week][weekday]:
                text += '[' + lesson['time'] + ']\n' + lesson['type'] + ' ' + lesson['subj'] + '\n' + lesson['teacher'] + '\n' + lesson['spot'] + '\n\n'

            if len(text) == 0:
                text = 'Пар нет!'

            api.messages.send(user_id=user_id, message=text, reply_to=msg_id, random_id=get_random_id())

    def send_full_shedule(api, user_id, msg_id):
        with io.open(Shedule.PATH, 'r', encoding='utf-8-sig') as file:  
            data = json.load(file)
            api.messages.send(user_id=user_id, attachment=data['full'], reply_to=msg_id, random_id=get_random_id())
