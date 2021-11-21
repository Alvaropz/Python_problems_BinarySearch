'''
Given a list of integers nums, return whether there exist integers a, b, and c such that a^2 + b^2 = c^2.
'''

# Binary Search - Your code took 47 milliseconds — faster than 86.23% in Python.


def pythagorean_triplets(nums):
    squares = [number ** 2 for number in nums]
    set_squares = set(squares)
    for number_1 in squares:
        for number_2 in squares:
            if number_1 + number_2 in set_squares:
                return True
    return False