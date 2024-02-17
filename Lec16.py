# Use of break and continue with while loop
# Example: Write a python code to find the sum of positive integers starting with 1 which are not divisible by 2 and 3. Stop when the sum exceeds 1000.
i = 0
s = 0
while True:
	i=i+1
	if(i% 2 ==0 or i%3 == 0):
		continue
	s = s+i
	if(s>1000):
		break
print(i,s)

# Use of else with loops

def isPrime(n):
	if n < 2:
		return False
	if n == 2:
		return True
	if n % 2 ==0:
		return False
	for k in range(3, int(n**0.5)+1,2):
		if n % k ==0:
			return False
	return True

a, b = 200, 211
for k in range(a, b+1):
	if isPrime(k):
		print(f'{k} is a prime')
		break
else:
	print(f'There is no prime between {a} and {b}')

# Example: Find two integers m and n with n − m = 100 such that there is no prime between m and n.
N = 10**6
for i in range(2, N):
	for k in range(i, i+101):
		if isPrime(k):
			break
	else:
		print(f'There is no prime between {i} and {i+100}')
		break
else:
	print('Choose a larger range')

# Use of else with while loop.
# Example: Toss a sixed faced dice six times. If you get 6 you win otherwise you loose.
from random import sample
i = 1
while(i<=6):
	face = sample(range(1,7),1)[0]
	if(face==6):
		print('You win')
		break
	i+=1
else:
	print('You lose')


# Finding a root using the Newton-Raphson method
# Example: Find a root of a x2 − 3x + e−2x = 0 using the Newton-Raphsom scheme. Use while loop to terminate the iteration scheme when no of iteration exceeds 20
def Newton_raphson(f, df, x0, max_it=20,tol=1e-5):
	f0 = f(x0)
	itr = 0
	while(abs(f(x0))>=tol and itr<=max_it):
		x1 = x0-f0/df(x0)
		x0 = x1
		f0 = f(x0)
		itr += 1
	converged = itr<max_it
	return x0, converged, itr

from math import exp
f = lambda x: x**2-3*x+exp(-2*x)
df = lambda x: 2*x-3-2*exp(-2*x)
sol, converged, itr = Newton_raphson(f,df, 100,tol=1e-5)
if converged:
	print(f'Newtons method converged in {itr} iterations')
	print(f'The soluntion is {sol}')
else:
	print(f'Newtons method did not converge')

Output:
77 1014
211 is a prime
There is no prime between 370262 and 370362
You win
Newtons method converged in 9 iterations
The soluntion is 2.9991726809491017
