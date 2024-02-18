#1. Input three real numbers and print the maximum of their absolute values.
a = 500
b = -200
c = 300
if (abs(a)>abs(b)) and (abs(a)>abs(c)):
	print(f"The maximum magnitude is {abs(a)}")
elif((abs(b)> abs(a)) and (abs(b)>abs(c))):
	print(f"The maximum magnitude is {abs(b)}")
else:
	print(f"The maximum magnitude is {abs(c)}")

# 2. Suppose an investment is made to a bank by an individual. The bank gives an annual interest
# at the rate 3.4 %. In case of senior citizen over the age of 60, the return is calculated using
# compound interest, otherwise using simple interest. Create a Python user-defined function
# to input the investment amount, the age of the investor, and the number of years for which
# investment is made, and print the returns.

def Investment(principal,age,years):
	rate = 3.4
	if age<60:
		amount = principal + (principal*rate*years/100)
	else:
		amount = principal*((1+(rate/100))**years)
	print(f'The returns after {years} years is {amount:.3f}')

Investment(20000, 56, 6)
Investment(20000, 66, 6)

# 3. Create a user-defined function to input a list of marks (at least in 5 subjects), and print the
# grades ‘A’, ‘B’, ‘C’, and ‘D’ based on the average marks. You may decide the criteria for the
# grades yourself.

M = [87,97,76,80,94]

def grades(L):
	avg = sum(L)/len(L)
	if avg>=90.0:
		print("A Grade")
	elif avg>=80.0:
		print("B Grade")
	elif avg>=70.0:
		print("C Grade")
	else:
		print("D Grade")


grades(M)

# 4. Create the Gaussian function with the name ‘gaussian’:f(x) = 1s√2πe− 12 (x−m/s )2 You may use some default values for the parameters m and s.

from math import sqrt,exp,pi
def gaussian(x,m,s):
	return exp(-0.5*((x-m)/s)**2)/(s*sqrt(2*pi))

print(gaussian(2.6,0,1))

# 5. Write a python program to input a point in the x-y plane, say (xi, yi), and check if the point is origin, or lies on the x − axis, y − axis or the quadrant number. Also print the distance between (xi, yi) and (1, −1).
X = (-2,-3)
Y = (1,-1)

if X[0] == 0.0 and X[1] == 0.0:
	print("The point chosen is the origin (0,0).")
elif X[0] == 0.0 and X[1] != 0.0:
	print("The point lies on the y-axis.")
elif X[0] != 0.0 and X[1] == 0.0:
	print("The point lies on the x-axis.")
elif X[0] > 0.0 and X[1] > 0.0:
	print("The point lies in the first quadrant.")
elif X[0] < 0.0 and X[1] > 0.0:
	print("The point lies in the second quadrant.")
elif X[0] < 0.0 and X[1] < 0.0:
	print("The point lies in the third quadrant.")
else:
	print("The point lies in the fourth quadrant.")
d = sqrt((X[0]-Y[0])**2 + (X[1]-Y[1])**2)
print(f"The distance of the point {X} from {Y} is {d:.4f} units.")

Output:
The maximum magnitude is 500
The returns after 6 years is 24080.000
The returns after 6 years is 24442.928
B Grade
0.013582969233685615
The point lies in the third quadrant.
The distance of the point (-2, -3) from (1, -1) is 3.6056 units.
