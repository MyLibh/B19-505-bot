from src.Logger import Log
from src.db import db, Act
from vk_api.utils import get_random_id
from src.BotKeyboard import BotKeyboard, BKPerms
from src.Diary import *
from src.Util import *
from src.Shedule import Shedule

def _handle_admins(api, user, text, atts, msg_id):
    if user in db.admins:
        if db.last_action[user] == Act.Demote:
            if text == 'назад':
                db.last_action[user] = Act.Empty    
                BotKeyboard.send_admin_keyboard(api=api, user_id=user)               
            else:
                id = get_user_id(api, text)
                if id in db.editors:
                    db.remove_editor(id)
                    BotKeyboard.send_menu_keyboard(api=api, user_id=id, msg='Тебя понизили')
                    api.messages.send(user_id=user, message='Demoted', reply_to=msg_id, random_id=get_random_id())
                else:
                    api.messages.send(user_id=user, message='Not an editor', reply_to=msg_id, random_id=get_random_id())
                db.last_action[user] = Act.Empty
        elif db.last_action[user] == Act.Promote:
            if text == 'назад':
                db.last_action[user] = Act.Empty    
                BotKeyboard.send_admin_keyboard(api=api, user_id=user)                
            else:
                id = get_user_id(api, text)
                if db.add_editor(id) == True:
                    BotKeyboard.send_menu_keyboard(api=api, user_id=id, msg='Поздравляю!\nТеперь ты редактор', perms=BKPerms.EDITOR)
                    api.messages.send(user_id=user, message='Promoted', reply_to=msg_id, random_id=get_random_id())
                else:
                    api.messages.send(user_id=user, message='Already editor', reply_to=msg_id, random_id=get_random_id())
                db.last_action[user] = Act.Empty
        elif text == 'admin':
            BotKeyboard.send_admin_keyboard(api=api, user_id=user)
        elif text == 'demote':
            db.last_action[user] = Act.Demote
            api.messages.send(user_id=user, message='Enter acc link to demote', reply_to=msg_id, random_id=get_random_id())
        elif text == 'promote':
            db.last_action[user] = Act.Promote
            api.messages.send(user_id=user, message='Enter acc link to promote', reply_to=msg_id, random_id=get_random_id())
        elif text == 'назад':
            db.last_action[user] = Act.Empty
            BotKeyboard.send_menu_keyboard(api=api, user_id=user, msg='Откатил', perms=BKPerms.ADMIN)       
        else:
            return False
        return True
    else:
        return False
        
def _handle_editors(api, user, text, atts, msg_id):
    if user in db.editors:
        if db.last_action[user] == Act.Send:
            if text == 'назад':
                db.last_action[user] = Act.Empty    
                BotKeyboard.send_editor_keyboard(api=api, user_id=user)                 
            else:
                for user_id in db.users:
                    if user_id != user:
                        api.messages.send(user_id=user_id, message=text, attachment=get_attachs(atts), random_id=get_random_id())
                db.last_action[user] = Act.Empty
                api.messages.send(user_id=user, message='Рассылка выполнена', reply_to=msg_id, random_id=get_random_id())
        elif db.last_action[user] == Act.AddInfo:
            if text == 'назад':
                db.last_action[user] = Act.Choose
                BotKeyboard.send_editor_keyboard_add(api=api, user_id=user)                    
            else:
                if len(text) == 0:
                    text = 'Info'
                Info.set_info(text, get_attachs(atts))
                BotKeyboard.send_menu_keyboard(api=api, user_id=user, msg='Добавлено!', perms=BKPerms.EDITOR)
                db.last_action[user] = Act.Empty
        elif db.last_action[user] == Act.Choose:
            if text == 'дз':
                db.last_action[user] = Act.AddHT_subj
                BotKeyboard.send_ht_keyboard(api=api, user_id=user)
            elif text == 'информация':
                db.last_action[user] = Act.AddInfo
                api.messages.send(user_id=user, message='Какой инфой хочешь поделиться?', random_id=get_random_id())
            elif text == 'назад':
                db.last_action[user] = Act.Empty
                BotKeyboard.send_editor_keyboard_add(api=api, user_id=user)
            else: 
                db.last_action[user] = Act.Empty
                BotKeyboard.send_menu_keyboard(api=api, user_id=user, msg='Давай по новой', perms=BKPerms.EDITOR)
        elif db.last_action[user] == Act.AddHT_subj:
            if text == 'назад':
                db.last_action[user] = Act.Choose
                BotKeyboard.send_editor_keyboard_add(api=api, user_id=user)
            else:
                for subj in Subject:
                    if subj.value == text:
                        db.last_action[user] = Act.AddHT_task
                        Hometask.subj = subj.value
                        api.messages.send(user_id=user, message='Добавляй!', random_id=get_random_id())
                        return True
                db.last_action[user] = Act.Choose
                api.messages.send(user_id=user, message='Я не знаю такого предмета...', reply_to=msg_id, random_id=get_random_id())
                BotKeyboard.send_editor_keyboard_add(api=api, user_id=user)
        elif db.last_action[user] == Act.AddHT_task:
            if text == 'назад':
                db.last_action[user] = Act.Choose
                BotKeyboard.send_editor_keyboard_add(api=api, user_id=user)
            else:
                if len(text) == 0:
                    text = 'Hometask'
                Diary.set_ht(text, get_attachs(atts), Hometask.subj)
                BotKeyboard.send_menu_keyboard(api=api, user_id=user, msg='Домашка добавлена!', perms=BKPerms.EDITOR)
                db.last_action[user] = Act.Empty
        elif text == 'назад':
            db.last_action[user] = Act.Empty
            BotKeyboard.send_menu_keyboard(api=api, user_id=user, msg='Откатил', perms=BKPerms.EDITOR)       
        elif text == 'editor':
            BotKeyboard.send_editor_keyboard(api=api, user_id=user)
        elif text == 'рaзослать':
            db.last_action[user] = Act.Send
            api.messages.send(user_id=user, message='Каково будет сообщение?', reply_to=msg_id, random_id=get_random_id())
        elif text == 'добавить':
            db.last_action[user] = Act.Choose
            BotKeyboard.send_editor_keyboard_add(api=api, user_id=user)     
        else:
            return False
        return True
    else:
        return False

