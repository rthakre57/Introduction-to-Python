# Working with Numpy arrays

import numpy as np
v = np.array([3,-2,4])
w = np.array([5,2.5,3.8])

print(v+w)

print(v*w) # Term by term multiplication

print(v.dot(w))

print(2*v-3*w)

from numpy import linalg as la

print(la.norm(v))

print(np.cross(v,w))

##fibonacci numbers using lambda function.
def fibonacci(count):
    fib_list = [0, 1]
 
    any(map(lambda _: fib_list.append(sum(fib_list[-2:])),
                                         range(2, count)))
 
    return fib_list[:count]
 
print(fibonacci(10))

def fibonacci(count):
	fib_list=[0,1]
	for i in range(2,count):
		fib_list.append(fib_list[i-2]+fib_list[i-1])
		
	return fib_list

print(fibonacci(10))

Output:
[8.  0.5 7.8]
[15.  -5.  15.2]
25.2
[ -9.  -11.5  -3.4]
5.385164807134504
[-17.6   8.6  17.5]
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

