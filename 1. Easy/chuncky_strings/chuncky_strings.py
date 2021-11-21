'''
Given a string s and an integer n, split up s into n-sized pieces.
'''

#Binary Search -Your code took 1 millisecond — faster than 100.00% in Python

def chuncky_strings_optimised(s, n):
    mod_s = s
    lenght_list = []
    for index in range(0, len(s), n):
        lenght_list.append(mod_s[index:index+n])
    return lenght_list

#Binary Search - Your code took 2 milliseconds — faster than 59.98% in Python

def chuncky_strings(s, n):
    mod_s = s
    lenght_list = []
    while len(mod_s) > 0:
        if mod_s[:n] != '':
            lenght_list.append(mod_s[:n])
            mod_s = mod_s[n:]
    return lenght_list




        
