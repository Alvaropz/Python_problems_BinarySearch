'''
Given two strings a and b that represent binary numbers, add them and return their sum, also as a string.

The input strings are guaranteed to be non-empty and contain only 1s and 0s.
'''

# Binary Search - Your code took 1 millisecond — faster than 100.00% in Python.

def add_binary_numbers(a, b):
    intA = int(a, 2)
    intB = int(b, 2)
    total = intA + intB
    return bin(total)[2:]