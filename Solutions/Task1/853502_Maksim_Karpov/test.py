import argparse
import random


def word_count(arg_ans, arg_file):
    input_arr = []
    if arg_ans == "1":
        try:
            with open(arg_file) as file_1:

                input_arr = list(file_1.read().split())
        except IOError:
            print("Не найден такой файл")
            return 0

    else:
        chooser = input("1.Чтение из файла\n2.Чтение с клавиатуры\n")
        while chooser != "1" and chooser != "2":
            chooser = input("Вы ввели не то")

        if chooser == "1":
            try:
                with open("task_1.txt") as file_1:

                    input_arr = list(file_1.read().split())
            except IOError:
                print("Не найден такой файл")
                return 0

        elif chooser == "2":

            input_arr = list(input("Введите строку").split())

        del chooser

    first_dict = {a: {"word": '', "counts": 1} for a in range(len(input_arr))}

    for i in range(len(input_arr)):
        first_dict[i]["word"] = input_arr[i]

    del input_arr

    word_counts = []
    right_dict = first_dict.copy()

    for i in first_dict:
        if word_counts.count(first_dict[i]["word"]) == 0:
            word_counts.append(first_dict[i]["word"])
        else:
            for j in first_dict:
                if first_dict[j]["word"] == first_dict[i]["word"]:
                    right_dict[j]["counts"] += 1
                    right_dict.pop(i)
                    break
            continue
    del word_counts
    del first_dict

    for i in right_dict:
        print("Слово ", right_dict[i]["word"], "повторяется ", right_dict[i]["counts"], "раз")

    counters = []
    for i in right_dict:
        counters.append(right_dict[i]["counts"])
    counters.sort()
    counters.reverse()
    top_word = list()

    for j in range(len(counters)):
        for i in right_dict:
            if right_dict[i]["counts"] == counters[j]:
                if top_word.count(right_dict[i]["word"]) > 0:
                    break
                top_word.append(right_dict[i]["word"])

    if len(right_dict) < 10:
        print("Т.к в вашей строке не нашлось 10 различных повторяющихся слов мы вывели эти")
    print("Топ повторяющихся слов :", top_word)


def rebuild_array(temp_array):
    input_array = []
    temp = ""
    temp_array += " "
    for i in temp_array:
        temp += i
        if i == " ":
            input_array.append(int(temp))
            temp = ""
    print(input_array)
    del temp
    del temp_array
    return input_array


def quick_sort(arg_ans, arg_file):
    print("Задача 2")

    def quick(array, first, last):

        if first >= last:
            return

        i, j = first, last
        pivot = int(array[random.randint(first, last)])

        while i <= j:
            while int(array[i]) < pivot:
                i += 1
            while int(array[j]) > pivot:
                j -= 1
            if i <= j:
                array[i], array[j] = array[j], array[i]
                i, j = i + 1, j - 1
        quick(array, first, j)
        quick(array, i, last)

    input_array = []

    if arg_ans == "1":
        try:
            with open(arg_file) as file_1:
                input_array = file_1.read()
        except IOError:
            print("Не найден такой файл")
            return 0
    else:
        chooser = input("1.Чтение из файла\n2.Чтение с клавиатуры\n")

        while chooser != "1" and chooser != "2":
            chooser = input("Вы ввели не то")

        if chooser == "1":
            with open("task_2_3.txt") as file_1:
                input_array = file_1.read()
        elif chooser == "2":
            input_array = input("Введите строку")

    input_array = list(input_array.split())
    print(input_array)

    quick(input_array, 0, len(input_array)-1)

    print(input_array)



def merge_sort(arg_ans, arg_file):


    def merge(array):

        if len(array) > 1:
            mid = len(array) // 2
            left_half = array[:mid]
            right_half = array[mid:]

            merge(left_half)
            merge(right_half)

            i = 0
            j = 0
            k = 0
            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    array[k] = left_half[i]
                    i = i + 1
                else:
                    array[k] = right_half[j]
                    j = j + 1
                k = k + 1

            while i < len(left_half):
                array[k] = left_half[i]
                i = i + 1
                k = k + 1

            while j < len(right_half):
                array[k] = right_half[j]
                j = j + 1
                k = k + 1

    input_ar = []

    if arg_ans == "1":
        try:
            with open(arg_file) as file_1:
                input_ar = file_1.read()
        except IOError:
            print("Не найден такой файл")
            return 0
    else:
        chooser = input("1.Чтение из файла\n2.Чтение с клавиатуры\n")
        input_ar = []
        while chooser != "1" and chooser != "2":
            chooser = input("Вы ввели не то")

        if chooser == "1":
            with open("quick_sort_3.txt") as file_1:
                input_ar = file_1.read()
        elif chooser == "2":
            input_ar = list(input("Введите строку"))

    input_ar = rebuild_array(input_ar)

    merge(input_ar)

    print(input_ar)


def fib_func(n):
    fib_1, fib_2 = 0, 1
    for i in range(n):
        fib_1, fib_2 = fib_2, fib_1 + fib_2
        yield fib_1


def fibonacci():
    while 1:
        try:
            n = int(input("Введите количество членов ряда Фибоначчи\n"))
            break
        except ValueError:
            print("Не число :/ ")
    for fib in fib_func(n):
        print(fib, end=" ")


parser = argparse.ArgumentParser(description="Choose a task")
parser.add_argument("-a", "--Answer", type=str, required=False, help="Выберите Задачу\n1.Задача word count\n2.Задача "
                                                                     "quick sort\n3.Задача merge sort\n4.Задача "
                                                                     "Фибоначчи \n")
parser.add_argument("-c", "--Chooser", type=str, required=False, help="1.Чтение из файла\n2.Чтение с "
                                                                      "клавиатуры\n")
parser.add_argument("-f", "--File_name", type=str, required=False, help="Название файла")
args = parser.parse_args()

if args.Answer == "1":
    word_count(args.Chooser, args.File_name)
elif args.Answer == "2":
    quick_sort(args.Chooser, args.File_name)
elif args.Answer == "3":
    merge_sort(args.Chooser, args.File_name)
elif args.Answer == "4":
    fibonacci()
else:
    answer = input("1.Задача word count\n2.Задача quick sort\n3.Задача merge sort\n4.Задача Фибоначчи \n")
    while answer != "1" and answer != "2" and answer != "3" and answer != "4":
        answer = input("Вы ввели не то \n")

    if answer == "1":
        word_count(0, 0)
    elif answer == "2":
        quick_sort(0, 0)
    elif answer == "3":
        merge_sort(0, 0)
    elif answer == "4":
        fibonacci()

    del answer
