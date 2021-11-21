'''
Given a positive integer n, determine whether you can make n by summing up some non-negative multiple of 3 and some non-negative multiple of 7.
'''

# Binary Search - Your code took 2 milliseconds — faster than 96.62% in Python.

def three_and_seven(n):
    if n % 3 == 0:
        return True
    if n % 7 == 0:
        return True
    if n > 9:
        while n > 9:
            n = n-(int("1"+(len(str(n))-1)*"0"))
            if n % 3 == 0:
                return True
            if n % 7 == 0:
                return True
    return False