
import string
import random

import re


def polindrom():
    str = input('Input text: ').replace(" ", "").lower()
    if str == str[::-1]:
        print('is a polindrom')
    else:
        print('is not a polindrom')




def upper_for_word():
    str = input('Input text: ')
    words = input('Input words: ')

    words = words.split()
    for word in words:
         str = str.replace(word, word.upper())
    print(str)

upper_for_word()


print()