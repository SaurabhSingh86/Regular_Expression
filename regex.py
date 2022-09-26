import re

nameage = """
Saurabh is 28 and Gaurav is 24 
Purnima is 26 and Priyanka is 35
"""

# fetch the ages
age = re.findall(r'\d{1,3}', nameage)
print(age)
# ['28', '24', '26', '35']

