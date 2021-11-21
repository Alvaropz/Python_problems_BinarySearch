'''
Given a string numeral representing a Roman numeral, convert it to an integer.

A Roman numeral is represented by writing its symbols from left to right from greatest to least, with the only exception being when when representing one less than a symbol.

For example, the Roman numerals from 1 to 12 are: I, II, III, IV, V, VI, VII, VIII, IX, X, XI, XII

The values of Roman numerals are as follows:

{
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}
'''

# Binary Search - Your code took 1 millisecond — faster than 100.00% in Python.

def CCCXXVV(numeral):
    numbers = 0
    dict_roman_numbers = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    index = 0
    while index < len(numeral):
        if index+1 < len(numeral):
            checker = numeral[index] + numeral[index+1]
            if checker == "IV":
                numbers += 4
                index += 1
            elif checker == "IX":
                numbers += 9
                index += 1
            elif checker == "XL":
                numbers += 40
                index += 1
            elif checker == "XC":
                numbers += 90
                index += 1
            elif checker == "CD":
                numbers += 400
                index += 1
            elif checker == "CM":
                numbers += 900
                index += 1
            elif index < len(numeral) and numeral[index] in dict_roman_numbers:
                numbers += dict_roman_numbers[numeral[index]]
        elif numeral[-1] == "I":
            numbers += 1
        elif numeral[-1] == "X":
            numbers += 10
        elif numeral[-1] == "C":
            numbers += 100
        index += 1
    return numbers