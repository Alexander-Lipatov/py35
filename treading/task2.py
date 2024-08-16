"""
Задание 2

Пользователь с клавиатуры вводит путь к файлу.
После чего запускаются три потока. Первый поток за-
полняет файл случайными числами. Два других потока
ожидают заполнения. Когда файл заполнен оба потока
стартуют. Первый поток находит все простые числа, вто-
рой поток факториал каждого числа в файле. Результаты
поиска каждый поток должен записать в новый файл. На
экран необходимо отобразить статистику выполненных
операций.
"""
import random
from typing import List, Text
from threading import Thread
from math import factorial

class FileOperations:
    @staticmethod
    def write_to_file(path: str, content: str):
        with open(path, 'w') as file:
            file.write(content)
            print(f"File '{path}' has been written.")
    
    @staticmethod
    def load_from_file(path: str):
        with open(path, 'r') as file:
            return file.read().split()

class Task2:
    def __init__(self) -> None:
        self.path = input("Input path to file './path/to/file.txt': ")

    def gen_numbers(self) -> List[int]:
        list = [random.randint(10, 50) for _ in range(20)]
        content = ' '.join(map(str, list))
        FileOperations.write_to_file(self.path, content)

    def is_simple(self, number):
        if number < 2:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True

    def simple_numbers(self):
        
        load_numbers = FileOperations.load_from_file(self.path)
        simple_numbers = []
        for number in load_numbers:
            if self.is_simple(int(number)):
                simple_numbers.append(int(number))

        FileOperations.write_to_file('simple_numbers.txt','\n'.join(map(str, simple_numbers)))
        print(f"Simple numbers have been written to file'simple_numbers.txt'")

    def factorial_numbers(self):
        load_numbers = FileOperations.load_from_file(self.path)
        factorial_numbers = []
        for number in load_numbers:
            factorial_numbers.append(str(factorial(int(number))))  
        FileOperations.write_to_file('factorial_numbers.txt','\n'.join(factorial_numbers)) 
        print(f"Factorial numbers have been written to file'factorial_numbers.txt'")
         


    @staticmethod
    def start():
        task2 = Task2()
        t1 = Thread(target=task2.gen_numbers, daemon=True)
        t2 = Thread(target=task2.simple_numbers, daemon=True)
        t3 = Thread(target=task2.factorial_numbers, daemon=True)
        t1.start()
        print(t1)
        t1.join()
        t2.start()
        t3.start()
        t2.join()
        t3.join()
        


if __name__ == '__main__':
    Task2.start()