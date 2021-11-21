'''
Given a list of [x, y] coordinates in a Cartesian plane, return whether the coordinates form a straight line segment.
'''

# Binary Search - Your code took 75 milliseconds — faster than 29.30% in Python.

def line_segment(coordinates):
    difference_set = set()
    for cartesian in range(1, len(coordinates)):
        diff_y = coordinates[cartesian][1] - coordinates[cartesian-1][1]
        diff_x = coordinates[cartesian][0] - coordinates[cartesian-1][0]
        if diff_x == 0:
            return False
        div_y_x = diff_y / diff_x
        difference_set.add(div_y_x)
        if len(difference_set) > 1:
            return False
    return True