# Tuple

# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round "()" brackets.
# Tuples are used to group together related data.
# Tuples can contain elements of different data types.

#Note: Tuples are immutable, meaning that once they are created, their elements cannot be changed, added, or removed.

# Creating a Tuple
t = ()  # Empty tuple
print(type(t))  # Output: <class 'tuple'>
t = tuple()  # Empty tuple using tuple() constructor
print(type(t))  # Output: <class 'tuple'>

#important Note: Single element tuple
t = (1)  # Not a tuple
print(type(t))  # Output: <class 'int'>
t = ("A")  # Tuple with one element
print(type(t))  # Output: <class 'str'>
t = (1,)  # Tuple with one element
print(type(t))  # Output: <class 'tuple'>

# Tuple with single string elements
t1 = ("Hello",)  # Tuple with one string element
print(type(t1))  # Output: <class 'tuple'>
t2 = ("Hello")  # Not a tuple
t3 = tuple("Hello")  # Tuple from string
print(type(t2))  # Output: <class 'str'>
print(t3)  # Output: ('H', 'e', 'l', 'l', 'o') => Returms each character as an element of the tuple


# t4 = tuple(["Hello"],[1,2],3,"ram")  # Tuple from list
# File "d:\learn\py\01_python\03_data_structures\02_tuple.py", line 33, in <module>
#     t4 = tuple(["Hello"],[1,2],3,"ram") 
# TypeError: tuple expected at most 1 argument, got 4
t4 = (["Hello"],[1,2],3,"ram")  # Tuple from list
# print(type(t4))  # Output: <class 'tuple'>
print(t4)  # Output: (['Hello'], [1, 2], 3, 'ram') => Returms each list as an element of the tuple
# Note: here the last element "ram" not seperated as character like the previous example

my_tuple = (1, 2, 3, "Hello", 5.5)
print(my_tuple)  # Output: (1, 2, 3, 'Hello', 5.5)  
print(type(my_tuple))  # Output: <class 'tuple'>
print(len(my_tuple))  # Output: 5
print(my_tuple[3],type(my_tuple[3]))  # Output: Hello <class 'str'>

# Accessing Tuple Elements
print(my_tuple[0])  # Output: 1
print(my_tuple[-1])  # Output: 5.5
print(my_tuple[1:4])  # Output: (2, 3, 'Hello')
print(my_tuple[::-1])  # Output: (5.5, 'Hello', 3, 2, 1)

# Imutable Nature of Tuples
# my_tuple[0] = 10  # This will raise a TypeError because tuples are immutable

# Mutable in tuple([List]) by using List and the List's indesx tuple[][]=" "
t5 = (["Hello"], [1, 2], 3, "ram")
print(t5)  # Output: (['Hello'], [1, 2], 3, 'ram')
t5[0][0] = "Hi"  # Changing the first element of the list inside the tuple
print(t5)  # Output: (['Hi'], [1, 2], 3, 'ram')
t5[1][1] = 45  # Changing the second element of the list inside the tuple
print(t5)  # Output: (['Hi'], [1, 45], 3, 'ram')

# Tuple Unpacking
a = 1
b = 10
c = "a"
print(a, b, c)  # Output: 1 10 a
a, b, c = 1, 10, "a"
t6 = (1, 10, "a")
a, b, c = t6
t7 = (1, 10, "a")    
a,b,c = t7 # Space doesn't matter
print(t7)  # Output: (1, 10, 'a')
print(type(t6))  # Output: <class 'tuple'>
print(a, b, c)  # Output: 1 10 a
print(t6)  # Output: (1, 10, 'a')


# Tuple Methods

# count(): Returns the number of times a specified value appears in the tuple. 
t8 = (1, 2, 3, 1, 4, 1)
print(t8.count(1))  # Output: 3 (counts the occurrences of 1)
print(t8.count(10))  # Output: 0 (counts the occurrences of 10)

# index(): Searches the tuple for a specified value and returns the position of where it was found.
print(t8.index(3))  # Output: 2 (index of first occurrence of 3)
# print(t8.index(10))  # This will raise a ValueError because 10 is not in the tuple

#iterating through a tuple
for item in t8:
    print(item) # Output: 1 2 3 1 4 1 (each element on a new line)

#list to tuple,tuple to list
list1 = [1,2,3,4]
tuple1 = tuple(list1)
print(type(tuple1)) # Output: <class 'tuple'>
print(tuple1) # Output: (1, 2, 3, 4)
tuple2 = (5,6,7,8)
list2 = list(tuple2)
print(type(list2)) # Output: <class 'list'>
print(list2) # Output: [5, 6, 7, 8]

#Concatenation of tuples
t9 = (1,2,3)
t10 = (4,5,6)
t11 = t9 + t10
print(t11) # Output: (1, 2, 3, 4, 5, 6)
# Note : Tuples can only be concatenated with other tuples (not with lists or other data types).

#
#
# Note : Tuples are immutable, so concatenation creates a new tuple and does not modify the original tuples.
# also adding of an element at end is possible by concatenation
t9 = t9 + (7,)# adding single element
print(t9) # Output: (1, 2, 3, 7)
t9 = t9 + (8,9,10) # adding multiple elements
print(t9) # Output: (1, 2, 3, 7, 8, 9, 10)
t01 = ("a",3,4,5)
t01 = t9 + t01 # adding tuple with different data types
print(t01) # Output: (1, 2, 3, 7, 8, 9, 10, 'a', 3, 4, 5)
#
#
#

# Multiplication of tuples
t12 = t9 * 3
print(t12) # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)
t13 = t9[3]*2 # Multiplying the fourth element of t9 by 2
t14 = t01[0]*3 # Multiplying the first element of t01 by 3
print(t13) # Output: 14 (7*2=14)
print(t14) # Output: aaa ('a' repeated 3 times)

