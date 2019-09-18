from src.Core import Core, start

def main():
    Core.init()

    review = '[UPDATE]\n v2.0-alpha\n\n[CHANGELOG]\n\n\nПо всем вопросам/предложениям пиши @big_black_hot_brother'
    start(review, silent=True)

if __name__ == '__main__':
    main()