#Lists

L = [2,3,5,7,11,13,17,19,23,29]

print(len(L))

print(L[0])

print(L[1:5])

print(L[-3])

print(L.append(31))
print(L)

L[2]=10
print(L)

L.insert(5,100)
print(L)

L.remove(100)
print(L)

M = [37,41,43,53]

print(L+M)

# List of list
A = [[1,2,3],[4,5,6],[7,8,9]]

## List of numbers in a arithmetic progression.
print(list(range(10)))

print(list(range(0,51,5)))

## Copying a list
M1 = M

M[1]=100

print(M,M1)

M2 = M.copy()
print(M2)

M2[1] =500
print(M,M2)

Output:
10
2
[3, 5, 7, 11]
19
None
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
[2, 3, 10, 7, 11, 13, 17, 19, 23, 29, 31]
[2, 3, 10, 7, 11, 100, 13, 17, 19, 23, 29, 31]
[2, 3, 10, 7, 11, 13, 17, 19, 23, 29, 31]
[2, 3, 10, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 53]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
[37, 100, 43, 53] [37, 100, 43, 53]
[37, 100, 43, 53]
[37, 100, 43, 53] [37, 500, 43, 53]
