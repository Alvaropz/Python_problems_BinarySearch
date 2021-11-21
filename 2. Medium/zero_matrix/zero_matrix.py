'''
Given a two-dimensional matrix of integers, for each zero in the original matrix, replace all values in its row and column with zero, and return the resulting matrix.
'''

# Binary Search - Your code took 69 milliseconds — faster than 15.22% in Python

def zero_matrix_v_one(matrix):
    set_r, set_c = set(), set()
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if (not c in set_c or not r in set_r) and matrix[r][c] == 0:
                set_c.add(c)
                set_r.add(r)
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if r in set_r or c in set_c:
                matrix[r][c] = 0
    return matrix

# Binary Search - Your code took 77 milliseconds — faster than 14.33% in Python.

def zero_matrix_v_two(matrix):
    set_r, set_c = set(), set()
    for r in range(len(matrix)):
        if 0 in matrix[r]:
            set_r.add(r)
        for c in range(len(matrix[r])):
            if matrix[r][c] == 0:
                set_c.add(c)
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if r in set_r or c in set_c:
                matrix[r][c] = 0
    return matrix

# Binary Search - Your code took 88 milliseconds — faster than 12.67% in Python.

def zero_matrix_v_three(matrix):
    set_r = set()
    set_c = set()
    new_matrix = []
    for r in range(len(matrix)):
        if 0 in matrix[r]:
            set_r.add(r)
        for c in range(len(matrix[r])):
            if matrix[r][c] == 0:
                set_c.add(c)
    for r in range(len(matrix)):
        temp_list = []
        for c in range(len(matrix[r])):
            if r in set_r or c in set_c:
                temp_list.append(0)
            else:
                temp_list.append(matrix[r][c])
        new_matrix.append(temp_list)
    return new_matrix