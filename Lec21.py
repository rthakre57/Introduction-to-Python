class student: #Emty class
	pass


s1=student() #constructor call
s2=student()

s1.name='John'  #attributes of s1
s1.roll='MAT101'
s1.DOB='July 15,1995'
s1.grade='A+'

print(s1.name)
print(s1.DOB)


# Classes with methods

#Class Methods and self arguments
#• Class methods (or functions) are exactly same as ordinary function that we have seen earlier.
#• Class methods must have first argument as ‘self’. We do not pass any value to self parameter.
#  Whenever an object (instantance) is created python provides its value automatically

 #Class Variables and Object Variables
#• There are two types of variables, class variables and object variables. Class variables are
#onwed by the class and object variables are owned by each object in the following sense:
#– If a class has n objects then there will be n separate copies of the object variables.
#– The object variables are not shared between objects.
#– Changes made to object variable by one object does not reflect in other objects.
#– If a class has one class variable, then there will only one copy for that variable. All the
#object of that class will share the class variable

class student:
	Total=0

	def __init__(self,name,roll,total_marks=0):
		self.name=name
		self.roll=roll
		self.total_marks=total_marks
		student.Total +=1
		print(f"A new student {self.name} is added with roll number {self.roll}")
		print(f"Total number of students is {student.Total}")

	def getmarks(self,marks):
		for m in marks:
			self.total_marks +=m
		self.avg=self.total_marks/len(marks)
		print(f"total marks is {self.total_marks}")
		print(f"average marks is {self.avg}")

	def average(self):
		return self.avg


s1=student('John','MAT101')
print(s1)

s2=student('Sara','MAT111')

print(student.Total)

s1.getmarks([96,89,55,67])

print(s1.average())

# init() Method (Class construction)
#Some class methods have names starting and ending with a double underscores. These methods
#are called special methods. The constructor __init__() is one such example. This method has a
#special siginificance in Python classes.
#The __init__() is automatically executed when an object of a class is created. This method is
#useful to initiate the variables in the class objects.
#Inside the constructor __init__, the argument self is a variable holding the new instance to be
#constructed.
#Other special methods make it possible to perform arithmetic operations with instances, to compare instances with >, >=, !=, etc., to call instances as we call ordinary functions, and to test if an
#instance evaluates to True or False, to mention some possibilities.

# __call__() method
#The __call__() method lets the class act like a function so that its instance can be called directly
#(viz. ’obj(arg1, arg2,..)’)

### Class for numerical 1st derivative

class derivatives():

	def __init__(self , f , h=1E-8):
		self.f=f
		self.h=float(h)

	def __call__(self , x):
		f,h=self.f,self.h
		return (f(x+h)-f(x))/h

from math import sin,cos,pi 
df =derivatives(sin,0.0001)
x0=pi/4
print(df(x0)) 


#Special Methods
#A collection of special methods, with two leading and trailing underscores in the method names,
#offers special syntax in Python programs. The table below provides an overview of the most
#important special methods.
#__init__(self, args)                constructor: a = A(args)
#__del__(self)                       destructor: del a
#__call__(self, args)                call as function: a(args)
#__str__(self)                        pretty print: print a, str(a)
#__repr__(self)                       representation: a = eval(repr(a))
#__add__(self, b)                      a + b invokes a.__add__(b)
#__sub__(self, b)                      a - b invokes a.__sub__(b)
#__mul__(self, b)                      a*b invokes a.__mul__(b)
#__div__(self, b)                      a/b invokes a.__div__(b)
#__pow__(self, b)                      a**p involes a.__pow__(b)
#__lt__(self, b)                       a < b involes a.__lt__(b)
#__gt__(self, b)                        a > b involes a.__gt__(b)
#__le__(self, b)                       a <= b involes a.__le__(b)
#__ge__(self, b)                       a => b involes a.__ge__(b)
#__eq__(self, b)                       a == b involes a.__eq__(b)
#__ne__(self, b)                       a != b involes a.__ne__(b)
#__bool__(self)                        boolean expression, as in if a:
#__len__(self)                         length of a (int): len(a)
#__abs__(self)                         abs(a)

