'''
Given a list of integers nums, find the first missing positive integer. In other words, find the lowest positive integer that does not exist in the list. 
The list can contain duplicates and negative numbers as well.
'''

# Binary Search - Your code took 168 milliseconds — faster than 16.02% in Python.

def first_missing_positive_list(nums):
    nums.sort()
    pos_list = [item for item in nums if item > 0]
    pos_list = list(dict.fromkeys(pos_list))
    if len(pos_list) == 0:
        return 1
    if pos_list[0] != 1:
        return 1
    elif len(pos_list) == 1:
        return 2
    for index in range(1, len(pos_list)):
        if pos_list[index]-1 != pos_list[index-1]:
            return pos_list[index-1]+1
    return pos_list[-1]+1

# Binary Search - Your code took 39 milliseconds — faster than 71.23% in Python

def first_missing_positive_set(nums):
    if len(nums) == 0:
        return 1
    set_numbers = set(nums)
    element = 1
    while True:
        if not element in set_numbers:
            return element
        element += 1