'''
Given an integer list nums where each number represents the maximum number of hops you can make, determine whether you can reach to the last index starting at index 0.
'''

# Binary Search - Your code took 97 milliseconds — faster than 46.17% in Python.

def hoppable_v_one(nums):
    hops = nums[0] - 1
    for idx in range(len(nums)-1):
        if nums[idx] > hops and hops >= 0:
            hops = nums[idx]
        if hops <= 0:
            return False
        hops -= 1
    return True

# Binary Search - Your code took 112 milliseconds — faster than 29.84% in Python

def hoppable_v_two(nums):
    temp_hop = nums[0]
    for index in range(1, len(nums)):
        if temp_hop > 0:
            temp_hop -= 1
            if nums[index] >= temp_hop:
                temp_hop = nums[index]
        else:
            return False
    return True