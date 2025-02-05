'''This is a function that takes a input password and validates whether 
it meets the following conditions, a minimum of 8 characters, Upper and
lower case letters. A number. What is the best way to do this I decide 
Regular expressions because with procedural program it will be tedious'''

import re #regular expression module

sample_password = ''
regex_minimum_char = r'\w{8,}'
regex_upper_lower = r'[a-zA-Z]+'
regex_number = r'[\d]+'

def validate(sample):
    if re.findall(regex_minimum_char,sample)==None:
        return 'The password must be 8 characters or more.'
    if re.findall(regex_number,sample)==None:
        return 'Password must atleast have a number.'
    if re.findall(regex_upper_lower, sample)==None:
        return 'Password must include upper and lower case letters.'
    return 'Good password'

sample ='prinokfdsfsd'

print(validate(sample))