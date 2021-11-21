'''
Given an integer n, return whether n = k * k for some integer k.

This should be done without using built-in square root function.
'''

# Binary Search - Your code took 1143 milliseconds — faster than 26.63% in Python.

def check_if_number_is_perfect_square(n):
    if n == 0:
        return True
    for number in range(1,n+1):
        square = number * number
        if square == n:
            return True
        if square > n:
            return False