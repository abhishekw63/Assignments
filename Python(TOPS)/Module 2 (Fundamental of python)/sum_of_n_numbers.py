print('''\u2605 Write a python program to sum of the first n positive integers.''')

term=int(input('How many numbers of summation you want? '))
sum=0
for i in range(1,term+1):
    sum=sum+i

print(f'\u2192 summation of {term} number is {sum}')

print('\u2726\u2726\u2726  Using Formula \u2726\u2726\u2726') 

#t=a+(n-1)d
#s=n(n+1)/2

result_by_formula=(term * (term+1)) // 2 #use floor division
print('\u2192 result using formula is ',result_by_formula)