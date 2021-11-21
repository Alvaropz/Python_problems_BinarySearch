'''
Given a list of integers nums, return whether all numbers appear an even number of times.

This should be done in \mathcal{O}(1)O(1) space.
'''

# Binary Search - Your code took 33 milliseconds — faster than 97.41% in Python.

from collections import Counter

def even_frequency(nums):
    counting = Counter(nums)
    for value in counting.values():
        if value % 2 != 0:
            return False
    return True