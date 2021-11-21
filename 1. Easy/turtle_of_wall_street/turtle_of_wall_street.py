'''
You are given a list of integers nums representing stock prices of a company in chronological order. 

You can buy at most one share of stock per day, but you can hold onto multiple stocks and can sell stocks on any number of days. Return the maximum profit you can earn.
'''

# Binary Search - Your code took 83 milliseconds — faster than 75.97% in Python.

def turtle_of_wall_street(nums):
    if len(nums) == 1:
        return 0
    total = 0
    nums = nums[::-1]
    i = 0
    j = len(nums)
    while i + 1 < j:
        if nums[i] >= nums[i+1]:
            biggest_n = nums[i]
            while i < j and biggest_n >= nums[i]:
                total += (biggest_n - nums[i])
                i += 1
        else:
            i += 1
    return total