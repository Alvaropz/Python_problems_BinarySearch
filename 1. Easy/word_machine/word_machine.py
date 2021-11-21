'''
You are given a list of strings ops where each element is either:

A non-negative integer that should be pushed into a stack
"POP" meaning pop the top element in the stack
"DUP" meaning duplicate the top element in the stack
"+" meaning pop the top two and push the sum
"-" meaning pop the top two and push top - second
Return the top element in the stack after applying all operations. If there are any invalid operations, return -1.

Following the operations:

We push 1 into the stack: [1]
We push 5 into the stack: [1, 5]
We duplicate the top element: [1, 5, 5]
We push 3 into the stack: [1, 5, 5, 3]
We pop 3 and 5 and push their difference 3 - 5: [1, 5, -2]
We return the top element which is -2

Invalid operation:
ops = ["+"]
-1
'''

#Binary Search - Your code took 104 milliseconds — faster than 19.74% in Python

def word_machine(ops):
        stack = []
        for index_check, element_check in enumerate(ops):
            if element_check.isdigit() and int(element_check) > -1:
                break
            if index_check == len(ops)-1:
                return -1
        for element in ops:
            if element.isdigit():
                element = int(element)
            if element == "POP":
                try:
                    stack.pop(-1)
                except:
                    return -1
            elif element == "DUP":
                try:
                    stack.append(stack[-1])
                except:
                    return -1
            elif element == "+":
                try:
                    stack.append(stack[-1]+stack[-2])
                    del stack[-3:-1]
                except:
                    return -1
            elif element == "-":
                try:
                    stack.append(stack[-1]-stack[-2])
                    del stack[-3:-1]
                except:
                    return -1
            else:
                stack.append(element)
        return stack[-1]

#Binary Search - Your code took 84 milliseconds — faster than 45.95% in Python

def word_machine_v2(ops):
    stack = []
    for element in ops:
        if element.isdigit():
            element = int(element)
        if element == "POP":
            try:
                stack.pop(-1)
            except:
                return -1
        elif element == "DUP":
            try:
                stack.append(stack[-1])
            except:
                return -1
        elif element == "+":
            try:
                stack.append(stack[-1]+stack[-2])
                del stack[-3:-1]
            except:
                return -1
        elif element == "-":
            try:
                stack.append(stack[-1]-stack[-2])
                del stack[-3:-1]
            except:
                return -1
        else:
            stack.append(element)
    return stack[-1]

#Binary Search - Your code took 69 milliseconds — faster than 89.32% in Python

def word_machine_optimised(ops):
    stack = []
    for element in ops:
        if element.isdigit():
            element = stack.append(int(element))
            continue
        if element == "POP":
            try:
                stack.pop(-1)
            except:
                return -1
        elif element == "DUP":
            try:
                stack.append(stack[-1])
            except:
                return -1
        elif element == "+":
            try:
                stack.append(stack[-1]+stack[-2])
                del stack[-3:-1]
            except:
                return -1
        elif element == "-":
            try:
                stack.append(stack[-1]-stack[-2])
                del stack[-3:-1]
            except:
                return -1
    return stack[-1]