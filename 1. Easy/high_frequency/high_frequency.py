'''
Given a list of integers nums, find the most frequently occurring element and return the number of occurrences of that element.

For example, given the list [1, 4, 1, 7, 1, 7, 1, 1], return 5 since the the element 1 appears 5 times.
'''

#Binary Search - Your code took 1 millisecond — faster than 99.88% in Python

from collections import Counter 

def high_frequency(nums):
    dict_ocurrencies = Counter(nums)
    return max(dict_ocurrencies.values())