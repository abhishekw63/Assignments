star='\u2605'
separator='\u25ac'
bullet_point='\u25cf'
arrow='\u2794'

question=f'''{star} Write a Python function that takes a list of words and returns the length
  of the longest one.'''

centered_align=question.center(30)
print(centered_align)

print(f'{separator} ' * 30)

def longest_word(words):
    max=words[0]
    for word in words:
        if(len(max)<len(word)):
            max=word
        else:
            pass
    
    return max

'''
#pyhtonic approach

def longest_word(words):
    if not words:
        return 0:
    
    longest_word_length=max(words,key=len)
    return  len(longest_word_length)

'''

input_words=input('enter the words separated by comma:')
words=input_words.split(',') #string.split(separator, maxsplit)

#words = [word for word in user_input.split() if word!=' '] #list comprehension

result=longest_word(words)

print(f'{arrow} Longest word is {result} with {len(result)}.')

'''for word in words:
    print(f'word:{word} with length of {len(word)}.') '''

