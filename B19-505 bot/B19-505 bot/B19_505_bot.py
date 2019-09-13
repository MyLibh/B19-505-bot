from src.Core import Core

def main():
    Core.init()
    
    review = '[UPDATE] v1.0\nТеперь домашка будет появляться\n\nХочешь помочь в обновлении дз/инфы?\n пиши @big_black_hot_brother'
    Core.start(review)

if __name__ == '__main__':
    main()