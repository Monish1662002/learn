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


