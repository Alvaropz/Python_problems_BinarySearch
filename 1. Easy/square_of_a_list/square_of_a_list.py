'''
Given a list of integers sorted in ascending order nums, square the elements and give the output in sorted order.
'''

# Binary Search - Your code took 298 milliseconds — faster than 49.43% in Python

def square_of_a_list(nums):
    square_list = [number**2 for number in nums]
    square_list.sort()
    return square_list

