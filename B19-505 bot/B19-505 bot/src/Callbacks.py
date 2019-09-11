import re
from src.Logger import Log
from src.db import db
from vk_api.utils import get_random_id
from src.BotKeyboard import BotKeyboard
from src.Diary import Subject, Diary
from enum import Enum

class Act(Enum):
    Empty = 0
    Report = 1
    Send = 2
    AddInfo = 3
    AddHT   = 4

def OnEventNew(api, event):
    Log('MSG: ' + str(event.obj.from_id) + ' ' + event.obj.text)

    if OnEventNew.act_id == Act.Report and event.obj.from_id == OnEventNew.user_id:
        api.messages.send(user_id=event.obj.from_id, message='Спасибо за фидбэк!', reply_to=event.obj.id, random_id=get_random_id())
        api.messages.send(user_id=142026123, message='[BUGREPORT]:\n' + event.obj.text, random_id=get_random_id())
        OnEventNew.act_id = Act.Empty
        return 

    if len(event.obj.text) == 0:
        Log('ATTACHMENT')
        api.messages.send(user_id=event.obj.from_id, message='Извини, но я тебя не понимаю', reply_to=event.obj.id, random_id=get_random_id())
        return

    pattern = re.compile(r'\w+')
    cmd = pattern.findall(event.obj.text)[0]

    #:   editors
    if event.obj.from_id in db.editors:
        if OnEventNew.act_id == Act.Send and event.obj.from_id == OnEventNew.user_id:
            for user_id in db.users:
                if user_id != event.obj.from_id:
                    api.messages.send(user_id=user_id, message=event.obj.text, random_id=get_random_id())

            api.messages.send(user_id=event.obj.from_id, message='Рассылка выполнена', reply_to=event.obj.id, random_id=get_random_id())
            OnEventNew.act_id = Act.Empty
            return
        elif cmd.lower() == 'назад':
            BotKeyboard.send_menu_keyboard(api=api, user_id=event.obj.from_id, msg='Откатил', perms=5)
            return
        elif cmd.lower() == 'editor':
            BotKeyboard.send_editor_keyboard(api=api, user_id=event.obj.from_id)
            return
        elif cmd.lower() == 'рaзослать':
            OnEventNew.act_id = Act.Send
            OnEventNew.user_id = event.obj.from_id
            api.messages.send(user_id=event.obj.from_id, message='Каково будет сообщение?', reply_to=event.obj.id, random_id=get_random_id())
            return
        elif cmd.lower() == 'добавить':
            BotKeyboard.send_editor_keyboard_add(api=api, user_id=event.obj.from_id)
            return

    #:  users
    if cmd.lower() == 'help':
        api.messages.send(user_id=event.obj.from_id, message='start - подписаться на рассылку\nhelp - показать, что я умею\nreport - сообщить об ошибке', reply_to=event.obj.id, random_id=get_random_id())
    elif cmd.lower() == 'start' or cmd.lower() == 'начать':
        if db.add_user(event.obj.from_id) == True:
            api.messages.send(user_id=event.obj.from_id, message='Теперь ты подписан на рассылку', reply_to=event.obj.id, random_id=get_random_id())

            BotKeyboard.send_menu_keyboard(api, event.obj.from_id)
        else:
            api.messages.send(user_id=event.obj.from_id, message='Ты уже подписан', reply_to=event.obj.id, random_id=get_random_id())
    elif cmd.lower() == 'report':
        OnEventNew.act_id = Act.Report
        OnEventNew.user_id = event.obj.from_id
        api.messages.send(user_id=event.obj.from_id, message='Опиши проблему', reply_to=event.obj.id, random_id=get_random_id())
    elif cmd.lower() == 'info':
        api.messages.send(user_id=event.obj.from_id, message='Последняя актуальная информация:\nundefined', reply_to=event.obj.id, random_id=get_random_id())
    elif cmd.lower() == 'дз':
        BotKeyboard.send_ht_keyboard(api=api, user_id=event.obj.from_id)
    elif cmd.lower() == 'назад':
        BotKeyboard.send_menu_keyboard(api=api, user_id=event.obj.from_id, msg='Откатил')
    else:
        for subj in Subject:
            if subj.value == cmd.lower():
                Diary.send_last_ht(api, event.obj.id, event.obj.from_id, subj.value)
                return

        api.messages.send(user_id=event.obj.from_id, message='Извини, но я не умею отвечать на такой запрос', reply_to=event.obj.id, random_id=get_random_id())
OnEventNew.act_id = Act.Empty
OnEventNew.user_id = int()

def OnEventJoin(api, event):
    Log('JOIN: ' + str(event.obj.user_id))

def OnEventLeave(api, event):
    Log('LEAVE: ' + str(event.obj.user_id))

    db.remove_user(event.obj.user_id)

    api.messages.send(user_id=event.obj.user_id, message='Очень жаль, что ты покидаешь нас. Пока', random_id=get_random_id())

def onEventDefault(api, event):
    Log('EVENT: ' + str(event.type))