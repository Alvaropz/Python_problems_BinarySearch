# Binary Search - Your code took 3 milliseconds — faster than 93.86% in Python

def run_length_encoding_string(s):
    new_str = ""
    counter = 1
    for index, element in enumerate(s):
        if index+1 < len(s):
            if element == s[index+1]:
                counter += 1
            else:
                new_str += str(counter) + element
                counter = 1
        else:
            new_str += str(counter) + element
    return new_str

# Binary Search - Your code took 4 milliseconds — faster than 45.01% in Python

def run_length_encoding_list(s):
    new_str = ""
    counter = 1
    char_list = [char for char in s]
    for index, element in enumerate(char_list):
        if index+1 < len(char_list):
            if element == char_list[index+1]:
                counter += 1
            else:
                new_str += str(counter) + element
                counter = 1
        else:
            new_str += str(counter) + element
    return new_str