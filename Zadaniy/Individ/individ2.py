#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Истории литературы известен случай написания романа объемом
около 50 тыс. слов, в котором ни разу не была употреблена
самая популярная в английском алфавите буква E. Название
его – «Gadsby». Напишите программу, которая будет считывать
список слов из файла и собирать статистику о том, в каком
проценте слов используется каждая буква алфавита. Выведите
результат для всех 26 букв английского алфавита и отдельно
отметьте букву, которая встречалась в словах наиболее редко.
В вашей программе должны игнорироваться знаки препинания и
регистр символов.
"""

import math


if __name__ == "__main__":

    # Создание словаря со счетчиком слов, содержащих все буквы
    counts = {}
    for ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        counts[ch] = 0

    # Открытие файла, обработка слов и обновление словаря со счетчиком
    num_words = 0
    inf = open("individ2.txt", "r")
    for word in inf:
        word = word.upper().rstrip()
        unique = []
        for ch in word:
            if ch not in unique and ch >= "A" and ch <= "Z":
                unique.append(ch)
        for ch in unique:
            counts[ch] = counts[ch] + 1
        num_words = num_words + 1

    # Закрытие файла
    inf.close()

    # Вывод результата для каждой буквы и определение редкости в словах
    smallest_count = min(counts.values())
    for ch in sorted(counts):
        if counts[ch] == smallest_count:
            smallest_letter = ch
        percentage = counts[ch] / num_words * 100
        print(ch, "встречается в %.2f процентах слов" % percentage)

    # Вывод самой редкой буквы
    print()
    print("Самая редко встречающаяся буква:", smallest_letter)







