print('''\u2605 Write a Python program to get a single string from two given strings,
  separated by a space and swap the first two characters of each string.''')

print('\u25ac ' * 35)

def combining_and_swapping(string1,string2):

    s1=string2[0:2]+string1[2:]
    s2=string1[0:2]+string2[2:]

    s3=s1+' '+s2
    return s3



string1=input("\u25cf enter the sentence 1:")
string2=input("\u25cf enter the sentence 2:")

result=combining_and_swapping(string1,string2)

print(f'\u2794 Swapping of first two characters and concatenating them:{result}')