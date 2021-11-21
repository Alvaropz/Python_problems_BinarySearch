'''
Given a list of integers nums, return the largest integer k where k and -k both exist in nums (they can be the same integer). If there's no such integer, return -1.
'''

# Binary Search - Your code took 28 milliseconds — faster than 48.80% in Python.

from collections import Counter

def k_and_minus_k(nums):
    set_nums = set()
    for number in nums:
        if not number in set_nums:
            set_nums.add(number)
    for val in list(reversed(sorted(set_nums))):
        if val*-1 in set_nums:
            return val
    return -1

# Binary Search - Your code took 34 milliseconds — faster than 36.28% in Python.

def k_and_minus_k_dictionary(nums):
    nums.sort()
    dict_counting = Counter(nums)
    for key in list(reversed(dict_counting)):
        if key*-1 in dict_counting:
            return key
    return -1