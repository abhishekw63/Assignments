star='\u2605'
separator='\u25ac'
bullet_point='\u25cf'
arrow='\u2794'

question=f'''{star} Write a Python function to reverses a string if its length is a multiple of
  4.'''

centered_aligned=question.center(30)
print(centered_aligned)

print(f'{separator} ' * 33)

def reversed_string(s1):
    if len(s1)%4==0:
        return s1[::-1]
    else:
        return s1
input_string=input(f'{bullet_point} Enter the sentence:')

result=reversed_string(input_string)

print(f'{arrow} Final string is "{result}" with length {len(input_string)}')
