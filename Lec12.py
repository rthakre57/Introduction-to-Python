# Loops in Python

# For loop

# Printing the amount received on an investement under compound interest every year for 10 year.

principal = 20000
rate = 5.0
for years in range(1,11):
	amount = principal*(1+rate/100)**years
	print(f'Amounnt after {years}yr. is Rs.{amount:.4f}')


# Suppose we want to print the amount received on an investement under compound interest until the returned is doubled.

# Use of Break
for years in range(1,20):
	amount = principal*(1+rate/100)**years
	print(f'Amounnt after {years} yrs. is Rs.{amount:.4f}')
	if(amount>=2*principal):
		break


# Generate a random list of 20 integers one by one between 1 and 100 and find their sum.
import random
s = 0
x = []
for i in range(20):
	a = random.randint(1,100)
	x.append(a)
	s = s+a
print(x)
print(s)

# Genererate a random number between 0 and 1. If the number generated is >= 0.5, then assign it to ‘head’ else assign it to ‘tail’. Do this experiment 500 times and count number of heads and tail.
import random
Tosses = 500
heads = 0
tails = 0
for k in range(Tosses):
	coin = random.random()
	if(coin>=0.5):
		heads = heads+1
	else:
		tails = tails+1
print(heads, tails)

# Find the sum of integers between 1 and 100 (both inclusive) which are divisible 2 or divisible by 3 or divisible by 5. Also count how many such integers are there.
s = 0
count = 0
for n in range(1,101):
	if(n%2==0 or n%3==0 or n%5==0):
		count = count + 1
		s = s+n
print(count, s)

# Use of continue
# How many integers are there between 1 and 100 (both inclusive) which are not divisible by 2, 3 and 5? Also print these numbers.

count = 0
for n in range(1,101):
	if(n%2==0 or n%3==0 or n%5==0):
		continue
	count = count+1
	print(n, end=" ")

# List comprehensions for compact creation of lists
L = [n for n in range(1,101) if(n%2==0 or n%3==0 or n%5==0)]
print(len(L))
print(sum(L))

from math import gcd
N = 100
print(len([k for k in range(1,N+1) if gcd(N,k)==1]))

# Nested for loop
#Two integers are coprime if their gcd is 1. Euler phi function of a postive integer n is the number of integers less than n which are coprime n. It is denoted by φ(n). For each n from 1 to 20, print φ(n).
from math import gcd
N= 20
for k in range(1,N+1):
	count = 0
	for i in range(1,k+1):
		if (gcd(i,k)==1):
			count = count +1
	print(f'{k:2.0f} : {count}')

# Write an user defined function to check if a psoitive integer n is prime.
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

print(isPrime(-2))
print(isPrime(1))
print(isPrime(144))
print(isPrime(4989277))

#Write a Python programme to find the number of primes between 2 and n.
def PrimePi(n):
	Primes = [p for p in range(2,n+1) if isPrime(p)]
	return len(Primes)

print(PrimePi(200))

Output:
Amounnt after 1yr. is Rs.21000.0000
Amounnt after 2yr. is Rs.22050.0000
Amounnt after 3yr. is Rs.23152.5000
Amounnt after 4yr. is Rs.24310.1250
Amounnt after 5yr. is Rs.25525.6313
Amounnt after 6yr. is Rs.26801.9128
Amounnt after 7yr. is Rs.28142.0085
Amounnt after 8yr. is Rs.29549.1089
Amounnt after 9yr. is Rs.31026.5643
Amounnt after 10yr. is Rs.32577.8925
Amounnt after 1 yrs. is Rs.21000.0000
Amounnt after 2 yrs. is Rs.22050.0000
Amounnt after 3 yrs. is Rs.23152.5000
Amounnt after 4 yrs. is Rs.24310.1250
Amounnt after 5 yrs. is Rs.25525.6313
Amounnt after 6 yrs. is Rs.26801.9128
Amounnt after 7 yrs. is Rs.28142.0085
Amounnt after 8 yrs. is Rs.29549.1089
Amounnt after 9 yrs. is Rs.31026.5643
Amounnt after 10 yrs. is Rs.32577.8925
Amounnt after 11 yrs. is Rs.34206.7872
Amounnt after 12 yrs. is Rs.35917.1265
Amounnt after 13 yrs. is Rs.37712.9828
Amounnt after 14 yrs. is Rs.39598.6320
Amounnt after 15 yrs. is Rs.41578.5636
[88, 81, 27, 40, 61, 20, 57, 42, 23, 93, 3, 36, 58, 86, 26, 36, 50, 29, 92, 7]
955
266 234
74 3782
1 7 11 13 17 19 23 29 31 37 41 43 47 49 53 59 61 67 71 73 77 79 83 89 91 97 74
3782
40
 1 : 1
 2 : 1
 3 : 2
 4 : 2
 5 : 4
 6 : 2
 7 : 6
 8 : 4
 9 : 6
10 : 4
11 : 10
12 : 4
13 : 12
14 : 6
15 : 8
16 : 8
17 : 16
18 : 6
19 : 18
20 : 8
False
False
False
True
46
