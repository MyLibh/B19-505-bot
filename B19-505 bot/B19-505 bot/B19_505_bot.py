import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import src

def main():
    src.Logger.Log('')
    src.Logger.Log('Starting...')

    config = src.Config.Config('config/credentials.txt')
    src.db.db.load()

    vk_session = vk_api.VkApi(token=config.token)
    vk         = vk_session.get_api()
    longpoll   = VkBotLongPoll(vk_session, config.group_id)

    for user_id in src.db.db.users:
        if user_id in src.db.db.admins:
            src.BotKeyboard.BotKeyboard.send_menu_keyboard(vk, user_id, perms=31415926)
        elif user_id in src.db.db.editors:
            src.BotKeyboard.BotKeyboard.send_menu_keyboard(vk, user_id, perms=5)
        else:
            src.BotKeyboard.BotKeyboard.send_menu_keyboard(vk, user_id)

    src.Logger.Log('Bot started')
        
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            src.Callbacks.OnEventNew(vk, event)
        elif event.type == VkBotEventType.GROUP_JOIN:
            src.Callbacks.OnEventJoin(vk, event)
        elif event.type == VkBotEventType.GROUP_LEAVE:
            src.Callbacks.OnEventLeave(vk, event)
        else:
            src.Callbacks.onEventDefault(vk, event)
        

if __name__ == '__main__':
    main()