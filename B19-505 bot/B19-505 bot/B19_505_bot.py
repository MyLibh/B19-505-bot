from src.Core import Core, start

def main():
    Core.init()
    
    review = '[UPDATE] v1.0\nТеперь домашка и инфа будут появляться!\n\nХочешь помочь в обновлении дз/инфы?\nПиши @big_black_hot_brother'
    start(review, silent=False)

if __name__ == '__main__':
    main()