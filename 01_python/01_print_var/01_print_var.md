# Rules
1. Starts with letter or _
2. Never Begins with Symbols or num
3. Only Contains (A-z,a-z,0-9,_)
4. Case Sensitive
5. No keywords are Var names 
> help("keywords")

###  print "Hello World" # incorrect
    ^^^^^^^^^^^^^^^^^^^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?

###  File "D:\learn\py\python\print\print.py", line 4, in <module>
    print ["hello world"] # incorrect
    ~~~~~~^^^^^^^^^^^^^^^
TypeError: 'builtin_function_or_method' object is not subscriptable
> Using print [...] makes Python think you're trying to index the print function (like print[0]), which is invalid.

### PS D:\learn\py> & C:/Users/monis/AppData/Local/Programs/Python/Python313/python.exe d:/learn/py/python/print_var/print_var.py
10 20
30
Traceback (most recent call last):
  File "d:\learn\py\python\print_var\print_var.py", line 13, in <module>
    print (a+b+c)
           ~~~^~
TypeError: unsupported operand type(s) for +: 'int' and 'tuple'
PS D:\learn\py> 


### IndentationError: unexpected indent
PS D:\learn\py> & C:/Users/monis/AppData/Local/Programs/Python/Python313/python.exe d:/learn/py/python/print_var/print_var.py
  File "d:\learn\py\python\print_var\print_var.py", line 23
    break=700  # incorrect  (keyword)
         ^
### SyntaxError: invalid syntax
PS D:\learn\py> & C:/Users/monis/AppData/Local/Programs/Python/Python313/python.exe d:/learn/py/python/print_var/print_var.py
  File "d:\learn\py\python\print_var\print_var.py", line 23
    break=700
         ^
### SyntaxError: invalid syntax
PS D:\learn\py> & C:/Users/monis/AppData/Local/Programs/Python/Python313/python.exe d:/learn/py/python/print_var/print_var.py
  File "d:\learn\py\python\print_var\print_var.py", line 23
    break = 700
          ^
SyntaxError: invalid syntax
PS D:\learn\py>

# STACK AHD HEEP MEMORY
 
> x=9 ,y=0

```
x,y are stored in Stack Memory ,and the Values or Objects are stored in the heep memory .
Both are in the Memory but they have the relations between them 
```

# ID FUNCtion
![Description](/imgs/IDfunction.png)
* id() - give the address of the variable values