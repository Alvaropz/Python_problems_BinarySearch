'''
Write a function that rotates a list of numbers to the left by k elements. Numbers should wrap around.

Note: The list is guaranteed to have at least one element, and k is guaranteed to be less than or equal to the length of the list.

Bonus: Do this without creating a copy of the list. How many swap or move operations do you need?
'''

# Binary Search - Your code took 8 milliseconds — faster than 31.03% in Python

def rotate_list_by_k_less(nums, k):
    initial_list = [nums[index] for index in range(k, len(nums))]
    initial_list = initial_list + nums[:k]
    return initial_list

# Your code took 5 milliseconds — faster than 99.93% in Python

def rotate_list_by_k_optimised(nums, k):
    return nums[k:] + nums[:k]