# 3-dimensional array

import numpy as np
m1 = np.arange(9).reshape(3,3)
m2 = np.arange(10,19).reshape(3,3)
m3 = np.arange(20,29).reshape(3,3)
M = np.array([m1,m2,m3])
print(M)

M[1]

M[1][:,1]

M[1][:,1][1]

M[1,1,1]

 #Python array requires less momery and is faster than python lists
import numpy as np
import sys
import time
n = 100000
L1 = range(n)
L2 = range(n)
M1 = np.arange(n)
M2 = np.arange(n)

sys.getsizeof(L1)
sys.getsizeof(L1)*n
M1.itemsize
M1.itemsize*n

initialTime = time.time()
L12 = [x*y for x,y in zip(L1,L2)]
print("Time taken by Python Lists to perform multiplication:",
((time.time() - initialTime))*1000,
"msec")

initialTime = time.time()
M12 = M1*M2
print("Time taken by numpy array to perform multiplication:",
((time.time() - initialTime)*1000),
"msec")

Output:

[[[ 0  1  2]
  [ 3  4  5]
  [ 6  7  8]]

 [[10 11 12]
  [13 14 15]
  [16 17 18]]

 [[20 21 22]
  [23 24 25]
  [26 27 28]]]
Time taken by Python Lists to perform multiplication: 14.95981216430664 msec
Time taken by numpy array to perform multiplication: 0.0 msec
