from src.Core import Core, start

def main():
    Core.init()

    review = '[UPDATE]\n v1.5\n\n[CHANGELOG]\nДобавлено расписание и учебники\n\nПо всем вопросам/предложениям пиши @big_black_hot_brother'
    start(review, silent=True)

if __name__ == '__main__':
    main()