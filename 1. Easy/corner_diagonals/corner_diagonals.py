'''
You are given an integer n representing the length of an n by n board. 
Remove all cells that are diagonal to one of the four corners (top left, top right, bottom right, and bottom left) and return the number of empty cells leftover.
'''

# Binary Search - Your code took 1 millisecond — faster than 100.00% in Python.

def corner_diagonals(n):
    total_squares = n**2
    if n % 2 == 0:
        diagonal = total_squares - n*2
    else:
        diagonal = (total_squares - n*2) + 1
    return diagonal