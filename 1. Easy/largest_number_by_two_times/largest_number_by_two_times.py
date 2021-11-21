'''
Given a list of integers nums, return whether the largest number is bigger than the second-largest number by more than two times.
'''

#Binary Search - Your code took 1 millisecond — faster than 99.71% in Python

def largest_number_by_two_times(nums):
    nums.sort()
    if nums[-2]*2 >= nums[-1]:
        return False
    return True