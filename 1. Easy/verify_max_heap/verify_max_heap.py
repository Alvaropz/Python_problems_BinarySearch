'''
Given a list of integers nums, return whether it represents a max heap. That is, for every i we have that:

nums[i] ≥ nums[2*i + 1] if 2*i + 1 is within bounds
nums[i] ≥ nums[2*i + 2] if 2*i + 2 is within bounds
'''

# Binary Search - Your code took 69 milliseconds — faster than 20.92% in Python.

def verify_max_heap(nums):
    lenght_nums = len(nums)
    for idx in range(int(len(nums)/2)):
        plus_two = (2*idx)+2
        plus_one = (2*idx)+1
        if plus_one < lenght_nums and nums[idx] < nums[plus_one]:
            return False
        elif plus_two < lenght_nums and nums[idx] < nums[plus_two]:
            return False
    return True