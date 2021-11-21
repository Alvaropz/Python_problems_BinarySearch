'''
Given a list of integers nums, put all the zeros to the back of the list by modifying the list in-place. The relative ordering of other elements should stay the same.

Can you do it in O(1) additional space?
'''

# Binary Search - Your code took 48 milliseconds — faster than 95.51% in Python.

def in_place_move_zeros_to_end_of_list(nums):
    sorted_list = [number for number in nums if number != 0]
    sorted_list.extend([0]*nums.count(0))
    return sorted_list