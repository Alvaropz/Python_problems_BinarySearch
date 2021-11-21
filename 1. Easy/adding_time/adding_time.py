'''
Given a string representing as 12-hour clock time with am/pm, and an integer n , add n minutes to the time and return the new time in the same format.

s = "5:30pm"
n = 90
outcome = "07:00pm"
'''

# Binar Search - Your code took 14 milliseconds — faster than 12.44% in Python.

def adding_time(s, n):
    hours = n // 60
    minutes = n % 60
    numbers = s.split(":")
    numbers[1] = numbers[1][:2]
    numbers = list(map(int, numbers))
    if "pm" in s and numbers[0] != 12: 
        numbers[0] += 12
    numbers[0] += hours
    numbers[1] += minutes
    if numbers[1] >= 60:
        numbers[1] -= 60
        numbers[0] += 1
    if (numbers[0] < 12 and not "pm" in s) or numbers[0] == 24 and int(s[:s.index(":")]) != 12:
        if numbers[0] == 24:
            numbers[0] = 12
        numbers[0] = str(numbers[0]).zfill(2)
        numbers[1] = str(numbers[1]).zfill(2) + "am"
        return numbers[0] + ":" + numbers[1]
    elif numbers[0] >= 12 and numbers[0] < 24 and "pm" in s:
        if numbers[0] > 12:
            numbers[0] = str(numbers[0]-12).zfill(2)
        else:
            numbers[0] = str(numbers[0])
        numbers[1] = str(numbers[1]).zfill(2) + "pm"
        return numbers[0] + ":" + numbers[1]
    if numbers[0] > 12 and numbers[0] < 24 and int(s[:s.index(":")]) != 12:
        print("first")
        return str(numbers[0]-12).zfill(2) + ":" + str(numbers[1]).zfill(2) + "pm"
    elif numbers[0] < 12 and int(s[:s.index(":")]) != 12:
        print("second")
        return str(numbers[0]).zfill(2) + ":" + str(numbers[1]).zfill(2) + "am"
    if numbers[0] > 24:
        count_days = 0
        while numbers[0] > 24:
            numbers[0] -= 24
            count_days += 1
        numbers.append(count_days)
    if numbers[0] > 12 and numbers[0] < 24 and int(s[:s.index(":")]) != 12:
        return str(numbers[0]-12).zfill(2) + ":" + str(numbers[1]).zfill(2) + "pm"
    elif numbers[0] < 12 and int(s[:s.index(":")]) != 12:
        return str(numbers[0]).zfill(2) + ":" + str(numbers[1]).zfill(2) + "am"
    if numbers[0] == 12 and n < 60 and "pm" in s and not numbers[0] == 12 > int(s[:s.index(":")]):
        return "12:" + str(numbers[1]).zfill(2) + "pm"
    elif numbers[0] == 12 and n < 60 and "am" in s and not numbers[0] == 12 > int(s[:s.index(":")]):
        return  "12:" + str(numbers[1]).zfill(2) + "am"
    if len(numbers) != 3:
        if numbers[0] == 12 and "pm" in s:
            return "12:" + str(numbers[1]).zfill(2) + "am"
        elif numbers[0] == 12 and "am" in s:
            return "12:" + str(numbers[1]).zfill(2) + "pm"
    else:
        if numbers[0] == 12 and "pm" in s:
            return "12:" + str(numbers[1]).zfill(2) + "pm"
        elif numbers[0] == 12 and "am" in s:
            return "12:" + str(numbers[1]).zfill(2) + "am"
    if int(s[:s.index(":")]) == 12 and numbers[0] > 12 and numbers[0] != 24:
        return str(numbers[0]-12).zfill(2) + ":" + str(numbers[1]).zfill(2) + "am"
    elif int(s[:s.index(":")]) == 12 and numbers[0] > 12 and numbers[0] != 24:
        return str(numbers[0]-12).zfill(2)  + ":" + str(numbers[1]).zfill(2) + "pm"
    if int(s[:s.index(":")]) == 12 and numbers[0] == 24 and "am" in s:
        return "12:" + str(numbers[1]).zfill(2) + "pm"
    elif int(s[:s.index(":")]) == 12 and numbers[0] == 24 and "pm" in s:
        return "12:" + str(numbers[1]).zfill(2) + "am"