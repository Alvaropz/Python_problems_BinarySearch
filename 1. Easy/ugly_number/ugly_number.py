'''
Given an integer n, return whether its prime factors only include 2, 3 or 5.
'''

# Binary Search - Your code took 13 milliseconds — faster than 16.46% in Python.

def ugly_number(n):
    if n > 0:
        while n > 1:
            if n % 5 == 0:
                n = int(n/5)
            elif n % 3 == 0:
                n = int(n/3)
            elif n % 2 == 0:
                n = int(n/2)
            else:
                return False
        return True
    return False