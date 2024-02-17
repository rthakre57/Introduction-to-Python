# Approximation of π using Monte-carlo method
N = 10000
import random
count = 0
for i in range(N):
	x,y = random.random(), random.random()
	if(x**2+y**2<1):
		count = count +1
		ratio = count/N
print(ratio*4)

#Looping over a dictionary
# Create a dictionary of 10 students whose roll numbers are 1 to 10. For each students fill in marks in 5 subjects which is list of random numbers between 1 to 100. Find the average marks of each student and add the average as value for the key ‘Avg’ for each student.
import random
d = {}
for k in range(1,11):
	d[k] = {}
for roll in d.keys():
	d[roll]['marks']= [random.randint(1,100) for i in range(5)]
for roll in d.keys():
	s = sum(d[roll]['marks'])
	avg = s/len(d[roll]['marks'])
	d[roll]['Avg']=avg

print(d)

# Printing a pyramid of stars.
height = 10 # No. of stars in the bottom row
m = 2*height -1 # No. of spaces required in the bottom row.
for i in range(0, height): # i runs over rows
	for j in range(0, m+1):
		print(end = " ") # creating the blank spaces in row ith row
	for k in range(0,i+1):
		print("*", end = " ") # printing i stars in i-th line
	print(" ") # Line break
	m = m-1 # decreasing m after each row

Output:

3.13
{1: {'marks': [50, 80, 61, 20, 29], 'Avg': 48.0}, 2: {'marks': [21, 26, 11, 32, 70], 'Avg': 32.0}, 3: {'marks': [66, 40, 3, 60, 99], 'Avg': 53.6}, 4: {'marks': [36, 38, 1, 99, 75], 'Avg': 49.8}, 5: {'marks': [24, 94, 6, 35, 52], 'Avg': 42.2}, 6: {'marks': [1, 74, 92, 54, 20], 'Avg': 48.2}, 7: {'marks': [18, 10, 16, 18, 72], 'Avg': 26.8}, 8: {'marks': [42, 92, 55, 73, 29], 'Avg': 58.2}, 9: {'marks': [98, 85, 25, 83, 43], 'Avg': 66.8}, 10: {'marks': [91, 81, 49, 75, 9], 'Avg': 61.0}}
                    *  
                   * *  
                  * * *  
                 * * * *  
                * * * * *  
               * * * * * *  
              * * * * * * *  
             * * * * * * * *  
            * * * * * * * * *  
           * * * * * * * * * *  
