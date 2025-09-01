![Data Types](/09_imgs/Python-data-types.webp)

# Integer
Example:
a = 5
b = -3
print(a,b)
print(type(a,b))
```
5 -3
Traceback (most recent call last):
  File "d:\learn\py\python\print_var\datatypes.py", line 5, in <module>
    print(type(a,b))

          ~~~~^^^
```
__TypeError: type() takes 1 or 3 arguments__

print(type(a))
print(type(b))

# Float
> d=0.0.5 #incorrect
print(d)
print
File "d:\learn\py\python\print_var\datatypes.py", line 19
    d=0.0.5 #incorrect
         ^^
__SyntaxError: invalid syntax__

# Boolean
* Should be in Pascal case
> a = false 
# incorrect should be in pascal case
print(a)
print(type(a))
File "d:\learn\py\python\print_var\datatypes.py", line 25, in <module>
    a = false #incorrect should be in pascal case
        ^^^^^
__NameError: name 'false' is not defined. Did you mean: 'False'?__

# string
## single line String
a = 'hello'
c = "7"

## multi line String
#a = '''hello    #incorrect(Unclosed Qutate)

a="""hello
world"""
b="'hello  Boys'"
c='''hello
world'''