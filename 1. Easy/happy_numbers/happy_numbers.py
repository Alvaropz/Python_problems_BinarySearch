'''
Given an integer n, we apply this transformation until it becomes a 1: take each of the digits in n, square it, and then take their sum.

Return whether n will end up in 1 after the transformations.
'''

# Binary Search - Your code took 2 milliseconds — faster than 77.07% in Python.

def happy_numbers(n):
    square_lists = set()
    while True:
        if n > 9:
            n = sum(int(number)**2 for number in str(n))
        else:
            n = n**2
        if n in square_lists:
            return False
        square_lists.add(n)
        if 1 in square_lists:
            return True