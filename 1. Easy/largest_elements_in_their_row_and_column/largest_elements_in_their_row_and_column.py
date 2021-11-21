'''
You are given a two-dimensional list of integers matrix containing 1s and 0s. Return the number of elements in matrix such that:

matrix[r][c] = 1
matrix[r][j] = 0 for every j ≠ c and matrix[i][c] = 0 for every i ≠ r
'''

# Binary Search - Your code took 41 milliseconds — faster than 100.00% in Python.

def largest_elements_in_their_row_and_column(matrix):
    count = 0
    for index_matrix in range(len(matrix)):
        if matrix[index_matrix].count(1) == 1:
            index_unique_one = matrix[index_matrix].index(1)
            current_matrix_index = index_matrix
            for index_check in range(len(matrix)):
                if index_check != current_matrix_index and matrix[index_check][index_unique_one] == 1:
                    break
                if index_check == len(matrix)-1:
                    count += 1
    return count