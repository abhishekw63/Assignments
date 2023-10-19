star='\u2605'
separator='\u25ac'
bullet_point='\u25cf'
arrow='\u2794'

question=f'''Write a Python program to get a string made of the first 2 and the last
2 chars from a given a string. If the string length is less than 2, return the empty string.'''

center_aligned=question.center(30)

print(f'{separator} '* 33)

def first_2_last_2(s1):
    if len(s1)>=2:
        s1_a=s1[0:2:1]
        s1_b=s1[-2:len(s1):1]

        return s1_a+s1_b
    else:
        s2=''
        #print(len(s2))
        return s2
input_string=input(f'{bullet_point} Enter the sentence:')

result=first_2_last_2(input_string)

print(f'{arrow} final string is "{result}" ')