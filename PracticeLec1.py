#1. Write Python codes to input radius of a sphere and print its surface area and volume.
from math import pi
r = float(input("Enter the radius of the sphere: "))
Area = 4*pi*r**2
Volume = (4/3)*pi*r**3
print(f'The Surface area of a sphere with radius {r} is {Area:.4f} sq.units.')
print(f'The volume of a sphere with radius {r} is {Area:.4f} cubic units.')

#Input a positive integer n and integer k<=n. Verify the following properties:
from math import comb
n = int(input('Enter an integer greater than 1: '))
k = int(input('Enter an integer lesser than or equal to n: '))
#i.
comb(n,k) == comb(n,n-k)
print(comb(n,k))
#ii.
k*comb(n,k) == n*comb(n-1,k-1)

#iii.
comb(n,k-1) + comb(n,k) == comb(n+1,k)

#3. Input a complex number z and explore some of its properties.
from cmath import *

z = 3 + 5j # Equivalently it can be defined as complex(3,5)
print(z)

a=z.conjugate()
print(a)

b=z.real
print(b)

c=z.imag
print(c)

cos(z)
print(cos(z))

d=e**z
print(d)

e=sqrt(z)
print(e)

f=abs(z)
print(f)


g=phase(z) # Reurns the argument of z
print(g)

import math
print(math.atan2(z.imag, z.real)) # This is equivalent to phase(z) 

Output:
Enter the radius of the sphere: 3
The Surface area of a sphere with radius 3.0 is 113.0973 sq.units.
The volume of a sphere with radius 3.0 is 113.0973 cubic units.
Enter an integer greater than 1: 6
Enter an integer lesser than or equal to n: 4
15
(3+5j)
(3-5j)
3.0
5.0
(-73.46729221264526-10.471557674805572j)
(5.697507299833738-19.260508925287418j)
(2.101303392521568+1.189737764140758j)
5.830951894845301
1.0303768265243125
1.0303768265243125
