import re

nameage = """
Saurabh is 28 and Gaurav is 24 
Purnima is 26 and Priyanka is 35
"""

# fetch ages
age = re.findall(r'\d{1,2}', nameage)
# print(age)
# ['28', '24', '26', '35']

# fetch names
names = re.findall(r'[A-Z][a-z]*', nameage)
# print(names)
# ['Saurabh', 'Gaurav', 'Purnima', 'Priyanka']

res_dict = {name: age for name, age in zip(names, age)}
# print(res_dict)
# {'Saurabh': '28', 'Gaurav': '24', 'Purnima': '26', 'Priyanka': '35'}

# -------------------------------------------------------------------------------------------------------------------

# find a word in a string
""" WAP to find a word 'Python' in a string """
string = "Regular Expression tool is used in almost all the programming or scripting languages such as Python, Java, C++, Java PHP, etc"

# if re.search("Python", string):
# print("Python is present!")

# Python is present!

# re.findall() => returns list of matches
all_inform = re.findall("inform", "we need to inform him with the latest information")
# print(all_inform)
# ['inform', 'inform']

# for i in all_inform:
# print(i)
# inform
# inform


# -------------------------------------------------------------------------------------------------------------------
# Generate an iterator
# Get the starting & ending index of a particular string
string1 = "we need to inform him with the latest information"

# for i in re.finditer("inform", string1):
#     res = i.span()
#     print(res)

# (11, 17)
# (38, 44)

# -------------------------------------------------------------------------------------------------------------------
# Match word with a particular pattern
str1 = "Sat, hat, mat, pat"

# pattern = ends with 'at'
res = re.findall("[Shmp]at", str1)  # [Shmp] => matching the word starts form S, h, m, p
# print(res)
# ['Sat', 'hat', 'mat', 'pat']

# for i in res:
#     print(i)

# Sat
# hat
# mat
# pat


# -------------------------------------------------------------------------------------------------------------------
# Match series of range of characters
# I want fetch all the words in which the first letter is between the range h-m and ending with 'at'
str1 = "Sat, hat, mat, pat"

res = re.findall('[h-m]at', str1)
# print(res)
# ['hat', 'mat']

# for i in res:
#     print(i)

# hat
# mat

# using carrot symbol
# ^ => everything apart from specified range
res = re.findall('[^h-m]at', str1)  # apart from h-m print everything
# print(res)
# ['Sat', 'pat']
# -------------------------------------------------------------------------------------------------------------------
# Replace a particular string =>
str1 = "Sat, hat, rat, mat, pat"
# replace rat from Cat

result = re.compile("[r]at")
res = result.sub("Cat", str1)

# print(res)
# Sat, hat, Cat, mat, pat

str1 = result.sub("Tat", str1)
# print(str1)
# Sat, hat, Tat, mat, pat

# -------------------------------------------------------------------------------------------------------------------
# randstr = "here is \\droga"
# print(randstr)
# here is \droga => we get single \ instead of \\

# print(re.search(r'\\droga', randstr))
# <re.Match object; span=(8, 14), match='\\droga'>

# -------------------------------------------------------------------------------------------------------------------
rans = """keep the blue flag 
flying high
chelsea"""
# print(rans)
# keep the blue flag
# flying high
# chelsea

# we want to remove new line with the space
c = re.compile('\n')
rands = c.sub(' ', rans)
# print(rands)
# keep the blue flag  flying high chelsea

# -------------------------------------------------------------------------------------------------------------------
# Match a single character
s = "98765"
# I want to print only 5th digit
# print("Matches: ", len(re.findall("\d{5}", s)))
# Matches:  1

# print("Matches: ", len(re.findall('\D{5}', s)))
# Matches:  0


str2 = "12345098765125905"
# print("Matches: ", len(re.findall('\d{5}', str2)))
# Matches:  3

# print("Matches: ", len(re.findall('\D{5}', str2)))
# Matches:  0

# -------------------------------------------------------------------------------------------------------------------
num = "123 1234 12345 123456 1234567"

# print("Matches: ", len(re.findall("\d{5,7}", num)))
# Matches:  3
# -------------------------------------------------------------------------------------------------------------------
# To verify the phone number

pho_num = """123-456-7890"""

# All phone numbers should have
# 1. 3 starting digits and '-' sign
# 2. 3 middle digits and '-'
# 3. 4 digits at the end

# if re.search('\d{3}-\d{3}-\d{4}', pho_num):
#     print("It is a valid phone number")
# It is a valid phone number

# if re.search('\w{3}-\w{3}-\w{4}', pho_num):
#     print("It's a valid phone number")
# It's a valid phone number
# but the disadvantage of this is \w => [a-zA-Z0-9]
# e.g "123-45a-7890"  => the o/p in this case => It's a valid phone number

# -------------------------------------------------------------------------------------------------------------------
# check name is valid or not
# name = "Saurabh Singh"
# name2 = "B Dragon"
# name3 = """Gaurav
# Singh"""

# if re.search('\w{2,20}\s\w{2,20}', name):
#     print("It's a valid name")
# It's a valid name

# if re.search('\w{2,20}\s\w{2,20}', name2):
#     print("Valid")
# else:
#     print("Not valid")
# Not valid


