import argparse
from collections import Counter
import random


def find_word(filename):
    with open(filename) as file:
        text = file.read()
    for symbols in ".,-\n":
        text = text.replace(symbols, ' ')
    text = text.lower()
    dictText = dict.fromkeys(text.split())

    count = 0
    for i in text.split():
        for j in reversed(text.split()):
            if i == j:
                count = count + 1
        dictText[i] = count
        count = 0
    print('\n', dictText)

    maxes = Counter(dictText).most_common(10)
    string = ' '
    for x in maxes:
        string = string + ' ' + x[0]
    print('\n10 самых встречающихся слов: ', string.strip().capitalize() + '.')


def fibanachi(n):
    fib1 = 1
    fib2 = 1
    for i in range(n):
        fib2, fib1 = fib2 + fib1, fib2
        yield fib1


def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    else:
        q = random.choice(nums)
    l_nums = [n for n in nums if n < q]

    e_nums = [q] * nums.count(q)
    b_nums = [n for n in nums if n > q]
    return quick_sort(l_nums) + e_nums + quick_sort(b_nums)


def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0
    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:

            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1

            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1

        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    return sorted_list


def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2

    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])

    return merge(left_list, right_list)


parser = argparse.ArgumentParser(description='Choice the program and file')

parser.add_argument("filename", type=str)
parser.add_argument('-a', '--solveA', action="store_true")
parser.add_argument('-b', '--solveB', action="store_true")
parser.add_argument('-c', '--solveC', action="store_true")


args = parser.parse_args()

if args.solveA:
    find_word(args.filename)


elif args.solveB:
    with open(args.filename) as file:
        randNumb = file.read()

    print('\n' + randNumb)
    intRandNumb = [int(N) for N in randNumb.split()]
    print(quick_sort(intRandNumb))
    numb = merge_sort(intRandNumb)
    print(numb)

elif args.solveC:
    with open(args.filename, "r") as file:
        fib = int(file.read())
    for i in fibanachi(fib):
        print(i, end=' ')
