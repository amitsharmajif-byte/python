#1. 
find the min of three numbers 
number= 5,6,7
a=int(input('enter the first number'))
b=int(input('enter the second number'))
c=int(input('enter the third number'))
if a<b and a<c:
    print('smallest is a')
elif b<c:
    print('smallest is b')
else:
    print('smallest is c ')
