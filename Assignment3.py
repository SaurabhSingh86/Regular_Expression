""" WAP to fetch all the dates"""
# formats are :
"""	
DD-MM-YY
MM/DD/YY
DD/MM/YY
YY/MM/DD
Month D, Yr (February 17, 2009)
M/D/YY (2/17/2009)
D/M/YY (17/2/2009)
"""

import re

path = r'C:\Users\User\PycharmProjects\regex\date_format'


with open(path) as file:
    for line in file:
        if re.findall('\d{2}-\d{2}-\d{4}', line):
            print(re.findall('\d{2}-\d{2}-\d{4}', line))
        elif re.findall('\d{1,2}/\d{1,2}/\d{4}', line):
            print(re.findall('\d{1,2}/\d{1,2}/\d{4}', line))
        elif re.findall('\d{4}/\d{1,2}/\d{1,2}', line):
            print(re.findall('\d{4}/\d{1,2}/\d{1,2}', line))
        elif re.findall('[\w]\s\d{1,2},\s\d{4}', line):
            print(re.findall('\w{3,10}\s\d{1,2},\s\d{4}', line))

