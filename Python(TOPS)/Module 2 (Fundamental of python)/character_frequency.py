
print('''\u2605 Write a Python program to count the number of characters 
    (character frequency) in a string.''')
print('\u25ac ' * 25)

def character_frequency_count(input_string):
    char_frequency={}

    for char in input_string:
        if char!=' ':
            if char not in char_frequency:
                char_frequency[char]=1
            else:
                char_frequency[char]+=1
        else:
            pass
    
    return char_frequency



input_string=input('\u25cf enter the sentence:')
result=character_frequency_count(input_string)

for char,freq in result.items():
    print(f'\u2794 character {char} with {freq} frequency. ')

#2794 -arrow
#2605-star
#25ac- rectangle

print('\u25ac' * 30)
print('\u2605 using counter class.')

from collections import Counter
def using_counter_class(input_string):

    input_string=input_string.replace(' ','')
    character_frequency_using_counter=Counter(input_string)
    return character_frequency_using_counter    


result_using_counter=using_counter_class(input_string)
#print(result_using_counter)
#print(type(result_using_counter))

for char_c,freq_c in result_using_counter.items():
    print(f'\u2794 character {char_c} with frequency {freq_c}')







