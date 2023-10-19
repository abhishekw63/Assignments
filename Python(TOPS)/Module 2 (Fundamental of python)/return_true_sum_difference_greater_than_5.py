print('''\u2605 Write a Python program that will return true,
    if the two given integer values are equal or their sum or difference is 5''')

num1=int(input('Enter the number1:'))
num2=int(input('Enter the number2:'))

if num1==num2 or num1-num2==5 or num2-num1==5:
    print('True \u2714')
else:
    print('Condition is not matched \u274C')

#Pythonic approach:if num1==num2 or abs(num1-num2)