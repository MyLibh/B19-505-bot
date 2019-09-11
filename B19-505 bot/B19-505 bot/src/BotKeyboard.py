from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id


class BotKeyboard(object):
    def send_menu_keyboard(api, user_id, msg='Смотри, какие классные виджеты)', perms=0):
        
        keyboard = VkKeyboard(one_time=False)

        if perms == 5:
            keyboard.add_button('Editor', color=VkKeyboardColor.POSITIVE)
            keyboard.add_line()
        elif perms == 31415926:
            keyboard.add_button('Admin', color=VkKeyboardColor.POSITIVE)
            keyboard.add_line()

        keyboard.add_button('Info', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line() 
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