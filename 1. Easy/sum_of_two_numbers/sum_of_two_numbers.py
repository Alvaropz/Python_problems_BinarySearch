'''
Given a list of numbers nums and a number k, return whether any two numbers from the list add up to k. You may not use the same element twice.

Note: Numbers can be negative or 0.
'''

# BinarySearch - Your code took 148 milliseconds — faster than 4.27% in Python

import collections
from collections import Counter

def sum_of_two_numbers(nums, k):
    pairs = Counter(nums)
    if len(pairs) > 1:
        for first_key, first_value in pairs.items():
            for second_key in pairs.keys():
                if first_value > 1 or first_key != second_key:
                    if first_key + second_key == k:
                        return True
    return False