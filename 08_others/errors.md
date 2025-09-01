# Types of error in python
### Syntax of Python in TensorFlow - The Engineering Projects
Errors in Python are typically three main types:
* syntax errors, 
* runtime errors (exceptions), and 
* logical errors. 
# 1. Syntax errors
A syntax error occurs when the Python interpreter cannot parse the code because it violates the language's rules.

The program will not run until these errors are fixed.

<u>Example: Forgetting a colon at the end of a for loop or if statement. </u>
```
 if True
    print("This will cause a syntax error")
```
### IndentationError: A specific type of syntax error caused by incorrect or inconsistent indentation.

# 2. Runtime errors (Exceptions)
 A runtime error, or exception, occurs while the program is running, even if the syntax is correct.  Python provides try-except blocks to handle . 
## Common types of runtime errors include:
### NameError: Raised when a local or global variable name is not found.
python
> print(my_variable) # my_variable is not defined


### TypeError: Raised when an operation or function is applied to an object of an inappropriate type.
python
> "hello" / 3
 * Division operation is invalid for a string and an integer


### ZeroDivisionError: Raised when the second operand of a division or modulo operation is zero.
python
> result = 100 / 0

### ValueError: Raised when a function receives an argument of the correct type but an invalid value.
python
> int("hello") # The string "hello" cannot be converted to an integer


### IndexError: Raised when an index of a sequence (like a list or string) is out of range.
python
> my_list = [1, 2, 3]
print(my_list[3]) # Index 3 is out of range for this list


### KeyError: Raised when a dictionary key is not found.
python
> my_dict = {"name": "Alice"}
print(my_dict["age"]) # The key "age" does not exist


### AttributeError: Raised when an attribute reference or assignment fails, often because an object does not have that attribute or method.
python
> my_list = [1, 2, 3]
my_list.append_item(4) # The list object has no method named append_item


### ModuleNotFoundError: Raised when an import statement fails to find the module.
FileNotFoundError: Raised when an operation (like open()) is attempted on a file that doesn't exist. 
# 3. Logical errors
A logical error causes a program to produce incorrect results or behavior, but it does not  display an error message. These are the most difficult errors to debug because the program runs seemingly(normally) without issue. 

<u>Example: Calculating an average by dividing by a constant instead of the total number of items.</u> 
python
>scores = [90, 85, 95]
average = sum(scores) / 2 # Incorrect logic: should divide by len(scores)

print(average) # Prints the wrong result, but no error is raised