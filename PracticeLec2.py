#1. Try to create a list of 10 points in three dimensional space {(xi, yi.zi)} for i = 1, 2, . . . , 10 using zip command.

x = range(2,12)
y = range(-10,10,2)
z = range(-4,26,3)

print(zip(x,y,z))

print(list(zip(x,y,z)))

#2. Explore what happens when you apply zip(x,y) in case x and y are of different lengths.

x = range(10)
y = range(15)

print(len(x),len(y))

z = list(zip(x,y))
print(z)

print(list(zip(range(15),range(10)))) # We see that on using the command zip(x,y) when x and y are of different lengths, we get a list of ordered pairs, the length of which, is the minimum of the lengths of x and y (in this case, 10).


#3. Explore methods such as insert, pop, remove, extend on a list.

L = [1,-19,2,-3,17,43,356]

L.insert(5,47) # insert takes 2 arguments : index (place where you want to␣,→insert the element)  and object (the element you␣ ,→wish to insert)

print(L) 

L.pop(3)

print(L)

L.remove(2) # removes the element 2 from the list
print(L)

M = [0, -4, 6, 35]

L.extend(M) # Appends the elements of M at the end of the list L
print(L)


#4. Define a long sentence and store it in a variable S. Count how many words are there in S. Also count how many characters are there excluding spaces.

S = "The quick brown fox jumps over the lazy dog."
words = S.split() # the split command returns a list of the words in the string
print(words)

print(len(words)) # returns the number of words in the sentence

print(len(S)) # counts the number of characters, including the spaces

print(S.count(" ")) # counts the number of blank spaces in the string

print(len(S) - S.count(" ")) # gives the number of characters excluding the spaces

# 5. Create a nested dictionary of books having three keys as three subjects with values as dictio-nary of the book title, author name, publisher, and year of publication.

Books = {'Mathematics':{'Book Title': 'The Joy of x', 'Author': 'Steve Strogatz',

'Publisher': 'Mariner Books','Year of Publication':2012},
'Chemistry':{'Book Title': 'The Disappearing Spoon', 'Author': 'Sam Kean',

'Publisher': 'Little, Brown and Company','Year of Publication': 2010},
'Physics':{'Book Title': 'Seven Brief Lessons on Physics', 'Author':'Carlo Rovelli',

'Publisher': 'Penguin Books', 'Year of Publication': 2015}}

print(Books)

print(Books.keys())

print(Books.values())

Output:
<zip object at 0x000001DE54148700>
[(2, -10, -4), (3, -8, -1), (4, -6, 2), (5, -4, 5), (6, -2, 8), (7, 0, 11), (8, 2, 14), (9, 4, 17), (10, 6, 20), (11, 8, 23)]
10 15
[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)]
[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)]
[1, -19, 2, -3, 17, 47, 43, 356]
[1, -19, 2, 17, 47, 43, 356]
[1, -19, 17, 47, 43, 356]
[1, -19, 17, 47, 43, 356, 0, -4, 6, 35]
['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog.']
9
44
8
36
{'Mathematics': {'Book Title': 'The Joy of x', 'Author': 'Steve Strogatz', 'Publisher': 'Mariner Books', 'Year of Publication': 2012}, 'Chemistry': {'Book Title': 'The Disappearing Spoon', 'Author': 'Sam Kean', 'Publisher': 'Little, Brown and Company', 'Year of Publication': 2010}, 'Physics': {'Book Title': 'Seven Brief Lessons on Physics', 'Author': 'Carlo Rovelli', 'Publisher': 'Penguin Books', 'Year of Publication': 2015}}
dict_keys(['Mathematics', 'Chemistry', 'Physics'])
dict_values([{'Book Title': 'The Joy of x', 'Author': 'Steve Strogatz', 'Publisher': 'Mariner Books', 'Year of Publication': 2012}, {'Book Title': 'The Disappearing Spoon', 'Author': 'Sam Kean', 'Publisher': 'Little, Brown and Company', 'Year of Publication': 2010}, {'Book Title': 'Seven Brief Lessons on Physics', 'Author': 'Carlo Rovelli', 'Publisher': 'Penguin Books', 'Year of Publication': 2015}])
