'''
Given a two-dimensional integer matrix, sort each of the columns in ascending order.
'''

# Binary Search - Your code took 83 milliseconds — faster than 4.30% in Python. Additional comments: Even if this code is really slow, after checking others' code, the performance improve "only" up to 10% aprox.
def column_sort(matrix):
    if len(matrix) > 1:
        new_matrix = []
        temp_matrix = []
        for inner_index in range(len(matrix[0])):
            for outer_index in range(len(matrix)):
                temp_matrix.append(matrix[outer_index][inner_index])
            new_matrix.append(sorted(temp_matrix))
            temp_matrix = []
        sorted_matrix = []
        for inner_index in range(len(new_matrix[0])):
            for outer_index in range(len(matrix[0])):
                temp_matrix.append(new_matrix[outer_index][inner_index])
            sorted_matrix.append(temp_matrix)
            temp_matrix = []
        return sorted_matrix
    return matrix