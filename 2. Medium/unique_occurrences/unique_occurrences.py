'''
Given a list of integers nums, return whether the number of occurrences of every value in the array is unique.

Note: Numbers can be negative.
'''

from collections import Counter

# Binary Search - Your code took 19 milliseconds — faster than 66.36% in Python

def unique_occurrences(nums): 
    dict_ocurrences = Counter(nums)
    list_of_values = list(dict_ocurrences.values())
    for counting in list_of_values:
        if list_of_values.count(counting) > 1:
            return False
    return True