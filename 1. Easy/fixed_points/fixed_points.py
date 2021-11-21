'''
Given a list of unique integers nums sorted in ascending order, return the minimum i such that nums[i] == i. If there's no solution, return -1.

This should be done in \mathcal{O}(log(n))O(log(n)) time.
'''

# Binary Searchc- Your code took 43 milliseconds — faster than 49.82% in Python.

def fixed_points(nums):
    if len(nums) == 1 and nums[0] != 0 or not nums:
        return -1
    min_index_val = nums[0]
    for index, number in enumerate(nums):
        if index == number:
            if min_index_val < 0 and number >= min_index_val:
                min_index_val = index
    if min_index_val < 0 or min_index_val == nums[0] != 0:
        return -1
    return min_index_val