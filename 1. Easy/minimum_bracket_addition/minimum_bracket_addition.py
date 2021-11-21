'''
Given a string s containing brackets ( and ), return the minimum number of brackets that can be inserted so that the brackets are balanced.
'''

# Binary Search - Your code took 20 milliseconds — faster than 78.66% in Python

def minimum_bracket_addition(s):
    stack = []
    for bracket in s:
        if bracket == ")" and "(" in stack:
            stack.pop()
        else:
            stack.append(bracket)            
    return len(stack)
