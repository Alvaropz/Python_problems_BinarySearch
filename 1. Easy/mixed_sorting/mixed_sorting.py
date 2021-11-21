'''
Given a list of integers nums, sort the array such that:

All even numbers are sorted in increasing order
All odd numbers are sorted in decreasing order
The relative positions of the even and odd numbers remain the same
'''

# Binary Search - Your code took 2 milliseconds — faster than 85.02% in Python

def mixed_sorting(nums):
    returned_list = []
    even = sorted([number for number in nums if number % 2 == 0])
    index_even = [index for index, number in enumerate(nums) if number % 2 == 0]
    odd = sorted([number for number in nums if number % 2 != 0])
    index_odd = [index for index, number in enumerate(nums) if number % 2 != 0]
    odd.reverse()
    ordered_list = list(zip(index_even, even)) + list(zip(index_odd, odd))
    ordered_list.sort()
    index = 0
    while index != len(ordered_list):
        returned_list.append(ordered_list[index][1])
        index += 1
    return returned_list