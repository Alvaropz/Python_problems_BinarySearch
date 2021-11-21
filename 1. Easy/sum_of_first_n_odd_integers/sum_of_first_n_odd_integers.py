'''
Given an integer n, return the sum of the first n positive odd integers.
'''

# Binary Search - Your code took 74 milliseconds — faster than 26.19% in Python

def sum_of_first_n_odd_integers(n):
    return sum([num for num in range(n*2) if num % 2 != 0])

# Binary Search - Your code took 74 milliseconds — faster than 99.89% in Python

def sum_of_first_n_odd_integers_optimised(n):
    return n**2