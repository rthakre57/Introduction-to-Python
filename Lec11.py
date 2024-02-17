# Branching (making decisions)

# Suppose marks obtained is greater than or equals to 75 then print Distinction, otherwise print No disctinction

mark = 70
if(mark>=75):
	print('Distinction')
else:
	print('No distinction')


# Suppose marks obtained is greater than or equals to 75 then print Distinction, if the marks obtained is greater than or equals to 60 then print First Division otherwise print Completed.
mark = 60
if(mark>=75):
	print('Distinction')
else:
	if(mark>=60):
		print('First Division')
	else:
		print('Completed')

# Combining if and else to elif

mark = 55
if(mark>=75):
	print('Distinction')
elif(mark>=60):
		print('First Division')
else:
	print('Completed')

# Input three positive real numbers and check if they can be sides of a triangle.

a, b, c = 4, 6, 6
if(a+b>c and a+c>b and b+c>a):
	print('a, b, c are sides of a triangle')
else:
	print('a, b, c are not sides of a functionstriangle')


# a, b, c are sides of a triangle
def is_triangle(a,b,c):
	if(a+b>c and a+c>b and b+c>a):
		return True
	else:
		return False

print(is_triangle(10,10,25))


a, b, c = 5, 6, 7
if(a+b>c and a+c>b and b+c>a):
	if(a==b and b==c):
		print('Equilateral triangle')
	elif(a==b or b==c or a==c):
			print('Isoceles triangle')
	else:
		print('Scalene triangle')
else:
	print('Not a triangle')



def Triangle(a,b,c):
	if(a+b>c and a+c>b and b+c>a):
		if(a==b and b==c):
			print('Equilateral triangle')
		elif(a==b or b==c or a==c):
				print('Isoceles triangle')
		else:
			print('Scalene triangle')
	else:
		print('Not a triangle')

Triangle(3,4,4)


# Roots of a quadratic covering all cases

from math import sqrt
from cmath import sqrt as csqrt
def solve_quad(a,b,c):
	if(a==0):
		if(b!=0):
			x1 = -c/b
			print(f"It has only one root, x1={x1}")
		else:
			print('It has no root')
	else:
		d = b**2-4*a*c
		if(d>=0):
			print('Roots are real')
			x1 = (-b+sqrt(b**2-4*a*c))/(2*a)
			x2 = (-b-sqrt(b**2-4*a*c))/(2*a)
			print(f'The roots are {x1} and {x2}')
		else:
			print('Roots are imaginary')
			x1 = (-b+csqrt(b**2-4*a*c))/(2*a)
			x2 = (-b-csqrt(b**2-4*a*c))/(2*a)
			print(f'The roots of are {x1} and {x2}')

solve_quad(-1,3,5)

Output:
No distinction
First Division
Completed
a, b, c are sides of a triangle
False
Scalene triangle
Isoceles triangle
Roots are real
The roots are -1.1925824035672519 and 4.192582403567252
