
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
            positive_count+=1
            if positive_count > 1: 
                positive_el.append(i)
                
        

    print(negative_sum)
    print(even_sum)
    print(uneven_sum)
    print(multiplication_index)
    print(multiplication_min_max)

    print(positive_el)


PZ_04_3_task1()


def func(i:int, b: bool)-> list:
    return [i, b]


print(func('1', True))


def func2(i:int, b: bool)-> list:
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

def square(lenght:int, char:str, is_empty: bool)-> str:
    print(lenght)
    string = ""
    for y in range(lenght):
        for x in range(lenght):
            if is_empty:
                if y==lenght-1:
                    string += ' '+char+' '
                elif y == 0:
                    string += ' '+char+' '
            else:
                string += ' '+char+' '
        string+='\n'

                
    print(string)
square(11, "*", True)





