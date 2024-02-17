#Working with NumPy Module
#• NumPy is the fundamental package for scientific computing in Python. It is a Python library that provides a multidimensional array object.

#• NumPy arrays facilitate advanced mathematical and other types of operations on large numbers of data.

#• The ‘for’ loop is more appropriate for use in case the number of iterations is known in advance.

#• The ‘while’ loop is preferably used in case the number of iterations is not specified before hand.

## Simple example of while loop
i = 1
while i<=10:
	print(i)
	i += 1

#In how many years an investment of Rs. 20000 will double if interest is calculated under compound interest at the rate 5% annually?
principal = 20000
rate = 5
amount = 20000
years = 1
while(amount<2*principal):
	amount = principal*(1+rate/100)**years
	print(f'Amount after {years}yr. is Rs.{amount:.4f}')
	years = years+1

# Example: Use while loop to find the gcd of two integers a and b.
a, b = 4, 8
a, b = abs(a), abs(b)
if(a==0):
	if(b==0):
		gcd = 'gcd does not exist'
	else:
		gcd = b
else:
	if(b==0):
		gcd = a
	else:
		if(a<b):
			a,b=b,a
		while(a%b!=0):
			a,b = b, a%b
		gcd = b
print(gcd)

# User Defined Function for GCD
def mygcd(a,b):
	a, b = abs(a), abs(b)
	if(a==0):
		if(b==0):
			gcd = 'gcd does not exist'
		else:
			gcd = b
	else:
		if(b==0):
			gcd = a
		else:
			if(a<b):
				a,b=b,a
			while(a%b!=0):
				a,b = b, a%b
			gcd = b
	return gcd

print(mygcd(480,1200))

# Example: How many tosses are rquired to get sixes on both the faces if two six faced dice are tossed together?

from random import sample
sample(range(1,7),1)[0]
s = 2
tosses=0
while(s !=12):
	n1, n2 = sample(range(1,7),1)[0], sample(range(1,7),1)[0]
	s = n1+n2
	tosses = tosses + 1
print(tosses)



from math import factorial, exp
print(exp(1))

error = 1
tol = 1e-20
eval = 1
n = 1
while(error>=tol):
	error = 1/factorial(n)
	eval = eval+error
	n = n+1
print(eval, n)

Output:
1
2
3
4
5
6
7
8
9
10
Amount after 1yr. is Rs.21000.0000
Amount after 2yr. is Rs.22050.0000
Amount after 3yr. is Rs.23152.5000
Amount after 4yr. is Rs.24310.1250
Amount after 5yr. is Rs.25525.6313
Amount after 6yr. is Rs.26801.9128
Amount after 7yr. is Rs.28142.0085
Amount after 8yr. is Rs.29549.1089
Amount after 9yr. is Rs.31026.5643
Amount after 10yr. is Rs.32577.8925
Amount after 11yr. is Rs.34206.7872
Amount after 12yr. is Rs.35917.1265
Amount after 13yr. is Rs.37712.9828
Amount after 14yr. is Rs.39598.6320
Amount after 15yr. is Rs.41578.5636
4
240
54
2.718281828459045
2.7182818284590455 23
