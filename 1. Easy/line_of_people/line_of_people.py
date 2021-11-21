'''
You are given integers n, a and b. You are standing in a line of n people. You don't know which position you're in, but you know there are at least a people in front of you and at most b people behind you.

Return the number of possible positions you could be in.
'''

# Binary Serach - Your code took 1 millisecond — faster than 100.00% in Python.


def line_of_people(n, a, b):
    if n == a == b:
        return 0
    elif a + b < n:
        return b + 1
    elif n == b or a > b:
        return n - a
    elif a < b < n:
        return (b - a) + (n - b)