'''
Given two lists of integers nums, and target, consider an operation where you take some sublist in nums and reverse it. 

Return whether it's possible to turn nums into target, given you can make any number of operations.
'''

# Binary Search - Your code took 36 milliseconds — faster than 96.96% in Python

def reverse_sublists_to_convert_to_target(nums, target):
    nums.sort()
    target.sort()
    if nums == target:
        return True
    return False