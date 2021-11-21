'''
Given an integer n, return whether it is equal to the sum of its own digits raised to the power of the number of digits.
'''

# Binary Search - Your code took 1 millisecond — faster than 99.85% in Python

def narcissistic_number(n):
    power = len(str(n))
    if n == sum([int(number)**power for number in str(n)]):
        return True
    return False