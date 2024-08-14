import threading
from multiprocessing import Process
from time import sleep


def print_word(word):
    sleep(5)
    print('hello,', word)


def greet(name):
    print('hello: ', name)


if __name__ == '__main__':
    # p1 = Process(target=print_word, args=('bob',), daemon=True)
    # p2 = Process(target=print_word, args=('alice',), daemon=True)
    # p1.start()
    # p2.start()
    # p1.join()
    # p2.join()

    t1 = threading.Thread(target=greet, args=('bob',), daemon=True)
    t2 = threading.Thread(target=greet, args=('alice',), daemon=True)
    t1.start()
    t2.start()
    t1.join()
    t2.join()



# https://habr.com/ru/companies/simbirsoft/articles/701020/
    


import asyncio


async def hello():
    print('Запуск функции hello')
    await asyncio.sleep(5)  # Отдаем управление обратно в Event loop пока ждем
    print('Переключение контекста в функцию hello')