'''
You are given a list of integers nums. Return the number of pairs i < j such that nums[i] = nums[j].
'''

# Binary Search - Your code took 44 milliseconds — faster than 73.02% in Python.

def equivalent_pairs(nums):
    d = {}
    total = 0
    for number in nums:
        if number in d:
            d[number] += 1
            total += d[number]
        else:
            d[number] = 0
    return total