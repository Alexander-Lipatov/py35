
import math
import string
import random
import time
import re
import os
import sys

from abc import ABCMeta, abstractmethod

# print(random.randrange(0, 100))
# print(random.randint(0, 100))
# print(random.sample(0, 100))


def polindrom():

    try:
        str = input('Input text: ').replace(" ", "").lower()
        if str == str[::-1]:
            print('is a polindrom')
        else:
            print('is not a polindrom')
    except Exception:
        print('Error')


def upper_for_word():
    str = input('Input text: ')
    words = input('Input words: ')

    words = words.split()
    for word in words:
        str = str.replace(word, word.upper())
    print(str)


def DZ_4_3_Task_1():
    list1 = [random.randrange(1, 100) for i in range(1, 10)]
    list2 = [random.randrange(1, 100) for i in range(1, 10)]
    print(list1)
    print(list2)
    list3 = [i for i in list1 + list2]
    # print(list3)

    list3 = []
    print("list3", list3)
    for i in list1 + list2:
        if i not in list3:
            list3.append(i)

    # print("без повторений", list3)

    list3 = []

    for i in list1:
        if i in list2 and i not in list3:
            list3.append(i)
    for i in list2:
        if i in list1 and i not in list3:
            list3.append(i)

    list3_min_max = []

    min = None
    max = None
    for i in list1 + list2:
        if min == None and max == None:
            min = i
            max = i
        if i < min:
            min = i
        if i > max:
            max = i
    list3_min_max.append(min)
    list3_min_max.append(max)

    print(list3_min_max)

    # print(list3)


def DZ_4_1_Task_3():

    text = "Пользователь вводит с клавиатуры некоторый текст, после чего пользователь вводит список зарезервированных слов. Необходимо найти в тексте все зарезервированные слова и изменить их регистр на верхний. Вывести на экран измененный текст."

    listText = text.split('.')
    print(listText)
    print(len(listText)-1)


def PZ_04_3_task1():
    list1 = [random.randrange(-100, 100) for i in range(1, 10)]
    print(list1)

    negative_sum = 0
    even_sum = 0
    uneven_sum = 0
    multiplication_index = 1
    multiplication_min_max = max(list1) * min(list1)
    positive_el = []
    positive_count = 0
    for i in list1:
        index = list1.index(i)

        if index % 3 == 0:
            print(index)
            print("list1[index]", list1[index])
            multiplication_index *= list1[index]
        if i % 2 != 0:
            uneven_sum += i
        if i % 2 == 0:
            even_sum += i
        if i < 0:
            negative_sum += i
            positive_el = []
            positive_count = 0

        if i > 0:
            positive_count += 1
            if positive_count > 1:
                positive_el.append(i)

    print(negative_sum)
    print(even_sum)
    print(uneven_sum)
    print(multiplication_index)
    print(multiplication_min_max)

    print(positive_el)


# PZ_04_3_task1()


def func(i: int, b: bool) -> list:
    return [i, b]


# print(func('1', True))


def func2(i: int, b: bool) -> list:
    return [i, b]


def main(i):
    print(i)
    time.sleep(1/10)
    return main(i+1)

# print(main(0))


def text_Bill_Gates():
    print(f'''
          “Don't compare yourself with anyone in this world…
          if you do so, you are insulting yourself.”
                                                    Bill Gates
          ''')

# text_Bill_Gates()

# Напишите функцию, которая принимает два числа
# в качестве параметра и отображает все четные числа
# между ними.


def func3(a: int, b: int) -> None:
    for i in range(a, b + 1):
        if i % 2 == 0:
            print(i)


# func3(1, 10)


# Напишите функцию, которая отображает пустой или
# заполненный квадрат из некоторого символа. Функция
# принимает в качестве параметров: длину стороны ква-
# драта, символ и переменную логического типа:
# ■ если она равна True, квадрат заполненный;
# ■ если False, квадрат пустой.


# def square(lenght: int, char: str, is_empty: bool) -> str:
#     print(lenght)
#     string = ""
#     for x in range(l):
#         for y in range(l):
#             pass

#     print(string)


# square(11, "*", True)

# Напишите функцию, которая возвращает минимальное
# из пяти чисел. Числа передаются в качестве параметров.


def min_five_number(*args):
    numbers = input('input numbers... : ').split(' ')
    min = args[0]
    for i in args[:6:]:
        if i < min:
            min = i
    return min


# print(min_five_number(6,4,66,4,7,3123,123,23))

def range_params(args):
    if args[0] > args[1]:
        start = args[1]
        end = args[0]
    else:
        start = args[0]
        end = args[1]
    return start, end


def composition_numbers(*args):
    result = 1
    start, end = range_params(args)
    for i in range(start, end+1):
        result *= i

    return result


res = composition_numbers(10, 5)

# print(res)


def count_numbers(number):
    return len(str(number))

# print(count_numbers(1234))


def number_polindrom(number):
    if str(number) == str(number)[::-1]:
        return True
    return False


# print(number_polindrom(123431))

# Напишите функцию, вычисляющую произведение
# элементов списка целых. Список передаётся в качестве па-
# раметра. Полученный результат возвращается из функции.


def composition_numbers_2(nums_list=[]):
    result = 1

    for i in nums_list:
        result *= i

    return result

# print(composition_numbers_2([5,6,7,8,9,10]))


# Напишите функцию для нахождения минимума в
# списке целых. Список передаётся в качестве параметра.
# Полученный результат возвращается из функции.

def min_number(nums_list=[]):
    min = nums_list[0]
    for i in nums_list:
        if i < min:
            min = i
    return min

# print(min_number([6,5,4,3,2,3,4,5,6]))

# Напишите функцию, определяющую количество про-
# стых чисел в списке целых. Список передаётся в качестве
# параметра. Полученный результат возвращается из функции.


def simple_list(list):
    lst = []
    k = 0
    count = 0
    for num in list:
        for i in range(2, num):
            if num % i == 0:
                k = k+1
        if k == 0:
            count += 1
            lst.append(num)
    print(lst)
    return count


# print('simple_list', simple_list(list=[5, 7, 101]))


