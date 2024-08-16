"""
Задание 1

При старте приложения запускаются три потока.
Первый поток заполняет список случайными числами.
Два других потока ожидают заполнения. Когда список
заполнен оба потока запускаются. Первый поток находит
сумму элементов списка, второй поток среднеарифмети-
ческое значение в списке. Полученный список, сумма и
среднеарифметическое выводятся на экран.
"""

import threading
import random
import time
from typing import List

class Task1:
    list = []

    def fill(list:List):
        for _ in range(7):
            list.append(random.randint(0, 100))
        print(list)

    def my_sum(list):
        time.sleep(3)
        print(sum(list))

    def mid(list):
        time.sleep(2)
        print(sum(list)/len(list))

    @staticmethod
    def start():
        t1 = threading.Thread(target=Task1.fill, args=(Task1.list,), daemon=True)
        t2 = threading.Thread(target=Task1.my_sum, args=(Task1.list,), daemon=True)
        t3 = threading.Thread(target=Task1.mid, args=(Task1.list,), daemon=True)
        t1.start()
        t1.join()
        t2.start()
        t3.start()
        t2.join()
        t3.join()
        print(Task1.list)


if __name__ == '__main__':
    Task1.start()