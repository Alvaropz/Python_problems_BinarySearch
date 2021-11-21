'''
Given an integer n greater than or equal to 0, return the number of 1 bits in n.
'''

# Binary Search - Your code took 1 millisecond — faster than 100.00% in Python.

def number_of_bits(n):
    bit_list = []
    while n != 0:
        bit_list.append(n%2)
        n = int(n / 2)
    return bit_list.count(1)