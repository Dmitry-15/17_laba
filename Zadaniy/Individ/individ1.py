#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Написать программу, которая считывает текст из файла
и выводит его на экран, заменив цифры от 0 до 9
на слова «ноль», «один», ..., «девять», начиная
каждое предложение с новой строки.
"""


if __name__ == "__main__":
    digit = ['ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
    with open("individ1.txt", "r", encoding="utf-8") as file:
        string = file.read()
    string = string.replace('. ', '.\n')
    out = ''
    for al in string:
        if al.isnumeric():
            al = digit[int(al)]
        out += al
    print(out)