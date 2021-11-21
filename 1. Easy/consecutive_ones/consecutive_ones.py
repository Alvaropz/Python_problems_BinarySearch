'''
You are given a list of integers nums which contains at least one 1. Return whether all the 1s appear consecutively.
'''

# Binary Search - Your code took 21 milliseconds — faster than 82.71% in Python.

def consecutive_ones(nums):
    first_one = nums.index(1)
    if nums[first_one:].count(1) == len(nums[first_one:]):
        return True
    for number in range(first_one, len(nums)):
        if nums[number] != 1:
            if 1 in nums[number:]:
                return False
            else:
                return True