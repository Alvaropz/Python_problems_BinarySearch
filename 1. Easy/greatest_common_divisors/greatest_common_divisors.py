'''
Given a list of positive integers nums, return the largest positive integer that divides each of the integers.
'''

# Binary Search - Your code took 24 milliseconds — faster than 13.92% in Python.

def greatest_common_divisors(nums):
    divisor = 1
    set_checker = set()
    while divisor <= min(nums):
        count = 0
        for index in range(len(nums)):
            if nums[index] % divisor == 0:
                count += 1
            else:
                break
        if count == len(nums):
            if divisor in set_checker:
                return divisor
            else:
                set_checker.add(divisor)
        divisor += 1
    return max(set_checker)