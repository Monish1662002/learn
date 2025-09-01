dic = {} # Empty dictionary
dic2 = dict() # Empty dictionary
dic3 = {'name': 'John', 'age': 30, 'city': 'New York'} # Dictionary with initial values

print(dic3['name']) # Accessing value by key # Output: John
print(dic3.get('age')) # Accessing value using get method   # Output: 30

print(dic3.keys()) # Output: dict_keys(['name', 'age', 'city'])
print(dic3.values()) # Output: dict_values(['John', 30, 'New York'])
print(dic3.items()) # Output: dict_items([('name', 'John'), ('age', 30), ('city', 'New York')])

# Zip