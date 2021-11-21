'''
Given a list of integers nums, return whether you can rearrange the order of nums such that the difference between every consecutive two numbers is the same.
'''

# Binary Search - Your code took 245 milliseconds — faster than 44.21% in Python.

def arithmetic_sequence_permutation(nums):
    nums.sort()
    difference = abs(nums[0] - nums[1])
    i = 0
    j = len(nums)-1
    while i < j:
        if nums[i] + difference != nums[i+1]:
            return False
        i += 1
    return True

# Binary Search - Your code took 132 milliseconds — faster than 100.00% in Python.

def arithmetic_sequence_permutation_optimised(nums):
    nums_set = set(nums)
    if len(nums_set) == 1:
        return True
    if len(nums_set) != len(nums):
        return False
    start = min(nums)
    end = max(nums)
    if (end - start) % (len(nums) - 1) == 0:
        gap = (end - start) // (len(nums) - 1)
        for i in range(start, end + 1, gap):
            if i not in nums_set:
                return False
    else:
        return False
    return True