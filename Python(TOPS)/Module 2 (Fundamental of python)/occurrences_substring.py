print('''\u2605 Write a Python program to count occurrences of a substring in a string.''')

print('\u25ac '*35)

print('\u2714 Method 1:Using counter.')

def count_substring(input_string,sub_string):
   start=0
   count=0
   while start< len(input_string):#abhishekabhi
        start=input_string.find(sub_string,start)
        if start==-1:
            break 
        else:
            count+=1
            start+=len(sub_string)
    
   return count 
input_string=input('\u25cf enter the sentence:')
sub_string=input('\u25cf enter the substring:')
occurrences=count_substring(input_string,sub_string)
print(f"\u2794 Occurrences of substring '{sub_string}' is {occurrences:^5} times.")
print('  ')

print('\u2714 Method 2:re.findall method')
import re
def count_occurrence1(input_string,sub_string):
    occurrences1=re.findall(sub_string,input_string)
    #print(occurrences1)
    return len(occurrences1)
occurrences1=count_occurrence1(input_string,sub_string)
print(f"\u2794 Occurrences of substring '{sub_string}' is {occurrences1:^5} times.")
print('  ')

print('\u2714 Method 3:Using starswith')
def count_occurrances2(input_string,_sub_string):
    start=0
    count=0

    while start<len(input_string):
        if input_string.startswith(sub_string,start):
            count+=1
            start+=len(sub_string)
        else:
            start+=1
    return count
occurrences2=count_occurrances2(input_string,sub_string)
print(f"\u2794 Occurrences of substring '{sub_string}' is {occurrences2:^5} times.")
print('  ')

print('\u2714 Method 4:Using list comprehension')
def count_occurrences4(input_string,sub_string):
    
    count=sum(1 for i in range(0, len(input_string)-len(sub_string)+1 ) if input_string[i:i+len(sub_string)] == sub_string)
    return count
occurrences4=count_occurrences4(input_string,sub_string)
print(f"\u2794 Occurrences of substring '{sub_string}' is {occurrences4:^5} times.")