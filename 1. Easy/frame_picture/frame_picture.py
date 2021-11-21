'''
Given a list of words, frame it rectangularly, line by line.

Note: Each line should be separated by a newline separator, or \n.
'''

# Binary Search - Your code took 3 milliseconds — faster than 96.73% in Python

def frame_picture(words):
    max_lenght = len(max(words, key=len))
    new_string = "*"*(max_lenght+4) + "\n"
    for word in words:
        new_string += "* " + word + (max_lenght - len(word))*" " + " *\n"
    new_string += "*"*(max_lenght+4)
    return new_string