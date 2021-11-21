'''
Given an integer n, return its base 3 representation as a string.
'''

# Binary Search - Your code took 1 millisecond — faster than 100.00% in Python.

def integer_to_base_three(n):
    base_three = ""
    abs_value = abs(n)
    while abs_value > 0:
        base_three += str(abs_value%3)
        abs_value = int(abs_value/3)
    if n < 0:
        reversed_string = str(base_three)[::-1]
        return "-" + reversed_string
    else:
        return base_three[::-1]