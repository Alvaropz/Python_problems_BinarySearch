'''
Given a non-negative integer num, return whether it is a palindrome.

Bonus: Can you solve it without using strings?
'''

# Binary Search - Your code took 4 milliseconds — faster than 96.21% in Python.

def palindrome_integer(num):
    list_numbers = []
    while num > 0:
        list_numbers.append(num % 10)
        num = num // 10
    i = 0
    j = len(list_numbers)-1
    while i < j:
        if list_numbers[i] != list_numbers[j]:
            return False
        i += 1
        j -= 1
    return True

# Binary Search - Your code took 4 milliseconds — faster than 96.81% in Python

def palindrome_integer_string(num):
    str_num = str(num)
    while True:
        if len(str_num) <= 1:
            break
        if str_num[-1] != str_num[0]:
            return False
        str_num = str_num[1:-1]
    return True

# Binary Search - Your code took 8 milliseconds — faster than 11.62% in Python

import math

def palindrome_integer_integer(num):
    list_values = []
    while num > 0:
        temp_val = int((num / 1) % 10)
        num = math.trunc(num / 10)
        list_values.append(temp_val)
    while len(list_values) > 1:
        if list_values[0] == list_values[-1] and len(list_values) > 1:
            list_values.pop(0)
            list_values.pop(-1)
        else:
            return False
    return True