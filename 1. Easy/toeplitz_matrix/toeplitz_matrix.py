'''
Given a two-dimensional matrix of integers matrix, determine whether it's a Toeplitz matrix. A Toeplitz is one where every diagonal descending from left to right has the same value.

Constraints

n, m ≤ 250 where n and m are the number of rows and columns in matrix
'''

# Binary Search - Your code took 8 milliseconds — faster than 15.15% in Python.

def toeplitz_matrix(matrix):
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if r+1 < len(matrix) and c+1 < len(matrix[r]):
                    if matrix[r][c] != matrix[r+1][c+1]:
                        return False
        return True