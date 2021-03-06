from vk_api.bot_longpoll import VkBotLongPoll
from src.Logger import Log

class LongPoll(VkBotLongPoll):
    def listen(self):
        while True:
            try: 
                for event in self.check():
                    yield event
            except Exception as e:
                Log(str(e), 'Error')