# Напишите функцию, удаляющую из списка целых
# некоторое заданное число. Из функции нужно вернуть
# количество удаленных элементов.

def remove_number(list, number):
    if not number in list:
        print(list)
        return 0
    list.remove(number)
    return 1 + remove_number(list, number)


# print('remove_number', remove_number([5, 101, 7, 101], 101))


def extend_lists(list1: list, list2: list) -> list:
    return list1+list2

# print(extend_lists([1,2,3], [9,8,7]))


def degree_number_list(degree=1, list=[]):
    new_list = []

    for i in list:
        new_list.append(i**degree)

    return new_list


# print(degree_number_list(2, [2,3,4]))


# Написать рекурсивную функцию нахождения наи-
# большего общего делителя двух целых чисел.


class Obj:
    pass


def func(a, b: list[Obj]):
    if b == 0:
        return a
    return func(b, a % b)


# print(func(18, 4))


number = random.randrange(1000, 9999)


def bulls_and_cows(user_number: int):
    user_number = int(input("Please enter number"))
    cows = 0
    bulls = 0
    # print(number)


def sortSecond(val):

    print('val[0]')
    print(val[0])
    print('val[1]')
    print(val[1])
    return val[0]


# list1 to demonstrate the use of sorting
# using second key
list1 = [(4, 2), (1, 3), (7, 1)]

# sorts the array in ascending according to
# second element
# list1.sort(key=sortSecond)
# print(list1)

# sorts the array in descending according to
# second element
# list1.sort(key=sortSecond,reverse=True)
# print(list1)


# сортировка и поиск

# task_1

# Необходимо отсортировать первые две трети списка
# в порядке возрастания, если среднее арифметическое
# всех элементов больше нуля; иначе — лишь первую треть.
# Остальную часть списка не сортировать, а расположить
# в обратном порядке.

