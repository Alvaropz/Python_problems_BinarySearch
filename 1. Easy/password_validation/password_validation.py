'''
Given a string password, return whether these conditions are met:

At least 8 characters and at most 20 characters.
Contains at least one digit
Contains at least one lower alphabetical character and one upper alphabetical character
Contains at least one character within a set of special characters: !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~
Does not contain any other character such as tabs or new lines.
'''

# Binary Search - Your code took 4 milliseconds — faster than 13.19% in Python

import string

def password_validation(password):
    if not (len(password) > 7 and len(password) < 21):
        return False
    lower = list(string.ascii_lowercase)
    upper = list(string.ascii_uppercase)
    digit = [str(number) for number in range(10)]
    special = list(r"!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~")
    special.append('"')
    lower_check = any(lower_char in password for lower_char in lower)
    upper_check = any(upper_char in password for upper_char in upper)
    digit_check = any(digit_char in password for digit_char in digit)
    special_check = any(special_char in password for special_char in special)
    if lower_check != True or upper_check != True or digit_check != True or special_check != True:
        return False
    for char in password:
        if char not in lower + upper + digit + special:
            return False
    return True