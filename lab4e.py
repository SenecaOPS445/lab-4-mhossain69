#!/usr/bin/env python3

def substring_operations(s):
    return s.split(' ')

def format_string(name, code, number):
    return f'{name} - {code} - {number}'

def is_digits(s):
    return s.isdigit()

if __name__ == '__main__':
    course_name = 'Open System Automation'
    course_code = 'OPS445'
    course_number = 445
    substrings = substring_operations(course_name)
    formatted_string = format_string(course_name, course_code, course_number)
    print('Substrings:', substrings)
    print('Formatted String:', formatted_string)
    print('is_digits (3058):', is_digits('3058'))
    print('is_digits (x3058):', is_digits('x3058'))
    print('is_digits (8503x):', is_digits('8503x'))
    print('is_digits (8503):', is_digits('8503'))
