'''
Given a list of integers nums sorted in ascending order and an integer k, return whether any two elements from the list add up to k. You may not use the same element twice.

Note: Numbers can be negative or 0.

This should be done in O(1) space.
'''

# Binary Search - Your code took 68 milliseconds — faster than 7.80% in Python.

from collections import Counter

def sum_of_two_numbers_with_sorted_list(nums, k):
    if len(nums) > 1:
        counting_dict = Counter(nums)
        for key in counting_dict.keys():
            if (counting_dict[key] > 1 or (counting_dict[key] == 1 and  k - key != key)) and k - key in counting_dict.keys():
                return True
    return False

# Binary Search - Your code took 23 milliseconds — faster than 78.05% in Python.

def sum_of_two_numbers_with_sorted_list_optimised(nums, k):
    i = 0
    j = len(nums)-1
    while i < j:
        cur_sum = nums[i] + nums[j]
        if cur_sum == k:
            return True
        elif cur_sum < k:
            i += 1
        else:
            j -= 1
    return False