'''
Given an integer n less than or equal to 10, compute its factorial.

The factorial of a number n is defined as n * (n - 1) * (n - 2) * ... * 1.
'''

# Binary Search - Your code took 1 millisecond — faster than 99.92% in Python.
   
def factorial_factory(n):
    if n == 0:
        return 1
    factorial_number = n
    for number in range(1, n):
        factorial_number *= (n-number)
    return factorial_number