#str V/s repr

#__str__ and repr() both are used to get a string representation of an object.
#The __str__ is the 2nd most commonly used operator overloading in Python after __init__.
#The __str__ is run automatically whenever an instance is converted to its print string.



class triangle:

	def __init__(self,a,b,c):
		self.a=a
		self.b=b
		self.c=c

	def area(self):
		from math import sqrt
		s=(self.a+self.b+self.c)/2.0
		a=sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
		return a

	def __str__(self):
		return'(triangle with sides: %g ,%g,%g)' %(self.a,self.b,self.c)

	def __repr__(self):
		return '(triangle with sides: %g ,%g,%g)' %(self.a,self.b,self.c)

T=triangle(4,4,5)
T.area()
print(T)
print(T.area())
 
#• __str__ must return string object whereas __repr__ can return any expression.
#• If __str__ is missing then repr function is used as fallback
#• __repr__ representation is more precise, unambiguous, and can be used by developers .

#Vector class in 3d

import math

class vec3D:

	def __init__(self,x,y,z):

		self.x=x
		self.y=y
		self.z=z

	def __add__(self, other):

		return vec3D(self.x+other.x,self.y+other.y,self.z+other.z)

	def __sub__(self, other):
		return vec3D(self.x-other.x,self.y-other.y,self.z-other.z)

	def __mul__(self,other):
		return self.x*other.x+self.y*other.y+self.z*other.z

	def __eq__(self , other):
		return self.x==other.x and self.y==other.y  and self.z==other.z

	def __abs__(self):
		return math.sqrt(self.x**2+self.y**2+self.z**2)

	def __ne__(self,other):
		return not self.__eq__(other)

	def collinear(self,other1,other2):
		x= math.sqrt((other1.x-self.x)**2 +(other1.y-self.y)**2 + (other1.z-self.z)**2)
		y= math.sqrt((other2.x-other1.x)**2 +(other2.y-other1.y)**2 + (other2.z-other1.z)**2)
		z= math.sqrt((other2.x-self.x)**2 +(other2.y-self.y)**2 + (other2.z-self.z)**2)
		if x+y==z:
			print("Vectors are collinear")
		else:
			print("Vectors are not collinear")
	def right_angle_triangle(self,other1,other2):
		x= (other1.x-self.x)**2 +(other1.y-self.y)**2 + (other1.z-self.z)**2
		y= (other2.x-other1.x)**2 +(other2.y-other1.y)**2 + (other2.z-other1.z)**2
		z= (other2.x-self.x)**2 +(other2.y-self.y)**2 + (other2.z-self.z)**2
		if x+z==y:
			print("triangle are right angle triangle")
		else:
			print("triangle are not right angle triangle")
		
	def dot(self,other):
		return self.x*other.x+self.y*other.y+self.z*other.z

	def cross(self,other):
		x=(self.y*other.z)-(self.z*other.y)
		y=(self.z*other.x)-(self.x*other.z)
		z=(self.x*other.y)-(self.y*other.x)
		return vec3D(x,y,z)

	def distance_to(self,other):
		z=self-other
		return abs(z)

	def __str__(self):
		return '(%g,%g,%g)'  %(self.x,self.y,self.z)


u=vec3D(-4,6,10)
v=vec3D(2,4,6)
w=vec3D(14,0,-2)

u.collinear(v,w)
print(u.__add__(v))
print(u.__sub__(v))
print(u.dot(v))
print(u.cross(v))
print(u.distance_to(v))
print(u.__str__()) 


import numpy as np 
import scipy as sp 

class quadratic(object):
	def __init__(self,a,b,c):
		self.a=a
		self.b=b
		self.c=c

	def __call__(self,x):
		return self.a * x**2 +self.b * x+self.c

	def discrminant(self):
		return self.b**2 -4*self.a*self.c

	def roots(self):
		d=self.discrminant()
		print(d)
		if d>=0:
			print("Roots are real and they are:")
			x1=(-self.b-np.sqrt(d))/(2.0*self.a)
			x2=(-self.b+np.sqrt(d))/(2.0*self.a)
		else:
			print("Roots are imaginary and they are:")
			x1=(-self.b-np.sqrt(d))/(2.0*self.a)
			x2=(-self.b+np.sqrt(d))/(2.0*self.a)
		return x1 , x2

	def __str__(self):
		s="f(x)="
		if self.a:
			s+="%f x**2" %self.a
		if self.b:
			if self.b > 0:
				s+="+"
			else:
				s+="-"
			s+="%f x" %abs(self.b)
		if self.c:
			if self.c > 0:
				s+="+"
			else:
				s+="-"
			s+="%f" %abs(self.c)
		return s

