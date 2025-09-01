```
A string is a sequence of characters enclosed in single quotes ' ', double quotes " ", or triple quotes ''' ''' / """ """.
```
![Strings](/imgs/Strings.png)
```
s1 = 'Hello'
s2 = "Python"
s3 = '''This is
a multiline string'''

2. String Operations
a. Concatenation
s1 = "Hello"
s2 = "World"
s3 = s1 + " " + s2  # "Hello World"

b. Repetition
s = "Hi! "
print(s * 3)  # "Hi! Hi! Hi! "

c. Indexing

Access individual characters using 0-based index.

s = "Python"
print(s[0])  # 'P'
print(s[-1]) # 'n' (last character)

d. Slicing

Extract a substring using [start:end:step].

s = "Python"
print(s[0:4])  # 'Pyth'
print(s[::2])  # 'Pto' (every 2nd char)
```
3. String Functions & Methods
|Method	          |Description	                                                        |Example

len(s)	          |Length of string	                             |len("Python")                                 |→ 6
s.lower()	      |Convert to lowercase	                         |"PYTHON".lower()                              |→ "python"
s.upper()	      |Convert to uppercase	                         |"python".upper()                              |→ "PYTHON"
s.title()	      |Capitalize each word	                         |"hello world".title()                         |→"Hello World"
s.lstrip()	      |Remove left spaces                            |" hello".lstrip()                             |→ "hello"
s.strip()	      |Remove leading & trailing spaces	             |" hello ".strip()                             |→ "hello"
s.rstrip()	      |Remove right spaces	                         |"hello ".rstrip()                             |→ "hello"
s.replace(a,b)	  |Replace substring a with b	                 |"Hello".replace('l','x')                      | → "Hexxo"
s.split(sep)	  |Split string into list	                     |"a,b,c".split(',')                            |→ ['a','b','c']
sep.join(list)	  |Join list into string	                     |'-'.join(['a','b','c'])                       |→ "a-b-c"
s.find(sub)	      |Find substring, return index or -1	         |"Python".find('t')                            |→ 2
s.count(sub)	  |Count occurrences	                         |"Python".count('o')                           |→ 1
s.startswith(sub) |Check start	                                 |"Python".startswith('Py')                     |→ True
s.endswith(sub)	  |Check end	                                 |"Python".endswith('on')                       |→ True
s.isalpha()	      |Check all letters	                         |"Hello".isalpha()                             |→ True
s.isdigit()	      |Check all digits	                             |"123".isdigit()                               |→ True
s.isspace()	      |Check spaces only	                         |" ".isspace()                                 |→ True

```
1. String Formatting
a. Using f-string (Python 3.6+)
name = "Monish"
age = 20
print(f"My name is {name} and age is {age}")

b. Using .format()
name = "Monish"
age = 20
print("My name is {} and age is {}".format(name, age))

c. Using % formatting
name = "Monish"
age = 20
print("My name is %s and age is %d" % (name, age))

5. Escape Sequences
Sequence	Description
\n	New line
\t	Tab
\\	Backslash
\'	Single quote
\"	Double quote
print("Hello\nWorld")  # Hello (newline) World

6. Multi-line Strings
s = """This is
a multi-line
string"""
print(s)

7. String Membership
s = "Python"
print('P' in s)   # True
print('x' not in s)  # True

8. Iterating Strings
s = "Python"
for char in s:
    print(char)

9. Immutability

Strings cannot be changed in-place.

s = "Hello"
# s[0] = 'h'  # Error
s = "h" + s[1:]  #  Correct way

10. Common Use-Cases

Reversing a string:

s = "Python"
print(s[::-1])  # 'nohtyP'


Check palindrome:

s = "madam"
print(s == s[::-1])  # True


Remove spaces:

s = "   hello   "
print(s.strip())  # "hello"
```