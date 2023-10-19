print('''\u2605 Write a Python program to test whether a passed letter is a vowel or not.''')

character=input('enter the character:')

if character=='a' or character=='A':
    print('it is vowel')
elif character=='e' or character=='E':
    print('it is vowel')
elif character=='i' or character=='I':
    print('it is vowel')
elif character=='o' or character=='O':
    print('it is vowel')
elif character=='u' or character=='U':
    print('it is vowel')
else:
    print('it is consonant')

print('----Using in operator----')
if character.lower() in {'a','e','i','o','u'}:
    print ('it is vowel')
else:
    print('it is consonent')