'''
Given a Unix path, represented as a list of strings, return its resolved version.

In Unix, ".." means to go to the previous directory and "." means to stay on the current directory. By resolving, we mean to evaluate the two symbols so that we get the final directory we're currently in.
'''

# Binary Search - Your code took 181 milliseconds — faster than 7.33% in Python

def unix_path_resolution(path):
        final_path = []
        path = list(filter(lambda x: x != ".", path))
        if len(path) == 0:
            return final_path
        if path[0] != ".." and path[0] != ".":
            final_path.append(path[0])
        for i in range(1, len(path)):
            if path[i] == ".." and final_path:
                final_path.pop()
            elif path[i] != "..":
                final_path.append(path[i])
        return final_path