# if re.search('\w{2,20}\s\w{2,20}', name3):
#     print("valid name")
# valid name
# -------------------------------------------------------------------------------------------------------------------
# to verify the E-mail addresses
# Email address should include -
# 1. 1-20 lowercase & uppercase letters, numbers, plus._%+-
# 2. An @ symbol
# 3. 2-20 lowercase & uppercase letters, numbers, plus.-
# 4. a period
# 5. 2-3 lowercase & uppercase letters

all_emails = "ss@sing.com s%s@gmail.com  @ss.com dc@.com s.singh@gmail.com s_singh@gmail.com  ss@.com"

# for i in re.findall('[\w._%+-]{1,20}@[\w.-]{2,20}.[a-zA-Z]{2,3}', all_emails):
#     print(i)
# ss@sing.com
# s%s@gmail.com
# s.singh@gmail.com
# s_singh@gmail.com

# print("Email Matches: ", len(re.findall('[\w._%+-]{1,20}@[\w.-]{2,20}.[A-Za-z]{2,3}', all_emails)))
# Email Matches:  4

# -------------------------------------------------------------------------------------------------------------------
# profile = """hello everyone! my name is Saurabh Singh and i'm 28 years old my email id is saurabhsingh@cogniquest.ai
# and my contact no is 8602825320 & pincode is 560100"""
# name = re.findall('[A-Z][a-z]*', profile)
# age = re.findall(r'\d+ years', profile)
# email= re.findall('[\w.+_%-]{2,20}@[\w.-]{2,20}.[A-Za-z]{2,3}', profile)
# Mobile = re.findall('\d{10,12}', profile)
# pincode = re.findall('\d{6}', profile)
# print(f'Employee details is: {name}, {age}, {email}, {Mobile}, {pincode}')



# -------------------------------------------------------------------------------------------------------------------
# email = 'saurabhsingh@yahoo.com'
# domain_ = email.split('@')[-1]
# domain = domain_.split('.')[0]
#
# if domain in "gmailhotmailrediffyahoo":
#     print("personal")

# -------------------------------------------------------------------------------------------------------------------
# Scrap all the phone numbers from a webpage using RE
import urllib.request
import re

url ="https://www.summet.com/dmsi/html/codesamples/addresses.html"

response = urllib.request.urlopen(url)
html = response.read()
htmlStr = html.decode()
pdata = re.findall('\(\d{3}\) \d{3}-\d{4}', htmlStr)
# for data in pdata:
#     print(data)


# -------------------------------------------------------------------------------------------------------------------
nameage = """
Saurabh is 28 and Gaurav is 24 
Purnima is 26 and Priyanka is 35
"""

# fetch ages
age = re.findall(r'\s\d{1,2}\s ', nameage)
# print(age)

# -------------------------------------------------------------------------------------------------------------------
dollars = "$799 Rs 63,601 $899,799,999 $899,799,999.99999 $89 Rs 71,561 79,920 $999 $1099 A$1399"

# print(re.findall("\$[^ ]+", dollars))

# -------------------------------------------------------------------------------------------------------------------
s = "hello everyone how are you how the things going on"
# + =>

# -------------------------------------------------------------------------------------------------------------------
string = 'Fruits 32, Animals 80, Cars 34'
# '\D+'
# print(re.findall('\d+', string))
# ['32', '80', '34']

# print(re.findall('\D+', string))
# ['Fruits ', ', Animals ', ', Cars ']

# -------------------------------------------------------------------------------------------------------------------
string = 'Zero:0 one:1 Two:2 Three:3 Four:4 Five:5 Six:6 Seven:7 eight:8 Nine:9 Ten:10 Twenty:20 Thirty:30 Forty:40 Fifty:50 Sixty:60 Seventy:70 Eighty:80 Ninety:90 Hundred:100'

# print(re.findall('\d+', string))
# ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100']

# print(re.findall('\D+', string))
# ['Zero:', ' one:', ' Two:', ' Three:', ' Four:', ' Five:', ' Six:', ' Seven:', ' eight:', ' Nine:', ' Ten:', ' Twenty:', ' Thirty:', ' Forty:', ' Fifty:', ' Sixty:', ' Seventy:', ' Eighty:', ' Ninety:', ' Hundred:']


print(re.split('\d+', string))  # #This statement splits the string on the basis of matching values between pattern and string.
# ['Zero:', ' one:', ' Two:', ' Three:', ' Four:', ' Five:', ' Six:', ' Seven:', ' eight:', ' Nine:', ' Ten:', ' Twenty:', ' Thirty:', ' Forty:', ' Fifty:', ' Sixty:', ' Seventy:', ' Eighty:', ' Ninety:', ' Hundred:', '']
# -------------------------------------------------------------------------------------------------------------------
string = 'a1 \nb2 \nc4'
pattern = '\d'  # This statement defines the regular expression for matching with the string.

# empty string
replace = 's'
new_string = re.sub(pattern, replace,
                    string)  # This statement replaces those matched characters with a string stored in a replace variable.
print(new_string)  # This statement displays the new string after the replacement of characters.

text = "Regular Expression is also referred as Regex."
regex = "\d"
res = re.search(regex, text)  # This statement searches the regular expression in a string.
if res:
    print("Regular expression found inside the string")
else:
    print("Regular expression not found inside the String")

# -------------------------------------------------------------------------------------------------------------------



# -------------------------------------------------------------------------------------------------------------------
