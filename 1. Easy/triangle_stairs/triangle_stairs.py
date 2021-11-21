'''
Given n, return a string of stairs of size n. For example given n = 4 return
'''

# Binary Search - Your code took 12 milliseconds — faster than 88.49% in Python

def triangle_stairs(n):
    star_string = ""
    for stair in range(1,n):
        star_string += (n - stair) * (" ") + stair * "*" + "\n"
    star_string += n * "*"
    return star_string