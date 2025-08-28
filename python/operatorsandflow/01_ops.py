# Python Operators with Examples

# 1. Arithmetic Operators
a = 10
b = 3

print("Arithmetic Operators:")
print("Addition:", a + b)        # Adds a and b → 13
print("Subtraction:", a - b)     # Subtracts b from a → 7
print("Multiplication:", a * b)  # Multiplies a and b → 30
print("Division:", a / b)        # Divides a by b → 3.333...(division always yields float)
print("Floor Division:", a // b) # Division result without decimal → 3(rounded down to nearest smaller integer [left of the number line])
print("Modulus:", a % b)         # Remainder → 1
print("Exponent:", a ** b)       # a raised to the power of b → 1000

# Addition examples
print("Addition:", 7 + 3)        # 10   
print(1.6+3)           # 4.6
print(3.5 + 2.5)       # 6.0
print("String Concatenation:", "Hello" + " " + "World")  # "Hello World"
print("2"+"3")  # "23" (string concatenation)
string1 = "Hello"
string2 = "World"
print(string1 - string2)  #TypeError: unsupported operand type(s) for -: 'str' and 'str'


# miltiplication examples
print(string1 * 3)  # "HelloHelloHello"
print(3 * string2)  # "WorldWorldWorld"
print(string1 * string2)  #TypeError: can't multiply sequence by non-int of type 'str'
# 2. Comparison Operators
x = 5
y = 10

print("Comparison Operators:")
print("Equal:", x == y)          # False
print("Not Equal:", x != y)      # True
print("Greater Than:", x > y)    # False
print("Less Than:", x < y)       # True
print("Greater or Equal:", x >= y) # False
print("Less or Equal:", x <= y)    # True


# 3. Logical Operators
p = True
q = False

print("Logical Operators:")
print("AND:", p and q)   # True if both are True → False
print("OR:", p or q)     # True if any one is True → True
print("NOT:", not p)     # Reverses True to False → False
print(not 2>3) # True
print(not 3>2) # False


# 4. Assignment Operators
num = 10
print("Assignment Operators:")
num += 5  # num = num + 5 → 15
print("After += :", num)
num -= 3  # num = num - 3 → 12
print("After -= :", num)
num *= 2  # num = num * 2 → 24
print("After *= :", num)
num /= 4  # num = num / 4 → 6.0
print("After /= :", num)
num //= 2  # num = num // 2 → 3.0
print("After //= :", num)
num %= 2   # num = num % 2 → 1.0
print("After %= :", num)
num **= 3  # num = num ** 3 → 1.0
print("After **= :", num)

print("\n")

# 5. Bitwise Operators
m = 6  # 110 in binary
n = 2  # 010 in binary

print("Bitwise Operators:")
print("AND:", m & n)   # 110 & 010 = 010 → 2
print("OR:", m | n)    # 110 | 010 = 110 → 6
print("XOR:", m ^ n)   # 110 ^ 010 = 100 → 4
print("NOT:", ~m)      # ~110 = -(m+1) → -7
print("Left Shift:", m << 1) # 110 << 1 = 1100 → 12
print("Right Shift:", m >> 1) # 110 >> 1 = 011 → 3

m = 6  # Binary: 110
n = 2  # Binary: 010

print("Bitwise Operators:")
print("AND:", m & n)     # 6 & 2 = 2
print("OR:", m | n)      # 6 | 2 = 6
print("XOR:", m ^ n)     # 6 ^ 2 = 4
print("NOT:", ~m)        # ~6 = -7
print("Left Shift:", m << 1)  # 6 << 1 = 12
print("Right Shift:", m >> 1) # 6 >> 1 = 3

m = 6  # Binary: 110
n = 2  # Binary: 010

print("Bitwise Operators:")
print("AND:", m & n)     # 6 & 2 = 2
print("OR:", m | n)      # 6 | 2 = 6
print("XOR:", m ^ n)     # 6 ^ 2 = 4
print("NOT:", ~m)        # ~6 = -7
print("Left Shift:", m << 1)  # 6 << 1 = 12
print("Right Shift:", m >> 1) # 6 >> 1 = 3

# Explanation:

# AND (m & n)
# Binary of 6 → 110
# Binary of 2 → 010
# 110 & 010 → 010 (Only common 1s stay) → 2

# OR (m | n)
# 110 | 010 → 110 (1 if any bit is 1) → 6

# XOR (m ^ n)
# 110 ^ 010 → 100 (1 if bits are different) → 4

# NOT (~m)
# ~6 → -(6 + 1) → -7
# Works as bitwise inversion in Python.

# Left Shift (m << 1)
# Shifts bits of 6 (110) to left → 1100 → 12

# Right Shift (m >> 1)
# Shifts bits of 6 (110) to right → 011 → 3

print("\n")

# 6. Identity Operators
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print("Identity Operators:")
print("a is b:", a is b)     # True (same object in memory)
print("a is c:", a is c)     # False (different object)
print("a is not c:", a is not c) # True

print("\n")

# 7. Membership Operators
nums = [1, 2, 3, 4, 5]
name="Hello world"

print("Hello" in name )# True)
print("olleH" in name )# False)
print("Membership Operators:in")
print("3 in nums:", 3 in nums)        # True
print("10 not in nums:", 10 not in nums) # True

# 8. is Operators--> compare memory locations of two objects
print("is Operators:")
a=5
b=5
print(a is b) # True
print(a is not b) # False

a=5000
b=5001
print(a is b) # False
print(a is not b) # True