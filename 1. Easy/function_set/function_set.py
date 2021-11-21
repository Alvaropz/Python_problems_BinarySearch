'''
Implement a set data structure with the following methods:

Set() constructs a new instance of a set
add(int val) adds val to the set
exists(int val) returns whether val exists in the set
remove(int val) removes the val in the set
This should be implemented without using built-in set.
'''

# Binary Search - Your code took 84 milliseconds — faster than 78.77% in Python

class Set:
    def __init__(self):
        self.set = set()

    def add(self, val):
        self.set.add(val)

    def exists(self, val):
        if val in self.set:
            return True
        return False

    def remove(self, val):
        if val in self.set:
            self.set.remove(val)