'''
Given a list of integers nums, a string op representing either "+", "-", "/", or "*", and an integer val, perform the operation on every number in nums with val and return the result.

Note: "/" is integer division.
'''

#Binary Search - Your code took 1 millisecond — faster than 99.93% in Python


def operations(nums, op, val):
    if op == "+":
        return [add+val for add in nums]
    if op == "-":
        return [sus-val for sus in nums]
    if op == "*":
        return [pro*val for pro in nums]
    if op == "/":
        return [int(div/val) for div in nums]