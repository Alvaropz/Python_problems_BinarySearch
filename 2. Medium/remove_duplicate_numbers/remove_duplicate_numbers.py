'''
Given a list of integers nums, remove numbers that appear multiple times in the list, while maintaining order of the appearance in the original list.

It should use \mathcal{O}(k)O(k) space where k is the number of unique integers.
'''

# Binary Search - Your code took 154 milliseconds — faster than 76.43% in Python.

from collections import Counter

def remove_duplicate_numbers(nums):
    dict_number = Counter(nums)
    return [number for number in nums if dict_number[number] == 1]