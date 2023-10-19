
print('''\u2605 Write a Python program to find whether a given number is even or odd,
    print out an appropriate message to the user.''')

num=int(input('enter the number:'))

if num==0:
    print('it is neutral number')
elif num%2==0:
    print('it is a even number')
else:
    print('it is odd number')