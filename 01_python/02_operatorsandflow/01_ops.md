# Python Operators – Quick Reference

## 1. Arithmetic Operators
Used for mathematical operations.

| Operator | Description          | Example | Output |
|----------|----------------------|---------|--------|
| `+`      | Addition             | `10 + 5` | `15` |
| `-`      | Subtraction          | `10 - 5` | `5` |
| `*`      | Multiplication       | `10 * 5` | `50` |
| `/`      | Division (float)     | `10 / 5` | `2.0` |
| `//`     | Floor Division       | `10 // 3` | `3` |
| `%`      | Modulus (remainder)  | `10 % 3` | `1` |
| `**`     | Exponentiation       | `2 ** 3` | `8` |

---
### Floor Division (`//`) in Python

## What is Floor Division?
Floor division is a division operation that **rounds the result down to the nearest whole number**, moving towards negative infinity.

---

## Syntax
result = a // b

print(10 / 3)   # 3.3333 (Normal division)
print(10 // 3)  # 3 (Floor division)
print(-10 / 3)   # -3.3333 (Normal division)
print(-10 // 3)  # -4 (Floor division)
print(10 / -3)   # -3.3333 (Normal division)
print(10 // -3)  # -4 (Floor division)

Quick Note

/ → Returns a float with decimal part.

// → Returns an integer rounded down to nearest whole number.
```


## 2. Comparison Operators
Used to compare values, returns `True` or `False`.

| Operator | Description           | Example     | Output |
|----------|-----------------------|-------------|--------|
| `==`     | Equal to              | `5 == 5`    | `True` |
| `!=`     | Not equal to          | `5 != 3`    | `True` |
| `>`      | Greater than          | `5 > 3`     | `True` |
| `<`      | Less than             | `5 < 3`     | `False` |
| `>=`     | Greater or equal to   | `5 >= 5`    | `True` |
| `<=`     | Less or equal to      | `5 <= 3`    | `False` |

---

## 3. Logical Operators
Used to combine conditions.

| Operator | Description   | Example            | Output |
|----------|---------------|--------------------|--------|
| `and`    | Both true     | `(5 > 3 and 2 < 4)` | `True` |
| `or`     | At least one true | `(5 > 3 or 2 > 4)` | `True` |
| `not`    | Negates value | `not(5 > 3)`        | `False` |

---

## 4. Assignment Operators
Used to assign values with or without operations.

| Operator | Example   | Equivalent To |
|----------|-----------|---------------|
| `=`      | `x = 5`   | Assigns 5 to x |
| `+=`     | `x += 3`  | `x = x + 3` |
| `-=`     | `x -= 3`  | `x = x - 3` |
| `*=`     | `x *= 3`  | `x = x * 3` |
| `/=`     | `x /= 3`  | `x = x / 3` |
| `//=`    | `x //= 3` | `x = x // 3` |
| `%=`     | `x %= 3`  | `x = x % 3` |
| `**=`    | `x **= 3` | `x = x ** 3` |

---

## 5. Bitwise Operators
Operate on binary values (bits).

| Operator | Description  | Example   | Output |
|----------|--------------|-----------|--------|
| `&`      | AND          | `6 & 3`   | `2` |
| `|`      | OR           | `6 | 3`   | `7` |
| `^`      | XOR          | `6 ^ 3`   | `5` |
| `~`      | NOT          | `~6`      | `-7` |
| `<<`     | Left Shift   | `6 << 1`  | `12` |
| `>>`     | Right Shift  | `6 >> 1`  | `3` |

---

## 6. Membership Operators
Check for membership in a sequence (list, string, tuple).

| Operator | Description | Example                | Output |
|----------|-------------|-----------------------|--------|
| `in`     | Present?    | `3 in [1, 2, 3]`      | `True` |
| `not in` | Not present?| `5 not in [1, 2, 3]`  | `True` |

---

## 7. Identity Operators
Check if two objects are the same in memory.

| Operator | Description     | Example     | Output |
|----------|-----------------|-------------|--------|
| `is`     | Same object?    | `a is b`    | `True/False` |
| `is not` | Not same object?| `a is not b`| `True/False` |

---

### Example Code
```python
a, b = 10, 3
print(a + b)        # Arithmetic
print(a > b)        # Comparison
print(a > 5 and b < 5)  # Logical
a += 5
print(a)            # Assignment
print(6 & 3)        # Bitwise
print(3 in [1, 2, 3])  # Membership
x = [1, 2]
y = x
print(x is y)       # Identity
