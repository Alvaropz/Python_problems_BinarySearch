'''
Given a list of integers, find the largest product of two distinct elements.
'''

#Bindary Search - Your code took 1 millisecond — faster than 100.00% in Python

def max_product(nums):
    nums.sort()
    result_first_two = nums[0] * nums[1]
    result_last_two = nums[-1] * nums[-2]
    if result_first_two > result_last_two:
        return result_first_two
    else:
        return result_last_two