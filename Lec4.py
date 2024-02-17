from math import perm, comb, factorial
n = 20
r = 12
print(perm(n,r))
print(comb(n,r))
perm(n,r)==factorial(n)/factorial(n-r)
comb(n,r) == factorial(n)/(factorial(r)*factorial(n-r))

from math import *

print(sqrt(5))
#sqrt(-1) # math domain error

import cmath
dir(cmath)
print(cmath.sqrt(-1))
z = 4+3j
print(cmath.sqrt(z))

print(abs(z))

Output:
60339831552000
125970
2.23606797749979
1j
(2.1213203435596424+0.7071067811865476j)
5.0
