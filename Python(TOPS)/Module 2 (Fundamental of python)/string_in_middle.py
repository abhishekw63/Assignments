star='\u2605'
separator='\u25ac'
bullet_point='\u25cf'
arrow='\u2794'

question=f'''{star} Write a Python function to insert a string in the middle of a string.'''

center_aligned=question.center(30)
print(center_aligned)

print(f'{separator} ' * 33)

def insertion(s1,m1):
    insert_index=len(s1)//2

    s2=s1[0:insert_index]+ m1 + s1[insert_index::]
    #s2=s1[0:insert_index]+ m1 + s1[insert_index+len(m1)::] #this will skip secon step by length of m1
    return s2

input_string=input(f'{bullet_point} Enter the sentence:')
sub_string=input(f'{bullet_point} Enter the substring:')

result=insertion(input_string,sub_string)

print(f'{arrow} Final string is "{result}."')