import vk_api
from vk_api.bot_longpoll import VkBotEventType

from src.Config import Config
from src.LongPoll import LongPoll
from src.db import db
from src.BotKeyboard import BotKeyboard
from src.Logger import Log
import src.Callbacks

class Core(object):
    session = None
    api = None
    longpoll = None

    def init():
        Log('')
        Log('Starting...')

        Config.load()
        Log('Config loaded')

        Core.session  = vk_api.VkApi(token=Config.token)
        Core.api      = Core.session.get_api()
        Core.longpoll = LongPoll(Core.session, Config.group_id)
        Log('Authed')

        if Core.api.groups.getOnlineStatus(group_id=Config.group_id)['status'] == 'none':
            Core.api.groups.enableOnline(group_id=Config.group_id)

        db.load()
        Log('db loaded')

def _send_keyboards(text):
    for user_id in db.users:
        BotKeyboard.send_menu_keyboard(Core.api, user_id, perms=db.users[user_id], msg=text)


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
