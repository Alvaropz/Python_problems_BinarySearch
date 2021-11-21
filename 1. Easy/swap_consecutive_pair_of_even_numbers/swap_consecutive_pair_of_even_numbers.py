'''
Given an integer list nums, swap every consecutive even integer with each other.
'''

# Binary Search - Your code took 7 milliseconds — faster than 79.65% in Python.

def swap_consecutive_pair_of_even_numbers(nums):
    i = 0
    j = len(nums)-1
    while i < j:
        if nums[i] % 2 == 0:
            second_i = i+1
            while second_i <= j:
                if nums[second_i] % 2 == 0:
                    nums[i], nums[second_i] = nums[second_i], nums[i]
                    i = second_i
                    break
                second_i += 1
        i += 1
    return nums
