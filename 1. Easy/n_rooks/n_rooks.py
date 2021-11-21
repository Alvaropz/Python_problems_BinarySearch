'''
You've got an integer n representing a chessboard of size n x n. Return the number of ways you can place n rooks, such that no two rooks attack each other.

Two ways are considered different if in one of the ways, some cell of the chessboard is occupied, and in the other way, the cell is not occupied.

Note: two rooks are attacking each other if they are either on the same row or on the same column.

n = 3
Output: 6

Here are the different chessboard configurations, where X is a rook.

X O O 
O X O
O O X

X O O 
O O X
O X O

O X O
X O O
O O X

O X O
O O X
X O O

O O X
O X O
X O O

O O X
X O O
O X O
'''

# Binary Search - Your code took 1 millisecond — faster than 100.00% in Python.

def n_rooks(n):
    if n > 1:
        rows = (n*n)-n
        ref_number = 1
        while ref_number < n-1:
            rows *= (ref_number)
            ref_number += 1
        return rows
    return 1