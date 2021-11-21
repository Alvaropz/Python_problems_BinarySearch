'''
Given a string s representing characters typed into an editor, with "<-" representing a backspace, return the current state of the editor.
'''

# Binary Search - Your code took 119 milliseconds — faster than 29.81% in Python.

def text_editor(s):
    i = 0
    j = len(s)-1
    list_text_editor = []
    while i <= j:
        list_text_editor.append(s[i])
        if s[i] == "-":
            if len(list_text_editor) > 1 and s[i-1] == "<":
                list_text_editor.pop()
                list_text_editor.pop()
                if len(list_text_editor) > 0:
                    list_text_editor.pop()
        i += 1 
    return "".join(list_text_editor)