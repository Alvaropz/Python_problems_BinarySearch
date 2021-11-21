'''
Given a list of integers nums and an integer k, let's create a new set of possible elements { nums[k], nums[nums[k]], nums[nums[nums[k]]], ... } stopping before it's out of index.

Return the size of this set, or -1 if there's a cycle.
'''

# Binary Search - Your code took 2 milliseconds — faster than 77.99% in Python.

def recursive_index(nums, k):
    final_set = set()
    while k < len(nums):
        if not nums[k] in final_set:
            final_set.add(nums[k])
        else:
            return -1
        k = nums[k]
    return len(final_set)