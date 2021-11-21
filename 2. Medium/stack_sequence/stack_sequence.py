'''
Given a list of integers pushes, and another list of integers pops, return whether this is a valid sequence of stack push and pop actions.
'''

# Binary Search - Your code took 36 milliseconds — faster than 32.02% in Python.

def stack_sequence(pushes, pops):
    stack = []
    i = 0
    for value in pushes:
        stack.append(value)
        if stack[-1] == pops[i]:
            while stack and stack[-1] == pops[i]:
                stack.pop()
                i += 1
    return len(stack) == 0