
import string
import random
import time
import re
import os
import sys

print(sys.path)

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


def square(lenght: int, char: str, is_empty: bool) -> str:
    print(lenght)
    string = ""
    for x in range(l):
        for y in range(l):
            pass

    print(string)


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
                        print(f'Значение {value} найдено под индексом {\
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


# unic_tuple(tuple1, tuple2, tuple3

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
            file.write(f'{user["id"]}|{user["first_name"]}|{\
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
                print(f'Сотрудник {line['first_name']} {\
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
                print(f'Сотрудник {user["first_name"]} {\
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

    def employee_view(data: list|dict):
        if isinstance(data, list):
            for user in data:
                print(f'{user['id']}\t{user['first_name']}\t{\
                        user['last_name']}\t{user['age']}')
        elif isinstance(data, dict):
            print(f'{data['id']}\t{data['first_name']}\t{\
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
        text_option= '\n'.join(
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