q=quadratic(2,3,-5)
print(q)
print(q.roots())

 #Public, Private and Protected Variables
#• Public variables are those variables that are defined in the class and can be accessed from
#anywhere in the programme using dot (.) operator. Here anywhere means that the public
#variables can be accessed from within the class as well as from outside the class in which it
#is defined.
#• Private variables, on the other hand are those variables that are defined in the class with a
#double scores prefix ( __ ). These variables can be accessed only from within the class and
#from nowhere outside the class.
#• To make instance variable protected we add a prefix single under score ( _ ). This effectively
#prevents it to be accessed, unless it is from within a sub-class.


class students:
	def __init__(self,name,age, average,hobby):
		self.name =name
		self.__age=age
		self.__average=average
		self._hobby=hobby

	def display(self):
		print("Studentsname is:",self.name)
		print("students age is:",self.__age)
		print("Students average marks is:",self.__average)
		print("Students hobby is:",self._hobby)


A=students("Mr.XYZ",23,54.24,'reading')
print(A.display())
print(A.name)
#print(A.__age)
print(A._students__age)
A._students__age=32
print(A._students__age)
print(A._hobby)
A._hobby="dancing"
print(A._hobby)

#Private Methods
#Like private attributes python also allows you to have private methods to discourage people from
#accessing part of a class that have implementation details. However, if neccessary it can be accessed using objectname. __classname__privatemethodsname

class students:
	def __init__(self, name,age,average):
		self.name = name # Public variable
		self.__age = age # Private variable
		self.__average = average
	def __display(self): ## Private methods
		print("Students name is:", self.name)
		print("Students age is:", self.__age)
		print("Students average marks is: ", self.__average)

A = students("Mr. XYZ",24,87.9)
print(A.name)
#print(A.display())
print(A._students__display())

#Create a python class with name sphere created by the radius and methods to print volume and surface area.
class sphere:
	def __init__(self, radius):
		self.radius=radius

	def surface_area(self):
		import numpy as np
		a=4.0*np.pi*self.radius**2
		print(f'The surface area of sphere with radius {self.radius} is {a:.3f}.')

	def volume(self):
		import numpy as np
		v=(4/3)*np.pi*self.radius**3
		print(f'The volume of the sphere with radius {self.radius} is {v:.3f}.')

s=sphere(5.0)
s.surface_area()
s.volume()
print(s.radius)


#Write an Account class to represent a bank account initialized with account number and
#starting balance. Include deposit(amount) and withdraw(amount) methods. Withdrawals
#should only be performed if the balance is high enough. Include the account number and
#balance in the __str__() method, and include a program to test your class

class account:
	def __init__(self,account_num,init_balance=0):
		self.acnum=account_num
		self.balance=init_balance

	def deposit(self,amount):
		self.balance+=amount

	def withdraw(self,amount):
		if self.balance>=amount:
			self.balance -=amount
		else:
			print("Insufficient Balance. cannot Withdraw!")

	def __str__(self):
		return "Acccount Number: %s  \nTotal Balance: %g" %(self.acnum,self.balance)

A=account('BA303SB',20000)
print(A)

A.deposit(30000)
print(f'Total Balance is:{A.balance}.')
A.withdraw(60000)

#Create a python class with name rationals with special methods methods to add, subtract,
#multiply and divide rational numbers
class rationals:
	def __init__(self,x):
		self.x = x
	def __add__(self,other):
		return rationals(self.x + other.x)
	def __sub__(self,other):
		return rationals(self.x - other.x)
	def __mul__(self,other):
		return rationals(self.x*other.x)
	def __truediv__(self,other):
		return rationals(self.x/other.x)
	def __str__(self):
		return '%g' %(self.x)
