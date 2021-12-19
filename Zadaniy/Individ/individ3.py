#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Выбрать любую папку на своем компьютере, имеющую
вложенные директории. Вывести на печать в терминал
ее содержимое и всех подкаталогов при помощи
функции print_docs(directory).
"""

import os


def print_docs(directory):
    all_files = os.walk(directory)
    for catalog in all_files:
        print(f'Папка {catalog[0]} содержит:')
        print(f'Директории: {", ".join([folder for folder in catalog[1]])}')
        print(f'Файлы: {", ".join([file for file in catalog[2]])}')
        print('-' * 40)


if __name__ == '__main__':
    print_docs('C:/Users/Plotnikov/17laba')
