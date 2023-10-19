star = '\u2605'
separator = '\u25ac'
bullet_point = '\u25cf'
arrow = '\u2794'

question= f'''{star} Write a Python program to add 'ing' at the end of a given string (length
  should be at least 3). If the given string already ends with 'ing' then add
  'ly' instead. If the string length of the given string is less than 3, leave it
  unchanged. '''

# Center-align the text
centered_text = question.center(65) #console_width=65

# Print the centered text
print(centered_text)

print(f'{separator} '*33)

def adding_function(string1):
    if len(string1)>=3:
        
        if string1[-3::]=='ing': #[-3:len(string1):1]
          s1=string1[0:-3:1]+'ily' #for replacing s1=string1[0:-3:1]
          return s1
        
        else:
           s1=string1+'ing'
           return s1
           
    else:
       return string1    



input_string=input(f'{bullet_point} Enter the sentence:')

result=adding_function(input_string)

print(f'{arrow} Final string is:{result}')
