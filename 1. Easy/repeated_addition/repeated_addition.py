'''
Given a positive integer n, sum all of its digits to get a new number. Repeat this operation until it's less than 10.
'''

# Binary Search - Your code took 1 millisecond — faster than 100.00% in Python

def repeated_addition(n):
    temp_number = n
    while n > 9:
        n = sum([int(number) for number in str(temp_number)])
        temp_number = n
    return n