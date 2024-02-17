# Tuples

T = (54,753,624,736,452)

print(len(T))

T[0]

T[2:4]

# T[2]=10 'tuple' object does not support item assignment


#Working with sets.

S1 = {1,4,2,5,2,5,1}

print(type(S1))

S2 = {8,6,0,54,2,1,42}

print(S1.union(S2))

print(S1.intersection(S2))

print(S2.difference(S1))

print(S1.issubset(S2))

len(S1)

# S1[0]   'set' object is not subscriptable

S1.add(726)

S1.clear()
print(S1)
print(S2)

S2.discard(0)
print(S2)

Output:

5
<class 'set'>
{0, 1, 2, 4, 5, 6, 8, 42, 54}
{1, 2}
{0, 6, 8, 42, 54}
False
set()
{0, 1, 2, 6, 54, 8, 42}
{1, 2, 6, 54, 8, 42}
