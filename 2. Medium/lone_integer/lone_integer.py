'''
You are given a list of integers nums where each integer occurs exactly three times except for one which occurs once. Return the lone integer.

Bonus: solve it in \mathcal{O}(1)O(1) space.
'''

# Binary Search - Your code took 45 milliseconds — faster than 27.16% in Python.

from collections import Counter

def lone_integer(nums):
    dict_nums = Counter(nums)
    for key in dict_nums:
        if dict_nums[key] == 1:
            return key

# Binary Search - Your code took 49 milliseconds — faster than 25.53% in Python.

def lone_integer_filter(nums):
    dict_nums = Counter(nums)
    return list(filter(lambda x: x[1] == 1, dict_nums.items()))[0][0]