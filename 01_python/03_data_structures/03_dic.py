dic = {} # Empty dictionary
dic2 = dict() # Empty dictionary
dic3 = {'name': 'John', 'age': 30, 'city': 'New York'} # Dictionary with initial values

print(dic3['name']) # Accessing value by key # Output: John

# print(dic3['New York']) # KeyError: 'New York' the key does not exist

print(dic3.get('age')) # Accessing value using get method   # Output: 30

# Accessing in the dictionary
print(dic3.keys()) # Output: dict_keys(['name', 'age', 'city'])
print(dic3.values()) # Output: dict_values(['John', 30, 'New York'])
print(dic3.items()) # Output: dict_items([('name', 'John'), ('age', 30), ('city', 'New York')])

# Accessing the non-existing key
# print(dic3['country']) # KeyError: 'country' the key does not exist

# Using get method to access non-existing key
print(dic3.get('country')) # Output: None Error not thrown
# print(dic3['country']) # KeyError: 'country'
print(dic3.get('country',"no keyfound")) # Output: no keyfound

# Zip
name = ["Anbu","Raju","Mohan"]
age = [21,22,23]

user = zip(name,age) # [('Anbu', 21), ('Raju', 22), ('Mohan', 23)]
print(dict(user)) # {'Anbu': 21, 'Raju': 22, 'Mohan': 23}

# Adding new key-value pair
dic3['country'] = 'USA'
print(dic3) # {'name': 'John', 'age': 30, 'city': 'New York', 'country': 'USA'}
dic3['work'] = {'School':'Teacher','college':'Professor'} # Nested dictionary New value is added
print(dic3) # {'name': 'John', 'age': 30, 'city': 'New York', 'country': 'USA', 'work': {'School': 'Teacher', 'college': 'Professor'}}

# Updating existing key-value pair
dic3['age'] = 31
print(dic3) # {'name': 'John', 'age': 31, 'city': 'New York', 'country': 'USA'}
dic3.update({'age':32,'city':'LA'}) # Multiple values can be updated
print(dic3) # {'name': 'John', 'age': 32, 'city': 'LA', 'country': 'USA'}
dic3.update({'frnds':3}) # New key-value pair is added
print(dic3) # {'name': 'John', 'age': 32, 'city': 'LA', 'country': 'USA', 'frnds': 3}
skills = {'Python': 'Advanced', 'Java': 'Intermediate'}
dic3.update(skills) # Multiple values can be updated
print(dic3) # {'name': 'John', 'age': 32, 'city': 'LA', 'country': 'USA', 'Python': 'Advanced', 'Java': 'Intermediate'}


# citizinship in dic3
print('citizinship' in dic3) # False
print('John' in dic3) # False  
print('country' in dic3) # True 
print('USA' in dic3.values()) # True
print('John' in dic3.values()) # True

# Deleting key-value pair
# 1.pop(key)
dic3.pop('Java') # Removes the key 'Java' and its value
print(dic3) # {'name': 'John', 'age': 32, 'city': 'LA', 'country': 'USA', 'Python': 'Advanced'}

# 2.popitem() -> removes the last inserted key-value pair
dic3.popitem() # Removes the last inserted key-value pair
print(dic3) # {'name': 'John', 'age': 32, 'city': 'LA', 'country': 'USA'}
 
# dic3.popitem("city") # TypeError: popitem() takes no arguments (1 given)
print(dic3) # {'name': 'John', 'age': 32, 'city': 'LA', 'country': 'USA'}

# 3.del
del dic3['country'] # Deletes the key 'country' and its value
print(dic3) # {'name': 'John', 'age': 32, 'city': 'LA'} 
del dic3 # Deletes the entire dictionary
# print(dic3) # NameError: name 'dic3' is not defined
# 4.clear() -> clears all the items in the dictionary
dic3 = {'name': 'John', 'age': 30, 'city': 'New York'}
dic3.clear() # Clears all items in the dictionary
print(dic3) # {} Empty dictionary

# Iterating through a dictionary
dic3 = {'name': 'John', 'age': 30, 'city': 'New York'}
for key in dic3:
    print(key) # Prints all keys

for key in dic3:
    print(key,dic3[key]) # Prints all key-value pairs

# dic.items() -> returns a view object that displays a list of a dictionary's key-value tuple pairs
for key, value in dic3.items():
    print(key, value) # Prints all key-value pairs

# output:
#  name John
#  age 30
#  city New York 

print(len(dic3)) # Length of the dictionary # Output: 3
print(dic3.items()) # dict_items([('name', 'John'), ('age', 30), ('city', 'New York')])

# Example
name = input("Enter your name: ") #raja dhurai singam
frq = {}
for i in name:
    if i in frq:
        frq[i] = 1
    else:
        frq[i] +=1
print(frq)
# Output: {'A': 1, 'n': 1, 'b': 1, 'u': 1} if input is Anbu
# Output: {'r': 2, 'a': 3, 'j': 1, ' ': 2, 'd': 1, 'h': 1, 'u': 1, 'i': 1, 's': 1, 'g': 1, 'm': 1} if input is raja dhurai singam