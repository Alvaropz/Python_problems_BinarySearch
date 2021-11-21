'''
Given a list of integers nums, sort the list in the following way:

First number is the maximum
Second number is the minimum
Third number is the 2nd maximum
Fourth number is the 2nd minimum
And so on.
'''

# Binary Search - Your code took 335 milliseconds — faster than 6.86% in Python

def large_to_small_sort(nums):
    if len(nums) > 1:
        new_list = []
        copied_nums = sorted(nums.copy())
        while len(copied_nums) > 1:
            new_list.append(copied_nums[-1])
            new_list.append(copied_nums[0])
            copied_nums.pop(-1)
            copied_nums.pop(0)
        if len(copied_nums) == 1:
            new_list.append(copied_nums[0])
        return new_list
    return nums