x = rationals(35)
print(x)
y = rationals(6)
print(x + y)
print(x - y)
print(x*y)
print(x/y)

#Create a class Country that stores the name of the country, its population, and its area. Then
#write a program that reads in a set of countries and prints (i) the country with the largest area,
#(ii) the country with the largest population and (iii) the country with the largest population
#density.
class Country:
	def __init__(self, name, population, area):
		self.name = name
		self.pop = population
		self.area = area

names = ['Australia', 'India', 'Nauru', 'Malta']
pop = [21766711, 1189172906,9322,408333]
area = [2967893,1269338,8,122]
C = Country(names,pop,area)
density = [C.pop[i]/C.area[i] for i in range (len(C.pop))]
for i in range (len(C.pop)):
	if C.area[i] == max(C.area):
		print(f'The country with the largest area is {C.name[i]}')
	if C.pop[i] == max(C.pop):
		print(f'The country with the highest population is {C.name[i]}')
	if density[i] == max(density):
		print(f'The country with the highest population density is {C.name[i]}')




#program to multiply two matrices
A=[]
n=int(input("Enter N for NxN matrix:"))
print("Enter the elemnts::>")
for i in range(n):
	row=[]
	for j in range(n):
		row.append(int(input()))
	A.append(row)
print(A)
#Display the 2D array
print("Display array in matrix form")
for i in range(n):
	for j in range(n):
		print(A[i][j], end=" ")
	print()	
 
B=[]
n=int(input("Enter N for NxN matrix:"))
print("Enter the elemnts::>")
for i in range(n):
	row=[]
	for j in range(n):
		row.append(int(input()))
	B.append(row)
print(B)
#Display the 2D array
print("Display array in matrix form")
for i in range(n):
	for j in range(n):
		print(B[i][j], end=" ")
	print()	

result=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(A)):
	for j in range(len(B[0])): 
		for k in range(len(B)):
			result[i][j]+=A[i][k]*B[k][j]
print("Resulltant matix is::>")
for r in result:
	print(r)
print("Display array in matrix form")
for i in range(n):
	for j in range(n):
		print(result[i][j], end="   ")
	print()	

Output:
John
July 15,1995
A new student John is added with roll number MAT101
Total number of students is 1
<__main__.student object at 0x0000024D13FB8070>
A new student Sara is added with roll number MAT111
Total number of students is 2
2
total marks is 307
average marks is 76.75
76.75
0.7070714246681931
(triangle with sides: 4 ,4,5)
7.806247497997997
Vectors are collinear
(-2,10,16)
(-6,2,4)
76
(-4,44,-28)
7.483314773547883
(-4,6,10)
f(x)=2.000000 x**2+3.000000 x-5.000000
49
Roots are real and they are:
(-2.5, 1.0)
Studentsname is: Mr.XYZ
students age is: 23
Students average marks is: 54.24
Students hobby is: reading
None
Mr.XYZ
23
32
reading
dancing
Mr. XYZ
Students name is: Mr. XYZ
Students age is: 24
Students average marks is:  87.9
None
The surface area of sphere with radius 5.0 is 314.159.
The volume of the sphere with radius 5.0 is 523.599.
5.0
Acccount Number: BA303SB  
Total Balance: 20000
Total Balance is:50000.
Insufficient Balance. cannot Withdraw!
35
41
29
210
5.83333
The country with the largest area is Australia
The country with the highest population is India
The country with the highest population density is Malta
Enter N for NxN matrix:3
Enter the elemnts::>
1
2
3
4
5
6
7
8
9
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Display array in matrix form
1 2 3 
4 5 6 
7 8 9 
Enter N for NxN matrix:3
Enter the elemnts::>
1
2
3
4
5
6
7
8
9
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Display array in matrix form
1 2 3 
4 5 6 
7 8 9 
Resulltant matix is::>
[30, 36, 42]
[66, 81, 96]
[102, 126, 150]
Display array in matrix form
30   36   42   
66   81   96   
102   126   150 
