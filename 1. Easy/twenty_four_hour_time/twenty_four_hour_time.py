'''
Given a string s, representing a 12-hour clock time with am/pm, return its 24-hour equivalent.
'''

#Your code took 2 milliseconds — faster than 99.81% in Python

def solve(s):
    if "pm" in s:
        if s[:2] == "12":
            return "12" + s[2:5]
        new_pm = str(int(s[:2]) + 12) + s[2:5]
        return new_pm
    else:
        if s[:2] == "12":
            return "00" + s[2:5]
        return s[:-2]