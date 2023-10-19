# Write python program that swap two number with temp variable and without temp variable

print('\u2605 Write python program that swap two number with temp variable and without temp variable')

num1=int(input('enter the number1:'))
num2=int(input('enter the number2:'))

num1_without_3rd_variable=num1
num2_without_3rd_variable=num2

print(f'before swap-> NUMBER1 {num1} and NUMBER2 {num2}')

temp=num1
num1=num2
num2=temp

print(f'after swap using 3rd variable-> NUMBER1 {num1} and  NUMBER2 {num2}')

num1_without_3rd_variabl=num1_without_3rd_variable+num2_without_3rd_variable #a=a+b
num2_without_3rd_variable=num1_without_3rd_variable-num2_without_3rd_variable #b=a-b
num1_without_3rd_variable=num1_without_3rd_variable-num2_without_3rd_variable  #a=a-b

print(f'after swapping without 3rd variable-> NUMBER1 {num1} and  NUMBER2 {num2}')




