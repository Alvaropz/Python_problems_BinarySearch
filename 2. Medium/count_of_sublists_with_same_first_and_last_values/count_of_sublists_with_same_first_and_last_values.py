'''
Given a list of integers nums, return the number of sublists where the first element and the last element have the same value.
'''

# Binary Search - Your code took 15 milliseconds — faster than 49.47% in Python.

def count_of_sublists_with_same_first_and_last_values(nums):
    dict_nums = {}
    total = 0
    for number in nums:
        if number in dict_nums:
            dict_nums[number] += 1
        else:
            dict_nums[number] = 1
        total += dict_nums[number]
    return total