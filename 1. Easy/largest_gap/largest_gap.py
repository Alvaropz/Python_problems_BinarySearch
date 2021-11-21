'''
Given a list of integers nums, return the largest difference of two consecutive integers in the sorted version of nums.
'''

# Binary Search - Your code took 306 milliseconds — faster than 41.80% in Pythona

def largest_gap(nums):
    nums.sort()
    largest_gap = 0
    for index, number in enumerate(nums):
        if index+1 != len(nums):
            diff = nums[index+1] - number
            if diff > largest_gap:
                largest_gap = diff
    return largest_gap