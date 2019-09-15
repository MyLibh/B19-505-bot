from src.Core import Core, start

def main():
    Core.init()

    review = '[UPDATE] v1.3\n[CHANGELOG]\nПо всем вопросам/предложениям пиши @big_black_hot_brother'
    start(review, silent=True)

if __name__ == '__main__':
    main()