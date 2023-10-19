print('''\u2605 Write a Python program to count the occurrences of each word in a
  given sentence.''')

print("\u25ac "* 35)

def count_occurrences(input_sentence):
    words=input_sentence.split() #splitting sentence into words
   # print(words)

    words_count={} # creating a empty dictionary to store the words

    for word in words: #iterating through the words and count thier occurrences 
        
        word=word.strip('. ,!') # removing punctuation
        #can be ignored: strip method
        word=word.lower() #convert to lower case for uniformity

        if word not in words_count:
            words_count[word]=1
        else:
            words_count[word]+=1
    
    
    return words_count

input_sentence=input("\u25cf Enter the sentence:")

word_occurrence=count_occurrences(input_sentence) 

for word,count in word_occurrence.items():
    print(f'''\u2794 Word is '{word}' with {count} frequency''')

'''
using while loop
input_sentence = input('Enter the sentence:')

words = input_sentence.split()
words = [word.lower() for word in words]

word_dict = {}

n = 0
while n < len(words):
    word = words[n]
    
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1

    n += 1

for word, count in word_dict.items():
    print(f'Word -> {word} -> {count}')
'''
