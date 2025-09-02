# List
# 2 types of list creation
# 1. Using square brackets []
my_list = [1, 2, 3, 4, 5]
print(my_list)  
# Output: [1, 2, 3, 4, 5]
# 2. Using the list() constructor
another_list = list((6, 7, 8, 9, 10))
print(another_list)  
# Output: [6, 7, 8, 9, 10]  

# List indexing and slicing
# Accessing elements using positive indexing
first_element = my_list[0]
print(first_element)  
# Output: 1
# Accessing elements using negative indexing    
last_element = my_list[-1]
print(last_element) 
# Output: 5

# Slicing a list
my_list = [1, 2, 3, 4, 5]

sub_list = my_list[1:4] # Similar to the string slicing
print(sub_list)  
# Output: [2, 3, 4]

# Slicing with step
step_list = my_list[::2]
print(step_list)  
# Output: [1, 3, 5]

# Reversing a list using slicing
reversed_list = my_list[::-1]
print(reversed_list)  
# Output: [5, 4, 3, 2, 1]   

len_list = len(my_list)
print(len_list)  
# Output: 5 

list_notrevsersed = my_list[5:0] # Empty list
print(list_notrevsersed)  
# Output: []




# Mutability of lists
print(id(my_list)) # 1549593043008 
my_list[0] = 10
print(my_list)  
# Output: [10, 2, 3, 4, 5]
print(id(my_list)) # 1549593043008 (same as before, showing mutability)

# Iterating through a list
for item in my_list:
    print(item) # 10 2 3 4 5 (each on a new line)


# List Methods
# 1. count
# 2. index
# 3. pop
# 4. remove
# 5. sort
# 6. insert
# 7. append
# 8. extend

#Count 
my_list = ["ram", "shyam", "hari", "ram"]
print(my_list.count("ram")) # 2
print(my_list.count("gita")) # 0

# Index
print(my_list.index("hari")) # 2
# print(my_list.index("gita")) # ValueError: 'gita' is not in list  

# in count of 0 means not found,but in index it raises error

# To avoid error, we can use 'in' keyword
if "gita" in my_list:
    print(my_list.index("gita"))

# Pop
popped_element = my_list.pop() # Removes and returns the last element
print(popped_element) # ram
print(my_list) # ['ram', 'shyam', 'hari']   
popped_index = my_list.pop(1) # Removes and returns the element at index 1
print(popped_index) # shyam
print(my_list) # ['ram', 'hari']
# If index is out of range, it raises IndexError
# my_list.pop(5) # IndexError: pop index out of range
# To avoid error, we can check the length

# Remove
my_list.remove("hari")  # Removes the first occurrence of "hari"
print(my_list) # ['ram']
# If the element is not found, it raises ValueError
# my_list.remove("gita") # ValueError: list.remove(x): x not in list
# To avoid error, we can use 'in' keyword

# Sort
num_list = [5, 2, 9, 1, 5, 6]
num_list.sort() # Sorts the list in ascending order
print(num_list) # [1, 2, 5, 5, 6, 9]
num_list.sort(reverse=True) # Sorts the list in descending order
print(num_list) # [9, 6, 5, 5, 2, 1]
# Sort with key (e.g., by length of strings)
str_list = ["apple", "banana", "kiwi", "cherry"]
str_list.sort(key=len)  # Sorts by length of strings
print(str_list) # ['kiwi', 'apple', 'banana', 'cherry']

# Insert
my_list = ["ram", "shyam", "hari"]
my_list.insert(1, "gita") # Inserts "gita" at index 1
print(my_list) # ['ram', 'gita', 'shyam', 'hari']
my_list.insert(0, "sita") # Inserts "sita" at the beginning
print(my_list) # ['sita', 'ram', 'gita', 'shyam', 'hari']
my_list.insert(len(my_list), "laxman") # Inserts "laxman" at the end
print(my_list)      # ['sita', 'ram', 'gita', 'shyam', 'hari', 'laxman']    
# If index is out of range, it inserts at the end
my_list.insert(10, "bharat") # Inserts "bharat" at the end
print(my_list) # ['sita', 'ram', 'gita', 'shyam', 'hari', 'laxman', 'bharat']

# Append
my_list = ["ram", "shyam", "hari"]
my_list.append("gita") # Appends "gita" at the end
print(my_list) # ['ram', 'shyam', 'hari', 'gita'] 

# append does not insert at specific index, it always adds at the end

# Append can add only one element at a time
my_list.append(["laxman", "sita"]) # Appends the entire list as a single element
print(my_list) # ['ram', 'shyam', 'hari', 'gita', ['laxman', 'sita']]
my_list2 = [2,3,4,"five"]
my_list2.append([6,7])
print(my_list2) # [2, 3, 4, 'five', [6, 7]]

# my_list2.index(6) # ValueError: 6 is not in list
my_list2.index([6,7]) # 4
# Because [6,7] is a single element in the list

# To avoid error, we can use 'in' keyword
# To add multiple elements, use extend

# Extend
my_list = ["ram", "shyam", "hari"]

my_list.extend(["gita", "laxman"]) # Extends the list by appending elements from the iterable

print(my_list) # ['ram', 'shyam', 'hari', 'gita', 'laxman']
# Note: Extend always iterates over its argument and but append push the entire argument as a single element
# So, extend is different from append
my_list3 = [1,2,3]
my_list3.append("jolly") 
print(my_list3) # [1, 2, 3, 'jolly']
my_list3.extend("jolly") 
print(my_list3) # [1, 2, 3, 'jolly', 'j', 'o', 'l', 'l', 'y']
# Because string is an iterable, so it adds each character as a separate element

# extends index at the end, it does not take specific index
# Extend can add multiple elements at a time
# It can take any iterable (list, tuple, set, etc.)
my_list.extend(("sita", "bharat")) # Extends the list by appending elements from the tuple
print(my_list)
# ['ram', 'shyam', 'hari', 'gita', 'laxman', 'sita', 'bharat']

#Heterogeneous lists
hetero_list = [1, "two", 3.0, [4, "four"], (5, "five"), {6: "six"}]
print(hetero_list)
# [1, 'two', 3.0, [4, 'four'], (5, 'five'), {6: 'six'}]
# Lists can contain elements of different data types
for item in hetero_list:
    print(f"{item} is of type {type(item)}")    
# 1 is of type <class 'int'>
# two is of type <class 'str'>
# 3.0 is of type <class 'float'>
# [4, 'four'] is of type <class 'list'>
# (5, 'five') is of type <class 'tuple'>
# {6: 'six'} is of type <class 'dict'>

# Nested lists,2D lists,lists of lists,lists within lists
nested_list = [[1, 2, 3], ["a", "b", "c"], [True, False]]
print(nested_list)  
print(nested_list[0]) # [1, 2, 3]
print(nested_list[1]) # ['a', 'b', 'c']
print(nested_list[2]) # [True, False]
print(nested_list[0][1]) # 2
print(nested_list[1][2]) # c
print(nested_list[2][0]) # True 
# Iterating through a nested list
for sublist in nested_list:
    for item in sublist:
        print(item) 
# 1
# 2
# 3 
# a
# b
# c
# True
# False 

# List comprehension
l=[]

for i in range(10):
    l.append(i)
print(l) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

l2 = [i for i in range(15)]
print(l2) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
l3 = [i*i for i in range(10)]
print(l3) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

new_list = [1,2,3,4,5]
print(new_list[-1:3]) # empty list
print(new_list[-1:-3])# empty list
print(new_list[-1:-3:-1]) # [5,4]
