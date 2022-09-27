""" Write a program to fetch $ value using regular expression"""

import re


path = r"C:\Users\User\PycharmProjects\regex\price.txt"

with open(path) as file:
    for line in file:
        if re.findall('\$[^ ]+', line):
            print(re.findall('\$[^ ]+', line))


    # for line in file:
    #     if re.findall('\s[$]\d+', line):
    #         print(re.findall('\s[$]\d+', line))
    #     if re.findall('\s[$]\d+,\d+.\d+', line) or re.findall('\s[$]\d+', line):
    #         print(re.findall('\s[$]\d+,\d+.\d+', line) or re.findall('\s[$]\d+', line))

        # res = re.findall('[A][$]\d+', line)      # if we want Australian dollar i.e. A$
        # res = re.findall('[$]\d+', line)         # if we want both US($) as well as Adollar(A$)
        # for item in out:
        #     print(item)

