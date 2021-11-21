'''
You are given a string s containing "1", "2", "3" and "?". 
Given that you can replace any “?” with "1", "2" or "3" return the smallest number you can make as a string such that no two adjacent digits are the same.
'''

# Binary Search - Your code took 227 milliseconds — faster than 10.14% in Python

def smallest_number_with_no_adjacent_duplicates(s):
    n_string = ''
    el_list = []
    if len(s) == 1 and s[0] == "?":
        return "1"
    for element in s:
        if element != "?":
            el_list.append(int(element))
        else:
            el_list.append("?")
    for index, element in enumerate(el_list):
        if element == "?":
            el_list[index] = 1
            if index != 0 and index != len(el_list)-1:
                if el_list[index-1] == el_list[index] or el_list[index] == el_list[index+1]:
                    el_list[index] += 1
                if el_list[index-1] == el_list[index] or el_list[index] == el_list[index+1]:
                    el_list[index] += 1
            if index == 0 and el_list[index+1] == 1:
                el_list[index] += 1
            if index == len(el_list)-1 and el_list[index-1] == 1:
                el_list[index] += 1
        n_string += str(el_list[index])
    return n_string