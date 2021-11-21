'''
You are given a list of integers nums of length n where all numbers in the list are from the interval [1, n][1,n] and some elements appear twice while others only once. Return all the numbers from [1, n][1,n] that are not in the list, sorted in ascending order.

Can you do it in \mathcal{O}(n)O(n) time, modify nums in-place and use \mathcal{O}(1)O(1) additional space?
'''

# Binary Search - Your code took 140 milliseconds — faster than 93.83% in Python

def missing_numbers_from_one_to_n(nums):
    missing_numbers = []
    total_len = len(nums)
    set_numbers = set(nums)
    for number in range(1, total_len+1):
        if not number in set_numbers:
            missing_numbers.append(number)
    return sorted(missing_numbers)