def _handle_users(api, user, text, atts, msg_id):
    if user in db.users:
        if db.last_action[user] == Act.Report:
            db.last_action[user] = Act.Empty
            if text != 'назад':
                api.messages.send(domain='big_black_hot_brother', message='[BUGREPORT]:\n' + text, random_id=get_random_id())
            BotKeyboard.send_menu_keyboard(api=api, user_id=user, msg='Спасибо за фидбэк!') 
        elif text == 'help':
            api.messages.send(user_id=user, message='start - подписаться на рассылку\nhelp - показать, что я умею\nreport - сообщить об ошибке', reply_to=msg_id, random_id=get_random_id())
        elif text == 'start' or text == 'начать' or text == 'старт':
             api.messages.send(user_id=user, message='Ты уже подписан', reply_to=msg_id, random_id=get_random_id())
        elif text == 'report':
            db.last_action[user] = Act.Report 
            BotKeyboard.send_report_keyboard(api, user)
        elif text == 'info':
            Info.send_last_info(api, msg_id, user)
        elif text == 'дз':
            BotKeyboard.send_ht_keyboard(api=api, user_id=user)
        elif text == 'назад':
            BotKeyboard.send_menu_keyboard(api=api, user_id=user, msg='Откатил')
        elif text == 'расписание':
            BotKeyboard.send_shedule_keyboard(api, user)
        elif is_subject(text):
            Diary.send_last_ht(api, msg_id, user, text)
        else:
            api.messages.send(user_id=user, message='Извини, но я не умею отвечать на такой запрос', reply_to=msg_id, random_id=get_random_id())
        return True
    else:
        return False

def OnEventNew(api, event):
    user = event.obj.from_id
    text = event.obj.text.lower()
    atts = event.obj.attachments
    msg_id = event.obj.id

    Log('MSG: ' + str(user))

    if _handle_admins(api, user, text, atts, msg_id) == False:
        if _handle_editors(api, user, text, atts, msg_id) == False:
            if _handle_users(api, user, text, atts, msg_id) == False:
                if text == 'start' or text == 'начать' or text == 'старт':
                    if db.add_user(user) == True:
                        api.messages.send(user_id=user, message='Теперь ты подписан на рассылку', reply_to=msg_id, random_id=get_random_id())
                        BotKeyboard.send_menu_keyboard(api, user)
                    else:
                        api.messages.send(user_id=user, message='Отправь start/начать/старт, чтобы подписаться', reply_to=msg_id, random_id=get_random_id())
        
def OnEventJoin(api, event):
    Log('JOIN: ' + str(event.obj.user_id))

def OnEventLeave(api, event):
    Log('LEAVE: ' + str(event.obj.user_id))

    db.remove_user(event.obj.user_id)

    api.messages.send(user_id=event.obj.user_id, message='Очень жаль, что ты покидаешь нас. Пока', random_id=get_random_id())

def onEventDefault(api, event):
    Log('EVENT: ' + str(event.type))