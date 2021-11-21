'''
Given a list of integers nums, you can perform the following operation: pick the largest integer in nums and turn it into the second largest number.

Return the minimum number of operations required to make all integers the same in the list.
'''

# Binary Search - Your code took 64 milliseconds — faster than 43.20% in Python.

from collections import Counter

def equal_piles(nums):
    total = 0
    uniques = list(dict.fromkeys(nums))
    uniques.sort()
    dict_nums = Counter(nums)
    for i in range(1, len(uniques)):
        total += (i*dict_nums[uniques[i]])
    return total