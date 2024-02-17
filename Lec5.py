import math
import cmath
a, b, c = 3, 5, -7
x1 = (-b+cmath.sqrt(b**2-4*a*c))/(2*a)
x2 = (-b-cmath.sqrt(b**2-4*a*c))/(2*a)
print(f'The roots are {x1} and {x2}')

a = float(input('Enter the value of a:'))
b = float(input('Enter the value of b:'))
c = float(input('Enter the value of c:'))
x1 = (-b+cmath.sqrt(b**2-4*a*c))/(2*a)
x2 = (-b-cmath.sqrt(b**2-4*a*c))/(2*a)
print(f'The roots are {x1} and {x2}')

a = float(input('Enter a:'))
b = float(input('Enter b:'))
c = float(input('Enter c:'))
s = (a+b+c)/(2.0)
A = cmath.sqrt(s*(s-a)*(s-b)*(s-c))
print(f'The area is given by {A:.4}')
print(f'The area is given by {A:.4f}')

Output:
The roots are (0.9067177514850918+0j) and (-2.5733844181517584+0j)
Enter the value of a:2
Enter the value of b:3
Enter the value of c:4
The roots are (-0.75+1.1989578808281798j) and (-0.75-1.1989578808281798j)
Enter a:2
Enter b:3
Enter c:4
The area is given by (2.905+0j)
The area is given by 2.9047+0.0000j
