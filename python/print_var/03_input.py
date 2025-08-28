name = input("Enter your name: ")
print("Hello", name)

num = int(input("Enter a number: "))  # Convert string to integer
print("Number + 10 =", num + 10)

price = float(input("Enter price: "))
print("Price + 5 =", price + 5)

a, b = input("Enter two numbers: ").split()
print("You entered:", a, b)

val = input("Enter True or False: ")
flag = val.lower() == "true"   # Converts to boolean
print("Boolean value:", flag)

s = "123"
print(int(s))    # String to Integer
print(float(s))  # String to Float
print(str(123))  # Integer to String
print(list(s))   # String to List of Characters
print(tuple(s))  # String to Tuple of Characters
print(bool(s))   # String to Boolean (True if not empty)
print(set(s))    # String to Set of Characters