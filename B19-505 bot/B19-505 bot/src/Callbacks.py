import random
import re
from src.Logger import Log
from src.db import db

def OnEventNew(api, event):
    Log('MSG: ' + str(event.obj.from_id) + ' ' + event.obj.text)

    if len(event.obj.text) == 0:
        Log('ATTACHMENT')
        api.messages.send(user_id=event.obj.from_id, message='Извини, но я тебя не понимаю', reply_to=event.obj.id, random_id=random.randint(0, 2e10))

        return

    pattern = re.compile(r'\w+')
    cmd = pattern.findall(event.obj.text)[0]

    if cmd == 'help':
        api.messages.send(user_id=event.obj.from_id, message='help - показать, что я умею\n\nДля редакторов:\nsendall - послать всем', reply_to=event.obj.id, random_id=random.randint(0, 2e10))
    elif cmd.lower() == 'start' or cmd.lower() == 'начать':
        if db.add_user(id=event.obj.from_id) == True:
            api.messages.send(user_id=event.obj.from_id, message='Теперь ты подписан на рассылку', reply_to=event.obj.id, random_id=random.randint(0, 2e10))
        else:
            api.messages.send(user_id=event.obj.from_id, message='Ты уже подписан', reply_to=event.obj.id, random_id=random.randint(0, 2e10))
    elif cmd == 'sendall' and 1:
        with open('data/users.txt') as users:
            lines = users.readlines()

            for user in lines:
                if int(user) != event.obj.from_id:
                    api.messages.send(user_id=int(user), message=event.obj.text[7:], random_id=random.randint(0, 2e10))

        api.messages.send(user_id=event.obj.from_id, message='Рассылка выполнена', reply_to=event.obj.id, random_id=random.randint(0, 2e10))

    else:
        api.messages.send(user_id=event.obj.from_id, message='Извини, но я не умею отвечать на такой запрос', reply_to=event.obj.id, random_id=random.randint(0, 2e10))

def OnEventJoin(api, event):
    Log('JOIN: ' + str(event.obj.user_id))

def OnEventLeave(api, event):
    Log('LEAVE: ' + str(event.obj.user_id))

    db.remove_user(event.obj.user_id)

    api.messages.send(user_id=event.obj.user_id, message='Очень жаль, что ты покидаешь нас. Пока', random_id=random.randint(0, 2e10))

def onEventDefault(api, event):
    Log('EVENT: ' + str(event.type))