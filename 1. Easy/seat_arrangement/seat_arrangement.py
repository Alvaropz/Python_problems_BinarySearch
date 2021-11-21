'''
You are given an integer n, the number of people looking to find a seat, and a list of integers seats where a 1 represents an already occupied seat and 0 represents empty space.

Given that no two people can sit next to each other, return whether all n people can find a seat.
'''

# Binary Search - Your code took 195 milliseconds — faster than 55.34% in Python.


def seat_arrangement(convention, n):
    if n == 0 or len(convention) == 1 and convention[0] == 0 and n == 1:
        return True
    if not convention:
        return False
    if len(convention) == 2:
        if convention[0] == 0 and convention[1] == 0:
            convention[0] = 1
            n -= 1
    else:         
        if convention[0] == 0 and convention[1] == 0:
            convention[0] = 1
            n -= 1
        if convention[-2] == convention[-1] == 0 and n > 0:
            convention[-1] = 1
            n -= 1
        for index in range(2, len(convention)):
            if index+1 < len(convention):
                if convention[index-1] == convention[index] == convention[index+1] == 0 and n > 0:
                    convention[index] = 1
                    n -= 1
    if n == 0:
        return True
    return False