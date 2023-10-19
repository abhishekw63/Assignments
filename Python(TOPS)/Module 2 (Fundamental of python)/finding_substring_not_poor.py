star='\u2605'
separator='\u25ac'
bullet_point='\u25cf'
arrow='\u2794'

question=f'''{star} Write a Python program to find the first appearance of the substring
 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the
 whole 'not'...'poor' substring with 'good'. Return the resulting string'''

centered_text=question.center(30)

print(centered_text)
print(f'{separator} ' * 33)

def finding_substring(input_string):
    input_string=input_string.lower()
    condition1=input_string.find('not')
    condition2=input_string.find('poor')

    if condition1!=-1 and condition2!=-1 and condition2>condition1:
        s1=input_string[0:condition1]+' '+'good' + input_string[condition2+4::]
        return s1
    else:
        return input_string


input_string=input(f'{bullet_point} Enter the sentence:')

result=finding_substring(input_string)

print(f'{arrow} Final string is:{result}')
