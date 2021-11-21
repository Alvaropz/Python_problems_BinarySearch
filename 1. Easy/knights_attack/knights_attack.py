'''
You are given a two-dimensional integer matrix of 1s and 0s, representing a rectangular chess board, where 0 is an empty cell and 1 is a knight.

Return whether any two knights are attacking each other.
'''

# Binary Search - Your code took 19 milliseconds — faster than 55.15% in Python.

def knights_attack(matrix):
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == 1:
                if r+2 < len(matrix) and c+1 < len(matrix[r]) and matrix[r+2][c+1] == 1:
                    return True
                if r+2 < len(matrix) and c-1 > -1 and matrix[r+2][c-1] == 1:
                    return True
                if r-2 > -1 and c+1 < len(matrix[r]) and matrix[r-2][c+1]== 1:
                    return True
                if r-2 > -1 and c-1 > -1 and matrix[r-2][c-1] == 1:
                    return True
                if r+1 < len(matrix) and c+2 < len(matrix[r]) and matrix[r+1][c+2] == 1:
                    return True
                if r-1 > -1 and c+2 < len(matrix[r]) and matrix[r-1][c+2] == 1:
                    return True
                if r+1 < len(matrix) and c-2 > -1 and matrix[r+1][c-2] == 1:
                    return True
                if r-1  > -1 and c-2 > -1 and matrix[r-1][c-2] == 1:
                    return True
    return False