#python program to solve quadratic equation

#Quadratic equation is ax^2 +bx +c =0
#use complex math module

import cmath
a= int(input('Enter value of a:'))
b= int(input('Enter value of b:'))
c= int(input('Enter value of c:'))
print('Given Quadratic equation is ;')
print('{0}x**2+{1}x +{2}=0'.format(a,b,c))

#calculating discriminat
d =(b**2)-(4*a*c)

#finding solutions of quadratic equation
solution1 =(-b -cmath.sqrt(d))/(2*a)
solution2 =(-b +cmath.sqrt(d))/(2*a)

#printing two solutions
print('solution are{0} and {1}'. format(solution1,solution2))
