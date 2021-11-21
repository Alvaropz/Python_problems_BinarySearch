'''
Given a list of integers nums, return whether there's an integer whose frequency in the list is same as its value.
'''

# Binary Search - Your code took 113 milliseconds — faster than 72.25% in Python.

from collections import Counter

def equivalent_value_and_frequency(nums):
    new_count_dict = Counter(nums)
    for key, value in new_count_dict.items():
        if key == value:
            return True
    return False