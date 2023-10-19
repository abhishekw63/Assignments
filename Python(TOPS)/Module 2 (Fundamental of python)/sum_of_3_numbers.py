print('''\u2605Write a Python program to sum of three given integers. 
      However, if two values are equal sum will be zero.''')

num1=int(input('enter the number1:'))
num2=int(input('enter the number2:'))
num3=int(input('enter the number3:'))

if num1==num2 or num1==num3 or num2==num3:  
    print('Condition matched! Result is 0')
else:
    result=num1+num2+num3
    print(result)

#pythonic approach: if num1==num2==num3