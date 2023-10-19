print('''\u2605 Write a Python program to calculate the length of a string.''')
str1=input('\u25cf enter the sentence:')
count=0
for x in str1: #shouldnt it stopped at str-1 ?
    count+=1
print('\u2192 Length of string is ',count)
print('\u2192 using len function: ',len(str1))