a, b, c, d = 635, 434.7353, 'Python', 4+3j
type(a), type(b), type(c), type(d)

x,y,z = [],(),{}
print(type(x), type(y), type(z))

course = "Python Course For Dharampeth M P Deo Memorial Science College."

print(type(course))

print(len(course))

print(course[0], course[20], course[-1])

print(course[0:10])

print(course.lower())

print(course.count('a'))

print('z' in course)

course.split()

print(list(course))

print(course+course)

print(type(course))

Output:

<class 'list'> <class 'tuple'> <class 'dict'>
<class 'str'>
62
P a .
Python Cou
python course for dharampeth m p deo memorial science college.
3
False
['P', 'y', 't', 'h', 'o', 'n', ' ', 'C', 'o', 'u', 'r', 's', 'e', ' ', 'F', 'o', 'r', ' ', 'D', 'h', 'a', 'r', 'a', 'm', 'p', 'e', 't', 'h', ' ', 'M', ' ', 'P', ' ', 'D', 'e', 'o', ' ', 'M', 'e', 'm', 'o', 'r', 'i', 'a', 'l', ' ', 'S', 'c', 'i', 'e', 'n', 'c', 'e', ' ', 'C', 'o', 'l', 'l', 'e', 'g', 'e', '.']
Python Course For Dharampeth M P Deo Memorial Science College.Python Course For Dharampeth M P Deo Memorial Science College.
<class 'str'>
