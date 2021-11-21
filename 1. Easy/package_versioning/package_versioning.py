'''
Given strings older and newer, each representing software package versions in the format major.minor.patch, return whether the newer version is actually newer than the older.
'''

#Binary Search - Your code took 1 millisecond — faster than 100.00% in Python

def package_versioning(older, newer):
    old = list(map(int, older.split(".")))
    new = list(map(int, newer.split(".")))
    if old == new:
        return False
    if old[0] > new[0]:
        return False
    elif old[1] > new[1] and old[0] < new[0]:
        return False
    elif old[2] > new[2] and old[1] < new[1] and old[0] < new[0]:
        return False
    return True