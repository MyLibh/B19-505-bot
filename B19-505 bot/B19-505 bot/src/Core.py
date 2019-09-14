import vk_api
from vk_api import VkUpload
from vk_api.bot_longpoll import VkBotEventType

from src.Config import Config
from src.LongPoll import LongPoll
from src.db import db
from src.BotKeyboard import BotKeyboard, BKPerms
from src.Logger import Log
import src.Callbacks

class Core(object):
    session = None
    api = None
    longpoll = None
    upload = None

    def init():
        Log('')
        Log('Starting...')

        Config.load('config/credentials.json')
        Log('Config loaded')

        Core.session  = vk_api.VkApi(token=Config.token)
        Core.api      = Core.session.get_api()
        Core.longpoll = LongPoll(Core.session, Config.group_id)
        Core.upload   = VkUpload(Core.session)
        Log('Authed')

        db.load()
        Log('db loaded')

def _send_keyboards(text):
    for user_id in db.users:
        if user_id in db.admins:
            BotKeyboard.send_menu_keyboard(Core.api, user_id, perms=BKPerms.ADMIN, msg=text)
        elif user_id in db.editors:
            BotKeyboard.send_menu_keyboard(Core.api, user_id, perms=BKPerms.EDITOR, msg=text)
        else:
            BotKeyboard.send_menu_keyboard(Core.api, user_id, msg=text)

def start(text='Bot started', silent=True):    
    if silent == False:
        _send_keyboards(text)
    Log('Bot started')

    for event in Core.longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            src.Callbacks.OnEventNew(Core.api, event)
        elif event.type == VkBotEventType.GROUP_JOIN:
            src.Callbacks.OnEventJoin(Core.api, event)
        elif event.type == VkBotEventType.GROUP_LEAVE:
            src.Callbacks.OnEventLeave(Core.api, event)
        else:
            src.Callbacks.onEventDefault(Core.api, event)            
