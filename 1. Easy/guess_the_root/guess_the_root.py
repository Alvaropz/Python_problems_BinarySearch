'''
Given a non-negative integer n, find a number r such that r * r = n and round down to the nearest integer.

Can you implement this without using the built-in square root?
'''

# Binary Search - Your code took 2 milliseconds — faster than 100.00% in Python.

def guess_the_root(n):
    return int(n**(1/2))