'''
You are given a list of integers nums. Return whether the list alternates from first strictly increasing to strictly decreasing and then strictly increasing etc. 

If a list is only strictly increasing, return true.
'''

# Binary Search - Your code took 26 milliseconds — faster than 86.50% in Python.

def strictly_alternating_list(nums):
    if nums[0] > nums[1]:
        return False
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            return False
    return True