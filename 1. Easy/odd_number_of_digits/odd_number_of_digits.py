'''
Given a list of positive integers nums, return the number of integers that have odd number of digits.
'''

# Binary Search - Your code took 203 milliseconds — faster than 77.46% in Python

def odd_number_of_digits_cl(nums):
    return len([word for word in nums if len(str(word)) % 2 != 0])

# Binary Search - Your code took 200 milliseconds — faster than 84.10% in Python

def odd_number_of_digits_for(nums):
    total_count = 0
    for number in nums:
        if len(str(number)) % 2 != 0:
            total_count += 1
    return total_count