
import string
import random
import time
import re


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


PZ_04_3_task1()


def func(i: int, b: bool) -> list:
    return [i, b]


print(func('1', True))


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


print(number_polindrom(123431))

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
        if k==0:
            count+=1
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

print('remove_number', remove_number([5, 101, 7, 101], 101))

def extend_lists(list1:list, list2:list)->list:
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

def func(a, b:list[Obj]):
    if b == 0:
        return a
    return func(b, a % b)

print(func(18, 4))


number = random.randrange(1000, 9999)

def bulls_and_cows(user_number:int):
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
list1 = [(4,2),(1,3),(7,1)]

# sorts the array in ascending according to 
# second element
list1.sort(key=sortSecond) 
print(list1)

# sorts the array in descending according to
# second element
list1.sort(key=sortSecond,reverse=True)
print(list1)

    


# сортировка и поиск

# task_1

# Необходимо отсортировать первые две трети списка
# в порядке возрастания, если среднее арифметическое
# всех элементов больше нуля; иначе — лишь первую треть.
# Остальную часть списка не сортировать, а расположить
# в обратном порядке.

def taks_1_sort(list:list):
    print(list)
    if sum(list)/len(list) > 0:
        start_list = sorted(list[:len(list)//3*2])
        end_list = list[len(list)//3*2:][::-1]
        return start_list + end_list
    else:
        start_list = sorted(list[:len(list)//3])
        end_list= list[len(list)//3:][::-1]
        return start_list + end_list

print(taks_1_sort([8,-5,3,-4,5,2,-7,8,-33,7,8,1]))

def grade():
    evaluations_list = [random.randint(1,13) for _ in range(10)]
    print(evaluations_list)

    input_params = input()
    

grade()