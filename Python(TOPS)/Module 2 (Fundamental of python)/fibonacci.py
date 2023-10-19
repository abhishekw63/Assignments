#Write a Python program to get the Fibonacci series of given range.

number=int(input('upto how many terms you want? '))
a=0
b=1

for i in range (0,number):  
    print(a,end=' ')
    c=a+b
    a=b
    b=c
