'''
Given a positive integer n representing the amount of cents you have, return the formatted currency amount. For example, given n = 123456, return "1,234.56".
'''

# Binary Search - Your code took 1 millisecond — faster than 100.00% in Python.

def penny_for_your_thoughts(n):
    str_n = str(n)
    str_n_len = len(str(n))
    if str_n_len == 1:
        return "0.0" + str_n
    elif str_n_len == 2:
        return "0." + str_n
    else:
        integer_str_n = str_n[:-2][::-1]
        decimal_str_n = "." + str_n[-2:]
        i = 0
        j = str_n_len - 1
        integers_list = []
        while i < j:
            if integer_str_n[i:i+3]:
                integers_list.append(integer_str_n[i:i+3][::-1])
            i += 3
        formated_string = ""
        for sub_list in list(reversed(integers_list)):
            formated_string += sub_list + ","
        if formated_string[-1] == ",":
            formated_string = formated_string[:-1]
        return formated_string + decimal_str_n
