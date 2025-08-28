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