def taks_1_sort(list: list):
    print(list)
    if sum(list)/len(list) > 0:
        start_list = sorted(list[:len(list)//3*2])
        end_list = list[len(list)//3*2:][::-1]
        return start_list + end_list
    else:
        start_list = sorted(list[:len(list)//3])
        end_list = list[len(list)//3:][::-1]
        return start_list + end_list

# print(taks_1_sort([8,-5,3,-4,5,2,-7,8,-33,7,8,1]))


def grade():
    evaluations_list = [random.randint(8, 13) for _ in range(10)]
    while True:
        variant = input(
            'выбрать действие: \n 1 - вывести список оценок \n 2 - изменить оценку \n 3 - Проверить стипендию \n 4 - Сортировка оценок \n')
        match variant:
            case '1':
                print(evaluations_list)
            case '2':
                try:
                    old = int(input('выбрать элемент для пересдачи: '))
                    new = int(input('поставить новую оценку: '))
                    evaluations_list[old-1] = int(new)
                except Exception:
                    print('Ошибка ввода')
                    continue
            case '3':
                average = sum(evaluations_list) / len(evaluations_list)
                if average > 10.7:
                    print(f'Стипендия доступна, ваша средняя оценка {average}')
                else:
                    print('Стипендия недоступна')
            case '4':
                print(sorted(evaluations_list))
            case _:
                break


# Написать программу, реализующую сортировку списка
# методом усовершенствованной сортировки пузырьковым
# методом. Усовершенствование состоит в том, чтобы ана-
# лизировать количество перестановок на каждом шагу, если
# это количество равно нулю, то продолжать сортировку
# нет смысла — список отсортирован.

def advanced_bubble_sorting(list: list):

    for i in range(len(list)-1):
        for j in range(len(list)-1-i):
            if list[j] > list[i]:
                list[j], list[i] = list[i], list[j]

    return list

# print(advanced_bubble_sorting([random.randint(1, 1000) for _ in range(1000)]))


# Написать программу «справочник». Создать два списка
# целых. Один список хранит идентификационные коды,
# второй — телефонные номера. Реализовать меню для
# пользователя:
# ■ Отсортировать по идентификационным кодам;
# ■ Отсортировать по номерам телефона;
# ■ Вывести список пользователей с кодами и телефонами;
# ■ Выход.

def reference():

    def random_list(i, j, len):
        unique = []
        count = 0
        while count < len:
            random_number = random.randint(i, j)
            if random_number not in unique:
                unique.append(random_number)
                count += 1
        return unique

    def shell(list, num):
        main = num
        second = 1 if num == 0 else 0
        n = len(list[main])
        d = n // 2
        while d > 0:
            for i in range(d, n):
                j = i
                t = list[main][i]
                z = list[second][i]
                while j >= d and list[main][j - d] > t:
                    list[main][j] = list[main][j - d]
                    list[second][j] = list[second][j - d]
                    j -= d
                list[main][j] = t
                list[second][j] = z
            d //= 2
        return list

    list_id = random_list(1, 100, 10)
    list_phone = random_list(100000, 999999, 10)
    main_list = [list_id, list_phone]
    zip_list = list(zip(list_id, list_phone))
    print(main_list)

    while True:
        variant = input(
            'выбрать действие: \n 1 - Отсортировать по идентификационным кодам; \n 2 - Отсортировать по номерам телефона; \n 3 - .sort(id); \n 4 - .sort(phone) \n')
        match variant:
            case '1':
                shell(main_list, 0)
                print(main_list)
            case '2':
                shell(main_list, 1)
                print(main_list)

            case '3':
                zip_list.sort(key=lambda x: x[0])
                print(zip_list)
            case '4':
                zip_list.sort(key=lambda x: x[1])
                print(zip_list)

            case _:
                break
# reference()


# Написать программу «книги». Создать два списка
# 1 - название, 2 - годы выпуска. Реализовать меню для пользователя:
# ■ Отсортировать по названию книг;
# ■ Отсортировать по годам выпуска;
# ■ Вывести список книг с названиями и годами выпуска;
# ■ Выход;


def books():
    list_name = [''.join(random.sample((string.ascii_lowercase), 6))
                 for _ in range(10)]
    list_year = [random.randint(1900, 2021) for _ in range(10)]
    main_list = list(zip(list_name, list_year))

    while True:
        variant = input('выбрать действие: \n 1 - Отсортировать по названию книг; \n 2 - Отсортировать по годам выпуска; \n 3 - Вывести список книг с названиями и годами выпуска; \n 4 - Выход \n')
        match variant:
            case '1':
                main_list.sort(key=lambda tup: tup[0])
                print(main_list)
            case '2':
                main_list.sort(key=lambda tup: tup[1])
                print(main_list)
            case '3':
                for name, year in main_list:
                    print(f'{name} - {year}')
            case _:
                break


# books()


def five_lists():
    list_1 = [random.randint(1, 100) for _ in range(10)]
    list_2 = [random.randint(1, 100) for _ in range(10)]
    list_3 = [random.randint(1, 100) for _ in range(10)]
    list_4 = [random.randint(1, 100) for _ in range(10)]

    list_5 = list_1 + list_2 + list_3 + list_4
    print(list_5)
    while True:
        variant = input(
            ' 1-по убыванию \n 2-по возрастанию \n 3-найти значение: ')
        match variant:
            case '1':
                list_5.sort()
                print(list_5)
            case '2':
                list_5.sort(reverse=True)
                print(list_5)
            case '3':
                search_value = input('какое значение будем искать:')
                for value in list_5:
                    if value == int(search_value):
                        print(f'Значение {value} найдено под индексом {
                              list_5.index(value)}')
                        break
                else:
                    print(f'Значение {search_value} не найдено')
            case _:
                break

# five_lists()


# dict = {'key': 'value', 'key': 'value', 'key': 'value'}

# for key in dict.keys():
#     dict[key] = '123'

# class Dict(dict):
#     def __new__(cls, *args, **kwargs):
#         self = dict.__new__(cls, *args, **kwargs)
#         self.__dict__ = self
#         return self
# d = Dict(dict)\
# print(d.key)


# https://habr.com/ru/articles/129201/

tuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
tuple2 = (6, 7, 8, 9, 10, 11, 12)
tuple3 = (10, 11, 12, 13, 14, 15)


def unic_tuple(*args, **kwargs):
    unic = set()
    for tuple in args:
        for value in tuple:
            unic.add(value)
    return unic


def unic_tuple2(*args, **kwargs):
    unic = set()
    for tuple in args:
        tup = set(tuple)

    return unic


# unic_tuple(tuple1, tuple2, tuple3)

print('____________________________________________')
# Создайте программу, хранящую информацию о вели-
# ких баскетболистах. Нужно хранить ФИО баскетболиста и
# его рост. Требуется реализовать возможность добавления,
# удаления, поиска, замены данных. Используйте словарь
# для хранения информации.


def baskedball_players():
    players = list()

    def add_player(name: str, height: int):
        player = dict()
        player['name'] = name
        player['height'] = height
        players.append(player)
        print(players)

    def delete_player(name: str):
        for player in players:
            if player['name'] == name:
                players.remove(player)
                break
        print(players)

    def search(text):
        for player in players:
            if player['name'] == text:
                print(player)
                break
        else:
            print(f'Игрок {text} не найден')

    def change_player(old_name, new_name, hight):
        for player in players:
            if player['name'] == old_name:
                player['name'] = new_name
                player['height'] = hight
                break
        else:
            print(f'Игрок {old_name} не найден')

    add_player('player-1', 150)
    add_player('player-2', 160)
    add_player('player-3', 190)

    delete_player('player-2')
    search('player-1')
    change_player('player-3', 'player-9', 202)

    print(players)
    return players


# baskedball_players()


def files():
    try:
        file = open('./text.txt', 'rt',)
        print(file.read())
        file.close()
    except Exception as e:
        print('файл не найден', e)


# Дано два текстовых файла. Выяснить, совпадают ли
# их строки. Если нет, то вывести несовпадающую строку
# из каждого файла.

def compare_files():
    try:
        file1 = open('./text.txt', 'rt',)
        file2 = open('./text2.txt', 'rt',)
        f1 = file1.read()
        f2 = file2.read()
        if f1 != f2:
            print(f1)
            print(f2)
            return False
        return True
    except Exception as e:
        print(e)


# print(compare_files())


# Дан текстовый файл. Необходимо создать новый файл
# и записать в него следующую статистику по исходному
# файлу:
# ■ Количество символов;
# ■ Количество строк;
# ■ Количество гласных букв;
# ■ Количество согласных букв;
# ■ Количество цифр.

def statistics_file():
    count_line = 0
    count_vowels = 0
    count_consonants = 0
    count_numbers = 0
    file = open('./text.txt', 'rt',)
    f = file.read()
    count_char = len(f)
    count_line = f.count('\n')+1
    count_vowels = len(re.findall(r'(?i)[aeiouy]', f))
    count_consonants = len(re.findall(r'(?i)(?![aeiouy])[a-z]', f))
    count_numbers = len(re.findall(r'\d', f))
    file.close()

    file = open('./file_out.txt', 'wt', encoding='utf-8')
    result = f'Всего символов: {count_char}\nВсего строк: {count_line}\nВсего гласных: {
        count_vowels}\nВсего согласных: {count_consonants}\nВсего цифр: {count_numbers}'
    file.write(result)
    file.close()


# statistics_file()


# Дан текстовый файл. Удалить из него последнюю
# строку. Результат записать в другой файл.
def remove_last_line():
    file = open('./text.txt', 'rt',)
    f = file.readlines()
    file.close()

    f.pop()

    new_file = open('./text3.txt', 'wt',)
    new_file.write(''.join(f))
    new_file.close()

# remove_last_line()

# Дан текстовый файл. Найти длину самой длинной
# строки.


def max_line_text():
    max_line = 0
    count = 0
    info = {}
    file = open('./text.txt', 'rt')
    line_list = file.readlines()
    for line in line_list:
        if len(line) > max_line:
            max_line = len(line)
            info['id'] = count
            info['len'] = max_line
        count += 1
    file.close()
    print(info)

# max_line_text()

# Дан текстовый файл. Посчитать сколько раз в нем
# встречается заданное пользователем слово.


def count_user_words():
    count = 0
    word = input('Ввудите слово: ')
    file = open('./text4.txt', 'rt')
    f = file.read()
    file.close()
    # count = f.count(word) // не правильный подсчет
    for w in f.split():
        clean_word = w.translate(str.maketrans('', '', string.punctuation))
        if clean_word == word:
            count += 1
    print(f'Слово {word} встречается {count} раз')
    return count

# count_user_words()

# Дан текстовый файл. Найти и заменить в нем задан-
# ное слово. Что искать и на что заменять определяется
# пользователем.


def search_and_change_word():
    word = input('Введите слово которое надо заменить: ')
    new_word = input('Введите новое слово: ')

    file = open('./text.txt', 'rt')
    f = file.read()
    file.close()

    f = f.replace(word, new_word)

    file = open('./text4.txt', 'wt')
    file.write(f)
    file.close()

# search_and_change_word()


# Напишите информационную систему «Сотрудники».
# Программа должна обеспечивать ввод данных, редакти-
# рование данных сотрудника, удаление сотрудника, поиск
# сотрудника по фамилии, вывод информации обо всех
# сотрудниках, указанного возраста, или фамилия которых
# начинается на указанную букву. Организуйте возможность
# сохранения найденной информации в файл. Также весь
# список сотрудников сохраняется в файл (при выходе из
# программы — автоматически, в процессе исполнения
# программы — по команде пользователя). При старте
# программы происходит загрузка списка сотрудников из
# указанного пользователем файла.


def employees():
    def read_data_from_file():
        data = list()
        file = './employees_db.txt'
        if not os.path.exists(file):
            new_file = open(file, 'w+')
            new_file.close()
        file = open(file, 'rt')
        list_data = file.readlines()
        file.close()
        for line in list_data:
            id, first_name, last_name, age = line.replace('\n', '').split('|')
            line_data = {
                'id': id,
                'first_name': first_name,
                'last_name': last_name,
                'age': age
            }
            data.append(line_data)
        print('Данные загружены...')
        return data

    def write_data_to_file(data):
        file = open('./employees_db.txt', 'wt')
        for user in data:
            file.write(f'{user["id"]}|{user["first_name"]}|{
                       user["last_name"]}|{user["age"]}\n')
        file.close()
        print('Сохранение успешно выполнено...')

    def check_employee(first_name='', last_name='', id=''):
        for line in data:
            if first_name == line['first_name'] and last_name == line['last_name'] or id == line['id']:
                return True
        return False

    def add_employee(id: str, first_name: str, last_name: str, age: str):
        if not check_employee(first_name=first_name, last_name=last_name):
            user = {
                'id': id,
                'first_name': first_name,
                'last_name': last_name,
                'age': age
            }
            data.append(user)
            print(f'Сотрудник {first_name} {last_name} добавлен.')
        else:
            print(f'Сотрудник {first_name} {last_name} уже существует.')

    def remove_employees(id: str):
        for line in data:
            if id == line['id']:
                data.remove(line)
                print(f'Сотрудник {line['first_name']} {
                    line['last_name']} удален')
                break
        else:
            print(f'Сотрудник c id {id} не найден')

    def serch_employee(text: str) -> None:
        if text.isdigit():
            age = int(text)
            for line in data:
                if int(line['age']) == age:
                    employee_view(data=line)
        elif len(text) == 1 and text.isalpha():
            for line in data:
                if line['last_name'][0].lower() == text.lower():
                    employee_view(data=line)
        else:
            for line in data:
                if text == line['last_name']:
                    employee_view(data=line)

    def edit_epmloyee(id, new_first_name=None, new_last_name=None, new_age=None):
        for user in data:
            if user['id'] == id:
                user['first_name'] = new_first_name if not new_first_name is None else user['first_name']
                user['last_name'] = new_last_name if not new_last_name is None else user['last_name']
                user['age'] = new_age if not new_age is None else user['age']
                print(f'Сотрудник {user["first_name"]} {
                      user["last_name"]} изменен')
                break

    def edit_view(id):
        while True:
            optiont_edit = input(
                '1. Изменить имя.\n2. Изменить фамилию.\n3. Изменить возраст\n0. Назад.\nВыберите опцию: ')
            match optiont_edit:
                case '1':
                    new_first_name = input('Введите новое имя: ')
                    edit_epmloyee(
                        id, new_first_name=new_first_name)
                case '2':
                    new_last_name = input(
                        'Введите новую фамилию: ')
                    edit_epmloyee(id, new_last_name=new_last_name)
                case '3':
                    new_age = input('Введите новый возраст: ')
                    edit_epmloyee(id, new_age=new_age)
                case '0':
                    break
                case _:
                    print('Введите корректный вариант')

    def employee_view(data: list | dict):
        if isinstance(data, list):
            for user in data:
                print(f'{user['id']}\t{user['first_name']}\t{
                    user['last_name']}\t{user['age']}')
        elif isinstance(data, dict):
            print(f'{data['id']}\t{data['first_name']}\t{
                data['last_name']}\t{data['age']}')

    menu_list = (
        'Показать всех сотрудников',
        'Поиск сотрудников',
        'Добавить сотрудника',
        'Изменить данные сотрудника',
        'Удалить сотрудника',
        'Сохранить запись в базу',
        'Выход'
    )

    data = read_data_from_file()

    while True:
        text_option = '\n'.join(
            [f"{num}. {option}" for num, option in enumerate(menu_list, start=1)])
        option = input(f'{text_option}\nВыберите опцию: ')

        print('____________________\n')
        match option:
            case '1':
                # Вывести всех сотрудников из базы данных.
                print('Список сотрудников:')
                print(f'ID\tИмя\tФамилия\tВозраст')
                employee_view(data)
            case '2':
                # Поиск сотрудника по фамилии, возрасту или первой букве фамилии.
                serch_text = input(
                    'Введите фамилию полностью, возраст сотрудника или первую букву его фамилии:\n')
                serch_employee(serch_text)
            case '3':
                # Добавление нового сотрудника в базу данных.
                # Получение данных о сотруднике от пользователя.
                id = int(data[-1]['id']) + 1 if len(data) != 0 else 1
                first_name = input('Введите имя сотрудника: ')
                last_name = input('Введите фамилию сотрудника: ')
                age = input('Введите возраст сотрудника: ')
                add_employee(id, first_name, last_name, age)
            case '4':
                # Изменение сотрудника из базы данных.
                id = input('Введите id сотрудника: ')
                if check_employee(id=id):
                    # Если сотрудник существует, пользователь может выбрать, какие данные изменить.
                    edit_view(id)
            case '5':
                # Удаление сотрудника из базы данных.
                id = input('Введите id сотрудника: ')
                remove_employees(id)
            case '6':
                # Сохранение изменений в файл.
                write_data_to_file(data)
            case '7':
                # Сохранение изменений в файл и выход из программы.
                write_data_to_file(data)
                break

            case _:
                print('Введите корректный вариант')

        print('____________________\n')


# employees()

# Синтаксис filter()

# filter(in_function|None, iterable)
# |__filter object


# Дан текстовый файл. Необходимо создать новый файл
# убрав из него все неприемлемые слова. Список неприем-
# лемых слов находится в другом файле.

def pz_9_2_1_change():
    list_ignore = ['consectetur', 'voluptatibus', 'repellendus', 'elit']
    file = open('./pz_9_2_1_files/text.txt')
    words_list = file.read()
    file.close()
    for word in list_ignore:
        words_list = words_list.replace(word, '*'*len(word))
    new_file = open('./pz_9_2_1_files/ignore_words.txt', 'w')
    new_file.write(words_list)
    new_file.close()


pz_9_2_1_change()


# Написать программу транслитерации с русского на
# английский и наоборот. Данные для транслитерации
# берутся из файла и записываются в другой файл. Направ-
# ление перевода определяется через меню пользователя.


class Stack:
    def __init__(self):
        self.__items = []

    def pop(self):
        pass

    def push(self):
        pass


class AddingStack(Stack):

    def __init__(self):
        Stack.__init__()
        self.sum = 0


myObj = Stack()


# Реализуйте класс «Автомобиль». Необходимо хранить
# в полях класса: название модели, год выпуска, произво-
# дителя, объем двигателя, цвет машины, цену. Реализуйте
# методы класса для ввода данных, вывода данных, реа-
# лизуйте доступ к отдельным полям через методы класса.

class Car:
    def __init__(self):
        self.__model = input('Введите модель: ')
        self.__year = input('Введите год выпуска: ')
        self.__producer = input('Введите производителя: ')
        self.__volume = input('Введите объём двигателя: ')
        self.__color = input('Введите цвет: ')
        self.__price = int(input('Введите цену: '))

    def get_params(self):
        print(f'модель {self.__model}')
        print(f'год выпуска {self.__year}')
        print(f'производителя {self.__producer}')
        print(f'объём двигателя {self.__volume}')
        print(f'цвет {self.__color}')
        print(f'цену {self.__price}')

    def get_model(self):
        print(f'модель {self.__model}')

    def get_yearl(self):
        print(f'год выпуска {self.__year}')

    def get_producer(self):
        print(f'производителя {self.__producer}')

    def get_volume(self):
        print(f'объём двигателя {self.__volume}')

    def get_color(self):
        print(f'цвет {self.__color}')

    def get_price(self):
        print(f'цену {self.__price}')

    def set_price(self, new_price):
        if isinstance(new_price, int):
            self.__price = new_price
        elif isinstance(new_price, str) and '%' in new_price:
            new_price = new_price.split('%')
            new_price = int(new_price[0])/100
            self.__price = int(self.__price - (self.__price * new_price))
        else:
            print('Некорректный ввод')

# car = Car()

# car.set_price('20%')
# car.get_price()
# car.set_price(5000)
# car.get_price()
# car.set_price('20')
# car.get_price()

# Реализуйте класс «Книга». Необходимо хранить в
# полях класса: название книги, год выпуска, издателя,
# жанр, автора, цену. Реализуйте методы класса для ввода
# данных, вывода данных, реализуйте доступ к отдельным
# полям через методы класса.


class Book:
    def __init__(self,
                 title=None, year=None, publisher=None,
                 genre=None, author=None, price=None
                 ):
        self.__title = title
        self.__year = year
        self.__publisher = publisher
        self.__genre = genre
        self.__author = author
        self.__price = price

    def input_data(self):
        """Метод для ввода данных о книге."""
        print("Введите данные о книге:")
        self.__title = input("Название книги: ")
        self.__year = int(input("Год издания:"))
        self.__publisher = input("Издатель: ")
        self.__genre = input("Жанр: ")
        self.__author = input("Автор: ")
        self.__price = float(input("Цена: "))

    def output_data(self):
        """Метод для вывода данных о книге"""
        print(f"Название книги: {self.__title}")
        print(f"Год издания: {self.__year}")
        print(f"Издатель: {self.__publisher}")
        print(f"Жанр: {self.__genre}")
        print(f"Автор: {self.__author}")
        print(f"Цена: {self.__price}")

    def get_title(self):
        """Метод для получения названия книги."""
        return self.__title

    def get_year(self):
        """Метод для получения года издания книги."""
        return self.__year

    def get_publishself(self):
        """Метод для получения информации об издателе."""
        return self.__publisher

    def get_genre(self):
        """Метод для получения жанра книги."""
        return self.__genre

    def get_author(self):
        """Метод для получения информации об авторе."""
        return self.__author

    def get_price(self):
        """Метод для получения цены книги."""
        return self.__price

# Реализуйте класс «Стадион». Необходимо хранить в
# полях класса: название стадиона, дату открытия, страну,
# город, вместимость. Реализуйте методы класса для ввода
# данных, вывода данных, реализуйте доступ к отдельным
# полям через методы класса.


class Studium:
    def __init__(self):
        self.__name = None
        self.__date = None
        self.__country = None
        self.__city = None
        self.__capacity = None

    def input_data(self):
        self.__name = input('название стадиона: ')
        self.__date = input('дата открытия: ')
        self.__country = input('страна: ')
        self.__city = input('город: ')
        self.__capacity = input('вместимость: ')

    def output_data(self):
        print(f'название стадиона: {self.__name}')
        print(f'дата открытия: {self.__date}')
        print(f'страна: {self.__country}')
        print(f'город: {self.__city}')
        print(f'вместимость: {self.__capacity}')

    def get_name(self):
        return self.__name

    def get_date(self):
        return self.__date

    def get_country(self):
        return self.__country

    def get_city(self):
        return self.__city

    def get_capacity(self):
        return self.__capacity


# man.print_data()
# print(man.fio)
# man.fio = 'asd asd asd'
# print(man.fio)


# Создайте класс Device, который содержит информа-
# цию об устройстве.
# С помощью механизма наследования, реализуйте класс
# класс Blender (содержит информацию о блендере), класс
# MeatGrinder (содержит информацию о мясорубке).
# Каждый из классов должен содержать необходимые
# для работы методы.

class Device:
    serial_number = 1

    def __init__(self, device) -> None:
        self.serial_number = Device.serial_number
        self.model = device['model']
        self.warranty = device['warranty']
        self.country = device['country']
        self.__is_turn_on = False
        Device.serial_number += 1

    def device_turn_on(self) -> None:
        self.__is_turn_on = True

    def device_turn_off(self):
        self.__is_turn_on = False


blenderModels = {
    'M5': {

    }
}


class Blender(Device):
    def __init__(
            self,
            power_consumption: int,
            speeds_count: int,
            turbo: bool,
            device: dict
    ) -> None:
        super(Blender, self).__init__(device)
        self.power_consumption = power_consumption
        self.speeds = speeds_count
        self.turbo = turbo

    def print(self):
        print(self.model)
        print(self.serial_number)
        print(self.warranty)
        print(self.country)
        print(self.power_consumption)
        print(self.speeds)
        print(self.turbo)


class BlenderM5(Blender):
    model = 'M5'
    power_consumption = 500
    speeds_count = 3
    turbo = True
    countries = {
        'USA': 2,
        'China': 1,
    }

    def __init__(
            self,
            country: str
    ) -> None:
        device = {
            'country': country,
            'model': BlenderM5.model,
            'warranty': BlenderM5.countries[country],
        }
        super().__init__(BlenderM5.power_consumption,
                         BlenderM5.speeds_count, BlenderM5.turbo, device)
        self.power_consumption = BlenderM5.power_consumption
        self.speeds = BlenderM5.speeds_count
        self.turbo = BlenderM5.turbo

    def print(self):
        print(self.model)
        print(self.serial_number)
        print(self.warranty)
        print(self.country)
        print(self.power_consumption)
        print(self.speeds)
        print(self.turbo)


class MeatGrinder(Device):

    def __init__(
            self,
            model,
            serial_number,
            warranty,
            country
    ) -> None:
        super().__init__(model, serial_number, warranty, country)

    def print(self):
        print(self.model)
        print(self.serial_number)
        print(self.warranty)
        print(self.country)


blender = BlenderM5('USA')

# meat_grinder = MeatGrinder('model_meat_grinder', '00002', '12 month', 'China')
# print(repr(blender.print()))
# blender.print()

# meat_grinder.print()

# К уже реализованному классу «Дробь» добавьте ста-
# тический метод, который при вызове возвращает коли-
# чество созданных объектов класса «Дробь».

# Создайте класс для конвертирования температуры из
# Цельсия в Фаренгейт и наоборот. У класса должно быть
# два статических метода: для перевода из Цельсия в Фа-
# ренгейт и для перевода из Фаренгейта в Цельсий. Также
# класс должен считать количество подсчетов температуры и
# возвращать это значение с помощью статического метода.


class ConverterTemp:
    count = 0

    @staticmethod
    def celsius_to_fahrenheit(celsius: float) -> float:
        ConverterTemp.count += 1
        return celsius * 1.8 + 32

    @staticmethod
    def fahrenheit_to_celsium(fahrenheit: float) -> float:
        ConverterTemp.count += 1
        return (fahrenheit - 32) / 1.8

    @staticmethod
    def getCount() -> int:
        return ConverterTemp.count


far = ConverterTemp.celsius_to_fahrenheit(30)
cel = ConverterTemp.fahrenheit_to_celsium(130)
print(far)
print(cel)
print(ConverterTemp.getCount())

# Создайте класс для перевода из метрической системы
# в английскую и наоборот. Функциональность необходимо
# реализовать в виде статических методов. Обязательно
# реализуйте перевод мер длины.


class ConverterMetricSystem:

    @staticmethod
    def meter_to_feet(meter: float) -> float:
        return meter * 3.2808
        passx

    @staticmethod
    def feet_to_meter(feet: float) -> float:
        return feet * 0.3048


print(ConverterMetricSystem.meter_to_feet(10))
print(ConverterMetricSystem.feet_to_meter(150))



print('_________________________________________')
# Создайте класс для подсчета площади геометрических
# фигур. Класс должен предоставлять функциональность
# для подсчета площади треугольника по разным формулам,
# площади прямоугольника, площади квадрата, площади
# ромба. Методы класса для подсчета площади должны
# быть реализованы с помощью статических методов. Также
# класс должен считать количество подсчетов площади и
# возвращать это значение с помощью статического метода.


class SquareFigures:
    count = 0

    @staticmethod
    def triangle_1(a, h):
        '''Площадь треугольника по стороне и высоте, опущенной на эту сторону: '''
        SquareFigures.count += 1
        return 0.5 * a * h

    @staticmethod
    def triangle_2(m, n, a):
        '''Площадь треугольника по двум сторонам и углу между ними: '''
        SquareFigures.count += 1

        return 0.5 * m * n * math.sin(a)

    @staticmethod
    def rectangle(a, b):
        SquareFigures.count += 1

        return a * b

    @staticmethod
    def square(a):
        SquareFigures.count += 1
        return a**2

    @staticmethod
    def rhomb(d1, d2):
        SquareFigures.count += 1
        return (d1 * d2) / 2

    @staticmethod
    def get_count():
        return SquareFigures.count


t1 = SquareFigures.triangle_1(10, 4)
t2 = SquareFigures.triangle_2(5, 10, 15)
rect = SquareFigures.rectangle(10, 5)
sq = SquareFigures.square(10)
rhomb = SquareFigures.rhomb(10, 5)

print(t1)
print(t2)
print(rect)
print(sq)
print(rhomb)
print(SquareFigures.get_count())


# Создайте класс для подсчета максимума из четырех
# аргументов, минимума из четырех аргументов, средне-
# арифметического из четырех аргументов, факториала
# аргумента. Функциональность необходимо реализовать
# в виде статических методов.


class ResultFourArgs:
    @staticmethod
    def max(*args):
        return max(args[:4])

    @staticmethod
    def min(*args):
        return min(args[:4])

    @staticmethod
    def average(*args):
        return sum(args[:4]) / len(args[:4])


print(ResultFourArgs.max(4,65,6,4))
print(ResultFourArgs.min(4,65,6,4))
print(ResultFourArgs.average(4,65,6,4))



# Реализуйте класс «Человек». Необходимо хранить в
# полях класса: ФИО, дату рождения, контактный телефон,
# город, страну, домашний адрес. Реализуйте методы класса
# для ввода данных, вывода данных, реализуйте доступ к
# отдельным полям через методы класса.

# К уже реализованному классу «Человек» добавьте
# статический метод, который при вызове возвращает ко-
# личество созданных объектов класса «Человек».

# Создайте класс Human, который будет содержать
# информацию о человеке.
# С помощью механизма наследования, реализуйте класс
# Builder (содержит информацию о строителе), класс Sailor
# (содержит информацию о моряке), класс Pilot (содержит
# информацию о летчике).
# Каждый из классов должен содержать необходимые
# для работы методы.
print('_________________HUMAN___________________')


class Human:
    count_human = 0
    __passport = None


    def __init__(self, fio, birthday, tel, city, country, addr):
        self.__fio = fio
        self.__birthday = birthday
        self.__tel = tel
        self.__city = city
        self.__country = country
        self.__addr = addr
        Human.count_human += 1

    @staticmethod
    def get_count_human():
        print(Human.count_human)
        return Human.count_human

    def print_data(self):
        print(f'ФИО: {self.__fio}')
        print(f'дата рождения: {self.__birthday}')
        print(f'контактный телефон: {self.__tel}')
        print(f'город: {self.__city}')
        print(f'страна: {self.__country}')
        print(f'домашний адрес: {self.__addr}')

    @property
    def fio(self):
        return self.__fio

    @fio.setter
    def fio(self, value):
        self.__fio = value


    @property
    def passport(self):
        return self.__passport
    
    @passport.setter
    def passport(self, value):
        return value


class Builder(Human):
    skils = ('Бетонщик', 'Плиточник', 'Штукатур')
    pass
    

class Sailor(Human):
    skils = ('...', '...', '...')

    pass
    

class Pilot(Human):
    skils = ('...', '...', '...')

    pass


man = Human('fio', '01.01.2000', '+1234567890',
            'Moscow', 'Russia', 'Red Square 1')
Human('asda asd', '12.12.1232', '123123123', '123123', 'asdasd', 'asdasdsad')
Human('asda asd', '12.12.1232', '123123123', '123123', 'asdasd', 'asdasdsad')
Human('asda asd', '12.12.1232', '123123123', '123123', 'asdasd', 'asdasdsad')
pilot = Pilot('asda asd', '12.12.1232', '123123123', '123123', 'asdasd', 'asdasdsad')
Human.get_count_human()
print(pilot.skils)


from dataclasses import dataclass

@dataclass(init=True, kw_only=True, eq=True, order=True, unsafe_hash=True, repr=False)
class Person:
    first_name: str
    last_name: str
    age: int

    def __repr__(self) -> str:
        return f'{self.first_name}, {self.last_name},{self.age}'

    def __delattr__(self, name: str) -> None:
        print('нельзя удалить', name)
        del self.__dict__[name]


person = Person(first_name='drfsd',last_name='drfsd1',age=247)
del person.age


list1 = [1,2,3,4]
print(list1)
del list1
# print(list1)

# Создайте класс Circle (окружность). Для данного
# класса реализуйте ряд перегруженных операторов:
# ■ Проверка на равенство радиусов двух окружностей
# (операция = =);
# ■ Сравнения длин двух окружностей (операции >, <,
# <=,>=);
# ■ Пропорциональное изменение размеров окружности,
# путем изменения ее радиуса (операции + - += -=).


# __eq__() – для равенства ==
# __ne__() – для неравенства !=
# __lt__() – для оператора меньше <
# __le__() – для оператора меньше или равно <=
# __gt__() – для оператора больше >
# __ge__() – для оператора больше или равно >=
# __ge__() – для оператора больше или равно >=
# __add__ - +   
# __sub__ - -
# __iadd__ - +=
# __isub__ - -=





class Circle:
    def __init__(self, radius:int):
        self.radius = radius

    @property
    def lenght(self):
        return 2 * math.pi * self.radius

    def __eq__(self, other):
        return self.radius ==  other.radius

    def __gt__(self, other):
        return self.lenght > other.lenght
    
    def __lt__(self, other):
        return self.lenght < other.lenght

    def __le__(self, other):
        return self.lenght <= other.lenght

    def __ge__(self, other):
        return self.lenght >= other.lenght

    def __add__(self, other:int):
        return self.radius + other

    def __sub__(self, other:int):
        return self.radius - other

    def __iadd__(self, other: int):
        return self.radius + other

    def __isub__(self, other:int):
        return self.radius - other

c1 = Circle(10)
c2 = Circle(15)
print(c1==c2)
print(c1>c2)
print(c1<c2)
print(c1>=c2)
print(c1<=c2)
print(c1+100)
print(c1-100)
c1+=11
c2-=11
print(c1)
print(c2)


# Создайте класс Complex (комплексное число). Более
# подробно ознакомиться с комплексными числами можно
# по ссылке.
# Создайте перегруженные операторы для реализации
# арифметических операций для по работе с комплексными
# числами (операции +, -, *, /).


class Complex:
    

    
    
    
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    
    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)
    
    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)
    
    def __mul__(self, other):
        return Complex(self.real * other.real + self.imag * other.imag * -1, self.real * other.imag + self.imag * other.real)
    
    def __truediv__(self, other):
        z3 = Complex(other.real,-other.imag)
        delitel = (z3 * other).real
        z4 = z3* self
        return Complex(z4.real / delitel, z4.imag / delitel)


    def __repr__(self) -> str:
        return str(self.real) + ("+" if self.imag >=0 else '') + str(self.imag) + 'i'


z1 = Complex(-4, 2)
z2 = Complex(1, -3)
print(z1, z2)
print(z1+z2)
print(z1-z2)
print(z1*z2)
print(z1/z2)


# Вам необходимо создать класс Airplane (самолет).

# ■ Проверка на равенство типов самолетов (операция
# = =);
# ■ Увеличение и уменьшение пассажиров в салоне са-
# молета (операции + - += -=);
# ■ Сравнение двух самолетов по максимально возмож-
# ному количеству пассажиров на борту (операции >
# < <= >=).




# Создать класс Flat (квартира). Реализовать перегру-
# женные операторы:
# ■ Проверка на равенство площадей квартир (операция
# ==);
# ■ Проверка на неравенство площадей квартир (опера-
# ция !=);
# ■ Сравнение двух квартир по цене (операции > < <= >=).


class Flat:
    def __init__(self):
        self.square = 0
        self.price = 0

    def __eq__(self, other) -> bool:
        return self.square == other.square




# Создайте функцию, возвращающую список со всеми
# простыми числами от 0 до 1000
# Используя механизм декораторов посчитайте сколько
# секунд, потребовалось для вычисления всех простых чисел.
# Отобразите на экран количество секунд и простые числа.





def benchmark(func):
    import time
    
    def wrapper(*args, **kwargs):
        start = time.time()
        func()
        end = time.time()
        print('[*] Время выполнения: {} секунд.'.format(end-start))
    return wrapper


@benchmark
def numbers():
    l = []
    for i in range(0, 10000+1):
        l.append(i)
    return l

numbers()



# Паттерн фабрика;

class Car:
    def __init__(self, name, max_speed, color) -> None:
        self.name=name
        self.max_speed = max_speed
        self.color = color

    def release(self):
        print(self.__dict__)

class ProductFactory:
    @staticmethod
    def create_car_BMW(color):

        return Car(name='BMW M5', max_speed=100, color=color)
    @staticmethod
    def create_car_AUDI(color, ):
        return Car(name='AUDI A5', max_speed=100, color=color)
    
car = ProductFactory.create_car_BMW('black')

car.release()

# creator = TruckCarWorkShop()
# truck  = creator.create_product()
# truck.release()


# Паттерн абстрактная фабрика;

class IEngine(metaclass=ABCMeta):
    @abstractmethod
    def release_engine(self):
        pass

class JapanesEngine(IEngine):

    def release_engine(self):
        print('japan engine')
    
class RussianEngine(IEngine):

    def release_engine(self):
        print('russian engine')

    
class ICar(metaclass=ABCMeta):
    @abstractmethod
    def release_car(self, engine:IEngine):
        pass

class JapanCar(ICar):
    def release_car(self, engine:IEngine):
        print('build japan car')
        engine.release_engine()


class RussianCar(ICar):
    def release_car(self, engine:IEngine):
        print('build rus car')
        engine.release_engine()


class IFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_engine(self) ->IEngine:
        pass

    @abstractmethod
    def create_car(self) ->ICar:
        pass

class JapanesFactory(IFactory):
    def create_engine(self) ->IEngine:
        return JapanesEngine()

    def create_car(self) ->ICar:
        return JapanCar()
    
class RussianFactory(IFactory):
    def create_engine(self) ->IEngine:
        return RussianEngine()

    def create_car(self) ->ICar:
        return RussianCar()
    

# factory = JapanesFactory()
# j_engine = factory.create_engine()
# j_car = factory.create_car()

# j_car.release_car(j_engine)



# Создайте классическую реализацию паттерна Singleton.
# Протестируйте работу созданного класса.
class Singleton:
    __instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    
    def __init__(self, val) -> None:
        if not hasattr(self, 'val'):
            self.val = val

# s1 = Singleton(1)
# s2 = Singleton(2)
# print(s1.val)
# print(s2.val)
# print(s1 == s2)

# Создайте реализацию паттерна Abstract Factory. Про-
# тестируйте работу созданного класса.


class Device:
    pass

class Phone(Device):
    pass

class Laptop(Device):
    pass

class Kitchen(Device):
    pass




# class IPhoneFactory(IFactory):
#     def create_device(self):
#         return IPhone()
    
# class IPadFactory(IFactory):

    



# Пользователь вводит с клавиатуры набор чисел и путь
# к файлу для сохранения полученных данных. Необходимо:
# ■ Сохранить все полученные числа.
# ■ Найти максимум, минимум. Эти значения сохранить
# в том же файле.
# ■ Отобразить числа.
# ■ Отобразить максимум и минимум.
# ■ Создать класс для логгирования операций. При созда-
# нии объекта класса нужно уточнить куда производится
# логгирование: экран или файл. В программе можно
# создать только один объект класса. Все действия
# объекта этого класса.




class Logger:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(Logger, cls).__new__(cls)
        return cls.__instance
    
    def __init__(self, view:str):
        if not hasattr(self, 'view'):
            self.view = view

    def log(self, text):
        if self.view == 'screen':
            print(text)
        elif self.view == 'file':
            with open('log.txt', 'a') as f:
                f.write(text + '\n')
        else:
            print('view not found')


logger = Logger(view='file')


numbers_list = [int(num) for num in input('numbers input: ').split(' ')]
path_to_file = './files/'
filename = 'datatext.txt'
file = open(path_to_file+filename, 'w')

logger.log('start')
min = min(numbers_list)
logger.log('min:'+ str(min))
max = max(numbers_list)
logger.log('max:' + str(max))

for num in numbers_list:
    logger.log(f'write number {num} to file')
    file.write(str(num) + ', ')
else:
    file.write('\n')

logger.log('write min number')
file.write(str(min) + '\n')
logger.log('write max number')
file.write(str(max))
file.close()
logger.log('end')


# file = open(path_to_file+filename, 'r')
# print(file.readline())
# print(file.readline(2))
# print(file.readline(3))