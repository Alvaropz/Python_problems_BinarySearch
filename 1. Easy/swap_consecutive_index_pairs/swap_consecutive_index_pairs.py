'''
Given a list of integers nums, swap each consecutive even indexes with each other, and swap each consecutive odd indexes with each other.
'''

# Binary Search - Your code took 11 milliseconds — faster than 24.73% in Python.

def swap_consecutive_index_pairs(nums):
    for i in range(0, len(nums), 4):
        if i+2 < len(nums):
            nums[i], nums[i+2] = nums[i+2], nums[i]
        if i+3 < len(nums):
            nums[i+1], nums[i+3] = nums[i+3], nums[i+1]
    return nums
