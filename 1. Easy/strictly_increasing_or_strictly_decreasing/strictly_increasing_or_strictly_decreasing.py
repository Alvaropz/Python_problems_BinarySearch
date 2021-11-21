'''
Given an list of numbers, determine whether the list is strictly increasing or strictly decreasing.
'''

#Binary Search - Your code took 3 milliseconds — faster than 68.68% in Python.

def strictly_increasing_or_strictly_decreasing(nums):
    if len(nums) > 1:
        if nums[0] < nums[1]:
            for index, number in enumerate(nums):
                if index+1 != len(nums) and number >= nums[index+1]:
                    return False
        else:
            for index, number in enumerate(nums):
                if index+1 != len(nums) and number <= nums[index+1]:
                    return False
    return True