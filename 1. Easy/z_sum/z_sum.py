'''
Given an n by n integer matrix, return the sum of all elements that form a Z in the matrix.
'''

# Binary Search - Your code took 1 millisecond — faster than 100.00% in Python

def z_sum(matrix):
    if len(matrix) > 2:
        top = sum(matrix[0])
        bottom = sum(matrix[-1])
        total_count = 0
        ref_index = len(matrix)-2
        for range_list in range(1, len(matrix)-1):
            total_count += matrix[range_list][ref_index]
            ref_index -= 1
        total_count += top + bottom
        return total_count
    elif len(matrix) == 1:
        top = sum(matrix[0])
        return top
    elif len(matrix) == 2:
        top = sum(matrix[0])
        bottom = sum(matrix[-1])
        return top + bottom
    else:
        return 0