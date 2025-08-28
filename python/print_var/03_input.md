### input() always returns a string.

### Error faced when multiple variables are used to get input
>a, b = input("Enter two numbers: ").split()
print("You entered:", a, b)

Type "help", "copyright", "credits" or "license" for more information.
>>> a, b = input("Enter two numbers: ").split()
Enter two numbers: print("You entered:", a, b)
Traceback (most recent call last):
  File "<python-input-0>", line 1, in <module>
    a, b = input("Enter two numbers: ").split()
    ^^^^
ValueError: too many values to unpack (expected 2)
>>> 