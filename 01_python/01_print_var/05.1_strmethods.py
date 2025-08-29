# String Methods
name = "alice rajan"
upper_name = name.upper()  # ALICE RAJAN

lower_name = name.lower()  # alice rajan

capitalized_name = name.capitalize()  # Alice rajan # Only first letter of the string is capitalized

title_name = name.title() # Alice Rajan # First letter of each word is capitalized

print(name) # alice rajan _> original string remains unchanged

find_index = print(name.find("a") )# 0 # returns the index of the first occurrence of "a"

not_found_index = print(name.find("z")) # -1 # returns -1 if the substring is not found

count_a = print(name.count("a")) # 3 # counts the occurrences of "a" in the string

replaced_name = print(name.replace("a", "@")) # @lice r@j@n # replaces all occurrences of "a" with "@"

# Note: The original string remains unchanged after replace

index_of_a = print(name.index("a")) # 0 # returns the index of the first occurrence of "a" -> similer to find but raises an error if not found

# not_found_index = print(name.index("z")) # ValueError: substring not found # raises an error if the substring is not found

split_name = print(name.split(" ")) # ['alice', 'rajan'] # splits the string into a list of substrings based on spaces

split_name = print(name.split("a")) # ['','lice r','j','n'] # splits the string into a list of substrings based on "a"

# is methods
is_lower = print(name.islower()) # True # checks if all characters in the string are lowercase  

is_upper = print(name.isupper()) # False # checks if all characters in the string are uppercase

is_alpha = print(name.isalpha()) # False # checks if all characters in the string are alphabetic (no spaces or special characters)

is_alnum = print(name.isalnum()) # False # checks if all characters in the string are alphanumeric (no spaces or special characters)
name1 = "alice123"
is_alnum1 = print(name1.isalnum()) # True # checks if all characters in the string are alphanumeric (no spaces or special characters)   

is_numeric = print(name.isnumeric()) # False # checks if all characters in the string are numeric

name2 = "12345"
is_numeric2 = print(name2.isnumeric()) # True # checks if all characters in the string are numeric

# String Formating
name = "Murugesan"
age = 30
print("My name is " + name + " and I am " + str(age) + " years old.") # My name is Murugesan and I am 30 years old.
print("My name is " , name , " and I am " , str(age) , " years old.") # My name is  Murugesan  and I am  30  years old.
print("My name is {}and I am {} years old.".format(name, age)) # My name is Murugesan and I am 30 years old.
print("My name is {}and I am {} years old.".format(age, name)) # My name is 30 and I am Murugesan years old.

# F-Strings (Python 3.6+)->Formatted string literals
print(f"My name is {name} and I am {age} years old.") # My name is Murugesan and I am 30 years old.

# String Concatenation
str1 = "Hello"
str2 = "World"
concatenated_str = str1 + " " + str2 # Hello World
print(concatenated_str)

repeated_str = str1 * 3 # HelloHelloHello
print(repeated_str)

print("str1"*"3") # error -> TypeError: can't multiply sequence by non-int of type 'str'
print("str1"+3) # error -> TypeError: can only concatenate str (not "int") to str
print("str1"+str(3)) # str13