'''
Given a list of integers nums, return the number of elements x there are such that x + 1 exists as well.
'''

from collections import Counter

# Binary Search - Your code took 73 milliseconds — faster than 28.95% in Python

def counting_plus_plus(nums):
    count = 0
    set_nums = set(nums)
    dict_count = Counter(nums)
    for key, value in dict_count.items():
        if key + 1 in set_nums:
            count += value
    return count

# Binary Search - Your code took 33 milliseconds — faster than 96.11% in Python (Code provided by animanny)

def counting_plus_plus_optimised(nums):
    setNum = set(nums)
    count = 0
    for num in nums:
        if num + 1 in setNum:
            count += 1
    return count