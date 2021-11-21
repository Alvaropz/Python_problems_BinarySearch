'''
Given a string s, return whether it's an IPv4 address.

IPv4 addresses must follow the format A.B.C.D, where A, B, C, and D are numbers between 0 and 255. Zero-prefixed numbers, such as 01 and 065, are not allowed, except for 0 itself.
'''

# Binary Search - Your code took 1 millisecond — faster than 100.00% in Python.

def ip_address(s):
    ip_list = s.split(".")
    if len(ip_list) != 4:
        return False
    for element in ip_list:
        if not element.isdigit():
            return False
        if "0" in element and len(element) > 1:
            return False
        if not (0 <= int(element) <= 255):
            return False
    return True