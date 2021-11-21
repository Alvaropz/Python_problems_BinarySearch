'''
Given an integer n, return the number of positive integers of length n such that the digits are strictly increasing.
n = 2
36
We have 12, 13, 14, 15, 16, 17, 18, 19, 23, 24, 25, 26, 26, 28, 29, 34, 35, 36, 37, 38, 39, 45, 46, 47, 48, 49, 56, 57, 58, 59, 67, 68, 69, 78, 79, 89.
'''

# Binary Search - Your code took 1 millisecond — faster than 100.00% in Python.

def increasing_digits(n):
    if n == 1 or n == 8:
        return 9
    elif n == 2 or n == 7:
        return 36
    elif n == 3 or n == 6:
        return 84
    elif n == 4 or n == 5:
        return 126
    elif n == 9:
        return 1
    else:
        return 0