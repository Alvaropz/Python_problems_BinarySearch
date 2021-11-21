'''
A Roomba robot is currently sitting in a Cartesian plane at (0, 0). You are given a list of its moves that it will make, containing NORTH, SOUTH, WEST, and EAST.

Return whether after its moves it will end up in the coordinate (x, y).
'''

# Binary Search - Your code took 17 milliseconds — faster than 78.98% in Python.

def roomba(moves, x, y):
    x_target = 0
    y_target = 0
    for move in moves:
        if move == "NORTH":
            y_target += 1
        elif move == "SOUTH":
            y_target -= 1
        elif move == "EAST":
            x_target += 1
        elif move == "WEST":
            x_target -= 1
    if x_target != x or y_target != y:
        return False
    return True