'''
Give a list of numbers nums, return the number of elements that are in the correct indices, if the list were to be sorted.
'''

#Binary Search - Your code took 2 milliseconds — faster than 95.87% in Python

def right_sorted(nums):
    count = 0
    nums_sorted = sorted(nums)
    for index in range(len(nums)):
        if nums[index] == nums_sorted[index]:
            count += 1
    return count