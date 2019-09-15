from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
from enum import Enum

class BKPerms(Enum):
    USER = 0
    EDITOR = 10
    ADMIN = 100

class BotKeyboard(object):
    def send_menu_keyboard(api, user_id, msg='Я снова здесь)', perms=BKPerms.USER):
        
        keyboard = VkKeyboard(one_time=False)

        if perms == BKPerms.ADMIN:
            keyboard.add_button('Admin', color=VkKeyboardColor.POSITIVE)

        if perms == BKPerms.ADMIN or perms == BKPerms.EDITOR:
            keyboard.add_button('Editor', color=VkKeyboardColor.POSITIVE)
            keyboard.add_line()
        
        #keyboard.add_button('Расписание', color=VkKeyboardColor.PRIMARY)
        #keyboard.add_line()
        keyboard.add_button('Info', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('ДЗ', color=VkKeyboardColor.PRIMARY)

        keyboard.add_line()  
        keyboard.add_button('help', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('report', color=VkKeyboardColor.NEGATIVE)

        api.messages.send(peer_id=user_id, random_id=get_random_id(), keyboard=keyboard.get_keyboard(), message=msg)

    def send_ht_keyboard(api, user_id):
        keyboard = VkKeyboard(one_time=False)

        
        keyboard.add_button('Ангем', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Матан', color=VkKeyboardColor.PRIMARY)

        keyboard.add_line() 
        keyboard.add_button('ЭВМ', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Инфа', color=VkKeyboardColor.PRIMARY)

        keyboard.add_line() 
        keyboard.add_button('ОГЗ', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Физика', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Дискретка', color=VkKeyboardColor.PRIMARY)

        keyboard.add_line()
        keyboard.add_button('Назад', color=VkKeyboardColor.DEFAULT)

        api.messages.send(peer_id=user_id, random_id=get_random_id(), keyboard=keyboard.get_keyboard(), message='По какому предмету?')

    def send_editor_keyboard(api, user_id):
        keyboard = VkKeyboard(one_time=False)

        keyboard.add_button('Рaзослать', color=VkKeyboardColor.NEGATIVE)
        keyboard.add_button('Добавить', color=VkKeyboardColor.POSITIVE)        
             
        keyboard.add_line()
        keyboard.add_button('Назад', color=VkKeyboardColor.DEFAULT)

        api.messages.send(peer_id=user_id, random_id=get_random_id(), keyboard=keyboard.get_keyboard(), message='Меню редактора открыто!')

    def send_editor_keyboard_add(api, user_id):
        keyboard = VkKeyboard(one_time=False)

        keyboard.add_button('Информация', color=VkKeyboardColor.NEGATIVE)
        keyboard.add_button('ДЗ', color=VkKeyboardColor.POSITIVE)        
             
        keyboard.add_line()
        keyboard.add_button('Назад', color=VkKeyboardColor.DEFAULT)

        api.messages.send(peer_id=user_id, random_id=get_random_id(), keyboard=keyboard.get_keyboard(), message='Меню добавления открыто!')

    def send_admin_keyboard(api, user_id):
        keyboard = VkKeyboard(one_time=False)

        keyboard.add_button('Demote', color=VkKeyboardColor.NEGATIVE)
        keyboard.add_button('Promote', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Назад', color=VkKeyboardColor.DEFAULT)

        api.messages.send(peer_id=user_id, random_id=get_random_id(), keyboard=keyboard.get_keyboard(), message='Hello, Dear deer)')

    def send_report_keyboard(api, user_id):
        keyboard = VkKeyboard(one_time=True)

        keyboard.add_button('Назад', color=VkKeyboardColor.DEFAULT)

        api.messages.send(peer_id=user_id, random_id=get_random_id(), keyboard=keyboard.get_keyboard(), message='Опиши проблему')

    def send_shedule_keyboard(api, user_id):
        keyboard = VkKeyboard(one_time=False)

        keyboard.add_button('Завтра', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Сегодня', color=VkKeyboardColor.PRIMARY)

        keyboard.add_line()
        keyboard.add_button('Назад', color=VkKeyboardColor.DEFAULT)

        api.messages.send(peer_id=user_id, random_id=get_random_id(), keyboard=keyboard.get_keyboard(), message='Что интересует?')