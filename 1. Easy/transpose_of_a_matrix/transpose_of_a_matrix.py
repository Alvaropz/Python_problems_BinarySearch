'''
Given an integer square (n by n) matrix, return its transpose. A transpose of a matrix switches the row and column indices. 

That is, for every r and c, matrix[r][c] = matrix[c][r].
'''

# Binary Search - Your code took 3 milliseconds — faster than 77.66% in Python.

def transpose_of_a_matrix(matrix):
    transpose_matrix = []
    for r in range(len(matrix)):
        temp_matrix = []
        for c in range(len(matrix)):
            temp_matrix.append(matrix[c][r])
        transpose_matrix.append(temp_matrix)
    return transpose_matrix