'''
Given a list of integers nums, return the number of times that the list changes from positive-to-negative or negative-to-positive slope.

Constraints

n ≤ 100,000 where n is the length of nums
'''

# Binary Search - Your code took 161 milliseconds — faster than 21.80% in Python.

def changing_directions(nums):
    i = 0
    j = len(nums)-1
    slope = 0
    while i+1 < j:
        if nums[i] > nums[i+1]:
            if nums[i+1] < nums[i+2]:
                slope += 1
        if nums[i] < nums[i+1]:
            if nums[i+1] > nums[i+2]:
                slope += 1
        i += 1
    return slope