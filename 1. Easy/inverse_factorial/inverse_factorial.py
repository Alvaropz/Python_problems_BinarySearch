'''
The factorial of a number n is defined as n! = n * (n - 1) * (n - 2) * ... * 1.

Given a positive integer a, return n such that n! = a. If there is no integer n that is a factorial, then return -1.
'''

# Binary Search - Your code took 1 millisecond — faster than 99.71% in Python.

def inverse_factorial(a):
    if a == 1:
        return 0
    total = 1
    for number in range(2, a+1):
        total *= number
        if total == a:
            return number
        if total > a:
            return -1