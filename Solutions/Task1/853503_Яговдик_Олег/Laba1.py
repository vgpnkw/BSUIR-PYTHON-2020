#!/usr/bin/env python3
# ./test.py

import sys
import argparse
import random
import pdb


def word_count(str):
    str.lower()

    words = str.split(' ')
    # Разбиваем текст на слова
    dictionary = {}

    for index in range(0, len(words)):
        str = words[index]

        if str == '':
            continue
        # Если вводят несколько пробелов, то появляется мусор

        if str[len(str) - 1] == ',' or str[len(str) - 1] == '.':
            str = str[0: len(str) - 1]
        # Избавляемся от запятых и точек в словах

        if dictionary.get(str) == None:
            dictionary[str] = 1
        # если слово встречается впервый раз, то присваевываем 1
        else:
            dictionary[str] = dictionary[str] + 1
    print(dictionary)
    # 2 Задание
    words = sorted(dictionary.items(), key=lambda count: count[1])
    # Сортируем элементы по значению
    # Нельзя перевернуть с помощью reverse(), т к кортеж - неизменяемый список

    dictionary = dict(words[-10:])
    words = list(dictionary.keys())
    print(' '.join(words))


def quick_sort(array, left_range, right_range):
    sup_arg = array[int(left_range + (right_range - left_range) / 2)]
    i = left_range
    j = right_range

    while i <= j:
        while array[i] < sup_arg:
            i = i + 1
        while array[j] > sup_arg:
            j = j - 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i = i + 1
            j = j - 1

    if left_range < j:
        quick_sort(array, left_range, j)
    if right_range > i:
        quick_sort(array, i, right_range)



def merg(list, left_range, mid, right_range):
    index_left = left_range
    index_right = mid
    buffer = []
    while index_left < mid and index_right < right_range:
        if list[index_left] < list[index_right]:
            buffer.append(list[index_left])
            index_left = index_left + 1
        else:
            buffer.append(list[index_right])
            index_right = index_right + 1
    if (index_left < mid):
        buffer.extend(list[index_left: mid])
    elif (index_right < right_range):
        buffer.extend(list[index_right: right_range])
    list[left_range: right_range] = buffer


def merg_sort(list, left_range, right_range):
    if left_range + 1 >= right_range:
        return
    mid = int((left_range + right_range) / 2)
    merg_sort(list, left_range, mid)
    merg_sort(list, mid, right_range)
    merg(list, left_range, mid, right_range)


def fib(n):
    cache = [0, 1]

    yield cache[0]
    yield cache[1]

    for index in range(2, n):
        cache[1] = cache[0] + cache[1]
        cache[0] = cache[1] - cache[0]
        yield cache[1]


def create_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', default='input')
    parser.add_argument('-a', '--fib_arg', default='5')
    parser.add_argument('-t', '--task', choices=['task1', 'task2', 'task3', 'task4'], default='task2')

    return parser



parser = create_parse()
namespace = parser.parse_args(sys.argv[1:])

str = ''
with open(namespace.file) as file:
    for line in file:
        str = str + line

if namespace.task == 'task1':
    word_count(str)
elif namespace.task == 'task2':
    array = [int(x) for x in str.split(' ')]
    quick_sort(array, 0, len(array) - 1)
    print(array)
elif namespace.task == 'task3':
    array = [int(x) for x in str.split(' ')]
    merg_sort(array, 0, len(str.split(' ')))
    print(array)
elif namespace.task == 'task4':
    n = int(namespace.fib_arg)
    print(list(fib(n)))
