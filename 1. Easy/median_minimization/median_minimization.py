'''
Given a list of integers nums, split it into two lists of equal size where the absolute difference between each list's median is as small as possible and return this difference.

Note: length of nums / 2 is guaranteed to be odd.
'''

# Binary Search - Your code took 12 milliseconds — faster than 84.71% in Python.

def median_minimization(nums):
    nums.sort()
    return abs(nums[:int(len(nums)/2)][-1] - nums[int(len(nums)/2):][0])