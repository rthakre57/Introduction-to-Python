# Functions and Branching

# Functions and Branching

principal = 20000
rate = 5.0
years = 5
amount = principal*(1+rate/100)**years
print(f'{amount:.4f}')

# Creating an user defined functions (subroutines)

def Compound_interest(principal, rate, years):
	amount = principal*(1+rate/100)**years
	return amount

amount = Compound_interest(20000,5.0, 5)
print(f'The amount Received is Rs.{amount:.4f}.')

# Case when the interest is calculated more than once in a year
def Compound_interest(principal, rate, years,n = 1):
	amount = principal*(1+rate/(n*100))**(n*years)
	return amount

amount = Compound_interest(20000,5.0, 5, n = 3)
print(f'The amount Received is Rs.{amount:.4f}.')

# User defined function for roots of a ax2 + bx + c = 0

from math import sqrt
a, b, c = 2, 3, -2
x1 = (-b+sqrt(b**2-4*a*c))/(2*a)
x2 = (-b-sqrt(b**2-4*a*c))/(2*a)
print(f'The roots of the quadratic are {x1} and {x2}')

def quad(a,b,c):
	x1 = (-b+sqrt(b**2-4*a*c))/(2*a)
	x2 = (-b-sqrt(b**2-4*a*c))/(2*a)
	return(x1,x2)

a, b, c = 2, 3, -2
x1,x2 = quad(a,b,c)
print(f'The roots of the quadratic are {x1} and {x2}')

# User defined function for Heron’s formula to find the area of triangle

from math import sqrt
def Heron(a,b,c):
	s = (a+b+c)/2.0
	A = sqrt(s*(s-a)*(s-b)*(s-c))
	return A

a, b, c = 3,7, 9
Area = Heron(a,b,c)
print(f'The area of the triangle is {Area:.4f}')

Output:

25525.6313
The amount Received is Rs.25525.6313.
The amount Received is Rs.25627.6489.
The roots of the quadratic are 0.5 and -2.0
The roots of the quadratic are 0.5 and -2.0
The area of the triangle is 8.7856
