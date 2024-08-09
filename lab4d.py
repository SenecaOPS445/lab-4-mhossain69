#!/usr/bin/env python3

def manipulate_string(s):
    return {
        'lower': s.lower(),
        'upper': s.upper(),
        'swapcase': s.swapcase(),
        'title': s.title(),
        'capitalize': s.capitalize()
    }

def first_five(s):
    return s[:5]

def last_seven(s):
    return s[-7:]

def middle_number(n):
    s = str(n)
    if '.' in s:
        integer_part, fractional_part = s.split('.')
        if fractional_part == '0':  # If the fractional part is zero, handle it as integer part
            return integer_part[len(integer_part) // 2]
        middle_index = len(fractional_part) // 2
        if len(fractional_part) % 2 == 0:
            return fractional_part[middle_index - 1:middle_index + 1]
        else:
            return fractional_part[middle_index]
    else:
        middle_index = len(s) // 2
        if len(s) % 2 == 0:
            return s[middle_index - 1:middle_index + 1]
        else:
            return s[middle_index]

def first_three_last_three(s1, s2):
    return s1[:3] + s2[-3:]

if __name__ == '__main__':
    course_name = 'Open System Automation'
    manipulations = manipulate_string(course_name)
    for key, value in manipulations.items():
        print(f'{key}: {value}')

    print('first_five:', first_five('Hello World!!'))
    print('last_seven:', last_seven('Hello World!!'))
    print('middle_number (1500):', middle_number(1500))
    print('middle_number (1.50):', middle_number(1.50))
    print('first_three_last_three:', first_three_last_three('Hello World!!', 'Seneca College'))