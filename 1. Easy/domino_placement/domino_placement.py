'''
You are given integers n and m representing a board of size n by m. You also have an unlimited number of 1 by 2 dominos.

Return the maximum number of dominos that can be placed on the board such that they don't overlap and every domino lies entirely within the board.
'''

# Binary Search - Your code took 1 millisecond — faster than 100.00% in Python.

def domino_placement(n, m):
    return int((n*m) / 2)