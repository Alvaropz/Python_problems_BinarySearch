'''
Implement a stack with the following methods:

MinimumStack() constructs a new instance of a minimum stack
append(int val) appends val to the stack
peek() retrieves the last element in the stack
min() retrieves the minimum value in the stack
pop() pops and returns the last element in the stack
Each method should be done in \mathcal{O}(1)O(1) time. You can assume that for peek, min and pop, the stack is non-empty when they are called.
'''

# Binary Search - Your code took 87 milliseconds — faster than 32.55% in Python.

class MinimumStack:
    def __init__(self):
        self.myTrack = {}
        self.myList = []
        self.minVal = float('inf')

    def append(self, val):
        self.myList.append(val)
        if val < self.minVal:
            self.minVal = val
        if val in self.myTrack:
            self.myTrack[val] += 1
        else:
            self.myTrack[val] = 1

    def peek(self):
        return self.myList[-1]

    def min(self):
        if not self.minVal in self.myTrack:
            self.minVal = min(list(self.myTrack))
        return self.minVal

    def pop(self):
        self.myTrack[self.myList[-1]] -= 1
        if self.myTrack[self.myList[-1]] == 0:
            del self.myTrack[self.myList[-1]]
        return self.myList.pop()