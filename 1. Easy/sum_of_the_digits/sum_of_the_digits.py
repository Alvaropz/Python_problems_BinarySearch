'''
Given a positive integer num, return the sum of its digits.

Bonus: Can you do it without using strings?
'''

# Binary Search -Your code took 3 milliseconds — faster than 32.04% in Python

def sum_of_the_digits(num):
    sum_t = 0
    new_number = num
    while new_number > 0:
        sum_number = new_number % 10
        sum_t += sum_number
        new_number = new_number // 10
    return sum_t