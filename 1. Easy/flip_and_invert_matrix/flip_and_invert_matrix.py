'''
You are given a two-dimensional integer matrix matrix containing 1s and 0s. For each row in matrix, reverse the row. 

Then, flip each value in the matrix such that any 1 becomes 0 and any 0 becomes 1.
'''

# Binary Search - Your code took 15 milliseconds — faster than 84.33% in Python.

def flip_and_invert_matrix(matrix):
    reversed_matrix = [list(reversed(sub_list)) for sub_list in matrix]
    return [[0 if number == 1 else 1 for number in sub_list] for sub_list in reversed_matrix]