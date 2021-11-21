'''
Given a list of integers nums, return whether there's two numbers such that one is a triple of another.
'''

# Binary Search - Your code took 36 milliseconds — faster than 46.01% in Python

def a_number_and_its_triple(nums):
    for number in nums:
        if number*3 == 0 and nums.count(0) > 1:
            return True
        elif number*3 == 0 and nums.count(0) == 1:
            continue
        if number*3 in nums:
            return True
    return False

# Binary Search - Your code took 46 milliseconds — faster than 38.84% in Python

def a_number_and_its_triple_v2(nums):
    if 0 in nums and nums.count(0) == 1:
        nums.remove(0)
    for number in nums:
        if number*3 in nums:
            return True
    return False