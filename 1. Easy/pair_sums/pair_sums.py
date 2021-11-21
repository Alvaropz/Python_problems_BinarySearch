'''
Given a list of positive integers nums, return the number of valid pairs of indices (i, j), with i < j, such that A[i] + A[j] is an odd number.
'''

# Binary Search - Your code took 9 milliseconds — faster than 82.62% in Python.

def pair_sums(nums):
    count_odds = 0
    count_evens = 0
    for number in nums:
        if number % 2 == 0:
            count_evens += 1
        else:
            count_odds += 1
    return count_odds * count_evens

# Binary Search - Your code took 8 milliseconds — faster than 90.63% in Python.

def pair_sums_optimised(nums):
    count_evens = 0
    for number in nums:
        if number % 2 == 0:
            count_evens += 1
    return count_evens * (len(nums)-count_evens)